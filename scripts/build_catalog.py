#!/usr/bin/env python3
"""Rebuild the public catalogs from an external manuscript checkout (stdlib only).

Never modify the source checkout. Fail closed on new LaTeX commands, missing keys,
unexpected columns, or changed catalog counts instead of silently dropping data.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import quote, urlsplit

SCHEMA_VERSION = 1
SPECS = {
    "benchmarks": {
        "source": "tables/table4_full.tex", "expected": 55,
        "title": "Benchmark catalog",
        "columns": ["name", "venue", "domain", "documents", "pages", "tokens", "questions", "multi_document", "multi_page", "single_page", "unanswerable", "evidence_source", "annotation_granularity", "evaluation"],
        "labels": ["Name", "Venue", "Domain", "#Docs", "#Pages", "#Tokens", "#QA", "MD", "MP", "SP", "Unans.", "Source", "Gran.", "Eval."],
        "missing": "unreported or inapplicable",
    },
    "direct-reading": {
        "source": "tables/table5_full.tex", "expected": 29,
        "title": "Methods without explicit retrieval",
        "columns": ["name", "venue", "ocr", "deep_parsing", "agent", "model", "learning", "evaluation"],
        "labels": ["Name", "Venue", "OCR", "Deep", "Agent", "Model", "Learning", "Eval."],
        "missing": "unconfirmed",
    },
    "explicit-retrieval": {
        "source": "tables/table6_full.tex", "expected": 110,
        "title": "Methods with explicit retrieval",
        "columns": ["name", "venue", "ocr", "deep_parsing", "modality", "granularity", "mechanism", "acquisition", "agent", "reasoning", "model", "learning", "evaluation"],
        "labels": ["Name", "Venue", "OCR", "Deep", "Modality", "Gran.", "Mechanism", "Acq.", "Agent", "Reasoning", "Model", "Learning", "Eval."],
        "missing": "unreported, unconfirmed, or inapplicable",
    },
}
REF_LABELS = {
    "tab:explicit-methods": "1 (representative explicit-retrieval methods)",
    "tab:benchmark-catalog": "4 (benchmark catalog)",
    "tab:direct-methods-full": "5 (methods without explicit retrieval)",
    "tab:explicit-methods-full": "6 (methods with explicit retrieval)",
    "app:explicit-retrieval": "the explicit-retrieval appendix",
}
ORDERING = (
    "Source row order is preserved. Within task groups, methods follow final "
    "conference submission deadlines, then first release within each conference; "
    "preprints/journal papers are inserted by first release (Table 1 convention)."
)
DATES = (
    "First release is separate from the citation year in the current BibTeX. "
    "YY.MM preferentially denotes the first arXiv version; an earlier official "
    "release, or the official release when no preprint exists, takes precedence. "
    "A -- month is unavailable and is stored as null, never as an invented month."
)
VENUES = (
    "Venue superscripts F/W/D/S/I/C mean Findings, Workshop, Datasets and "
    "Benchmarks, Short, Industry, and competition reports, respectively."
)


def braced(text: str, pos: int) -> tuple[str, int]:
    """Read balanced braces, respecting escaped literal braces."""
    if pos >= len(text) or text[pos] != "{":
        raise ValueError(f"Expected brace near {text[pos:pos+60]!r}")
    start, depth = pos + 1, 1
    pos += 1
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
            if depth == 0:
                return text[start:pos], pos + 1
        pos += 1
    raise ValueError("Unclosed brace")


def latex(text: str) -> str:
    """Translate only known markup; preserve qualifiers and fail on unknowns."""
    result, pos = [], 0
    wrappers = {"textbf", "textit", "mbox", "TableSixFit", "ensuremath"}
    symbols = {"MethodYes": "✓", "TableFourYes": "✓", "TableFiveYes": "✓",
               "MethodNo": "✗", "TableFourNo": "✗", "TableFiveNo": "✗",
               "textquoteright": "’", "textgreater": ">", "rightarrow": "→",
               "o": "ø", "O": "Ø", "l": "ł", "L": "Ł", "ss": "ß"}
    while pos < len(text):
        char = text[pos]
        if char == "{":
            value, pos = braced(text, pos)
            result.append(latex(value))
            continue
        if char != "\\":
            if char == "}":
                raise ValueError("Unbalanced closing brace")
            result.append(" " if char == "~" else "" if char == "$" else char)
            pos += 1
            continue
        pos += 1
        if pos >= len(text):
            raise ValueError("Trailing backslash")
        if not text[pos].isalpha():
            escape = text[pos]
            pos += 1
            if escape in "%#&_$ {}":
                result.append(escape)
            elif escape in "`'\"^~":
                if pos < len(text) and text[pos] == "{":
                    value, pos = braced(text, pos)
                else:
                    value, pos = text[pos], pos + 1
                accents = {"`": "\u0300", "'": "\u0301", '"': "\u0308", "^": "\u0302", "~": "\u0303"}
                result.append(unicodedata.normalize("NFC", latex(value) + accents[escape]))
            elif escape in ",;!":
                result.append(" ")
            else:
                raise ValueError(f"Unknown LaTeX escape \\{escape}")
            continue
        match = re.match(r"[A-Za-z]+", text[pos:])
        assert match
        command = match.group()
        pos += len(command)
        if command in wrappers | {"textsuperscript", "ref"}:
            while pos < len(text) and text[pos].isspace():
                pos += 1
            value, pos = braced(text, pos)
            if command == "textsuperscript":
                result.append("^(" + latex(value) + ")")
            elif command == "ref":
                result.append(REF_LABELS[value])
            else:
                result.append(latex(value))
        elif command in symbols:
            result.append(symbols[command])
        elif command in {"allowbreak", "selectfont", "raggedright"}:
            pass
        elif command == "par":
            result.append(" ")
        elif command in {"fontsize", "vspace"}:
            for _ in range(2 if command == "fontsize" else 1):
                _, pos = braced(text, pos)
        else:
            raise ValueError(f"Unknown LaTeX command \\{command} in {text!r}")
    return re.sub(r"\s+", " ", "".join(result)).strip()


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def bibtex(text: str) -> dict[str, dict]:
    """Read balanced BibTeX values; do not replace fields from provenance."""
    text = strip_comments(text)
    entries, pos = {}, 0
    while True:
        start = re.search(r"@([A-Za-z]+)\s*\{", text[pos:])
        if not start:
            if text[pos:].strip():
                raise ValueError("Unparsed BibTeX content")
            break
        if text[pos:pos + start.start()].strip():
            raise ValueError("Unparsed content between BibTeX entries")
        entry_type = start.group(1).lower()
        body, end = braced(text, pos + start.end() - 1)
        pos = end
        key, separator, content = body.partition(",")
        key = key.strip()
        if not separator or key in entries:
            raise ValueError(f"Missing or duplicate BibTeX key {key}")
        fields, cursor = {}, 0
        while cursor < len(content):
            while cursor < len(content) and (content[cursor].isspace() or content[cursor] == ","):
                cursor += 1
            if cursor == len(content):
                break
            field = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*", content[cursor:])
            if not field:
                raise ValueError(f"Unparsed BibTeX field in {key}: {content[cursor:cursor+80]!r}")
            name = field.group(1).lower()
            cursor += field.end()
            if content[cursor] == "{":
                value, cursor = braced(content, cursor)
            elif content[cursor] == '"':
                quoted = re.match(r'"((?:\\.|[^"\\])*)"', content[cursor:])
                if not quoted:
                    raise ValueError(f"Invalid quoted BibTeX value in {key}")
                value = quoted.group(1)
                cursor += quoted.end()
            else:
                bare = re.match(r"\d+", content[cursor:])
                if not bare:
                    raise ValueError(f"Unsupported BibTeX expression in {key}")
                value = bare.group()
                cursor += bare.end()
            if name in fields:
                raise ValueError(f"Duplicate field {name} in {key}")
            fields[name] = latex(value)
            if cursor < len(content) and not (content[cursor].isspace() or content[cursor] == ","):
                raise ValueError(f"Unparsed BibTeX value suffix in {key}")
        for required in ("title", "author", "year"):
            if not fields.get(required):
                raise ValueError(f"Missing {required} in {key}")
        entries[key] = {"citekey": key, "entry_type": entry_type, "fields": fields}
    return entries


def scholarly_url(url: str) -> bool:
    """Conservative URL allowlist for primary publication records already in source."""
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower()
    allowed = {"arxiv.org", "doi.org", "aclanthology.org", "openaccess.thecvf.com",
               "papers.nips.cc", "proceedings.neurips.cc", "proceedings.iclr.cc",
               "ojs.aaai.org", "openreview.net", "dl.acm.org", "ieeexplore.ieee.org",
               "link.springer.com", "proceedings.mlr.press", "www.sciencedirect.com"}
    return parsed.scheme in {"http", "https"} and host in allowed


def attach_links(entries: dict, provenance: dict) -> list[dict]:
    safe = []
    for key, entry in entries.items():
        fields, record = entry["fields"], provenance.get(key, {})
        candidates = []
        if fields.get("url"):
            candidates.append((fields["url"], "references.bib:url"))
        if fields.get("doi"):
            candidates.append(("https://doi.org/" + fields["doi"], "references.bib:doi"))
        for field in ("authorSourceUrl", "scholarResultUrl"):
            if isinstance(record.get(field), str):
                candidates.append((record[field], "reference_sources.json:" + field))
        # An explicit arXiv identifier is bibliographic evidence, not a guessed URL.
        for field in ("eprint", "journal", "note"):
            match = re.search(r"(?:arXiv\s*:\s*|^)(\d{4}\.\d{4,5})(?:v\d+)?\b", fields.get(field, ""), re.I)
            if match:
                candidates.append(("https://arxiv.org/abs/" + match.group(1), "references.bib:" + field))
        chosen = next(((url, source) for url, source in candidates if scholarly_url(url)), None)
        search = "https://scholar.google.com/scholar?q=" + quote(fields["title"], safe="")
        entry["paper_url"] = chosen[0] if chosen else None
        entry["scholar_search_url"] = search
        entry["link_provenance"] = {
            "source": chosen[1] if chosen else "title-based Google Scholar search",
            "kind": "paper" if chosen else "scholar_search",
            "verification": "recorded in manuscript source; not independently rechecked for this repository" if chosen else "search link only; no paper destination verified",
        }
        safe.append({"citekey": key, "paper_url": entry["paper_url"],
                     "scholar_search_url": search, "link_provenance": entry["link_provenance"]})
    return safe


def macro_argument(text: str, name: str) -> tuple[str, str]:
    match = re.search(r"\\" + re.escape(name) + r"\s*\{", text)
    if not match:
        raise ValueError(f"Missing \\{name}")
    value, end = braced(text, match.end() - 1)
    return value, text[:match.start()] + text[end:]


def split_cells(text: str) -> list[str]:
    """Split only top-level unescaped table separators."""
    cells, start, depth, pos = [], 0, 0, 0
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
        elif text[pos] == "&" and depth == 0:
            cells.append(text[start:pos].strip())
            start = pos + 1
        if depth < 0:
            raise ValueError("Unbalanced table row")
        pos += 1
    if depth:
        raise ValueError("Unbalanced table row")
    cells.append(text[start:].strip())
    return cells


def parse_table(source: Path, slug: str, entries: dict) -> dict:
    spec = SPECS[slug]
    content = strip_comments((source / spec["source"]).read_text(encoding="utf-8"))
    caption, _ = macro_argument(content, "caption")
    notes, rows, group = [], [], None
    in_notes = False
    for line_number, line in enumerate(content.splitlines(), 1):
        if r"\begin{minipage}" in line:
            in_notes = True
        if in_notes and line.startswith(r"\textbf{"):
            notes.append(latex(line))
        if line.startswith(r"\multicolumn{") and r"{\textit{" in line:
            candidate, _ = macro_argument(line, "textit")
            if "Continued" not in candidate and "End of Table" not in candidate:
                group = latex(candidate)
        if r"\citeyearpar{" not in line:
            continue
        if not line.rstrip().endswith(r"\\"):
            raise ValueError(f"Expected complete physical row at {spec['source']}:{line_number}")
        cells = split_cells(line.rstrip()[:-2])
        if len(cells) != len(spec["columns"]):
            raise ValueError(f"Wrong column count at {spec['source']}:{line_number}: {len(cells)}")
        citekey, name = macro_argument(cells[0], "citeyearpar")
        release, name = macro_argument(name, "MethodDate")
        if citekey not in entries:
            raise ValueError(f"Missing citation key {citekey}")
        if group is None:
            raise ValueError("Missing table group")
        release = latex(release)
        date = re.fullmatch(r"(\d{2})\.(\d{2}|--)", release)
        if not date:
            raise ValueError(f"Unknown release date {release}")
        year = 2000 + int(date[1])
        month = None if date[2] == "--" else int(date[2])
        if month is not None and not 1 <= month <= 12:
            raise ValueError(f"Invalid month {release}")
        entry = entries[citekey]
        values = [latex(name)] + [latex(cell) for cell in cells[1:]]
        order = len(rows) + 1
        row = {
            "id": f"{slug}-{order:03}", "source_order": order, "group": group,
            "source_table": spec["source"], "source_line": line_number,
            **dict(zip(spec["columns"], values)),
            "first_release_display": release, "first_release_year": year,
            "first_release_month": month,
            "first_release_iso": f"{year}-{month:02}" if month else str(year),
            "first_release_precision": "month" if month else "year",
            "citekey": citekey, "citation_year": entry["fields"]["year"],
            "title": entry["fields"]["title"], "authors": entry["fields"]["author"],
            "bibliography_entry_type": entry["entry_type"], "bibliography_fields": entry["fields"],
            "paper_url": entry["paper_url"], "scholar_search_url": entry["scholar_search_url"],
            "link_provenance": entry["link_provenance"],
        }
        rows.append(row)
    if len(rows) != spec["expected"]:
        raise ValueError(f"{slug}: expected {spec['expected']} rows, got {len(rows)}")
    if len({row["name"] for row in rows}) != len(rows):
        raise ValueError(f"Duplicate names in {slug}")
    groups = dict(Counter(row["group"] for row in rows))
    if slug == "explicit-retrieval" and groups != {"Retrieval-only methods": 20, "Document VQA methods": 90}:
        raise ValueError(f"Unexpected explicit-retrieval groups: {groups}")
    return {"schema_version": SCHEMA_VERSION, "catalog": slug,
            "title": spec["title"], "source_table": spec["source"],
            "caption": latex(caption), "record_count": len(rows), "groups": groups,
            "columns": dict(zip(spec["columns"], spec["labels"])),
            "conventions": {"ordering": ORDERING, "dates": DATES, "venue_superscripts": VENUES,
                            "missing_value": {"marker": "--", "meaning": spec["missing"]},
                            "superscripts": "Plain JSON/CSV uses ^(x); Markdown displays x as a superscript.",
                            "boolean_markers": "✓ = present/included; ✗ = absent/excluded, not unknown."},
            "notes": notes, "records": rows}


def markdown_text(value: object) -> str:
    text = html.escape(str(value), quote=False)
    text = text.replace("|", "&#124;").replace("*", "&#42;")
    return re.sub(r"\^\(([^()]*)\)", r"<sup>\1</sup>", text)


def paper_link(row: dict) -> str:
    if row["paper_url"]:
        return f"[Paper]({row['paper_url']})"
    return f"[Google Scholar search]({row['scholar_search_url']})"


def table(headers: list[str], rows: list[list[str]]) -> list[str]:
    return ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] + ["| " + " | ".join(row) + " |" for row in rows]


def render_page(catalog: dict) -> str:
    slug, rows = catalog["catalog"], catalog["records"]
    spec = SPECS[slug]
    lines = [f"# {catalog['title']}", "",
             "[Repository home](../README.md) · [Benchmarks](benchmarks.md) · [Direct reading](direct-reading.md) · [Explicit retrieval](explicit-retrieval.md)", "",
             f"**{len(rows)} records.** Generated from manuscript `{spec['source']}`. Source rows, groups, qualifiers, and notation are preserved.", "",
             f"[JSON](../data/{slug}.json) · [CSV](../data/{slug}.csv) · [Bibliography](../references.bib) · [Data dictionary](../data/README.md)", "",
             markdown_text(catalog["caption"]), "",
             "**Dates and citation years.** " + DATES, "",
             "**Order.** " + ORDERING, "",
             "**Notation.** ✓ = present/included; ✗ = absent/excluded. `--` means " + spec["missing"] + ". " + VENUES, "",
             "**Links.** “Paper” uses an academic URL or explicit arXiv identifier already recorded in the manuscript bibliography/provenance. Links were not independently rechecked for this repository. “Google Scholar search” is a title search, not a verified paper link.", "",
             "## Browse", ""]
    for index, (group, count) in enumerate(catalog["groups"].items(), 1):
        lines.append(f"- [{markdown_text(group)} ({count})](#group-{index})")
    lines += ["- [Full source notes](#source-notes)", ""]
    for index, group in enumerate(catalog["groups"], 1):
        subset = [row for row in rows if row["group"] == group]
        lines += [f'<a id="group-{index}"></a>', "", f"## {markdown_text(group)}", ""]
        if slug == "explicit-retrieval":
            if group == "Retrieval-only methods":
                summary_fields = ["venue", "first_release_display", "citation_year", "ocr", "deep_parsing", "modality", "granularity", "mechanism", "acquisition", "evaluation"]
                headers = ["Method / details", "Venue", "First release", "Bib year", "OCR", "Deep", "Modality", "Gran.", "Mechanism", "Acq.", "Eval.", "Source"]
            else:
                summary_fields = ["venue", "first_release_display", "citation_year", "modality", "granularity", "acquisition", "agent", "reasoning", "model", "evaluation"]
                headers = ["Method / details", "Venue", "First release", "Bib year", "Modality", "Gran.", "Acq.", "Agent", "Reasoning", "Model", "Eval.", "Source"]
            data = []
            for row in subset:
                data.append([f"[{markdown_text(row['name'])}](#{row['id']})"] + [markdown_text(row[key]) for key in summary_fields] + [paper_link(row)])
            lines += table(headers, data) + ["", "Each expandable record below contains every source column, including the complete retrieval mechanism.", ""]
        else:
            headers = spec["labels"][:2] + ["First release", "Bib year"] + spec["labels"][2:] + ["Citation / source"]
            data = []
            for row in subset:
                values = [markdown_text(row[col]) for col in spec["columns"]]
                values[0] = f"[{values[0]}](#{row['id']})"
                data.append(values[:2] + [row["first_release_display"], row["citation_year"]] + values[2:] + [f"`{row['citekey']}`<br>{paper_link(row)}"])
            lines += table(headers, data) + [""]
        for row in subset:
            lines += [f'<a id="{row["id"]}"></a>', "", "<details>", f"<summary>{markdown_text(row['name'])} — {markdown_text(row['title'])}</summary>", "",
                      f"**Paper:** {markdown_text(row['title'])}  ",
                      f"**Authors:** {markdown_text(row['authors'])}  ",
                      f"**Citation:** `{row['citekey']}`; current BibTeX year **{row['citation_year']}**; first release **{row['first_release_display']}**.  ",
                      f"**Source:** {paper_link(row)}. Recorded in `{row['link_provenance']['source']}`.  ",
                      f"**Manuscript row:** `{row['source_table']}:{row['source_line']}`; order {row['source_order']}.", ""]
            if slug == "explicit-retrieval":
                lines += table(["Field", "Source value"], [[label, markdown_text(row[col])] for col, label in zip(spec["columns"][1:], spec["labels"][1:])]) + [""]
            lines += ["**Current bibliographic fields**", ""]
            lines += table(["Field", "Value"], [[markdown_text(key), markdown_text(value)] for key, value in row["bibliography_fields"].items()])
            lines += ["", "</details>", ""]
    lines += ['<a id="source-notes"></a>', "", "## Full source notes", ""]
    lines += [markdown_text(note) + "\n" for note in catalog["notes"]]
    if slug == "explicit-retrieval":
        lines += ["**Shared evaluation abbreviations:** Ans. = answer quality; Ret. = evidence retrieval; Loc. = within-page localization; Eff. = efficiency and cost; Rob. = robustness. The source notes above qualify these labels for individual methods.", ""]
    return "\n".join(lines).rstrip() + "\n"


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict]) -> bytes:
    output = io.StringIO(newline="")
    columns = list(dict.fromkeys(key for row in rows for key in row))
    writer = csv.DictWriter(output, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({key: json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (dict, list)) else value for key, value in row.items()})
    return output.getvalue().encode("utf-8")


def verify_plain(value: object, trail: str = "") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            verify_plain(item, trail + "." + key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            verify_plain(item, f"{trail}[{index}]")
    elif isinstance(value, str) and re.search(r"\\[A-Za-z]|\\[%&#]|\\[{}]", value):
        raise ValueError(f"Unparsed LaTeX at {trail}: {value!r}")


def build(source: Path) -> tuple[dict[str, bytes], dict]:
    relative_sources = [spec["source"] for spec in SPECS.values()] + ["references.bib", "reference_sources.json", "tables/table1_explicit_methods.tex"]
    for relative in relative_sources:
        if not (source / relative).is_file():
            raise ValueError(f"Missing required manuscript source: {relative}")
    bib_bytes = (source / "references.bib").read_bytes()
    entries = bibtex(bib_bytes.decode("utf-8-sig"))
    if len(entries) != 165:
        raise ValueError(f"Expected 165 active bibliography entries, got {len(entries)}")
    provenance = json.loads((source / "reference_sources.json").read_text(encoding="utf-8-sig"))
    source_records = {row["key"]: row for row in provenance["records"]}
    if len(source_records) != len(provenance["records"]):
        raise ValueError("Duplicate keys in reference provenance")
    safe_links = attach_links(entries, source_records)
    outputs = {"references.bib": bib_bytes}
    catalogs = {slug: parse_table(source, slug, entries) for slug in SPECS}
    for slug, catalog in catalogs.items():
        verify_plain(catalog)
        outputs[f"data/{slug}.json"] = json_bytes(catalog)
        outputs[f"data/{slug}.csv"] = csv_bytes(catalog["records"])
        outputs[f"papers/{slug}.md"] = render_page(catalog).encode("utf-8")
    bibliography = {"schema_version": SCHEMA_VERSION, "source": "references.bib", "record_count": len(entries), "records": list(entries.values())}
    verify_plain(bibliography)
    outputs["data/bibliography.json"] = json_bytes(bibliography)
    outputs["data/bibliography.csv"] = csv_bytes([{ "citekey": entry["citekey"], "entry_type": entry["entry_type"], **entry["fields"], "paper_url": entry["paper_url"], "scholar_search_url": entry["scholar_search_url"], "link_provenance": entry["link_provenance"]} for entry in entries.values()])
    outputs["reference_sources.json"] = json_bytes({"schema_version": SCHEMA_VERSION, "description": "Public link-only subset derived from manuscript reference_sources.json and current references.bib. Bibliographic fields are sourced exclusively from references.bib. Private evidence paths and unrelated audit metadata are excluded.", "source_provenance_verified_date": provenance.get("verifiedDate"), "records": safe_links})
    all_rows = [row for catalog in catalogs.values() for row in catalog["records"]]
    report = {"bibliography_entries": len(entries), "catalog_records": {slug: catalog["record_count"] for slug, catalog in catalogs.items()}, "groups": {slug: catalog["groups"] for slug, catalog in catalogs.items()}, "unique_cited_keys_in_catalogs": len({row["citekey"] for row in all_rows}), "catalog_rows_with_paper_url": sum(bool(row["paper_url"]) for row in all_rows), "catalog_rows_with_search_only": sum(not row["paper_url"] for row in all_rows), "unavailable_release_months": [{"catalog": slug, "name": row["name"], "first_release_display": row["first_release_display"]} for slug, catalog in catalogs.items() for row in catalog["records"] if row["first_release_month"] is None], "all_citekeys_resolve": True, "all_table_rows_preserved": True, "unparsed_latex": False, "bibtex_copied_byte_identically": True}
    outputs["data/validation.json"] = json_bytes(report)
    manifest = {"schema_version": SCHEMA_VERSION, "description": "Content hashes of the external manuscript inputs and generated public artifacts. All paths are repository-relative; no source checkout location is recorded.", "sources": [{"path": relative, "sha256": hashlib.sha256((source / relative).read_bytes()).hexdigest()} for relative in relative_sources], "generated": [{"path": relative, "sha256": hashlib.sha256(content).hexdigest()} for relative, content in sorted(outputs.items())]}
    outputs["data/source_manifest.json"] = json_bytes(manifest)
    return outputs, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="External manuscript checkout containing tables/ and references.bib")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1], help="Companion repository root (default: this script's parent repository)")
    parser.add_argument("--check", action="store_true", help="Validate sources and compare all generated bytes without writing")
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if source == output or source in output.parents or output in source.parents:
        parser.error("Source checkout and output repository must be separate directories")
    try:
        outputs, report = build(source)
        mismatches = []
        for relative, content in outputs.items():
            target = output / relative
            if args.check:
                if not target.is_file() or target.read_bytes() != content:
                    mismatches.append(relative)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
        if mismatches:
            print("Generated files differ: " + ", ".join(mismatches), file=sys.stderr)
            return 1
        print(json.dumps(report, ensure_ascii=False, indent=2))
        print(f"{'Checked' if args.check else 'Generated'} {len(outputs)} files.")
        return 0
    except (ValueError, KeyError, OSError) as error:
        print(f"Catalog build failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

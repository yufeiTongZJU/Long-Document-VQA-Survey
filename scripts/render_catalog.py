#!/usr/bin/env python3
"""Render committed catalog JSON without importing or accessing a manuscript."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from build_catalog import SCHEMA_VERSION, SPECS, bibtex, csv_bytes, json_bytes, render_page, verify_plain


def read_json(root: Path, relative: str) -> dict:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def validate_catalog(catalog: dict, slug: str, bibliography: dict) -> None:
    """Validate declared metadata, identities, and bibliography consistency."""
    rows = catalog["records"]
    if catalog["schema_version"] != SCHEMA_VERSION or catalog["catalog"] != slug:
        raise ValueError(f"Wrong schema or catalog identity in {slug}")
    if catalog["record_count"] != len(rows):
        raise ValueError(f"{slug}: record_count does not match records")
    if catalog["groups"] != dict(Counter(row["group"] for row in rows)):
        raise ValueError(f"{slug}: group counts do not match records")
    ids, orders = set(), set()
    for row in rows:
        identity, order, key = row["id"], row["source_order"], row["citekey"]
        if not re.fullmatch(re.escape(slug) + r"-\d{3,}", identity) or identity in ids:
            raise ValueError(f"{slug}: invalid or duplicate record id {identity}")
        if type(order) is not int or order < 1 or order in orders:
            raise ValueError(f"{slug}: invalid or duplicate source_order {order}")
        ids.add(identity)
        orders.add(order)
        if key not in bibliography:
            raise ValueError(f"{slug}: missing citation key {key}")
        entry = bibliography[key]
        if row["bibliography_fields"] != entry["fields"] or row["bibliography_entry_type"] != entry["entry_type"]:
            raise ValueError(f"{slug}: bibliographic fields differ from bibliography.json for {key}")
        for field, bib_field in [("title", "title"), ("authors", "author"), ("citation_year", "year")]:
            if row[field] != entry["fields"][bib_field]:
                raise ValueError(f"{slug}: {field} differs from bibliography.json for {key}")
        for field in SPECS[slug]["columns"]:
            if not isinstance(row[field], str):
                raise ValueError(f"{slug}: table column {field} must be a string")
    verify_plain(catalog)


def render(root: Path) -> tuple[dict[str, bytes], dict]:
    bibliography = read_json(root, "data/bibliography.json")
    entries = {entry["citekey"]: entry for entry in bibliography["records"]}
    if bibliography["schema_version"] != SCHEMA_VERSION:
        raise ValueError("Wrong bibliography schema")
    if len(entries) != len(bibliography["records"]) or len(entries) != bibliography["record_count"]:
        raise ValueError("Bibliography has duplicate keys or an incorrect record_count")
    bib = bibtex((root / "references.bib").read_text(encoding="utf-8-sig"))
    if set(entries) != set(bib):
        raise ValueError("bibliography.json and references.bib have different citation keys")
    for key, entry in entries.items():
        if entry["fields"] != bib[key]["fields"] or entry["entry_type"] != bib[key]["entry_type"]:
            raise ValueError(f"bibliography.json differs from current references.bib for {key}")
    verify_plain(bibliography)
    outputs, counts = {}, {}
    for slug in SPECS:
        catalog = read_json(root, f"data/{slug}.json")
        validate_catalog(catalog, slug, entries)
        outputs[f"data/{slug}.csv"] = csv_bytes(catalog["records"])
        outputs[f"papers/{slug}.md"] = render_page(catalog).encode("utf-8")
        counts[slug] = catalog["record_count"]
    outputs["data/bibliography.csv"] = csv_bytes([
        {"citekey": entry["citekey"], "entry_type": entry["entry_type"], **entry["fields"],
         "paper_url": entry["paper_url"], "scholar_search_url": entry["scholar_search_url"],
         "link_provenance": entry["link_provenance"]} for entry in entries.values()
    ])
    # sources remains the original external-input audit. Only current artifact
    # hashes are refreshed, including edited canonical JSON without rewriting it.
    manifest = read_json(root, "data/source_manifest.json")
    for item in manifest["generated"]:
        relative = item["path"]
        target = (root / relative).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError("Manifest artifact path leaves the repository")
        content = outputs[relative] if relative in outputs else target.read_bytes()
        item["sha256"] = hashlib.sha256(content).hexdigest()
    outputs["data/source_manifest.json"] = json_bytes(manifest)
    return outputs, {"catalog_records": counts, "bibliography_entries": len(entries),
                     "current_json_validation": "passed", "original_source_provenance": "preserved"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Companion repository root")
    parser.add_argument("--check", action="store_true", help="Validate and compare derived files without writing")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        outputs, report = render(root)
        different = []
        for relative, content in outputs.items():
            target = root / relative
            if args.check:
                if not target.is_file() or target.read_bytes() != content:
                    different.append(relative)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
        if different:
            print("Derived files differ: " + ", ".join(different), file=sys.stderr)
            return 1
        print(json.dumps(report, ensure_ascii=False, indent=2))
        print(f"{'Checked' if args.check else 'Rendered'} {len(outputs)} files from committed JSON.")
        return 0
    except (KeyError, ValueError, TypeError, OSError) as error:
        print(f"Catalog render failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

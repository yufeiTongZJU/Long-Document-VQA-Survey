# Catalog data

The catalogs transcribe the manuscript's complete comparison tables. They preserve the source ordering, categories, strings, qualifiers, percentages, missing-value markers, and superscripts. They are descriptive catalogs, not a leaderboard. No performance scores or code links have been inferred.

| Catalog | Records | JSON | CSV | Reading view |
| --- | --- | --- | --- | --- |
| Benchmarks | 55 | [JSON](benchmarks.json) | [CSV](benchmarks.csv) | [Page](../papers/benchmarks.md) |
| Without explicit retrieval | 29 | [JSON](direct-reading.json) | [CSV](direct-reading.csv) | [Page](../papers/direct-reading.md) |
| With explicit retrieval | 110: 20 retrieval-only, 90 document VQA | [JSON](explicit-retrieval.json) | [CSV](explicit-retrieval.csv) | [Page](../papers/explicit-retrieval.md) |
| Active bibliography | 165 entries | [JSON](bibliography.json) | [CSV](bibliography.csv) | [Original BibTeX](../references.bib) |

The tables contain **194 catalog rows** referring to **158 distinct citation keys**. One paper can contribute several benchmarks or methods, so row counts are not counts of distinct papers. The bibliography also contains references cited elsewhere in the survey.

## JSON and CSV conventions

Each catalog JSON has `schema_version`, `catalog`, `title`, `source_table`, `caption`, `record_count`, `groups`, `columns`, `conventions`, `notes`, and `records`. `groups` preserves source group order and supplies its counts. `columns` maps machine-readable table fields to the manuscript's column labels. The full caption and notes are included after formatting conversion.

CSV has one row per source row, in the same order as JSON. Dictionary-valued columns (`bibliography_fields` and `link_provenance`) contain JSON strings. CSV uses UTF-8 and an empty cell for JSON null. The original `--` table marker remains `--`; it is distinct from a null month or paper URL.

| Shared field | Meaning |
| --- | --- |
| `id` | Catalog and current source row number; an anchor in its reading page. IDs may change if source rows are reordered. |
| `source_order` | One-based position in the source table. |
| `group` | Source group label, including any scale qualifiers. |
| `source_table`, `source_line` | Relative manuscript filename and one-based physical row line. |
| `name`, `venue` | Source display name and venue label, including source asterisks and superscripts. |
| `first_release_display` | Source `YY.MM` value; `26.--` retains an unavailable month. |
| `first_release_year`, `first_release_month` | Integer year and month; month is null when unavailable. |
| `first_release_iso`, `first_release_precision` | `YYYY-MM` / `month`, or `YYYY` / `year` when the month is unavailable. No day is inferred. |
| `citekey` | Exact key in the current manuscript bibliography. |
| `citation_year` | Exact `year` field in current BibTeX; a string, not the release year or venue label. |
| `title`, `authors` | Current BibTeX title and author field with LaTeX typography converted to text. Author separators remain BibTeX `and`. |
| `bibliography_entry_type`, `bibliography_fields` | Current BibTeX entry type and all fields; provenance metadata never replaces these values. |
| `paper_url` | Primary academic URL already recorded in source provenance/BibTeX, or an arXiv URL formed from an explicit identifier in BibTeX; null otherwise. |
| `scholar_search_url` | Google Scholar title-search URL built from the current BibTeX title. This is a search, not a paper link. |
| `link_provenance` | Link kind, originating source field, and verification limitation. Links have not been independently rechecked for this repository. |

## Original table columns

| Catalog | Fields after name and venue |
| --- | --- |
| Benchmarks | `domain`, `documents`, `pages`, `tokens`, `questions`, `multi_document`, `multi_page`, `single_page`, `unanswerable`, `evidence_source`, `annotation_granularity`, `evaluation` |
| Direct reading | `ocr`, `deep_parsing`, `agent`, `model`, `learning`, `evaluation` |
| Explicit retrieval | `ocr`, `deep_parsing`, `modality`, `granularity`, `mechanism`, `acquisition`, `agent`, `reasoning`, `model`, `learning`, `evaluation` |

These fields are **strings**. Values such as `✓(18.9%)`, `1.27M`, `90k; 102.2k`, or `Ret.^(a)` retain their original scope; they are not coerced into booleans or approximate numeric quantities. In particular, benchmark `pages` can denote an average or a full candidate collection under the source's conventions. Consult the full notes on each reading page before comparing values.

- `✓` means present/included; `✗` means absent/excluded. An absence mark is not an unknown value.
- For benchmarks, `--` means unreported or inapplicable. For direct-reading methods it means unconfirmed. For explicit retrieval it means unreported, unconfirmed, or inapplicable.
- JSON/CSV encodes a superscript as `^(x)`, for example `ACL’25^(F)` or `DSE^(t)(P^(V))`. The reading pages display true HTML superscripts. Superscripts retain their source meaning; `t` marks added retrieval/scoring/page-selection training, while `a` refers to qualified evaluation exceptions.
- `+` denotes combinations and `/` denotes alternatives in method comparison fields. Mechanism arrows and brackets are preserved. The direction of `→` specifies retrieval-output evidence on the left and generation input on the right.
- Asterisk annotations have table-specific meanings. The benchmark page explains pre-extracted inputs; the direct-reading page explains primarily single-page methods that also support multiple pages.
- Citation years can differ from venue and first-release years. Such differences are retained, not silently reconciled.

## Bibliography, provenance, and regeneration

[references.bib](../references.bib) is copied byte for byte from the supplied manuscript checkout. The original header's provenance pointer resolves to the public [reference_sources.json](../reference_sources.json), a link-only subset that omits private paths and unrelated audit metadata. That file does not provide replacement bibliographic fields. [bibliography.json](bibliography.json) contains all 165 active current BibTeX entries.

[source_manifest.json](source_manifest.json) records SHA-256 hashes using relative filenames only. Its `sources` hashes refer to the last imported manuscript snapshot and remain unchanged when committed JSON is edited and re-rendered; `generated` hashes describe current repository artifacts. [validation.json](validation.json) records row counts, citation coverage, groups, link coverage, and unavailable months at the last manuscript import. It is an import audit, not a claim that later repository edits match an external manuscript. Neither file records an external checkout path.

After editing canonical catalog JSON, run `python scripts/render_catalog.py`, followed by `python scripts/render_catalog.py --check`. This requires only the committed repository and updates CSV, reading pages, and artifact hashes without overwriting JSON or original source provenance. It checks current counts, groups, unique IDs, citation keys, and consistency with the bibliography. Update declared counts/groups when adding records; keep copied bibliographic fields consistent across catalog rows, `bibliography.json`, and `references.bib`.

Use `scripts/build_catalog.py --source /path/to/manuscript` only to deliberately import a manuscript snapshot. That importer replaces canonical JSON and the import audit; it is not the rendering command for JSON edits. It rejects unexpected snapshot counts, unknown LaTeX, malformed rows, duplicate names/keys, and missing citations. See [both workflows](../scripts/README.md).

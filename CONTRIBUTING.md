# Contributing

Thank you for helping improve the companion repository for *A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions*.

This snapshot was prepared on **2026-10-14** from the current manuscript and tables. The date identifies repository preparation, not a claimed exhaustive search or literature cutoff. Contributions are reviewed as proposed changes to that snapshot; the repository does not promise a continuous update schedule.

## Scope

Useful contributions include corrections to metadata, broken official links, transcription errors, taxonomy labels, and table qualifiers. Evidence-backed suggestions for missing relevant work are also welcome. Explain whether a suggested work is a direct-reading method, an explicit-retrieval method, a benchmark, or supporting background.

The survey includes single-page foundations and background literature as well as long-document methods. A bibliography entry alone is not evidence that a paper belongs in a method table. Please keep the distinction between retrieval-only and QA systems, and between single-page and multipage evaluation settings.

## Submit an issue or pull request

Include the following information so a proposed change can be checked:

1. **Affected record:** paper or benchmark name, existing citation key if available, and the file or page containing the issue.
2. **Current and proposed values:** show the specific field or sentence to change.
3. **Evidence:** link the paper and identify a page, section, table, or appendix supporting the correction. Prefer the official paper, proceedings, author-maintained repository, or official project page.
4. **Reasoning:** explain how the evidence fits the definitions in [taxonomy.md](taxonomy.md), including any ambiguity or exceptions.
5. **For a suggested addition:** explain its relevance and provide complete bibliographic metadata and official resource links. Flag missing or unverified information explicitly.

For bibliography corrections, reuse the existing entry and citation key where possible. Prefer Google Scholar's BibTeX export when obtaining citation metadata, then check it against the official paper or proceedings. Preserve meaningful version, venue, and release-date distinctions; do not replace unknown values with guesses.

## Preserve classification boundaries

- **OCR** covers external extraction or textualization, including PDF extraction and VLM transcription; visual encoding alone does not establish OCR dependence.
- **Deep Parsing** requires document semantic overviews or explicit relations. Element descriptions or runtime memory alone are insufficient.
- **Modality** describes relevance matching; method **Granularity** describes generator inputs or retrieval-only outputs. Preserve any mapping between retrieval hits and generation inputs.
- **Iterative acquisition** requires feedback-driven acquisition beyond the current evidence set. **Multi-step reasoning** concerns a feedback loop and can occur over fixed evidence.
- Retrieval-side training markers and generation-side Learning describe different training scopes. Identify the trained and frozen components when relevant.
- Method evaluation labels require quantitative reporting in the paper. Benchmark labels describe supported evaluation capabilities. Preserve exceptions and pre-extracted-input qualifiers.

Retain the source tables' date and ordering conventions. A first-release month is not necessarily a venue date, and row order is not a performance ranking. Comparisons should specify input conditions, evidence annotations, budgets, and relevant parsing, indexing, and inference costs.

## Editing records and generated pages

Canonical records live in [data/](data/); the paper pages are generated views. Make a record correction in its canonical source and regenerate affected views using the repository's documented workflow. If you cannot regenerate a view, say so in the issue or pull request. Avoid editing a generated page as the only record of a correction.

Keep changes focused and preserve citation keys, provenance, table notes, and distinctions among absent, unknown, and not-applicable values. Separate a proposed research reinterpretation from a transcription or formatting fix, and explain any change that would diverge from the manuscript.

Before submitting, check that the edited record agrees with its supporting source, links resolve to the intended resource, generated views remain consistent, and the diff contains only the intended changes. Summarize the correction and the checks performed in the pull request.

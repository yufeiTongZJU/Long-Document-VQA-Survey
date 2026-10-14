# Taxonomy and reading guide

This guide explains the classifications used in *A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions*. The repository snapshot was prepared on **2026-10-14** from the current manuscript and its tables. This date records repository preparation; it is not a literature-search cutoff.

The survey focuses on evidence acquisition and use in document VQA. It includes single-page foundations, retrieval-only systems, QA systems, benchmarks, and background references. Inclusion in the bibliography does not by itself identify a work as a long-document QA method. Single-page and multipage direct-reading groups follow the methods' primary design and evaluation settings.

## Task and analytical components

Given a question and one or more visual documents, a system produces an answer and, optionally, evidence sources under limits on context, computation, and tool calls. **Closed-domain** specifies the input document for each question; **open-domain** requires identifying relevant sources within a shared document collection.

| Component | Function |
| --- | --- |
| **Document parsing** | Preserve accessible content and document structure while balancing fidelity and processing cost. |
| **Evidence organization and retrieval** | Locate and assemble question-relevant evidence, retaining its sources and addressing evidence gaps. |
| **Generator organization and learning** | Integrate and verify evidence through evidence presentation, reasoning roles, feedback, and learning objectives. |
| **Evaluation** | Assess answer correctness, evidence support, efficiency, and reliability, including errors across the pipeline. |

These are analytical functions, not a required execution sequence. A system can revisit parsing or retrieval during reasoning.

## Two technical routes

| Route | Definition and boundary |
| --- | --- |
| **Direct reading** | Answer from supplied document representations without explicit evidence retrieval in the answering pipeline. Hierarchical encoding, cross-page fusion, and compression can manage long inputs. Evidence-page prediction or a reported retrieval metric does not by itself change this classification. |
| **Explicit retrieval** | Select question-relevant documents, pages, or elements for a generator, or return evidence in a retrieval-only system. Acquisition can be fixed or feedback-driven. |

The routes are complementary: a generator can apply multipage reading techniques to retrieved evidence. For retrieval-only methods, generation attributes do not apply.

## Document parsing

**OCR** and **Deep Parsing** are independent dimensions.

| Field | Interpretation |
| --- | --- |
| **OCR: Yes** | Dependence on external extraction or textualization, including OCR, PDF text extraction, and VLM transcription or descriptions of charts and tables. Combining extracted text with page images still receives this label. |
| **OCR: No** | Primarily encode pages visually. This describes the pipeline's extraction dependence; it does not mean that the model cannot read text in an image. |
| **Deep Parsing: Summary** | Construct semantic overviews of pages or documents. |
| **Deep Parsing: Tree** | Represent section hierarchies or containment. |
| **Deep Parsing: Graph** | Represent explicit text–image, entity, or cross-page relations. |

Deep Parsing types can be combined. Element transcription or description alone is insufficient. Runtime memory or an agent's record of prior actions does not by itself establish Deep Parsing: the label concerns the semantic overviews or relations constructed for document content. Parsing can occur in advance or on demand.

## Evidence organization and retrieval

| Field | Interpretation |
| --- | --- |
| **Modality** | The **evidence-side representation used for relevance matching**: `Uni(T)` for text, `Uni(V)` for vision, and `Mixed(T/V)` for both. It does not specify every modality used elsewhere in the pipeline. |
| **Granularity** | Evidence units **received by the generator**; for retrieval-only systems, the returned units. `D` / Document denotes document-level evidence; `P` / Page denotes a full-page image or complete parsed page content; `E` / Element denotes independently accessible blocks, sections, charts, tables, or region crops. |
| **Mechanism** | Lexical or vector matching, LLM/VLM selection or reranking, region selection, and combinations with navigation or expansion. The representative table groups retriever families; the full table records more specific mechanisms and evidence mappings. |
| **Acquisition: One-shot** | No feedback-driven expansion beyond the current evidence set. Fixed multistage retrieval, graph traversal without such feedback, reranking, and refinement of existing evidence can fall here. |
| **Acquisition: Iterative** | Generation or control feedback leads to acquisition of evidence **beyond the current set**. Multiple retrieval stages alone do not establish this label. |

### Reading mechanism notation

- `D`, `P`, and `E` denote document, page, and element; superscripts `T`, `V`, and `TV` denote text, visual, and both.
- In `E^T → P^V`, retrieval or selection returns text elements and the generator receives page images. ViDoRAG's text-chunk-to-source-page mapping illustrates this distinction.
- The left side of an arrow describes retrieval or selection output; the right side describes generation input. Without an arrow, the granularity and modality are shared. Retrieval-only entries describe returned evidence.
- Parentheses after a model name specify evidence forms. Semicolons separate independent paths, and an arrow applies only within its path. Brackets group multiple items; commas inside them denote parallel items.
- `+` combines mechanisms or families. In the representative table, Visual means visual page/region retrieval; Text means text retrieval/reranking; MM means multimodal retrieval; LLM/VLM means model-based selection, reranking, navigation, or region refinement.

## Generator organization and learning

| Field | Interpretation |
| --- | --- |
| **Agent: Single / Multi** | Runtime reasoning roles and collaboration. The number of model or tool components alone is not the definition. |
| **Reasoning: Single-pass** | A fixed workflow, including a single chain of thought, structured decoding, or a fixed multi-agent pipeline. |
| **Reasoning: Multi-step** | Repeated feedback from intermediate results, tool observations, or verification revises judgments and actions. |
| **Learning: Pretraining / PT** | Added training for document representations and cross-modal alignment. |
| **Learning: SFT** | Added supervised fine-tuning with answer, evidence, or action demonstrations. |
| **Learning: RL** | Added reinforcement learning with answer, evidence, or process rewards. |

**Acquisition and reasoning describe different decisions.** Multi-step reasoning can reread or verify existing evidence while acquisition remains One-shot, as in ViDoRAG. Multi-agent organization and structural parsing do not, on their own, imply Iterative acquisition or Multi-step reasoning.

The superscript **t** in Mechanism marks added retrieval, scoring, or page-selection training; a family-level marker means at least one component in that family receives such training. **Learning** records added generation-side training of answering, control, or tool components. It does not imply that every module is trained or that modules are updated jointly. A standalone Yes in Learning records added training whose type is not listed. Model entries identify the main answer model or language-backbone family, not a complete component inventory.

## Evaluation and benchmark conditions

Method tables list dimensions **quantitatively reported in the original paper**. Benchmark tables list capabilities supported by the benchmark and its public annotations. A capability label is not a score or a claim of superiority.

| Label | Meaning |
| --- | --- |
| **Ans.** | Answer correctness or quality. |
| **Ret.** | Evidence retrieval or selection, typically page hits, recall, or ranking. Some entries instead measure document retrieval, element selection, or evidence coverage; retain their table-specific exceptions. |
| **Loc.** | Within-page element or region localization, such as spatial overlap. Exceptions include layout detection, attention overlap, box-center hits, and segmentation-mask evaluation. |
| **Eff.** | Processing efficiency and cost, including parsing, indexing, and online inference. |
| **Rob.** | Robustness under controlled perturbations or interference. |

Benchmark **Granularity** is the verification level supported by public evidence annotations. It differs from method Granularity, which describes generator inputs or retrieval-only outputs. In open-domain settings, page annotations with document identities also support document verification, which the table does not list again.

Preserve the following conditions when interpreting a benchmark:

- **Input scale versus evidence span:** many input pages need not imply cross-page reasoning. `MD`, `MP`, and `SP` refer to multi-document, multi-page, and single-page evidence requirements. `Unans.` denotes questions unanswerable from the supplied evidence.
- **Candidate setting:** Open uses a cross-document candidate collection; Closed supplies one document; Open/Closed supports both. Page counts alone cannot establish relative difficulty.
- **Counting conventions:** #Docs counts documents or independent page inputs. #Pages is the mean input pages per question, using a document-level mean when necessary; Open counts the full candidate collection, and an independent image counts as one page. #Tokens is the mean text-token count per input document. #QA counts questions, queries, or localization tasks.
- **Starting representation:** benchmark entries marked for pre-extracted inputs may provide figures, tables, text, or image segments. Their results do not directly evaluate complete parsing from raw pages.
- **Source types:** `TXT/L/C/TAB/I` denotes text/layout/charts/tables/images. Public annotations determine which retrieval and localization claims can be verified.

This catalog is **not a leaderboard**. Compare results only with their input conditions, evidence annotations, and resource budgets in view. Include parsing and indexing costs alongside online inference when assessing end-to-end benefits. More pages, richer structures, or more reasoning steps do not by themselves demonstrate better evidence support.

## Dates, ordering, and qualifiers

`YY.MM` denotes first release, preferentially the first arXiv version; an earlier official release, or the official release when no preprint exists, takes precedence. An unavailable month remains `--`. Publication year, first-release month, and venue are separate fields.

Within task groups, method ordering follows final conference submission deadlines, then first release within each conference; preprints and journal papers are inserted by first release. Benchmark groups follow primary evaluation target and input scale, with ordering following the method-table convention. Preserve the manuscript's ordering rather than treating rows as a performance ranking.

Venue superscripts `F/W/D/S/I/C` denote Findings, Workshop, Datasets and Benchmarks, Short, Industry, and competition reports. Marker meanings depend on the table: `*` in direct-reading methods identifies primary single-page/image evaluation with multipage support; `*` in benchmarks identifies pre-extracted inputs. Superscript `a` identifies evaluation exceptions explained in the corresponding notes. Absence, unavailable information, and attributes that do not apply must remain distinct.

The canonical records in [data/](data/) and their generated paper pages should be read with these definitions and the original table notes. Proposed corrections should follow [CONTRIBUTING.md](CONTRIBUTING.md).

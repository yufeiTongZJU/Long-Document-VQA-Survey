# Methods with explicit retrieval

[Repository home](../README.md) · [Benchmarks](benchmarks.md) · [Direct reading](direct-reading.md) · [Explicit retrieval](explicit-retrieval.md)

**110 records.** Generated from manuscript `tables/table6_full.tex`. Source rows, groups, qualifiers, and notation are preserved.

[JSON](../data/explicit-retrieval.json) · [CSV](../data/explicit-retrieval.csv) · [Bibliography](../references.bib) · [Data dictionary](../data/README.md)

Complete comparison of methods with explicit retrieval: 20 retrieval-only and 90 document VQA methods. Ordering and date conventions follow Table 1 (representative explicit-retrieval methods); venue superscripts follow Table 4 (benchmark catalog). Mechanism specifies retrievers, evidence mappings, and retrieval training; Model gives the main generator model family. + denotes combinations and / alternatives; -- denotes unreported, unconfirmed, or inapplicable information.

**Dates and citation years.** First release is separate from the citation year in the current BibTeX. YY.MM preferentially denotes the first arXiv version; an earlier official release, or the official release when no preprint exists, takes precedence. A -- month is unavailable and is stored as null, never as an invented month.

**Order.** Source row order is preserved. Within task groups, methods follow final conference submission deadlines, then first release within each conference; preprints/journal papers are inserted by first release (Table 1 convention).

**Notation.** ✓ = present/included; ✗ = absent/excluded. `--` means unreported, unconfirmed, or inapplicable. Venue superscripts F/W/D/S/I/C mean Findings, Workshop, Datasets and Benchmarks, Short, Industry, and competition reports, respectively.

**Links.** “Paper” uses an academic URL or explicit arXiv identifier already recorded in the manuscript bibliography/provenance. Links were not independently rechecked for this repository. “Google Scholar search” is a title search, not a verified paper link.

## Browse

- [Retrieval-only methods (20)](#group-1)
- [Document VQA methods (90)](#group-2)
- [Full source notes](#source-notes)

<a id="group-1"></a>

## Retrieval-only methods

| Method / details | Venue | First release | Bib year | OCR | Deep | Modality | Gran. | Mechanism | Acq. | Eval. | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DSE](#explicit-retrieval-001) | EMNLP’24 | 24.06 | 2024 | ✗ | ✗ | Uni(V) | Page | DSE<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20multimodal%20retrieval%20via%20document%20screenshot%20embedding) |
| [ColPali](#explicit-retrieval-002) | ICLR’25 | 24.06 | 2025 | ✗ | ✗ | Uni(V) | Page | ColPali<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Colpali%3A%20Efficient%20document%20retrieval%20with%20vision%20language%20models) |
| [RobTabCol](#explicit-retrieval-003) | ACL’25 | 25.02 | 2025 | ✗ | ✗ | Uni(V) | Page | RobTabCol<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Rob. | [Google Scholar search](https://scholar.google.com/scholar?q=Real-mm-rag%3A%20A%20real-world%20multi-modal%20retrieval%20benchmark) |
| [Light-ColPali](#explicit-retrieval-004) | ACL’25<sup>F</sup> | 25.06 | 2025 | ✗ | ✗ | Uni(V) | Page | ColPali<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Paper](https://aclanthology.org/2025.findings-acl.1003/) |
| [DocMMIR](#explicit-retrieval-005) | EMNLP’25<sup>F</sup> | 25.05 | 2025 | ✓ | ✗ | Mixed(T/V) | Doc. | OpenCLIP<sup>t</sup>(D<sup>TV</sup>) | One-shot | Ret.<sup>a</sup> Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=DocMMIR%3A%20A%20Framework%20for%20Document%20Multi-modal%20Information%20Retrieval) |
| [Evo-Retriever](#explicit-retrieval-006) | CVPR’26 | 26.03 | 2026 | ✗ | ✗ | Uni(V) | Page | Evo-Retriever<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. | [Paper](https://arxiv.org/abs/2603.16455) |
| [HEAVEN](#explicit-retrieval-007) | ACL’26<sup>F</sup> | 25.10 | 2026 | ✗ | Summary | Uni(V) | Page | DSE(P<sup>V</sup>) + ColQwen(P<sup>V</sup>) | One-shot | Ret.<sup>a</sup> Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Hybrid-vector%20retrieval%20for%20visually%20rich%20documents%3A%20Combining%20single-vector%20efficiency%20and%20multi-vector%20accuracy) |
| [ReAlign](#explicit-retrieval-008) | SIGIR’26 | 26.04 | 2026 | ✗ | ✗ | Uni(V) | Page | ReAlign<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Loc.<sup>a</sup> | [Paper](https://arxiv.org/abs/2604.07419) |
| [ZipRerank](#explicit-retrieval-009) | ICML’26 | 26.05 | 2026 | ✗ | ✗ | Uni(V) | Page | DSE(P<sup>V</sup>) + ZipRerank<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Paper](https://arxiv.org/abs/2605.11864) |
| [DocRetriever](#explicit-retrieval-010) | KDD’26 | 26.05 | 2026 | ✗ | ✗ | Uni(V) | Page | ColQwen(P<sup>V</sup>) + VLM(P<sup>V</sup>) | One-shot | Ret. Eff. | [Paper](https://arxiv.org/abs/2605.30027) |
| [LMS-Retrieval](#explicit-retrieval-011) | ICDAR’26 | 26.08 | 2026 | ✓ | Tree | Uni(T) | Elem. | LMS-Retrieval<sup>t</sup>(E<sup>T</sup>) | One-shot | Ret.<sup>a</sup> Loc. | [Google Scholar search](https://scholar.google.com/scholar?q=LMS-Retrieval%3A%20Layout-Aware%2C%20Modality-Aware%2C%20Structure-Aware%20Document%20Retrieval) |
| [LightSTAR](#explicit-retrieval-012) | ECCV’26 | 26.06 | 2026 | ✗ | ✗ | Uni(V) | Page | LightSTAR<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=LightSTAR%3A%20Efficient%20Visual%20Document%20Retrieval%20via%20Lightweight%20Selection%20with%20Vision-Adaptive%20Refinement) |
| [CMDR-Embed](#explicit-retrieval-013) | ECCV’26 | 26.07 | 2026 | ✗ | ✗ | Uni(V) | Page | CMDR-Embed<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=CMDR%3A%20Contextual%20Multimodal%20Document%20Retrieval) |
| [AdaMerge](#explicit-retrieval-014) | CIKM’26 | 26.09 | 2026 | ✗ | ✗ | Uni(V) | Page | ColQwen/ColNomic(P<sup>V</sup>) | One-shot | Ret. Eff. | [Paper](https://arxiv.org/abs/2609.22562) |
| [MMRetHeads](#explicit-retrieval-015) | EMNLP’26 | 26.05 | 2026 | ✗ | ✗ | Uni(V) | Page, Elem. | MMRetHeads(P<sup>V</sup>; E<sup>V</sup>) | One-shot | Ret. Loc.<sup>a</sup> | [Paper](https://arxiv.org/abs/2605.27243) |
| [MIDR](#explicit-retrieval-016) | EMNLP’26 | 26.09 | 2026 | ✓ | Summary | Uni(T) | Page | BM25F(P<sup>T</sup>) + EmbeddingGemma(P<sup>T</sup>) | One-shot | Ret. Eff. | [Paper](https://arxiv.org/abs/2609.01316) |
| [DocPC](#explicit-retrieval-017) | arXiv’26 | 26.08 | 2026 | ✗ | ✗ | Uni(V) | Doc. | ColQwen<sup>t</sup>(D<sup>V</sup>) | One-shot | Ret.<sup>a</sup> Eff. | [Paper](https://arxiv.org/abs/2608.25434) |
| [MarginMerge](#explicit-retrieval-018) | arXiv’26 | 26.08 | 2026 | ✗ | ✗ | Uni(V) | Page | MarginMerge<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Paper](https://arxiv.org/abs/2608.02969) |
| [DistilVDR](#explicit-retrieval-019) | EMNLP’26<sup>W</sup> | 26.08 | 2026 | ✗ | ✗ | Uni(V) | Page | DistilVDR<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. Eff. | [Paper](https://arxiv.org/abs/2608.10636) |
| [ConceptFormer](#explicit-retrieval-020) | arXiv’26 | 26.08 | 2026 | ✗ | ✗ | Uni(V) | Page | ConceptFormer<sup>t</sup>(P<sup>V</sup>) | One-shot | Ret. | [Paper](https://arxiv.org/abs/2608.15698) |

Each expandable record below contains every source column, including the complete retrieval mechanism.

<a id="explicit-retrieval-001"></a>

<details>
<summary>DSE — Unifying multimodal retrieval via document screenshot embedding</summary>

**Paper:** Unifying multimodal retrieval via document screenshot embedding  
**Authors:** Ma, Xueguang and Lin, Sheng-Chieh and Li, Minghan and Chen, Wenhu and Lin, Jimmy  
**Citation:** `ma2024unifying`; current BibTeX year **2024**; first release **24.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20multimodal%20retrieval%20via%20document%20screenshot%20embedding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:72`; order 1.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’24 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | DSE<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Unifying multimodal retrieval via document screenshot embedding |
| author | Ma, Xueguang and Lin, Sheng-Chieh and Li, Minghan and Chen, Wenhu and Lin, Jimmy |
| booktitle | Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing |
| pages | 6492--6505 |
| year | 2024 |

</details>

<a id="explicit-retrieval-002"></a>

<details>
<summary>ColPali — Colpali: Efficient document retrieval with vision language models</summary>

**Paper:** Colpali: Efficient document retrieval with vision language models  
**Authors:** Faysse, Manuel and Sibille, Hugues and Wu, Tony and Omrani, Bilel and Viaud, Gautier and Hudelot, Céline and Colombo, Pierre  
**Citation:** `ref7`; current BibTeX year **2025**; first release **24.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Colpali%3A%20Efficient%20document%20retrieval%20with%20vision%20language%20models). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:73`; order 2.

| Field | Source value |
| --- | --- |
| Venue | ICLR’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Colpali: Efficient document retrieval with vision language models |
| author | Faysse, Manuel and Sibille, Hugues and Wu, Tony and Omrani, Bilel and Viaud, Gautier and Hudelot, Céline and Colombo, Pierre |
| booktitle | International Conference on Learning Representations |
| year | 2025 |
| volume | 2025 |
| pages | 61424--61449 |

</details>

<a id="explicit-retrieval-003"></a>

<details>
<summary>RobTabCol — Real-mm-rag: A real-world multi-modal retrieval benchmark</summary>

**Paper:** Real-mm-rag: A real-world multi-modal retrieval benchmark  
**Authors:** Wasserman, Navve and Pony, Roi and Naparstek, Oshri and Goldfarb, Adi Raz and Schwartz, Eli and Barzelay, Udi and Karlinsky, Leonid  
**Citation:** `ref88`; current BibTeX year **2025**; first release **25.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Real-mm-rag%3A%20A%20real-world%20multi-modal%20retrieval%20benchmark). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:74`; order 3.

| Field | Source value |
| --- | --- |
| Venue | ACL’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | RobTabCol<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Rob. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Real-mm-rag: A real-world multi-modal retrieval benchmark |
| author | Wasserman, Navve and Pony, Roi and Naparstek, Oshri and Goldfarb, Adi Raz and Schwartz, Eli and Barzelay, Udi and Karlinsky, Leonid |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2025 |
| pages | 31660--31683 |

</details>

<a id="explicit-retrieval-004"></a>

<details>
<summary>Light-ColPali — Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings</summary>

**Paper:** Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings  
**Authors:** Ma, Yubo and Li, Jinsong and Zang, Yuhang and Wu, Xiaobao and Dong, Xiaoyi and Zhang, Pan and Cao, Yuhang and Duan, Haodong and Wang, Jiaqi and Cao, Yixin and Sun, Aixin  
**Citation:** `ref31`; current BibTeX year **2025**; first release **25.06**.  
**Source:** [Paper](https://aclanthology.org/2025.findings-acl.1003/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:75`; order 4.

| Field | Source value |
| --- | --- |
| Venue | ACL’25<sup>F</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings |
| author | Ma, Yubo and Li, Jinsong and Zang, Yuhang and Wu, Xiaobao and Dong, Xiaoyi and Zhang, Pan and Cao, Yuhang and Duan, Haodong and Wang, Jiaqi and Cao, Yixin and Sun, Aixin |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2025 |
| pages | 19568--19580 |
| year | 2025 |

</details>

<a id="explicit-retrieval-005"></a>

<details>
<summary>DocMMIR — DocMMIR: A Framework for Document Multi-modal Information Retrieval</summary>

**Paper:** DocMMIR: A Framework for Document Multi-modal Information Retrieval  
**Authors:** Li, Zirui and Siwei Wu and Yizhi Li and Xingyu Wang and Yi Zhou and Chenghua Lin  
**Citation:** `ref19`; current BibTeX year **2025**; first release **25.05**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=DocMMIR%3A%20A%20Framework%20for%20Document%20Multi-modal%20Information%20Retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:76`; order 5.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25<sup>F</sup> |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Doc. |
| Mechanism | OpenCLIP<sup>t</sup>(D<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocMMIR: A Framework for Document Multi-modal Information Retrieval |
| author | Li, Zirui and Siwei Wu and Yizhi Li and Xingyu Wang and Yi Zhou and Chenghua Lin |
| booktitle | EMNLP (Findings) |
| pages | 13117--13130 |
| year | 2025 |

</details>

<a id="explicit-retrieval-006"></a>

<details>
<summary>Evo-Retriever — Evo-retriever: Llm-guided curriculum evolution with viewpoint-pathway collaboration for multimodal document retrieval</summary>

**Paper:** Evo-retriever: Llm-guided curriculum evolution with viewpoint-pathway collaboration for multimodal document retrieval  
**Authors:** Li, Weiqing and Jinyue Guo and Yaqi Wang and Haiyang Xiao and Yuewei Zhang and Guohua Liu and Hao Henry Wang  
**Citation:** `ref131`; current BibTeX year **2026**; first release **26.03**.  
**Source:** [Paper](https://arxiv.org/abs/2603.16455). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:77`; order 6.

| Field | Source value |
| --- | --- |
| Venue | CVPR’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | Evo-Retriever<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Evo-retriever: Llm-guided curriculum evolution with viewpoint-pathway collaboration for multimodal document retrieval |
| author | Li, Weiqing and Jinyue Guo and Yaqi Wang and Haiyang Xiao and Yuewei Zhang and Guohua Liu and Hao Henry Wang |
| journal | arXiv preprint arXiv:2603.16455 |
| year | 2026 |

</details>

<a id="explicit-retrieval-007"></a>

<details>
<summary>HEAVEN — Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy</summary>

**Paper:** Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy  
**Authors:** Kim, Juyeon and Geon Lee and Dongwon Choi and Taeuk Kim and Kijung Shin  
**Citation:** `ref80`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Hybrid-vector%20retrieval%20for%20visually%20rich%20documents%3A%20Combining%20single-vector%20efficiency%20and%20multi-vector%20accuracy). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:78`; order 7.

| Field | Source value |
| --- | --- |
| Venue | ACL’26<sup>F</sup> |
| OCR | ✗ |
| Deep | Summary |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | DSE(P<sup>V</sup>) + ColQwen(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy |
| author | Kim, Juyeon and Geon Lee and Dongwon Choi and Taeuk Kim and Kijung Shin |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2026 |
| pages | 1073--1089 |
| year | 2026 |

</details>

<a id="explicit-retrieval-008"></a>

<details>
<summary>ReAlign — ReAlign: Optimizing the Visual Document Retriever with Reasoning-Guided Fine-Grained Alignment</summary>

**Paper:** ReAlign: Optimizing the Visual Document Retriever with Reasoning-Guided Fine-Grained Alignment  
**Authors:** Yang, Hao and Yifan Ji and Zhipeng Xu and Zhenghao Liu and Yukun Yan and Zulong Chen and Shuo Wang and Yu Gu and Ge Yu  
**Citation:** `ref84`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://arxiv.org/abs/2604.07419). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:79`; order 8.

| Field | Source value |
| --- | --- |
| Venue | SIGIR’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ReAlign<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Loc.<sup>a</sup> |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | ReAlign: Optimizing the Visual Document Retriever with Reasoning-Guided Fine-Grained Alignment |
| author | Yang, Hao and Yifan Ji and Zhipeng Xu and Zhenghao Liu and Yukun Yan and Zulong Chen and Shuo Wang and Yu Gu and Ge Yu |
| journal | arXiv preprint arXiv:2604.07419 |
| year | 2026 |

</details>

<a id="explicit-retrieval-009"></a>

<details>
<summary>ZipRerank — Very efficient listwise multimodal reranking for long documents</summary>

**Paper:** Very efficient listwise multimodal reranking for long documents  
**Authors:** Sun, Yiqun and Pengfei Wei and Lawrence B. Hsieh  
**Citation:** `ref125`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.11864). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:80`; order 9.

| Field | Source value |
| --- | --- |
| Venue | ICML’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | DSE(P<sup>V</sup>) + ZipRerank<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Very efficient listwise multimodal reranking for long documents |
| author | Sun, Yiqun and Pengfei Wei and Lawrence B. Hsieh |
| journal | arXiv preprint arXiv:2605.11864 |
| year | 2026 |

</details>

<a id="explicit-retrieval-010"></a>

<details>
<summary>DocRetriever — DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval with Comprehensive Benchmark</summary>

**Paper:** DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval with Comprehensive Benchmark  
**Authors:** Hu, Ruofan and Zhu, Menghui and Zhu, Jieming and Chen, Bo and Xu, Shengyang and Hong, Minjie and Yang, Xiaoda and Zhou, Sashuai and Tang, Li and Jin, Tao and Zhao, Zhou  
**Citation:** `ref106`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.30027). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:81`; order 10.

| Field | Source value |
| --- | --- |
| Venue | KDD’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval with Comprehensive Benchmark |
| author | Hu, Ruofan and Zhu, Menghui and Zhu, Jieming and Chen, Bo and Xu, Shengyang and Hong, Minjie and Yang, Xiaoda and Zhou, Sashuai and Tang, Li and Jin, Tao and Zhao, Zhou |
| booktitle | Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2 |
| pages | 1780--1791 |
| year | 2026 |

</details>

<a id="explicit-retrieval-011"></a>

<details>
<summary>LMS-Retrieval — LMS-Retrieval: Layout-Aware, Modality-Aware, Structure-Aware Document Retrieval</summary>

**Paper:** LMS-Retrieval: Layout-Aware, Modality-Aware, Structure-Aware Document Retrieval  
**Authors:** Qin, Man and French, Tim and Liu, Wei  
**Citation:** `ref127`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=LMS-Retrieval%3A%20Layout-Aware%2C%20Modality-Aware%2C%20Structure-Aware%20Document%20Retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:82`; order 11.

| Field | Source value |
| --- | --- |
| Venue | ICDAR’26 |
| OCR | ✓ |
| Deep | Tree |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | LMS-Retrieval<sup>t</sup>(E<sup>T</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret.<sup>a</sup> Loc. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | LMS-Retrieval: Layout-Aware, Modality-Aware, Structure-Aware Document Retrieval |
| author | Qin, Man and French, Tim and Liu, Wei |
| booktitle | International Conference on Document Analysis and Recognition |
| year | 2026 |
| pages | 123--139 |
| publisher | Springer Nature Switzerland |
| address | Cham |

</details>

<a id="explicit-retrieval-012"></a>

<details>
<summary>LightSTAR — LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement</summary>

**Paper:** LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement  
**Authors:** Guan, Tongkun and Haocheng Wang and Wei Shen and Xiaokang Yang  
**Citation:** `ref85`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=LightSTAR%3A%20Efficient%20Visual%20Document%20Retrieval%20via%20Lightweight%20Selection%20with%20Vision-Adaptive%20Refinement). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:83`; order 12.

| Field | Source value |
| --- | --- |
| Venue | ECCV’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | LightSTAR<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement |
| author | Guan, Tongkun and Haocheng Wang and Wei Shen and Xiaokang Yang |
| booktitle | European Conference on Computer Vision |
| pages | 669--687 |
| publisher | Springer Nature Switzerland |
| address | Cham |
| year | 2026 |

</details>

<a id="explicit-retrieval-013"></a>

<details>
<summary>CMDR-Embed — CMDR: Contextual Multimodal Document Retrieval</summary>

**Paper:** CMDR: Contextual Multimodal Document Retrieval  
**Authors:** Tanaka, Ryota and Taku Hasegawa and Kyosuke Nishida  
**Citation:** `ref79`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=CMDR%3A%20Contextual%20Multimodal%20Document%20Retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:84`; order 13.

| Field | Source value |
| --- | --- |
| Venue | ECCV’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | CMDR-Embed<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | CMDR: Contextual Multimodal Document Retrieval |
| author | Tanaka, Ryota and Taku Hasegawa and Kyosuke Nishida |
| booktitle | European Conference on Computer Vision |
| year | 2026 |
| pages | 77--95 |
| month | September |
| publisher | Springer Nature Switzerland |
| address | Cham |

</details>

<a id="explicit-retrieval-014"></a>

<details>
<summary>AdaMerge — AdaMerge: Tuning-Free Patch Compression for Multi-Vector Visual Document Retrieval</summary>

**Paper:** AdaMerge: Tuning-Free Patch Compression for Multi-Vector Visual Document Retrieval  
**Authors:** You, Jianxin and Kun Ni  
**Citation:** `ref144`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.22562). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:85`; order 14.

| Field | Source value |
| --- | --- |
| Venue | CIKM’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen/ColNomic(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | AdaMerge: Tuning-Free Patch Compression for Multi-Vector Visual Document Retrieval |
| author | You, Jianxin and Kun Ni |
| journal | arXiv preprint arXiv:2609.22562 |
| year | 2026 |

</details>

<a id="explicit-retrieval-015"></a>

<details>
<summary>MMRetHeads — Can Retrieval Heads See Images? Multimodal Retrieval Heads in Long-Context Vision-Language Models</summary>

**Paper:** Can Retrieval Heads See Images? Multimodal Retrieval Heads in Long-Context Vision-Language Models  
**Authors:** Li, Aaron Branson Cigres and Wang, Zhaowei and Zhao, Yu and Du, Yiming and Li, Haobo and Ren, Xiyu and Wong, Ginny and See, Simon and Luo, Lishu and Duan, Haodong and Minervini, Pasquale and Song, Yangqiu  
**Citation:** `ref126`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.27243). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:86`; order 15.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | MMRetHeads(P<sup>V</sup>; E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Loc.<sup>a</sup> |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Can Retrieval Heads See Images? Multimodal Retrieval Heads in Long-Context Vision-Language Models |
| author | Li, Aaron Branson Cigres and Wang, Zhaowei and Zhao, Yu and Du, Yiming and Li, Haobo and Ren, Xiyu and Wong, Ginny and See, Simon and Luo, Lishu and Duan, Haodong and Minervini, Pasquale and Song, Yangqiu |
| journal | arXiv preprint arXiv:2605.27243 |
| year | 2026 |

</details>

<a id="explicit-retrieval-016"></a>

<details>
<summary>MIDR — MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval</summary>

**Paper:** MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval  
**Authors:** Mahata, Debanjan and Atharva Tendle and Daniel Preotiuc-Pietro and Yong Zhuang and Ozan Irsoy  
**Citation:** `ref135`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.01316). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:87`; order 16.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26 |
| OCR | ✓ |
| Deep | Summary |
| Modality | Uni(T) |
| Gran. | Page |
| Mechanism | BM25F(P<sup>T</sup>) + EmbeddingGemma(P<sup>T</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval |
| author | Mahata, Debanjan and Atharva Tendle and Daniel Preotiuc-Pietro and Yong Zhuang and Ozan Irsoy |
| journal | arXiv preprint arXiv:2609.01316 |
| year | 2026 |

</details>

<a id="explicit-retrieval-017"></a>

<details>
<summary>DocPC — DocPC: Document-Level Visual Retrieval via Representative Page Composition</summary>

**Paper:** DocPC: Document-Level Visual Retrieval via Representative Page Composition  
**Authors:** You, Chengsong and Zhou, Junwei and Cao, Xiaoyu and Wang, Weiyao and Xu, Yiwei and Zhao, Ziyan and Sun, Zhen and Zhu, Qicheng and Fu, Xuanyi and Chen, Yufan and others  
**Citation:** `ref122`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.25434). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:88`; order 17.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Doc. |
| Mechanism | ColQwen<sup>t</sup>(D<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocPC: Document-Level Visual Retrieval via Representative Page Composition |
| author | You, Chengsong and Zhou, Junwei and Cao, Xiaoyu and Wang, Weiyao and Xu, Yiwei and Zhao, Ziyan and Sun, Zhen and Zhu, Qicheng and Fu, Xuanyi and Chen, Yufan and others |
| journal | arXiv preprint arXiv:2608.25434 |
| year | 2026 |

</details>

<a id="explicit-retrieval-018"></a>

<details>
<summary>MarginMerge — Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document Retrievers</summary>

**Paper:** Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document Retrievers  
**Authors:** Mahdizadeh, Ailar and Aria Salari and Sohail Rajabi and Shahriar Mirabbasi and Panos Nasiopoulos and Alireza Morsali  
**Citation:** `ref81`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.02969). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:89`; order 18.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | MarginMerge<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document Retrievers |
| author | Mahdizadeh, Ailar and Aria Salari and Sohail Rajabi and Shahriar Mirabbasi and Panos Nasiopoulos and Alireza Morsali |
| journal | arXiv preprint arXiv:2608.02969 |
| year | 2026 |

</details>

<a id="explicit-retrieval-019"></a>

<details>
<summary>DistilVDR — DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation</summary>

**Paper:** DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation  
**Authors:** Liu, Zhuchenyang and Ziyi Wang and Yao Zhang and Yu Xiao  
**Citation:** `ref91`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.10636). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:90`; order 19.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26<sup>W</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | DistilVDR<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation |
| author | Liu, Zhuchenyang and Ziyi Wang and Yao Zhang and Yu Xiao |
| journal | arXiv preprint arXiv:2608.10636 |
| year | 2026 |

</details>

<a id="explicit-retrieval-020"></a>

<details>
<summary>ConceptFormer — ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval</summary>

**Paper:** ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval  
**Authors:** Peng, Chunyi and Xu, Zhipeng and Yan, Yukun and Liu, Zhenghao and Yu, Shi and Mei, Sen and Sun, Yubo and Zhang, Yongheng and Zhou, Jie and Gu, Yu and Yu, Ge and Sun, Maosong  
**Citation:** `ref132`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.15698). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:91`; order 20.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ConceptFormer<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | -- |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval |
| author | Peng, Chunyi and Xu, Zhipeng and Yan, Yukun and Liu, Zhenghao and Yu, Shi and Mei, Sen and Sun, Yubo and Zhang, Yongheng and Zhou, Jie and Gu, Yu and Yu, Ge and Sun, Maosong |
| journal | arXiv preprint arXiv:2608.15698 |
| year | 2026 |

</details>

<a id="group-2"></a>

## Document VQA methods

| Method / details | Venue | First release | Bib year | Modality | Gran. | Acq. | Agent | Reasoning | Model | Eval. | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [MHST](#explicit-retrieval-021) | MM’22 | 22.07 | 2022 | Uni(T) | Page, Elem. | One-shot | Single | Single-pass | LayoutLM | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=Towards%20complex%20document%20understanding%20by%20discrete%20reasoning) |
| [CREAM](#explicit-retrieval-022) | ACM MM’24 | 24.10 | 2024 | Uni(T) | Page, Elem. | One-shot | Single | Single-pass | Llama | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=Cream%3A%20coarse-to-fine%20retrieval%20and%20multi-modal%20efficient%20tuning%20for%20document%20vqa) |
| [VisRAG](#explicit-retrieval-023) | ICLR’25 | 24.10 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | MiniCPM-V/GPT-4o | Ans. Ret. Eff. | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3640a1997a4c9571cea9db2c82e1fc35-Abstract-Conference.html) |
| [SV-RAG](#explicit-retrieval-024) | ICLR’25 | 24.11 | 2024 | Uni(V) | Page | One-shot | Single | Single-pass | PaliGemma/Phi-Vision/InternVL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2411.01106) |
| [PDF-WuKong](#explicit-retrieval-025) | IJCV’26 | 24.10 | 2026 | Mixed(T/V) | Elem. | One-shot | Single | Single-pass | InternLM-XComposer | Ans. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Wukong%3A%20A%20large%20multimodal%20model%20for%20efficient%20long%20pdf%20reading%20with%20end-to-end%20sparse%20sampling) |
| [VisDoMRAG](#explicit-retrieval-026) | NAACL’25 | 24.12 | 2025 | Mixed(T/V) | Page, Elem. | One-shot | Multi | Single-pass | Qwen-VL/Gemini/GPT-4o | Ans. Ret. | [Google Scholar search](https://scholar.google.com/scholar?q=Visdom%3A%20Multi-document%20qa%20with%20visually%20rich%20elements%20using%20multimodal%20retrieval-augmented%20generation) |
| [VDocRAG](#explicit-retrieval-027) | CVPR’25 | 25.04 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Phi-Vision | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Vdocrag%3A%20Retrieval-augmented%20generation%20over%20visually-rich%20documents) |
| [SuperRAG](#explicit-retrieval-028) | NAACL’25<sup>I</sup> | 25.02 | 2025 | Uni(T) | Page, Elem. | One-shot | Single | Single-pass | GPT-4o | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=Superrag%3A%20Beyond%20rag%20with%20layout-aware%20graph%20modeling) |
| [Doc-React](#explicit-retrieval-029) | ACL’25<sup>S</sup> | 24.12 | 2025 | Uni(V) | Page | Iterative | Single | Multi-step | GPT-4o | Ans. | [Paper](https://aclanthology.org/2025.acl-short.6/) |
| [VISA](#explicit-retrieval-030) | ACL’25 | 24.12 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Loc. | [Google Scholar search](https://scholar.google.com/scholar?q=Visa%3A%20Retrieval%20augmented%20generation%20with%20visual%20source%20attribution) |
| [NeuSym-RAG](#explicit-retrieval-031) | ACL’25 | 25.05 | 2025 | Mixed(T/V) | Doc., Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret.<sup>a</sup> Eff. | [Paper](https://aclanthology.org/2025.acl-long.311/) |
| [MDocAgent](#explicit-retrieval-032) | arXiv’25 | 25.03 | 2025 | Mixed(T/V) | Page | One-shot | Multi | Single-pass | Llama + Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2503.13964) |
| [FRAG](#explicit-retrieval-033) | arXiv’25 | 25.04 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | LLaVA/InternVL | Ans. | [Paper](https://arxiv.org/abs/2504.17447) |
| [VRAG-RL](#explicit-retrieval-034) | NIPS’25 | 25.05 | 2026 | Uni(V) | Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/529b876b5d87f997e98ed925a3ce9f01-Abstract-Conference.html) |
| [Dual-Stream RAG](#explicit-retrieval-035) | APWeb-WAIM’25 | 26.01 | 2025 | Mixed(T/V) | Page | One-shot | Multi | Single-pass | Qwen-VL | Ans. Ret. | [Google Scholar search](https://scholar.google.com/scholar?q=Dual-Stream%20Adaptive%20Retrieval%20and%20Hierarchical%20Agent%20Collaboration%20for%20Document%20Visual%20QA) |
| [Retrieval-aware Tuning](#explicit-retrieval-036) | EMNLP’25 | 24.11 | 2025 | Uni(V) | Page, Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Rob. | [Google Scholar search](https://scholar.google.com/scholar?q=M-longdoc%3A%20A%20benchmark%20for%20multimodal%20super-long%20document%20understanding%20and%20a%20retrieval-aware%20tuning%20framework) |
| [ViDoRAG](#explicit-retrieval-037) | EMNLP’25 | 25.02 | 2025 | Mixed(T/V) | Page | One-shot | Multi | Multi-step | GPT-4o/Qwen-VL/Llama-Vision | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Vidorag%3A%20Visual%20document%20retrieval-augmented%20generation%20via%20dynamic%20iterative%20reasoning%20agents) |
| [RGenCite](#explicit-retrieval-038) | EMNLP’25 | 25.05 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Loc.<sup>a</sup> | [Google Scholar search](https://scholar.google.com/scholar?q=Finragbench-v%3A%20A%20benchmark%20for%20multimodal%20rag%20with%20visual%20citation%20in%20the%20financial%20domain) |
| [SimpleDoc](#explicit-retrieval-039) | EMNLP’25 | 25.06 | 2025 | Mixed(T/V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=SimpleDoc%3A%20Multi%E2%80%90Modal%20Document%20Understanding%20with%20Dual%E2%80%90Cue%20Page%20Retrieval%20and%20Iterative%20Refinement) |
| [MoLoRAG](#explicit-retrieval-040) | EMNLP’25 | 25.09 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL/DeepSeek-VL/LLaVA | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Molorag%3A%20Bootstrapping%20document%20understanding%20via%20multi-modal%20logic-aware%20retrieval) |
| [LILaC](#explicit-retrieval-041) | EMNLP’25 | 25.11 | 2025 | Mixed(T/V) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret.<sup>a</sup> Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Lilac%3A%20Late%20interacting%20in%20layered%20component%20graph%20for%20open-domain%20multimodal%20multihop%20retrieval) |
| [DocAgent](#explicit-retrieval-042) | EMNLP’25 | 25.11 | 2025 | Uni(T) | Page, Elem. | Iterative | Multi | Multi-step | GPT-4o/Claude/Gemini | Ans. Ret. Eff. Rob. | [Google Scholar search](https://scholar.google.com/scholar?q=Docagent%3A%20An%20agentic%20framework%20for%20multi-modal%20long-context%20document%20understanding) |
| [M3DocRAG](#explicit-retrieval-043) | ICCV’25<sup>W</sup> | 24.11 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=M3docvqa%3A%20Multi-modal%20multi-page%20multi-document%20understanding) |
| [MMGraphRAG](#explicit-retrieval-044) | arXiv’25 | 25.07 | 2025 | Uni(T) | Elem. | One-shot | Single | Single-pass | Qwen + InternVL | Ans. Eff. | [Paper](https://arxiv.org/abs/2507.20804) |
| [RegionRAG](#explicit-retrieval-045) | AAAI’26 | 25.10 | 2026 | Uni(V) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37597) |
| [URaG](#explicit-retrieval-046) | AAAI’26 | 25.11 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=URaG%3A%20Unified%20retrieval%20and%20generation%20in%20multimodal%20LLMs%20for%20efficient%20long%20document%20understanding) |
| [M3RAG](#explicit-retrieval-047) | MMM’26 | 26.02 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Multi | Multi-step | Mistral + (MiniCPM-V/Qwen-VL) | Ans. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=M3RAG%3A%20Orchestrating%20Multi-agent%20Reasoning%20for%20Multi-hop%2C%20Multi-modal%20Understanding) |
| [Agentic Hybrid (EXTRACTOR)](#explicit-retrieval-048) | ICLR’26 | 25.09 | 2026 | Uni(T) | Doc., Page, Elem. | Iterative | Single | Multi-step | Qwen | Ans. Ret.<sup>a</sup> Eff. | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/10d35352a92bb40943bb4ed096a407b6-Abstract-Conference.html) |
| [SCAN](#explicit-retrieval-049) | EACL’26<sup>F</sup> | 25.05 | 2026 | Uni(V) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Loc. | [Google Scholar search](https://scholar.google.com/scholar?q=SCAN%3A%20Semantic%20Document%20Layout%20Analysis%20for%20Textual%20and%20Visual%20Retrieval-Augmented%20Generation) |
| [SCoPE VLM](#explicit-retrieval-050) | EACL’26 | 25.10 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=SCoPE%20VLM%3A%20Selective%20Context%20Processing%20for%20Efficient%20Document%20Navigation%20in%20Vision-Language%20Models) |
| [Doc-Researcher](#explicit-retrieval-051) | WWW’26 | 25.10 | 2026 | Mixed(T/V) | Doc., Page, Elem. | Iterative | Multi | Multi-step | Qwen/DeepSeek-R1 | Ans. Ret.<sup>a</sup> Loc. Eff. | [Paper](https://doi.org/10.1145/3774904.3792599) |
| [DMAP](#explicit-retrieval-052) | WWW’26 | 26.01 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Multi | Multi-step | GPT-4o/Qwen | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=Dmap%3A%20Human-aligned%20structural%20document%20map%20for%20multimodal%20document%20understanding) |
| [RAG-Anything](#explicit-retrieval-053) | arXiv’25 | 25.10 | 2025 | Uni(T) | Elem. | One-shot | Single | Single-pass | GPT-4o | Ans. | [Paper](https://arxiv.org/abs/2510.12323) |
| [MACT](#explicit-retrieval-054) | CVPR’26 | 25.08 | 2026 | -- | -- | -- | Multi | Multi-step | Qwen-VL + Qwen/MiMo-VL + MiMo/InternVL | Ans. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Visual%20document%20understanding%20and%20reasoning%3A%20A%20multi-agent%20collaboration%20framework%20with%20agent-wise%20adaptive%20test-time%20scaling) |
| [SLEUTH](#explicit-retrieval-055) | CVPR’26 | 25.11 | 2026 | Uni(V) | Page, Elem. | One-shot | Multi | Single-pass | Qwen-VL/GLM-V/Gemini | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=Resolving%20evidence%20sparsity%3A%20Agentic%20context%20engineering%20for%20long-document%20understanding) |
| [RobustVisRAG](#explicit-retrieval-056) | CVPR’26 | 26.02 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | MiniCPM-V | Ans. Ret. Rob. | [Google Scholar search](https://scholar.google.com/scholar?q=RobustVisRAG%3A%20Causality-Aware%20Vision-Based%20Retrieval-Augmented%20Generation%20under%20Visual%20Degradations) |
| [DocPrune](#explicit-retrieval-057) | CVPR’26 | 26.04 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Eff. | [Paper](https://arxiv.org/abs/2604.22281) |
| [HKRAG](#explicit-retrieval-058) | arXiv’25 | 25.11 | 2025 | Uni(V) | Page | One-shot | Multi | Multi-step | Phi-Vision | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2511.20227) |
| [CogDoc](#explicit-retrieval-059) | arXiv’25 | 25.12 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. | [Paper](https://arxiv.org/abs/2512.12658) |
| [LAD-RAG](#explicit-retrieval-060) | ACL’26 | 25.10 | 2026 | Uni(T) | -- | Iterative | Single | Multi-step | GPT-4o/Phi-Vision/Pixtral/InternVL | Ans. Ret. Eff. | [Paper](https://aclanthology.org/2026.acl-long.724/) |
| [ALDEN](#explicit-retrieval-061) | ACL’26 | 25.10 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=ALDEN%3A%20Reinforcement%20Learning%20for%20Active%20Navigation%20and%20Evidence%20Gathering%20in%20Long%20Documents) |
| [SlideAgent](#explicit-retrieval-062) | ACL’26 | 25.10 | 2026 | Uni(T) | Page, Elem. | One-shot | Multi | Single-pass | GPT-4o/InternVL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=SlideAgent%3A%20Hierarchical%20Agentic%20Framework%20for%20Multi-Page%20Visual%20Document%20Understanding) |
| [DocLens](#explicit-retrieval-063) | ACL’26 | 25.11 | 2026 | Mixed(T/V) | Page, Elem. | One-shot | Multi | Single-pass | Gemini/Claude | Ans. Ret. Loc. | [Google Scholar search](https://scholar.google.com/scholar?q=Doclens%3A%20A%20tool-augmented%20multi-agent%20framework%20for%20long%20visual%20document%20understanding) |
| [Lang2Act](#explicit-retrieval-064) | ACL’26<sup>F</sup> | 26.01 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Loc.<sup>a</sup> Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Lang2act%3A%20Fine-grained%20visual%20reasoning%20through%20self-emergent%20linguistic%20toolchains) |
| [MAB-DQA](#explicit-retrieval-065) | ACL’26 | 26.04 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=MAB-DQA%3A%20Addressing%20query%20aspect%20importance%20in%20document%20question%20answering%20with%20multi-armed%20bandits) |
| [Doc-V&#42;](#explicit-retrieval-066) | ACL’26 | 26.04 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://aclanthology.org/2026.acl-long.2129/) |
| [MM-Doc-R1](#explicit-retrieval-067) | ACL’26<sup>F</sup> | 26.04 | 2026 | Uni(T) | Page | Iterative | Multi | Multi-step | Qwen + Qwen-VL | Ans. Ret. Eff. | [Paper](https://aclanthology.org/2026.findings-acl.1488/) |
| [HiKEY](#explicit-retrieval-068) | ACL’26 | 26.05 | 2026 | Mixed(T/V) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret.<sup>a</sup> Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=HiKEY%3A%20Hierarchical%20Multimodal%20Retrieval%20for%20Open-Domain%20Document%20Question%20Answering) |
| [TRACE](#explicit-retrieval-069) | ACL’26 | 26.07 | 2026 | Uni(V) | Page | One-shot | Multi | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=TRACE%3A%20Traversal%20Retrieval-Augmented%20Chain%20of%20Evidence%20for%20Document%20Understanding) |
| [CAPS](#explicit-retrieval-070) | ACL’26 | 26.07 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL/LLaVA/DeepSeek-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Attention%20as%20Selector%3A%20Unlocking%20VLM%20Attention%20for%20Long%20Document%20Page%20Retrieval) |
| [FUMA](#explicit-retrieval-071) | ACL’26 | 26.07 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=Flow-Based%20Page%20Unique%20Semantic%20Mapping%20Architecture%20for%20Document%20Visual%20Question%20Answering) |
| [MDocRAG-RL](#explicit-retrieval-072) | ACL’26<sup>F</sup> | 26.07 | 2026 | Uni(V) | Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=MDocRAG-RL%3A%20Empowering%20Multi-Modal%20Document%20RAG%20via%20Complex%20Visual%20Reasoning%20with%20Reinforcement%20Learning) |
| [G<sup>2</sup>-Reader](#explicit-retrieval-073) | ICML’26 | 26.01 | 2026 | Uni(T) | Elem. | Iterative | Multi | Multi-step | Qwen-VL | Ans. Ret.<sup>a</sup> Eff. | [Paper](https://arxiv.org/abs/2601.22055) |
| [VimRAG](#explicit-retrieval-074) | ICML’26 | 26.02 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2602.12735) |
| [UniDocVLM](#explicit-retrieval-075) | KDD’26 | 26.08 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=Unidocvlm%3A%20Enhancing%20visual%20reasoning%20and%20document%20understanding%20for%20vlm%20via%20reinforcement%20learning) |
| [MLDocRAG](#explicit-retrieval-076) | arXiv’26 | 26.02 | 2026 | Uni(T) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2602.10271) |
| [MM-BizRAG](#explicit-retrieval-077) | ACL’26<sup>I</sup> | 26.06 | 2026 | Uni(T) | Page, Elem. | One-shot | Single | Single-pass | GPT-4.1 | Ans. Eff. | [Google Scholar search](https://scholar.google.com/scholar?q=MM-BizRAG%3A%20Rethinking%20Multimodal%20Retrieval-Augmented%20Generation%20for%20General%20Purpose%20Enterprise%20Q%26A) |
| [MoDora](#explicit-retrieval-078) | PACMMOD’26 | 26.02 | 2026 | Mixed(T/V) | Elem. | One-shot | Single | Single-pass | GPT-5 | Ans. Ret.<sup>a</sup> Eff. | [Paper](https://arxiv.org/abs/2602.23061) |
| [AdaNav](#explicit-retrieval-079) | ICDAR’26 | 26.08 | 2026 | -- | Page, Elem. | -- | Multi | -- | -- | Ans. | [Google Scholar search](https://scholar.google.com/scholar?q=AdaNav%3A%20Query-Adaptive%20Multi-granularity%20Navigation%20for%20Long%20Document%20Understanding) |
| [VisRAG 2.0](#explicit-retrieval-080) | ACM MM’26 | 25.10 | 2025 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2510.09733) |
| [VISOR](#explicit-retrieval-081) | ACM MM’26 | 26.04 | 2026 | Uni(V) | Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2604.09508) |
| [LFRAG](#explicit-retrieval-082) | arXiv’26 | 26.04 | 2026 | Uni(V) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret.<sup>a</sup> Eff. | [Paper](https://arxiv.org/abs/2605.22829) |
| [BayesRAG](#explicit-retrieval-083) | NIPS’26 | 26.01 | 2026 | Mixed(T/V) | Page, Elem. | One-shot | Single | Single-pass | GPT-4o | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2601.07329) |
| [AgenticOCR](#explicit-retrieval-084) | NIPS’26 | 26.02 | 2026 | Mixed(T/V) | Page, Elem. | One-shot | Single | Multi-step | Qwen-VL + Gemini | Ans. Ret. Loc. Eff. | [Paper](https://arxiv.org/abs/2602.24134) |
| [DocAtlas](#explicit-retrieval-085) | NIPS’26 | 26.07 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2608.07527) |
| [DocDancer](#explicit-retrieval-086) | EMNLP’26 | 26.01 | 2026 | Uni(T) | Page, Elem. | Iterative | Single | Multi-step | Qwen + Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2601.05163) |
| [Agent Consolidation](#explicit-retrieval-087) | EMNLP’26<sup>F</sup> | 26.01 | 2026 | Uni(T) | Page, Elem. | Iterative | Single | Multi-step | Qwen | Ans. Eff. | [Paper](https://arxiv.org/abs/2602.00585) |
| [AWM](#explicit-retrieval-088) | EMNLP’26<sup>F</sup> | 26.08 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2608.25618) |
| [Doc-REFRAG](#explicit-retrieval-089) | EMNLP’26 | 26.08 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Llama | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2608.30163) |
| [Doc-Search](#explicit-retrieval-090) | arXiv’26 | 26.06 | 2026 | Uni(V) | Page | Iterative | Single | Multi-step | Qwen | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2606.26122) |
| [Hybrid Retriever Evolution](#explicit-retrieval-091) | arXiv’26 | 26.06 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Single | Multi-step | Gemini/GPT-5 | Ans. Ret. | [Paper](https://arxiv.org/abs/2606.29648) |
| [MARDoc](#explicit-retrieval-092) | arXiv’26 | 26.06 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Multi | Multi-step | Qwen-VL | Ans. Eff. | [Paper](https://arxiv.org/abs/2606.05749) |
| [CDS](#explicit-retrieval-093) | arXiv’26 | 26.06 | 2026 | Uni(T) | Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2606.07252) |
| [FlowReader](#explicit-retrieval-094) | arXiv’26 | 26.06 | 2026 | Uni(T) | Elem. | Iterative | Multi | Multi-step | Qwen-VL | Ans. Eff. | [Paper](https://arxiv.org/abs/2606.07235) |
| [EviProp](#explicit-retrieval-095) | arXiv’26 | 26.06 | 2026 | Mixed(T/V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2606.08979) |
| [MAGE-RAG](#explicit-retrieval-096) | arXiv’26 | 26.06 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Eff. | [Paper](https://arxiv.org/abs/2606.15906) |
| [Six-tool Agent](#explicit-retrieval-097) | EMNLP’26<sup>I</sup> | 26.09 | 2026 | Uni(T) | Page, Elem. | Iterative | Single | Multi-step | Claude/Qwen | Ans. Eff. | [Paper](https://arxiv.org/abs/2609.29933) |
| [TAP-RAG](#explicit-retrieval-098) | arXiv’26 | 26.07 | 2026 | Uni(T) | Page, Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. | [Paper](https://arxiv.org/abs/2607.18917) |
| [HIEVI-RAG](#explicit-retrieval-099) | arXiv’26 | 26.07 | 2026 | Uni(V) | Page | One-shot | Single | Multi-step | Qwen-VL | Ans. Ret. | [Paper](https://arxiv.org/abs/2607.04625) |
| [HierDoc](#explicit-retrieval-100) | arXiv’26 | 26.07 | 2026 | Mixed(T/V) | Page, Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret.<sup>a</sup> Eff. | [Paper](https://arxiv.org/abs/2607.29638) |
| [DocTrace](#explicit-retrieval-101) | arXiv’26 | 26.08 | 2026 | Uni(V) | Page, Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2608.03292) |
| [DocMemo](#explicit-retrieval-102) | arXiv’26 | 26.08 | 2026 | Mixed(T/V) | Page | Iterative | Multi | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2608.07067) |
| [InSight-doc](#explicit-retrieval-103) | arXiv’26 | 26.08 | 2026 | Uni(V) | Page, Elem. | One-shot | Single | Multi-step | Qwen-VL | Ans. Loc. Eff. | [Paper](https://arxiv.org/abs/2608.10628) |
| [TRIDENT](#explicit-retrieval-104) | arXiv’26 | 26.08 | 2026 | Uni(T) | Page | One-shot | Single | Single-pass | GPT-4 | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2608.14841) |
| [D2-ScaleAgent](#explicit-retrieval-105) | arXiv’26 | 26.08 | 2026 | Uni(V) | Page, Elem. | Iterative | Multi | Multi-step | GPT-4o | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2608.16417) |
| [DocClaw](#explicit-retrieval-106) | arXiv’26 | 26.08 | 2026 | Mixed(T/V) | Page, Elem. | Iterative | Single | Multi-step | GPT-5/Gemini | Ans. Eff. | [Paper](https://arxiv.org/abs/2608.18685) |
| [ViSAR](#explicit-retrieval-107) | arXiv’26 | 26.09 | 2026 | Uni(V) | Page | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2609.02486) |
| [CAVR+WSPS+VET](#explicit-retrieval-108) | arXiv’26 | 26.09 | 2026 | Mixed(T/V) | Page, Elem. | One-shot | Single | Single-pass | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2609.13268) |
| [SCORE](#explicit-retrieval-109) | arXiv’26 | 26.09 | 2026 | Uni(V) | Page, Elem. | Iterative | Single | Multi-step | Qwen-VL | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2609.15800) |
| [TAEC](#explicit-retrieval-110) | arXiv’26 | 26.09 | 2026 | Mixed(T/V) | Page | Iterative | Single | Multi-step | Gemini | Ans. Ret. Eff. | [Paper](https://arxiv.org/abs/2609.37349) |

Each expandable record below contains every source column, including the complete retrieval mechanism.

<a id="explicit-retrieval-021"></a>

<details>
<summary>MHST — Towards complex document understanding by discrete reasoning</summary>

**Paper:** Towards complex document understanding by discrete reasoning  
**Authors:** Zhu, Fengbin and Lei, Wenqiang and Feng, Fuli and Wang, Chao and Zhang, Haozhou and Chua, Tat-Seng  
**Citation:** `ref86`; current BibTeX year **2022**; first release **22.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Towards%20complex%20document%20understanding%20by%20discrete%20reasoning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:96`; order 21.

| Field | Source value |
| --- | --- |
| Venue | MM’22 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | TF-IDF(E<sup>T</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | LayoutLM |
| Learning | SFT |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Towards complex document understanding by discrete reasoning |
| author | Zhu, Fengbin and Lei, Wenqiang and Feng, Fuli and Wang, Chao and Zhang, Haozhou and Chua, Tat-Seng |
| booktitle | Proceedings of the 30th ACM International Conference on Multimedia |
| year | 2022 |
| pages | 4857--4866 |

</details>

<a id="explicit-retrieval-022"></a>

<details>
<summary>CREAM — Cream: coarse-to-fine retrieval and multi-modal efficient tuning for document vqa</summary>

**Paper:** Cream: coarse-to-fine retrieval and multi-modal efficient tuning for document vqa  
**Authors:** Zhang, Jinxu and Yu, Yongqi and Zhang, Yu  
**Citation:** `ref118`; current BibTeX year **2024**; first release **24.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Cream%3A%20coarse-to-fine%20retrieval%20and%20multi-modal%20efficient%20tuning%20for%20document%20vqa). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:97`; order 22.

| Field | Source value |
| --- | --- |
| Venue | ACM MM’24 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | BGE(E<sup>T</sup>→[E<sup>T</sup>, P<sup>V</sup>]) + RankVicuna(E<sup>T</sup>→[E<sup>T</sup>, P<sup>V</sup>]) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Llama |
| Learning | SFT |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Cream: coarse-to-fine retrieval and multi-modal efficient tuning for document vqa |
| author | Zhang, Jinxu and Yu, Yongqi and Zhang, Yu |
| booktitle | Proceedings of the 32nd ACM International Conference on Multimedia |
| year | 2024 |
| pages | 925--934 |

</details>

<a id="explicit-retrieval-023"></a>

<details>
<summary>VisRAG — Visrag: Vision-based retrieval-augmented generation on multi-modality documents</summary>

**Paper:** Visrag: Vision-based retrieval-augmented generation on multi-modality documents  
**Authors:** Yu, Shi and Tang, Chaoyue and Xu, Bokai and Cui, Junbo and Ran, Junhao and Yan, Yukun and Liu, Zhenghao and Wang, Shuo and Han, Xu and Liu, Zhiyuan and Sun, Maosong  
**Citation:** `yu2025visrag`; current BibTeX year **2025**; first release **24.10**.  
**Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3640a1997a4c9571cea9db2c82e1fc35-Abstract-Conference.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:98`; order 23.

| Field | Source value |
| --- | --- |
| Venue | ICLR’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VisRAG-Ret<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | MiniCPM-V/GPT-4o |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visrag: Vision-based retrieval-augmented generation on multi-modality documents |
| author | Yu, Shi and Tang, Chaoyue and Xu, Bokai and Cui, Junbo and Ran, Junhao and Yan, Yukun and Liu, Zhenghao and Wang, Shuo and Han, Xu and Liu, Zhiyuan and Sun, Maosong |
| booktitle | International Conference on Learning Representations |
| volume | 2025 |
| pages | 21074--21098 |
| year | 2025 |

</details>

<a id="explicit-retrieval-024"></a>

<details>
<summary>SV-RAG — SV-RAG: LoRA-contextualizing adaptation of MLLMs for long document understanding</summary>

**Paper:** SV-RAG: LoRA-contextualizing adaptation of MLLMs for long document understanding  
**Authors:** Chen, Jian and Zhang, Ruiyi and Zhou, Yufan and Yu, Tong and Dernoncourt, Franck and Gu, Jiuxiang and Rossi, Ryan A. and Chen, Changyou and Sun, Tong  
**Citation:** `chen2024svrag`; current BibTeX year **2024**; first release **24.11**.  
**Source:** [Paper](https://arxiv.org/abs/2411.01106). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:99`; order 24.

| Field | Source value |
| --- | --- |
| Venue | ICLR’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | Col-Ret<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | PaliGemma/Phi-Vision/InternVL |
| Learning | SFT |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SV-RAG: LoRA-contextualizing adaptation of MLLMs for long document understanding |
| author | Chen, Jian and Zhang, Ruiyi and Zhou, Yufan and Yu, Tong and Dernoncourt, Franck and Gu, Jiuxiang and Rossi, Ryan A. and Chen, Changyou and Sun, Tong |
| journal | arXiv preprint arXiv:2411.01106 |
| year | 2024 |

</details>

<a id="explicit-retrieval-025"></a>

<details>
<summary>PDF-WuKong — Wukong: A large multimodal model for efficient long pdf reading with end-to-end sparse sampling</summary>

**Paper:** Wukong: A large multimodal model for efficient long pdf reading with end-to-end sparse sampling  
**Authors:** Xie, Xudong and Hao Yan and Liang Yin and Yang Liu and Jing Ding and Minghui Liao and Yuliang Liu and Wei Chen and Xiang Bai  
**Citation:** `ref142`; current BibTeX year **2026**; first release **24.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Wukong%3A%20A%20large%20multimodal%20model%20for%20efficient%20long%20pdf%20reading%20with%20end-to-end%20sparse%20sampling). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:100`; order 25.

| Field | Source value |
| --- | --- |
| Venue | IJCV’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Elem. |
| Mechanism | PDF-WuKong<sup>t</sup>(E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | InternLM-XComposer |
| Learning | SFT |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Wukong: A large multimodal model for efficient long pdf reading with end-to-end sparse sampling |
| author | Xie, Xudong and Hao Yan and Liang Yin and Yang Liu and Jing Ding and Minghui Liao and Yuliang Liu and Wei Chen and Xiang Bai |
| journal | International Journal of Computer Vision |
| volume | 134 |
| number | 7 |
| pages | 324 |
| year | 2026 |

</details>

<a id="explicit-retrieval-026"></a>

<details>
<summary>VisDoMRAG — Visdom: Multi-document qa with visually rich elements using multimodal retrieval-augmented generation</summary>

**Paper:** Visdom: Multi-document qa with visually rich elements using multimodal retrieval-augmented generation  
**Authors:** Suri, Manan and Mathur, Puneet and Dernoncourt, Franck and Goswami, Kanika and Rossi, Ryan A. and Manocha, Dinesh  
**Citation:** `ref10`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Visdom%3A%20Multi-document%20qa%20with%20visually%20rich%20elements%20using%20multimodal%20retrieval-augmented%20generation). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:101`; order 26.

| Field | Source value |
| --- | --- |
| Venue | NAACL’25 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | BGE(E<sup>T</sup>) + ColQwen(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | Qwen-VL/Gemini/GPT-4o |
| Learning | ✗ |
| Eval. | Ans. Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visdom: Multi-document qa with visually rich elements using multimodal retrieval-augmented generation |
| author | Suri, Manan and Mathur, Puneet and Dernoncourt, Franck and Goswami, Kanika and Rossi, Ryan A. and Manocha, Dinesh |
| booktitle | Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) |
| year | 2025 |
| pages | 6088--6109 |

</details>

<a id="explicit-retrieval-027"></a>

<details>
<summary>VDocRAG — Vdocrag: Retrieval-augmented generation over visually-rich documents</summary>

**Paper:** Vdocrag: Retrieval-augmented generation over visually-rich documents  
**Authors:** Tanaka, Ryota and Iki, Taichi and Hasegawa, Taku and Nishida, Kyosuke and Saito, Kuniko and Suzuki, Jun  
**Citation:** `ref11`; current BibTeX year **2025**; first release **25.04**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Vdocrag%3A%20Retrieval-augmented%20generation%20over%20visually-rich%20documents). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:102`; order 27.

| Field | Source value |
| --- | --- |
| Venue | CVPR’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VDoc-Ret<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Phi-Vision |
| Learning | SFT |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Vdocrag: Retrieval-augmented generation over visually-rich documents |
| author | Tanaka, Ryota and Iki, Taichi and Hasegawa, Taku and Nishida, Kyosuke and Saito, Kuniko and Suzuki, Jun |
| booktitle | 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| year | 2025 |
| pages | 24827--24837 |
| organization | IEEE |

</details>

<a id="explicit-retrieval-028"></a>

<details>
<summary>SuperRAG — Superrag: Beyond rag with layout-aware graph modeling</summary>

**Paper:** Superrag: Beyond rag with layout-aware graph modeling  
**Authors:** Yang, Chening and Duy-Khanh Vu and Minh-Tien Nguyen and Xuan-Quang Nguyen and Linh Nguyen and Hung Le  
**Citation:** `ref153`; current BibTeX year **2025**; first release **25.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Superrag%3A%20Beyond%20rag%20with%20layout-aware%20graph%20modeling). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:103`; order 28.

| Field | Source value |
| --- | --- |
| Venue | NAACL’25<sup>I</sup> |
| OCR | ✓ |
| Deep | Graph, Tree |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | OpenAI Embedding(P<sup>T</sup>; E<sup>T</sup>) + BM25(E<sup>T</sup>) + Cohere(E<sup>T</sup>) + LLM(P<sup>T</sup>; E<sup>T</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | GPT-4o |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Superrag: Beyond rag with layout-aware graph modeling |
| author | Yang, Chening and Duy-Khanh Vu and Minh-Tien Nguyen and Xuan-Quang Nguyen and Linh Nguyen and Hung Le |
| booktitle | Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 3: Industry Track) |
| pages | 544--557 |
| year | 2025 |

</details>

<a id="explicit-retrieval-029"></a>

<details>
<summary>Doc-React — Doc-react: Multi-page heterogeneous document question-answering</summary>

**Paper:** Doc-react: Multi-page heterogeneous document question-answering  
**Authors:** Wu, Junda and Xia, Yu and Yu, Tong and Chen, Xiang and Harsha, Sai Sree and Maharaj, Akash V. and Zhang, Ruiyi and Bursztyn, Victor and Kim, Sungchul and Rossi, Ryan A. and McAuley, Julian and Li, Yunyao and Sinha, Ritwik  
**Citation:** `ref30`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Paper](https://aclanthology.org/2025.acl-short.6/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:104`; order 29.

| Field | Source value |
| --- | --- |
| Venue | ACL’25<sup>S</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | GPT-4o |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doc-react: Multi-page heterogeneous document question-answering |
| author | Wu, Junda and Xia, Yu and Yu, Tong and Chen, Xiang and Harsha, Sai Sree and Maharaj, Akash V. and Zhang, Ruiyi and Bursztyn, Victor and Kim, Sungchul and Rossi, Ryan A. and McAuley, Julian and Li, Yunyao and Sinha, Ritwik |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) |
| year | 2025 |
| pages | 67--78 |

</details>

<a id="explicit-retrieval-030"></a>

<details>
<summary>VISA — Visa: Retrieval augmented generation with visual source attribution</summary>

**Paper:** Visa: Retrieval augmented generation with visual source attribution  
**Authors:** Ma, Xueguang and Zhuang, Shengyao and Koopman, Bevan and Zuccon, Guido and Chen, Wenhu and Lin, Jimmy  
**Citation:** `ref13`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Visa%3A%20Retrieval%20augmented%20generation%20with%20visual%20source%20attribution). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:105`; order 30.

| Field | Source value |
| --- | --- |
| Venue | ACL’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | DSE(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT |
| Eval. | Ans. Loc. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visa: Retrieval augmented generation with visual source attribution |
| author | Ma, Xueguang and Zhuang, Shengyao and Koopman, Bevan and Zuccon, Guido and Chen, Wenhu and Lin, Jimmy |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2025 |
| pages | 30154--30169 |

</details>

<a id="explicit-retrieval-031"></a>

<details>
<summary>NeuSym-RAG — Neusym-rag: Hybrid neural symbolic retrieval with multiview structuring for pdf question answering</summary>

**Paper:** Neusym-rag: Hybrid neural symbolic retrieval with multiview structuring for pdf question answering  
**Authors:** Cao, Ruisheng and Zhang, Hanchong and Huang, Tiancheng and Kang, Zhangyi and Zhang, Yuxin and Sun, Liangtai and Li, Hanqi and Miao, Yuxun and Fan, Shuai and Chen, Lu and Yu, Kai  
**Citation:** `ref156`; current BibTeX year **2025**; first release **25.05**.  
**Source:** [Paper](https://aclanthology.org/2025.acl-long.311/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:106`; order 31.

| Field | Source value |
| --- | --- |
| Venue | ACL’25 |
| OCR | ✓ |
| Deep | Graph, Summary |
| Modality | Mixed(T/V) |
| Gran. | Doc., Page, Elem. |
| Mechanism | BM25(P<sup>T</sup>; E<sup>T</sup>) + MiniLM(P<sup>T</sup>; E<sup>T</sup>) + BGE(P<sup>T</sup>; E<sup>T</sup>) + CLIP(E<sup>V</sup>) + VLM(D<sup>T</sup>; P<sup>TV</sup>; E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Neusym-rag: Hybrid neural symbolic retrieval with multiview structuring for pdf question answering |
| author | Cao, Ruisheng and Zhang, Hanchong and Huang, Tiancheng and Kang, Zhangyi and Zhang, Yuxin and Sun, Liangtai and Li, Hanqi and Miao, Yuxun and Fan, Shuai and Chen, Lu and Yu, Kai |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2025 |
| pages | 6211--6239 |
| month | July |

</details>

<a id="explicit-retrieval-032"></a>

<details>
<summary>MDocAgent — Mdocagent: A multi-modal multi-agent framework for document understanding</summary>

**Paper:** Mdocagent: A multi-modal multi-agent framework for document understanding  
**Authors:** Han, Siwei and Xia, Peng and Zhang, Ruiyi and Sun, Tong and Li, Yun and Zhu, Hongtu and Yao, Huaxiu  
**Citation:** `ref32`; current BibTeX year **2025**; first release **25.03**.  
**Source:** [Paper](https://arxiv.org/abs/2503.13964). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:107`; order 32.

| Field | Source value |
| --- | --- |
| Venue | arXiv’25 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | ColBERT(E<sup>T</sup>→P<sup>T</sup>) + ColPali(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | Llama + Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Mdocagent: A multi-modal multi-agent framework for document understanding |
| author | Han, Siwei and Xia, Peng and Zhang, Ruiyi and Sun, Tong and Li, Yun and Zhu, Hongtu and Yao, Huaxiu |
| journal | arXiv preprint arXiv:2503.13964 |
| year | 2025 |

</details>

<a id="explicit-retrieval-033"></a>

<details>
<summary>FRAG — Frag: Frame selection augmented generation for long video and long document understanding</summary>

**Paper:** Frag: Frame selection augmented generation for long video and long document understanding  
**Authors:** Huang, De-An and Subhashree Radhakrishnan and Zhiding Yu and Jan Kautz  
**Citation:** `ref154`; current BibTeX year **2025**; first release **25.04**.  
**Source:** [Paper](https://arxiv.org/abs/2504.17447). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:108`; order 33.

| Field | Source value |
| --- | --- |
| Venue | arXiv’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | LLaVA/InternVL |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Frag: Frame selection augmented generation for long video and long document understanding |
| author | Huang, De-An and Subhashree Radhakrishnan and Zhiding Yu and Jan Kautz |
| journal | arXiv preprint arXiv:2504.17447 |
| year | 2025 |

</details>

<a id="explicit-retrieval-034"></a>

<details>
<summary>VRAG-RL — Vrag-rl: Empower vision-perception-based rag for visually rich information understanding via iterative reasoning with reinforcement learning</summary>

**Paper:** Vrag-rl: Empower vision-perception-based rag for visually rich information understanding via iterative reasoning with reinforcement learning  
**Authors:** Wang, Qiuchen and Ding, Ruixue and Zeng, Yu and Chen, Zehui and Chen, Lin and Wang, Shihang and Xie, Pengjun and Huang, Fei and Zhao, Feng  
**Citation:** `wang2026vragrl`; current BibTeX year **2026**; first release **25.05**.  
**Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/529b876b5d87f997e98ed925a3ce9f01-Abstract-Conference.html). Recorded in `reference_sources.json:scholarResultUrl`.  
**Manuscript row:** `tables/table6_full.tex:109`; order 34.

| Field | Source value |
| --- | --- |
| Venue | NIPS’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | ColPali(P<sup>V</sup>) + VLM<sup>t</sup>(E<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Vrag-rl: Empower vision-perception-based rag for visually rich information understanding via iterative reasoning with reinforcement learning |
| author | Wang, Qiuchen and Ding, Ruixue and Zeng, Yu and Chen, Zehui and Chen, Lin and Wang, Shihang and Xie, Pengjun and Huang, Fei and Zhao, Feng |
| journal | Advances in Neural Information Processing Systems |
| volume | 38 |
| pages | 57133--57160 |
| year | 2026 |

</details>

<a id="explicit-retrieval-035"></a>

<details>
<summary>Dual-Stream RAG — Dual-Stream Adaptive Retrieval and Hierarchical Agent Collaboration for Document Visual QA</summary>

**Paper:** Dual-Stream Adaptive Retrieval and Hierarchical Agent Collaboration for Document Visual QA  
**Authors:** Fang, Qin and Ruixue Gou and Shiqi Liu and Minqi Song and Pan Yuan and Xian Peng  
**Citation:** `ref123`; current BibTeX year **2025**; first release **26.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Dual-Stream%20Adaptive%20Retrieval%20and%20Hierarchical%20Agent%20Collaboration%20for%20Document%20Visual%20QA). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:110`; order 35.

| Field | Source value |
| --- | --- |
| Venue | APWeb-WAIM’25 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | NV-Embed(E<sup>T</sup>→P<sup>V</sup>) + ColQwen(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Dual-Stream Adaptive Retrieval and Hierarchical Agent Collaboration for Document Visual QA |
| author | Fang, Qin and Ruixue Gou and Shiqi Liu and Minqi Song and Pan Yuan and Xian Peng |
| booktitle | Asia-Pacific Web (APWeb) and Web-Age Information Management (WAIM) Joint International Conference on Web and Big Data |
| pages | 402--416 |
| publisher | Springer Nature Singapore |
| address | Singapore |
| year | 2025 |

</details>

<a id="explicit-retrieval-036"></a>

<details>
<summary>Retrieval-aware Tuning — M-longdoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework</summary>

**Paper:** M-longdoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework  
**Authors:** Chia, Yew Ken and Cheng, Liying and Chan, Hou Pong and Song, Maojia and Liu, Chaoqun and Aljunied, Mahani and Poria, Soujanya and Bing, Lidong  
**Citation:** `ref16`; current BibTeX year **2025**; first release **24.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M-longdoc%3A%20A%20benchmark%20for%20multimodal%20super-long%20document%20understanding%20and%20a%20retrieval-aware%20tuning%20framework). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:111`; order 36.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | ColPali(P<sup>V</sup>→[P<sup>T</sup>, E<sup>V</sup>]) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT |
| Eval. | Ans. Ret. Rob. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | M-longdoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework |
| author | Chia, Yew Ken and Cheng, Liying and Chan, Hou Pong and Song, Maojia and Liu, Chaoqun and Aljunied, Mahani and Poria, Soujanya and Bing, Lidong |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 9244--9261 |

</details>

<a id="explicit-retrieval-037"></a>

<details>
<summary>ViDoRAG — Vidorag: Visual document retrieval-augmented generation via dynamic iterative reasoning agents</summary>

**Paper:** Vidorag: Visual document retrieval-augmented generation via dynamic iterative reasoning agents  
**Authors:** Wang, Qiuchen and Ding, Ruixue and Chen, Zehui and Wu, Weiqi and Wang, Shihang and Xie, Pengjun and Zhao, Feng  
**Citation:** `ref18`; current BibTeX year **2025**; first release **25.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Vidorag%3A%20Visual%20document%20retrieval-augmented%20generation%20via%20dynamic%20iterative%20reasoning%20agents). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:112`; order 37.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | NV-Embed(E<sup>T</sup>→P<sup>V</sup>) + ColQwen(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | GPT-4o/Qwen-VL/Llama-Vision |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Vidorag: Visual document retrieval-augmented generation via dynamic iterative reasoning agents |
| author | Wang, Qiuchen and Ding, Ruixue and Chen, Zehui and Wu, Weiqi and Wang, Shihang and Xie, Pengjun and Zhao, Feng |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 9124--9145 |

</details>

<a id="explicit-retrieval-038"></a>

<details>
<summary>RGenCite — Finragbench-v: A benchmark for multimodal rag with visual citation in the financial domain</summary>

**Paper:** Finragbench-v: A benchmark for multimodal rag with visual citation in the financial domain  
**Authors:** Zhao, Suifeng and Zhuoran Jin and Sujian Li and Jun Gao  
**Citation:** `ref109`; current BibTeX year **2025**; first release **25.05**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Finragbench-v%3A%20A%20benchmark%20for%20multimodal%20rag%20with%20visual%20citation%20in%20the%20financial%20domain). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:113`; order 38.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Loc.<sup>a</sup> |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Finragbench-v: A benchmark for multimodal rag with visual citation in the financial domain |
| author | Zhao, Suifeng and Zhuoran Jin and Sujian Li and Jun Gao |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| pages | 4215--4249 |
| year | 2025 |

</details>

<a id="explicit-retrieval-039"></a>

<details>
<summary>SimpleDoc — SimpleDoc: Multi‐Modal Document Understanding with Dual‐Cue Page Retrieval and Iterative Refinement</summary>

**Paper:** SimpleDoc: Multi‐Modal Document Understanding with Dual‐Cue Page Retrieval and Iterative Refinement  
**Authors:** Jain, Chelsi and Wu, Yiran and Zeng, Yifan and Liu, Jiale and Dai, Shengyu and Shao, Zhenwen and Wu, Qingyun and Wang, Huazheng  
**Citation:** `ref34`; current BibTeX year **2025**; first release **25.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=SimpleDoc%3A%20Multi%E2%80%90Modal%20Document%20Understanding%20with%20Dual%E2%80%90Cue%20Page%20Retrieval%20and%20Iterative%20Refinement). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:114`; order 39.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✓ |
| Deep | Summary |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>→P<sup>TV</sup>) + LLM(P<sup>T</sup>→P<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SimpleDoc: Multi‐Modal Document Understanding with Dual‐Cue Page Retrieval and Iterative Refinement |
| author | Jain, Chelsi and Wu, Yiran and Zeng, Yifan and Liu, Jiale and Dai, Shengyu and Shao, Zhenwen and Wu, Qingyun and Wang, Huazheng |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 28398--28415 |

</details>

<a id="explicit-retrieval-040"></a>

<details>
<summary>MoLoRAG — Molorag: Bootstrapping document understanding via multi-modal logic-aware retrieval</summary>

**Paper:** Molorag: Bootstrapping document understanding via multi-modal logic-aware retrieval  
**Authors:** Wu, Xixi and Yanchao Tan and Nan Hou and Ruiyang Zhang and Hong Cheng  
**Citation:** `ref35`; current BibTeX year **2025**; first release **25.09**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Molorag%3A%20Bootstrapping%20document%20understanding%20via%20multi-modal%20logic-aware%20retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:115`; order 40.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✗ |
| Deep | Graph |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL/DeepSeek-VL/LLaVA |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Molorag: Bootstrapping document understanding via multi-modal logic-aware retrieval |
| author | Wu, Xixi and Yanchao Tan and Nan Hou and Ruiyang Zhang and Hong Cheng |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 14035--14056 |
| month | November |

</details>

<a id="explicit-retrieval-041"></a>

<details>
<summary>LILaC — Lilac: Late interacting in layered component graph for open-domain multimodal multihop retrieval</summary>

**Paper:** Lilac: Late interacting in layered component graph for open-domain multimodal multihop retrieval  
**Authors:** Yun, Joohyung and Doyup Lee and Wook-Shin Han  
**Citation:** `ref36`; current BibTeX year **2025**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Lilac%3A%20Late%20interacting%20in%20layered%20component%20graph%20for%20open-domain%20multimodal%20multihop%20retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:116`; order 41.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Mixed(T/V) |
| Gran. | Elem. |
| Mechanism | MM-Embed(E<sup>TV</sup>; E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Lilac: Late interacting in layered component graph for open-domain multimodal multihop retrieval |
| author | Yun, Joohyung and Doyup Lee and Wook-Shin Han |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 20551--20570 |
| month | November |

</details>

<a id="explicit-retrieval-042"></a>

<details>
<summary>DocAgent — Docagent: An agentic framework for multi-modal long-context document understanding</summary>

**Paper:** Docagent: An agentic framework for multi-modal long-context document understanding  
**Authors:** Sun, Li and Liu He and Shuyue Jia and Yangfan He and Chenyu You  
**Citation:** `ref37`; current BibTeX year **2025**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Docagent%3A%20An%20agentic%20framework%20for%20multi-modal%20long-context%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:117`; order 42.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’25 |
| OCR | ✓ |
| Deep | Tree |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | Keyword(E<sup>T</sup>) + VLM(E<sup>T</sup>→[E<sup>TV</sup>, P<sup>V</sup>]) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | GPT-4o/Claude/Gemini |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. Rob. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docagent: An agentic framework for multi-modal long-context document understanding |
| author | Sun, Li and Liu He and Shuyue Jia and Yangfan He and Chenyu You |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 17712--17727 |
| month | November |

</details>

<a id="explicit-retrieval-043"></a>

<details>
<summary>M3DocRAG — M3docvqa: Multi-modal multi-page multi-document understanding</summary>

**Paper:** M3docvqa: Multi-modal multi-page multi-document understanding  
**Authors:** Cho, Jaemin and Mahata, Debanjan and Irsoy, Ozan and He, Yujie and Bansal, Mohit  
**Citation:** `cho2025m3docvqa`; current BibTeX year **2025**; first release **24.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M3docvqa%3A%20Multi-modal%20multi-page%20multi-document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:118`; order 43.

| Field | Source value |
| --- | --- |
| Venue | ICCV’25<sup>W</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | M3docvqa: Multi-modal multi-page multi-document understanding |
| author | Cho, Jaemin and Mahata, Debanjan and Irsoy, Ozan and He, Yujie and Bansal, Mohit |
| booktitle | 2025 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW) |
| pages | 6237--6247 |
| year | 2025 |
| organization | IEEE |

</details>

<a id="explicit-retrieval-044"></a>

<details>
<summary>MMGraphRAG — Mmgraphrag: Bridging vision and language with interpretable multimodal knowledge graphs</summary>

**Paper:** Mmgraphrag: Bridging vision and language with interpretable multimodal knowledge graphs  
**Authors:** Wan, Xueyao and Hang Yu  
**Citation:** `ref152`; current BibTeX year **2025**; first release **25.07**.  
**Source:** [Paper](https://arxiv.org/abs/2507.20804). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:119`; order 44.

| Field | Source value |
| --- | --- |
| Venue | arXiv’25 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | --(E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen + InternVL |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Mmgraphrag: Bridging vision and language with interpretable multimodal knowledge graphs |
| author | Wan, Xueyao and Hang Yu |
| journal | arXiv preprint arXiv:2507.20804 |
| year | 2025 |

</details>

<a id="explicit-retrieval-045"></a>

<details>
<summary>RegionRAG — RegionRAG: Region-level Retrieval-Augmented Generation for Visual Document Understanding</summary>

**Paper:** RegionRAG: Region-level Retrieval-Augmented Generation for Visual Document Understanding  
**Authors:** Li, Yinglu and Lu, Zhiying and Liu, Zhihang and Sun, Yiwei and Liu, Chuanbin and Xie, Hongtao  
**Citation:** `ref101`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37597). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:120`; order 45.

| Field | Source value |
| --- | --- |
| Venue | AAAI’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Elem. |
| Mechanism | RegionRetriever<sup>t</sup>(E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | RegionRAG: Region-level Retrieval-Augmented Generation for Visual Document Understanding |
| author | Li, Yinglu and Lu, Zhiying and Liu, Zhihang and Sun, Yiwei and Liu, Chuanbin and Xie, Hongtao |
| journal | Proceedings of the AAAI Conference on Artificial Intelligence |
| year | 2026 |
| volume | 40 |
| number | 8 |
| pages | 6662--6670 |

</details>

<a id="explicit-retrieval-046"></a>

<details>
<summary>URaG — URaG: Unified retrieval and generation in multimodal LLMs for efficient long document understanding</summary>

**Paper:** URaG: Unified retrieval and generation in multimodal LLMs for efficient long document understanding  
**Authors:** Shi, Yongxin and Jiapeng Wang and Zeyu Shan and Dezhi Peng and Zening Lin and Lianwen Jin  
**Citation:** `ref38`; current BibTeX year **2026**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=URaG%3A%20Unified%20retrieval%20and%20generation%20in%20multimodal%20LLMs%20for%20efficient%20long%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:121`; order 46.

| Field | Source value |
| --- | --- |
| Venue | AAAI’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | URaG<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | URaG: Unified retrieval and generation in multimodal LLMs for efficient long document understanding |
| author | Shi, Yongxin and Jiapeng Wang and Zeyu Shan and Dezhi Peng and Zening Lin and Lianwen Jin |
| journal | Proceedings of the AAAI Conference on Artificial Intelligence |
| year | 2026 |
| volume | 40 |
| number | 30 |
| pages | 25357--25365 |
| month | March |

</details>

<a id="explicit-retrieval-047"></a>

<details>
<summary>M3RAG — M3RAG: Orchestrating Multi-agent Reasoning for Multi-hop, Multi-modal Understanding</summary>

**Paper:** M3RAG: Orchestrating Multi-agent Reasoning for Multi-hop, Multi-modal Understanding  
**Authors:** Du, Haizhou and Wenhao Li  
**Citation:** `ref39`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M3RAG%3A%20Orchestrating%20Multi-agent%20Reasoning%20for%20Multi-hop%2C%20Multi-modal%20Understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:122`; order 47.

| Field | Source value |
| --- | --- |
| Venue | MMM’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | --(P<sup>V</sup>; E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Mistral + (MiniCPM-V/Qwen-VL) |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | M3RAG: Orchestrating Multi-agent Reasoning for Multi-hop, Multi-modal Understanding |
| author | Du, Haizhou and Wenhao Li |
| booktitle | International Conference on Multimedia Modeling |
| pages | 364--378 |
| publisher | Springer Nature Singapore |
| address | Singapore |
| year | 2026 |

</details>

<a id="explicit-retrieval-048"></a>

<details>
<summary>Agentic Hybrid (EXTRACTOR) — AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation</summary>

**Paper:** AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation  
**Authors:** Huang, Tiancheng and Cao, Ruisheng and Zhang, Yuxin and Kang, Zhangyi and Wang, Zijian and Wang, Chenrun and Luo, Yijie and Zheng, Hang and Qian, Lirong and Chen, Lu and Yu, Kai  
**Citation:** `ref157`; current BibTeX year **2026**; first release **25.09**.  
**Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/10d35352a92bb40943bb4ed096a407b6-Abstract-Conference.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:123`; order 48.

| Field | Source value |
| --- | --- |
| Venue | ICLR’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Doc., Page, Elem. |
| Mechanism | MiniLM(E<sup>T</sup>) + LLM<sup>t</sup>(D<sup>T</sup>; P<sup>T</sup>; E<sup>T</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen |
| Learning | SFT |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation |
| author | Huang, Tiancheng and Cao, Ruisheng and Zhang, Yuxin and Kang, Zhangyi and Wang, Zijian and Wang, Chenrun and Luo, Yijie and Zheng, Hang and Qian, Lirong and Chen, Lu and Yu, Kai |
| booktitle | International Conference on Learning Representations |
| year | 2026 |
| volume | 2026 |
| pages | 9927--9955 |
| month | April |

</details>

<a id="explicit-retrieval-049"></a>

<details>
<summary>SCAN — SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation</summary>

**Paper:** SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation  
**Authors:** Ueda, Nobuhiro and Yuyang Dong and Krisztián Boros and Daiki Ito and Takuya Sera and Masafumi Oyamada  
**Citation:** `ref102`; current BibTeX year **2026**; first release **25.05**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=SCAN%3A%20Semantic%20Document%20Layout%20Analysis%20for%20Textual%20and%20Visual%20Retrieval-Augmented%20Generation). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:124`; order 49.

| Field | Source value |
| --- | --- |
| Venue | EACL’26<sup>F</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Elem. |
| Mechanism | ColQwen(E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Loc. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation |
| author | Ueda, Nobuhiro and Yuyang Dong and Krisztián Boros and Daiki Ito and Takuya Sera and Masafumi Oyamada |
| booktitle | Findings of the Association for Computational Linguistics: EACL 2026 |
| pages | 1618--1637 |
| year | 2026 |

</details>

<a id="explicit-retrieval-050"></a>

<details>
<summary>SCoPE VLM — SCoPE VLM: Selective Context Processing for Efficient Document Navigation in Vision-Language Models</summary>

**Paper:** SCoPE VLM: Selective Context Processing for Efficient Document Navigation in Vision-Language Models  
**Authors:** Lim, Gyubeum and Koo, Yemo and Madisetti, Vijay Krishna  
**Citation:** `ref70`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=SCoPE%20VLM%3A%20Selective%20Context%20Processing%20for%20Efficient%20Document%20Navigation%20in%20Vision-Language%20Models). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:125`; order 50.

| Field | Source value |
| --- | --- |
| Venue | EACL’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SCoPE VLM: Selective Context Processing for Efficient Document Navigation in Vision-Language Models |
| author | Lim, Gyubeum and Koo, Yemo and Madisetti, Vijay Krishna |
| booktitle | Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2026 |
| pages | 95--140 |

</details>

<a id="explicit-retrieval-051"></a>

<details>
<summary>Doc-Researcher — Doc-researcher: A unified system for multimodal document parsing and deep research</summary>

**Paper:** Doc-researcher: A unified system for multimodal document parsing and deep research  
**Authors:** Dong, Kuicai and Huang, Shurui and Ye, Fangda and Han, Wei and Zhang, Zhi and Li, Dexun and Li, Wenjun and Yang, Qu and Wang, Gang and Wang, Yichao and Zhang, Chen and Liu, Yong  
**Citation:** `dong2026docresearcher`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Paper](https://doi.org/10.1145/3774904.3792599). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:126`; order 51.

| Field | Source value |
| --- | --- |
| Venue | WWW’26 |
| OCR | ✓ |
| Deep | Summary |
| Modality | Mixed(T/V) |
| Gran. | Doc., Page, Elem. |
| Mechanism | Jina(P<sup>T</sup>; E<sup>T</sup>; E<sup>V</sup>→E<sup>T</sup>) + LLM(D<sup>T</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen/DeepSeek-R1 |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Loc. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doc-researcher: A unified system for multimodal document parsing and deep research |
| author | Dong, Kuicai and Huang, Shurui and Ye, Fangda and Han, Wei and Zhang, Zhi and Li, Dexun and Li, Wenjun and Yang, Qu and Wang, Gang and Wang, Yichao and Zhang, Chen and Liu, Yong |
| booktitle | Proceedings of the ACM Web Conference 2026 |
| pages | 2349--2360 |
| year | 2026 |

</details>

<a id="explicit-retrieval-052"></a>

<details>
<summary>DMAP — Dmap: Human-aligned structural document map for multimodal document understanding</summary>

**Paper:** Dmap: Human-aligned structural document map for multimodal document understanding  
**Authors:** Fu, Shunliang and Yanxin Zhang and Yixin Xiang and Xiaoyu Du and Jinhui Tang  
**Citation:** `ref40`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Dmap%3A%20Human-aligned%20structural%20document%20map%20for%20multimodal%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:127`; order 52.

| Field | Source value |
| --- | --- |
| Venue | WWW’26 |
| OCR | ✓ |
| Deep | Tree, Summary |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | ColBERT(E<sup>T</sup>→P<sup>T</sup>) + ColPali(P<sup>V</sup>) + LLM(P<sup>T</sup>→P<sup>TV</sup>; E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | GPT-4o/Qwen |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Dmap: Human-aligned structural document map for multimodal document understanding |
| author | Fu, Shunliang and Yanxin Zhang and Yixin Xiang and Xiaoyu Du and Jinhui Tang |
| booktitle | Proceedings of the ACM Web Conference 2026 |
| year | 2026 |
| pages | 2037--2048 |
| month | April |

</details>

<a id="explicit-retrieval-053"></a>

<details>
<summary>RAG-Anything — Rag-anything: All-in-one rag framework</summary>

**Paper:** Rag-anything: All-in-one rag framework  
**Authors:** Guo, Zirui and Ren, Xubin and Xu, Lingrui and Zhang, Jiahao and Huang, Chao  
**Citation:** `ref42`; current BibTeX year **2025**; first release **25.10**.  
**Source:** [Paper](https://arxiv.org/abs/2510.12323). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:128`; order 53.

| Field | Source value |
| --- | --- |
| Venue | arXiv’25 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | OpenAI Embedding(E<sup>T</sup>→E<sup>TV</sup>) + BGE-reranker(E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | GPT-4o |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Rag-anything: All-in-one rag framework |
| author | Guo, Zirui and Ren, Xubin and Xu, Lingrui and Zhang, Jiahao and Huang, Chao |
| journal | arXiv preprint arXiv:2510.12323 |
| year | 2025 |

</details>

<a id="explicit-retrieval-054"></a>

<details>
<summary>MACT — Visual document understanding and reasoning: A multi-agent collaboration framework with agent-wise adaptive test-time scaling</summary>

**Paper:** Visual document understanding and reasoning: A multi-agent collaboration framework with agent-wise adaptive test-time scaling  
**Authors:** Yu, Xinlei and Chengming Xu and Zhangquan Chen and Yudong Zhang and Shilin Lu and Cheng Yang and Jiangning Zhang and Shuicheng Yan and Xiaobin Hu  
**Citation:** `ref28`; current BibTeX year **2026**; first release **25.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Visual%20document%20understanding%20and%20reasoning%3A%20A%20multi-agent%20collaboration%20framework%20with%20agent-wise%20adaptive%20test-time%20scaling). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:129`; order 54.

| Field | Source value |
| --- | --- |
| Venue | CVPR’26 |
| OCR | -- |
| Deep | ✗ |
| Modality | -- |
| Gran. | -- |
| Mechanism | Search(D<sup>--</sup>, E<sup>--</sup>); Vector/Keyword(E<sup>T</sup>) |
| Acq. | -- |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen-VL + Qwen/MiMo-VL + MiMo/InternVL |
| Learning | SFT + RL |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visual document understanding and reasoning: A multi-agent collaboration framework with agent-wise adaptive test-time scaling |
| author | Yu, Xinlei and Chengming Xu and Zhangquan Chen and Yudong Zhang and Shilin Lu and Cheng Yang and Jiangning Zhang and Shuicheng Yan and Xiaobin Hu |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| pages | 12300--12311 |
| year | 2026 |

</details>

<a id="explicit-retrieval-055"></a>

<details>
<summary>SLEUTH — Resolving evidence sparsity: Agentic context engineering for long-document understanding</summary>

**Paper:** Resolving evidence sparsity: Agentic context engineering for long-document understanding  
**Authors:** Liu, Keliang and Zizhi Chen and Mingcheng Li and Jingqun Tang and Dingkang Yang and Lihua Zhang  
**Citation:** `ref43`; current BibTeX year **2026**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Resolving%20evidence%20sparsity%3A%20Agentic%20context%20engineering%20for%20long-document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:130`; order 55.

| Field | Source value |
| --- | --- |
| Venue | CVPR’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>→[P<sup>V</sup>, E<sup>T</sup>]) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | Qwen-VL/GLM-V/Gemini |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Resolving evidence sparsity: Agentic context engineering for long-document understanding |
| author | Liu, Keliang and Zizhi Chen and Mingcheng Li and Jingqun Tang and Dingkang Yang and Lihua Zhang |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| pages | 19452--19462 |
| year | 2026 |

</details>

<a id="explicit-retrieval-056"></a>

<details>
<summary>RobustVisRAG — RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations</summary>

**Paper:** RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations  
**Authors:** Chen, I. and Liu, Yu-Wei and Wu, Tse-Yu and Chiang, Yu-Chien and Yang, Jen-Chieh and Chen, Wei-Ting  
**Citation:** `ref89`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=RobustVisRAG%3A%20Causality-Aware%20Vision-Based%20Retrieval-Augmented%20Generation%20under%20Visual%20Degradations). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:131`; order 56.

| Field | Source value |
| --- | --- |
| Venue | CVPR’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | RobustVisRAG<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | MiniCPM-V |
| Learning | ✓ |
| Eval. | Ans. Ret. Rob. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations |
| author | Chen, I. and Liu, Yu-Wei and Wu, Tse-Yu and Chiang, Yu-Chien and Yang, Jen-Chieh and Chen, Wei-Ting |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| year | 2026 |
| pages | 40802--40811 |

</details>

<a id="explicit-retrieval-057"></a>

<details>
<summary>DocPrune — DocPrune: Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning</summary>

**Paper:** DocPrune: Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning  
**Authors:** Choi, Joonmyung and Lee, Sanghyeok and Kim, Jongha and Kim, Sehyung and Ko, Dohwan and Kil, Jihyung and Kim, Hyunwoo J.  
**Citation:** `ref44`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://arxiv.org/abs/2604.22281). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:132`; order 57.

| Field | Source value |
| --- | --- |
| Venue | CVPR’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocPrune: Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning |
| author | Choi, Joonmyung and Lee, Sanghyeok and Kim, Jongha and Kim, Sehyung and Ko, Dohwan and Kil, Jihyung and Kim, Hyunwoo J. |
| journal | arXiv preprint arXiv:2604.22281 |
| year | 2026 |

</details>

<a id="explicit-retrieval-058"></a>

<details>
<summary>HKRAG — Hkrag: Holistic knowledge retrieval-augmented generation over visually-rich documents</summary>

**Paper:** Hkrag: Holistic knowledge retrieval-augmented generation over visually-rich documents  
**Authors:** Tong, Anyang and Xiang Niu and ZhiPing Liu and Chang Tian and Yanyan Wei and Zenglin Shi and Meng Wang  
**Citation:** `ref45`; current BibTeX year **2025**; first release **25.11**.  
**Source:** [Paper](https://arxiv.org/abs/2511.20227). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:133`; order 58.

| Field | Source value |
| --- | --- |
| Venue | arXiv’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | HKRAG-Ret<sup>t</sup>(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Phi-Vision |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Hkrag: Holistic knowledge retrieval-augmented generation over visually-rich documents |
| author | Tong, Anyang and Xiang Niu and ZhiPing Liu and Chang Tian and Yanyan Wei and Zenglin Shi and Meng Wang |
| journal | arXiv preprint arXiv:2511.20227 |
| year | 2025 |

</details>

<a id="explicit-retrieval-059"></a>

<details>
<summary>CogDoc — CogDoc: Towards unified thinking in documents</summary>

**Paper:** CogDoc: Towards unified thinking in documents  
**Authors:** Xu, Qixin and Wang, Haozhe and Liu, Che and Lin, Fangzhen and Chen, Wenhu  
**Citation:** `ref46`; current BibTeX year **2025**; first release **25.12**.  
**Source:** [Paper](https://arxiv.org/abs/2512.12658). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:134`; order 59.

| Field | Source value |
| --- | --- |
| Venue | arXiv’25 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | RL |
| Eval. | Ans. Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | CogDoc: Towards unified thinking in documents |
| author | Xu, Qixin and Wang, Haozhe and Liu, Che and Lin, Fangzhen and Chen, Wenhu |
| journal | arXiv preprint arXiv:2512.12658 |
| year | 2025 |

</details>

<a id="explicit-retrieval-060"></a>

<details>
<summary>LAD-RAG — Lad-rag: Layout-aware dynamic rag for visually-rich document understanding</summary>

**Paper:** Lad-rag: Layout-aware dynamic rag for visually-rich document understanding  
**Authors:** Sourati, Zhivar and Wang, Zheng and Liu, Marianne Menglin and Hu, Yazhe and Guo, Mengqing and Bharadwaj, Sujeeth and Han, Kyu J. and Sheng, Tao and Ravi, Sujith and Dehghani, Morteza and Roth, Dan  
**Citation:** `ref47`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Paper](https://aclanthology.org/2026.acl-long.724/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:135`; order 60.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | -- |
| Mechanism | Vector(E<sup>T</sup>→--) + LLM(E<sup>T</sup>→--) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | GPT-4o/Phi-Vision/Pixtral/InternVL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Lad-rag: Layout-aware dynamic rag for visually-rich document understanding |
| author | Sourati, Zhivar and Wang, Zheng and Liu, Marianne Menglin and Hu, Yazhe and Guo, Mengqing and Bharadwaj, Sujeeth and Han, Kyu J. and Sheng, Tao and Ravi, Sujith and Dehghani, Morteza and Roth, Dan |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 15945--15968 |
| year | 2026 |

</details>

<a id="explicit-retrieval-061"></a>

<details>
<summary>ALDEN — ALDEN: Reinforcement Learning for Active Navigation and Evidence Gathering in Long Documents</summary>

**Paper:** ALDEN: Reinforcement Learning for Active Navigation and Evidence Gathering in Long Documents  
**Authors:** Yang, Tianyu and Terry Ruas and Yijun Tian and Jan Philip Wahle and Daniel Kurzawe and Bela Gipp  
**Citation:** `ref128`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=ALDEN%3A%20Reinforcement%20Learning%20for%20Active%20Navigation%20and%20Evidence%20Gathering%20in%20Long%20Documents). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:136`; order 61.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | ALDEN: Reinforcement Learning for Active Navigation and Evidence Gathering in Long Documents |
| author | Yang, Tianyu and Terry Ruas and Yijun Tian and Jan Philip Wahle and Daniel Kurzawe and Bela Gipp |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 13371--13392 |
| year | 2026 |

</details>

<a id="explicit-retrieval-062"></a>

<details>
<summary>SlideAgent — SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding</summary>

**Paper:** SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding  
**Authors:** Jin, Yiqiao and Rachneet Kaur and Zhen Zeng and Sumitra Ganesh and Srijan Kumar  
**Citation:** `ref129`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=SlideAgent%3A%20Hierarchical%20Agentic%20Framework%20for%20Multi-Page%20Visual%20Document%20Understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:137`; order 62.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✓ |
| Deep | Tree, Summary |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | SFR(P<sup>T</sup>→P<sup>TV</sup>; E<sup>T</sup>→[P<sup>V</sup>, E<sup>T</sup>]) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | GPT-4o/InternVL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding |
| author | Jin, Yiqiao and Rachneet Kaur and Zhen Zeng and Sumitra Ganesh and Srijan Kumar |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 14858--14881 |
| year | 2026 |

</details>

<a id="explicit-retrieval-063"></a>

<details>
<summary>DocLens — Doclens: A tool-augmented multi-agent framework for long visual document understanding</summary>

**Paper:** Doclens: A tool-augmented multi-agent framework for long visual document understanding  
**Authors:** Zhu, Dawei and Meng, Rui and Chen, Jiefeng and Li, Sujian and Pfister, Tomas and Yoon, Jinsung  
**Citation:** `ref48`; current BibTeX year **2026**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Doclens%3A%20A%20tool-augmented%20multi-agent%20framework%20for%20long%20visual%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:138`; order 63.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | VLM(P<sup>TV</sup>→[P<sup>TV</sup>, E<sup>V</sup>]) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | Gemini/Claude |
| Learning | ✗ |
| Eval. | Ans. Ret. Loc. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doclens: A tool-augmented multi-agent framework for long visual document understanding |
| author | Zhu, Dawei and Meng, Rui and Chen, Jiefeng and Li, Sujian and Pfister, Tomas and Yoon, Jinsung |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2026 |
| pages | 26804--26829 |

</details>

<a id="explicit-retrieval-064"></a>

<details>
<summary>Lang2Act — Lang2act: Fine-grained visual reasoning through self-emergent linguistic toolchains</summary>

**Paper:** Lang2act: Fine-grained visual reasoning through self-emergent linguistic toolchains  
**Authors:** Xiong, Yuqi and Chunyi Peng and Zhipeng Xu and Zhenghao Liu and Zulong Chen and Yukun Yan and Shuo Wang and Yu Gu and Ge Yu  
**Citation:** `ref146`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Lang2act%3A%20Fine-grained%20visual%20reasoning%20through%20self-emergent%20linguistic%20toolchains). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:139`; order 64.

| Field | Source value |
| --- | --- |
| Venue | ACL’26<sup>F</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | RL |
| Eval. | Ans. Ret. Loc.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Lang2act: Fine-grained visual reasoning through self-emergent linguistic toolchains |
| author | Xiong, Yuqi and Chunyi Peng and Zhipeng Xu and Zhenghao Liu and Zulong Chen and Yukun Yan and Shuo Wang and Yu Gu and Ge Yu |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2026 |
| pages | 8375--8399 |
| year | 2026 |

</details>

<a id="explicit-retrieval-065"></a>

<details>
<summary>MAB-DQA — MAB-DQA: Addressing query aspect importance in document question answering with multi-armed bandits</summary>

**Paper:** MAB-DQA: Addressing query aspect importance in document question answering with multi-armed bandits  
**Authors:** Xiang, Yixin and Ma, Yunshan and Du, Xiaoyu and Chen, Yibing and Zhang, Yanxin and Tang, Jinhui  
**Citation:** `ref49`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=MAB-DQA%3A%20Addressing%20query%20aspect%20importance%20in%20document%20question%20answering%20with%20multi-armed%20bandits). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:140`; order 65.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✗ |
| Deep | Graph |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MAB-DQA: Addressing query aspect importance in document question answering with multi-armed bandits |
| author | Xiang, Yixin and Ma, Yunshan and Du, Xiaoyu and Chen, Yibing and Zhang, Yanxin and Tang, Jinhui |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2026 |
| pages | 22973--22992 |

</details>

<a id="explicit-retrieval-066"></a>

<details>
<summary>Doc-V&#42; — Doc-V&#42;: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA</summary>

**Paper:** Doc-V&#42;: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA  
**Authors:** Zheng, Yuanlei and Fu, Pei and Li, Hang and Wang, Ziyang and Zhang, Yuyi and Ruan, Wenyu and Zhang, Xiaojin and Wei, Zhongyu and Luo, Zhenbo and Luan, Jian and Chen, Wei and Bai, Xiang  
**Citation:** `ref50`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://aclanthology.org/2026.acl-long.2129/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:141`; order 66.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doc-V&#42;: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA |
| author | Zheng, Yuanlei and Fu, Pei and Li, Hang and Wang, Ziyang and Zhang, Yuyi and Ruan, Wenyu and Zhang, Xiaojin and Wei, Zhongyu and Luo, Zhenbo and Luan, Jian and Chen, Wei and Bai, Xiang |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2026 |
| pages | 45901--45923 |

</details>

<a id="explicit-retrieval-067"></a>

<details>
<summary>MM-Doc-R1 — MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning</summary>

**Paper:** MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning  
**Authors:** Lin, Jiahang and Hu, Kai and Wang, Binghai and Zhou, Yuhao and Xi, Zhiheng and Guo, Honglin and Liu, Shichun and Wang, Junzhe and Dou, Shihan and Zhou, Enyu and Yan, Hang and Han, Zhenhua and Gui, Tao and Zhang, Qi and Huang, Xuanjing  
**Citation:** `ref51`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://aclanthology.org/2026.findings-acl.1488/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:142`; order 67.

| Field | Source value |
| --- | --- |
| Venue | ACL’26<sup>F</sup> |
| OCR | ✓ |
| Deep | Tree |
| Modality | Uni(T) |
| Gran. | Page |
| Mechanism | BM25(P<sup>T</sup>→P<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen + Qwen-VL |
| Learning | RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning |
| author | Lin, Jiahang and Hu, Kai and Wang, Binghai and Zhou, Yuhao and Xi, Zhiheng and Guo, Honglin and Liu, Shichun and Wang, Junzhe and Dou, Shihan and Zhou, Enyu and Yan, Hang and Han, Zhenhua and Gui, Tao and Zhang, Qi and Huang, Xuanjing |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2026 |
| year | 2026 |
| pages | 29770--29783 |

</details>

<a id="explicit-retrieval-068"></a>

<details>
<summary>HiKEY — HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question Answering</summary>

**Paper:** HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question Answering  
**Authors:** Shin, Joongmin and Gyuho Shim and Jeongbae Park and Jaehyung Seo and Heui-Seok Lim  
**Citation:** `ref103`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=HiKEY%3A%20Hierarchical%20Multimodal%20Retrieval%20for%20Open-Domain%20Document%20Question%20Answering). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:143`; order 68.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✓ |
| Deep | Tree |
| Modality | Mixed(T/V) |
| Gran. | Elem. |
| Mechanism | BM25(E<sup>T</sup>) + GTE(E<sup>T</sup>) + MM-Embed(E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question Answering |
| author | Shin, Joongmin and Gyuho Shim and Jeongbae Park and Jaehyung Seo and Heui-Seok Lim |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 17967--17987 |
| year | 2026 |

</details>

<a id="explicit-retrieval-069"></a>

<details>
<summary>TRACE — TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding</summary>

**Paper:** TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding  
**Authors:** He, Liqi and Zuchao Li and Hao Huang and Ping Wang  
**Citation:** `ref57`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=TRACE%3A%20Traversal%20Retrieval-Augmented%20Chain%20of%20Evidence%20for%20Document%20Understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:144`; order 69.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✗ |
| Deep | Graph |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Multi |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding |
| author | He, Liqi and Zuchao Li and Hao Huang and Ping Wang |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 9806--9825 |
| year | 2026 |

</details>

<a id="explicit-retrieval-070"></a>

<details>
<summary>CAPS — Attention as Selector: Unlocking VLM Attention for Long Document Page Retrieval</summary>

**Paper:** Attention as Selector: Unlocking VLM Attention for Long Document Page Retrieval  
**Authors:** Zhu, Minfeng and Linxin Bao and Wei Chen and Linchao Zhu  
**Citation:** `ref97`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Attention%20as%20Selector%3A%20Unlocking%20VLM%20Attention%20for%20Long%20Document%20Page%20Retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:145`; order 70.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL/LLaVA/DeepSeek-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Attention as Selector: Unlocking VLM Attention for Long Document Page Retrieval |
| author | Zhu, Minfeng and Linxin Bao and Wei Chen and Linchao Zhu |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 24344--24365 |
| year | 2026 |

</details>

<a id="explicit-retrieval-071"></a>

<details>
<summary>FUMA — Flow-Based Page Unique Semantic Mapping Architecture for Document Visual Question Answering</summary>

**Paper:** Flow-Based Page Unique Semantic Mapping Architecture for Document Visual Question Answering  
**Authors:** Wang, Haosen and Jing Xiao and Chaochao Du and Xiaowang Zhang and Zhiyong Feng  
**Citation:** `ref65`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Flow-Based%20Page%20Unique%20Semantic%20Mapping%20Architecture%20for%20Document%20Visual%20Question%20Answering). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:146`; order 71.

| Field | Source value |
| --- | --- |
| Venue | ACL’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | FUMA<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen |
| Learning | SFT |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Flow-Based Page Unique Semantic Mapping Architecture for Document Visual Question Answering |
| author | Wang, Haosen and Jing Xiao and Chaochao Du and Xiaowang Zhang and Zhiyong Feng |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 36260--36280 |
| year | 2026 |

</details>

<a id="explicit-retrieval-072"></a>

<details>
<summary>MDocRAG-RL — MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning</summary>

**Paper:** MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning  
**Authors:** Wang, Zhongyu  
**Citation:** `ref147`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=MDocRAG-RL%3A%20Empowering%20Multi-Modal%20Document%20RAG%20via%20Complex%20Visual%20Reasoning%20with%20Reinforcement%20Learning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:147`; order 72.

| Field | Source value |
| --- | --- |
| Venue | ACL’26<sup>F</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | MDocRAG-RL<sup>t</sup>(P<sup>V</sup>) + VLM<sup>t</sup>(E<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning |
| author | Wang, Zhongyu |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2026 |
| pages | 8641--8651 |
| year | 2026 |

</details>

<a id="explicit-retrieval-073"></a>

<details>
<summary>G<sup>2</sup>-Reader — G^ 2-Reader: Dual Evolving Graphs for Multimodal Document QA</summary>

**Paper:** G^ 2-Reader: Dual Evolving Graphs for Multimodal Document QA  
**Authors:** Du, Yaxin and Song, Junru and Zhou, Yifan and Wang, Cheng and Gu, Jiahao and Chen, Zimeng and Chen, Menglan and Yao, Wen and Yang, Yang and Wen, Ying and Chen, Siheng  
**Citation:** `ref77`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Paper](https://arxiv.org/abs/2601.22055). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:148`; order 73.

| Field | Source value |
| --- | --- |
| Venue | ICML’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | Dense(E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | G^ 2-Reader: Dual Evolving Graphs for Multimodal Document QA |
| author | Du, Yaxin and Song, Junru and Zhou, Yifan and Wang, Cheng and Gu, Jiahao and Chen, Zimeng and Chen, Menglan and Yao, Wen and Yang, Yang and Wen, Ying and Chen, Siheng |
| journal | arXiv preprint arXiv:2601.22055 |
| year | 2026 |

</details>

<a id="explicit-retrieval-074"></a>

<details>
<summary>VimRAG — VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph</summary>

**Paper:** VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph  
**Authors:** Wang, Qiuchen and Wang, Shihang and Zeng, Yu and Zhang, Qiang and Zhang, Fanrui and Guo, Zhuoning and Zhang, Bosi and Huang, Wenxuan and Chen, Lin and Chen, Zehui and Xie, Pengjun and Ding, Ruixue  
**Citation:** `ref53`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.12735). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:149`; order 74.

| Field | Source value |
| --- | --- |
| Venue | ICML’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | GVE(P<sup>V</sup>) + VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph |
| author | Wang, Qiuchen and Wang, Shihang and Zeng, Yu and Zhang, Qiang and Zhang, Fanrui and Guo, Zhuoning and Zhang, Bosi and Huang, Wenxuan and Chen, Lin and Chen, Zehui and Xie, Pengjun and Ding, Ruixue |
| journal | arXiv preprint arXiv:2602.12735 |
| year | 2026 |

</details>

<a id="explicit-retrieval-075"></a>

<details>
<summary>UniDocVLM — Unidocvlm: Enhancing visual reasoning and document understanding for vlm via reinforcement learning</summary>

**Paper:** Unidocvlm: Enhancing visual reasoning and document understanding for vlm via reinforcement learning  
**Authors:** Cao, Zongsheng and Anran Liu and Jun Xie and Lang Chen and Feng Chen and Zigan Wang  
**Citation:** `ref54`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Unidocvlm%3A%20Enhancing%20visual%20reasoning%20and%20document%20understanding%20for%20vlm%20via%20reinforcement%20learning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:150`; order 75.

| Field | Source value |
| --- | --- |
| Venue | KDD’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VisRAG-Ret(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Unidocvlm: Enhancing visual reasoning and document understanding for vlm via reinforcement learning |
| author | Cao, Zongsheng and Anran Liu and Jun Xie and Lang Chen and Feng Chen and Zigan Wang |
| booktitle | Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2 |
| pages | 275--284 |
| year | 2026 |

</details>

<a id="explicit-retrieval-076"></a>

<details>
<summary>MLDocRAG — Mldocrag: Multimodal long-context document retrieval augmented generation</summary>

**Paper:** Mldocrag: Multimodal long-context document retrieval augmented generation  
**Authors:** Zhang, Yongyue and Yaxiong Wu  
**Citation:** `ref138`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.10271). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:151`; order 76.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | BGE(E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Mldocrag: Multimodal long-context document retrieval augmented generation |
| author | Zhang, Yongyue and Yaxiong Wu |
| journal | arXiv preprint arXiv:2602.10271 |
| year | 2026 |

</details>

<a id="explicit-retrieval-077"></a>

<details>
<summary>MM-BizRAG — MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&amp;A</summary>

**Paper:** MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&amp;A  
**Authors:** Bhathena, Hanoz and Parin Rajesh Jhaveri and Rohan Mittal and Prateek Singh and Aymen Kallala and Rachneet Kaur and Yiqiao Jin and Zhen Zeng and Adwait Ratnaparkhi and Denis Kochedykov  
**Citation:** `ref90`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=MM-BizRAG%3A%20Rethinking%20Multimodal%20Retrieval-Augmented%20Generation%20for%20General%20Purpose%20Enterprise%20Q%26A). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:152`; order 77.

| Field | Source value |
| --- | --- |
| Venue | ACL’26<sup>I</sup> |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | OpenAI(E<sup>T</sup>→E<sup>TV</sup>; P<sup>T</sup>→P<sup>TV</sup>) + BM25(E<sup>T</sup>→E<sup>TV</sup>; P<sup>T</sup>→P<sup>TV</sup>) + LLM(E<sup>T</sup>→E<sup>TV</sup>; P<sup>T</sup>→P<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | GPT-4.1 |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&amp;A |
| author | Bhathena, Hanoz and Parin Rajesh Jhaveri and Rohan Mittal and Prateek Singh and Aymen Kallala and Rachneet Kaur and Yiqiao Jin and Zhen Zeng and Adwait Ratnaparkhi and Denis Kochedykov |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) |
| pages | 1967--2000 |
| year | 2026 |

</details>

<a id="explicit-retrieval-078"></a>

<details>
<summary>MoDora — MoDora: Tree-Based Semi-Structured Document Analysis System</summary>

**Paper:** MoDora: Tree-Based Semi-Structured Document Analysis System  
**Authors:** Xu, Bangrui and Yao, Qihang and Tang, Zirui and Zhou, Xuanhe and He, Yeye and Yu, Shihan and Xu, Qianqian and Wang, Bin and Li, Guoliang and He, Conghui and others  
**Citation:** `ref94`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.23061). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:153`; order 78.

| Field | Source value |
| --- | --- |
| Venue | PACMMOD’26 |
| OCR | ✓ |
| Deep | Tree, Summary |
| Modality | Mixed(T/V) |
| Gran. | Elem. |
| Mechanism | Qwen-Embedding(E<sup>T</sup>) + LLM(E<sup>T</sup>→E<sup>TV</sup>) + VLM(E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | GPT-5 |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MoDora: Tree-Based Semi-Structured Document Analysis System |
| author | Xu, Bangrui and Yao, Qihang and Tang, Zirui and Zhou, Xuanhe and He, Yeye and Yu, Shihan and Xu, Qianqian and Wang, Bin and Li, Guoliang and He, Conghui and others |
| journal | Proceedings of the ACM on Management of Data |
| volume | 4 |
| number | 3 (SIGMOD) |
| pages | 1--26 |
| year | 2026 |
| publisher | ACM New York, NY, USA |

</details>

<a id="explicit-retrieval-079"></a>

<details>
<summary>AdaNav — AdaNav: Query-Adaptive Multi-granularity Navigation for Long Document Understanding</summary>

**Paper:** AdaNav: Query-Adaptive Multi-granularity Navigation for Long Document Understanding  
**Authors:** Xu, Yiming and Eric López and Artemis Llabrés and Maximiliano Hormazábal and Ernest Valveny and Dimosthenis Karatzas  
**Citation:** `ref64`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=AdaNav%3A%20Query-Adaptive%20Multi-granularity%20Navigation%20for%20Long%20Document%20Understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table6_full.tex:154`; order 79.

| Field | Source value |
| --- | --- |
| Venue | ICDAR’26 |
| OCR | -- |
| Deep | Tree |
| Modality | -- |
| Gran. | Page, Elem. |
| Mechanism | -- |
| Acq. | -- |
| Agent | Multi |
| Reasoning | -- |
| Model | -- |
| Learning | -- |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | AdaNav: Query-Adaptive Multi-granularity Navigation for Long Document Understanding |
| author | Xu, Yiming and Eric López and Artemis Llabrés and Maximiliano Hormazábal and Ernest Valveny and Dimosthenis Karatzas |
| booktitle | International Conference on Document Analysis and Recognition |
| pages | 55--72 |
| publisher | Springer Nature Switzerland |
| address | Cham |
| year | 2026 |

</details>

<a id="explicit-retrieval-080"></a>

<details>
<summary>VisRAG 2.0 — Visrag 2.0: Evidence-guided multi-image reasoning in visual retrieval-augmented generation</summary>

**Paper:** Visrag 2.0: Evidence-guided multi-image reasoning in visual retrieval-augmented generation  
**Authors:** Sun, Yubo and Chunyi Peng and Yukun Yan and Shi Yu and Zhenghao Liu and Chi Chen and Zhiyuan Liu and Maosong Sun  
**Citation:** `ref41`; current BibTeX year **2025**; first release **25.10**.  
**Source:** [Paper](https://arxiv.org/abs/2510.09733). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:155`; order 80.

| Field | Source value |
| --- | --- |
| Venue | ACM MM’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | VisRAG-Ret(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visrag 2.0: Evidence-guided multi-image reasoning in visual retrieval-augmented generation |
| author | Sun, Yubo and Chunyi Peng and Yukun Yan and Shi Yu and Zhenghao Liu and Chi Chen and Zhiyuan Liu and Maosong Sun |
| journal | arXiv preprint arXiv:2510.09733 |
| year | 2025 |

</details>

<a id="explicit-retrieval-081"></a>

<details>
<summary>VISOR — VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning</summary>

**Paper:** VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning  
**Authors:** Shen, Yucheng and Jiulong Wu and Jizhou Huang and Dawei Yin and Lingyong Yan and Min Cao  
**Citation:** `ref55`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://arxiv.org/abs/2604.09508). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:156`; order 81.

| Field | Source value |
| --- | --- |
| Venue | ACM MM’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM<sup>t</sup>(E<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning |
| author | Shen, Yucheng and Jiulong Wu and Jizhou Huang and Dawei Yin and Lingyong Yan and Min Cao |
| journal | arXiv preprint arXiv:2604.09508 |
| year | 2026 |

</details>

<a id="explicit-retrieval-082"></a>

<details>
<summary>LFRAG — LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding</summary>

**Paper:** LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding  
**Authors:** Zhu, Yifan and Yu Mi and Yue Lu and Yanchu Guan and Zhixuan Chu  
**Citation:** `ref130`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://arxiv.org/abs/2605.22829). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:157`; order 82.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | Graph |
| Modality | Uni(V) |
| Gran. | Elem. |
| Mechanism | LFRAG<sup>t</sup>(E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding |
| author | Zhu, Yifan and Yu Mi and Yue Lu and Yanchu Guan and Zhixuan Chu |
| journal | arXiv preprint arXiv:2605.22829 |
| year | 2026 |

</details>

<a id="explicit-retrieval-083"></a>

<details>
<summary>BayesRAG — BayesRAG: Probabilistic mutual evidence corroboration for multimodal retrieval-augmented generation</summary>

**Paper:** BayesRAG: Probabilistic mutual evidence corroboration for multimodal retrieval-augmented generation  
**Authors:** Li, Xuan and Yining Wang and Haocai Luo and Shengping Liu and Jerry Liang and Ying Fu and Jun Yu and Junnan Zhu  
**Citation:** `ref151`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Paper](https://arxiv.org/abs/2601.07329). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:158`; order 83.

| Field | Source value |
| --- | --- |
| Venue | NIPS’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | Qwen-Embedding(E<sup>T</sup>) + BGE-reranker(E<sup>T</sup>) + PE(E<sup>V</sup>) + ColNomic(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | GPT-4o |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | BayesRAG: Probabilistic mutual evidence corroboration for multimodal retrieval-augmented generation |
| author | Li, Xuan and Yining Wang and Haocai Luo and Shengping Liu and Jerry Liang and Ying Fu and Jun Yu and Junnan Zhu |
| journal | arXiv preprint arXiv:2601.07329 |
| year | 2026 |

</details>

<a id="explicit-retrieval-084"></a>

<details>
<summary>AgenticOCR — Agenticocr: Parsing only what you need for efficient retrieval-augmented generation</summary>

**Paper:** Agenticocr: Parsing only what you need for efficient retrieval-augmented generation  
**Authors:** Wang, Zhengren and Ma, Dongsheng and Zhong, Huaping and Li, Jiayu and Zhang, Wentao and Wang, Bin and He, Conghui  
**Citation:** `ref104`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.24134). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:159`; order 84.

| Field | Source value |
| --- | --- |
| Venue | NIPS’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | Qwen-VL-Reranker(P<sup>V</sup>) + VLM<sup>t</sup>(E<sup>V</sup>→E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL + Gemini |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Loc. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Agenticocr: Parsing only what you need for efficient retrieval-augmented generation |
| author | Wang, Zhengren and Ma, Dongsheng and Zhong, Huaping and Li, Jiayu and Zhang, Wentao and Wang, Bin and He, Conghui |
| journal | arXiv preprint arXiv:2602.24134 |
| year | 2026 |

</details>

<a id="explicit-retrieval-085"></a>

<details>
<summary>DocAtlas — DocAtlas: Long-Document Understanding as Mutable-State Interaction</summary>

**Paper:** DocAtlas: Long-Document Understanding as Mutable-State Interaction  
**Authors:** Wei, Hongchen and Wang, Yuanzhe and Liu, Bei and Yang, Yifan and Dai, Qi and Qiu, Kai and Li, Yunsheng and Chen, Dongdong and Luo, Chong and Chen, Zhenzhong and Guo, Baining  
**Citation:** `ref72`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2608.07527). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:160`; order 85.

| Field | Source value |
| --- | --- |
| Venue | NIPS’26 |
| OCR | ✓ |
| Deep | Tree, Summary |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | LLM(E<sup>T</sup>→[P<sup>TV</sup>, E<sup>V</sup>]) + VLM<sup>t</sup>(P<sup>TV</sup>; E<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocAtlas: Long-Document Understanding as Mutable-State Interaction |
| author | Wei, Hongchen and Wang, Yuanzhe and Liu, Bei and Yang, Yifan and Dai, Qi and Qiu, Kai and Li, Yunsheng and Chen, Dongdong and Luo, Chong and Chen, Zhenzhong and Guo, Baining |
| journal | arXiv preprint arXiv:2608.07527 |
| year | 2026 |

</details>

<a id="explicit-retrieval-086"></a>

<details>
<summary>DocDancer — Docdancer: Towards agentic document-grounded information seeking</summary>

**Paper:** Docdancer: Towards agentic document-grounded information seeking  
**Authors:** Zhang, Qintong and Lv, Xinjie and Wu, Jialong and Li, Baixuan and Tao, Zhengwei and Yan, Guochen and Zhang, Huanyao and Wang, Bin and Xu, Jiahao and Mi, Haitao and Zhang, Wentao  
**Citation:** `ref52`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Paper](https://arxiv.org/abs/2601.05163). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:161`; order 86.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26 |
| OCR | ✓ |
| Deep | Tree |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | Keyword(E<sup>T</sup>→[E<sup>TV</sup>, P<sup>V</sup>]) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen + Qwen-VL |
| Learning | SFT |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docdancer: Towards agentic document-grounded information seeking |
| author | Zhang, Qintong and Lv, Xinjie and Wu, Jialong and Li, Baixuan and Tao, Zhengwei and Yan, Guochen and Zhang, Huanyao and Wang, Bin and Xu, Jiahao and Mi, Haitao and Zhang, Wentao |
| journal | arXiv preprint arXiv:2601.05163 |
| year | 2026 |

</details>

<a id="explicit-retrieval-087"></a>

<details>
<summary>Agent Consolidation — Exploring Information Seeking Agent Consolidation</summary>

**Paper:** Exploring Information Seeking Agent Consolidation  
**Authors:** Yan, Guochen and Wu, Jialong and Tao, Zhengwei and Li, Bo and Zhang, Qintong and Xu, Jiahao and Mi, Haitao and Fang, Yuejian and Shen, Qingni and Zhang, Wentao and Wu, Zhonghai  
**Citation:** `ref155`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Paper](https://arxiv.org/abs/2602.00585). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table6_full.tex:162`; order 87.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26<sup>F</sup> |
| OCR | ✓ |
| Deep | -- |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | Keyword(E<sup>T</sup>) + LLM<sup>t</sup>(E<sup>T</sup>→[E<sup>TV</sup>, P<sup>V</sup>]) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen |
| Learning | SFT |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Exploring Information Seeking Agent Consolidation |
| author | Yan, Guochen and Wu, Jialong and Tao, Zhengwei and Li, Bo and Zhang, Qintong and Xu, Jiahao and Mi, Haitao and Fang, Yuejian and Shen, Qingni and Zhang, Wentao and Wu, Zhonghai |
| journal | arXiv preprint arXiv:2602.00585 |
| year | 2026 |

</details>

<a id="explicit-retrieval-088"></a>

<details>
<summary>AWM — AWM: Answerable Working Memory for Long-Document VQA Agents</summary>

**Paper:** AWM: Answerable Working Memory for Long-Document VQA Agents  
**Authors:** Zhou, Dongzhuoran and Zhu, Yuqicheng and Liu, Yule and Yang, Zhen and Lu, Rui and Dong, Yuxiao and Tang, Jie and Kharlamov, Evgeny  
**Citation:** `ref96`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.25618). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:163`; order 88.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26<sup>F</sup> |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | Jina(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | AWM: Answerable Working Memory for Long-Document VQA Agents |
| author | Zhou, Dongzhuoran and Zhu, Yuqicheng and Liu, Yule and Yang, Zhen and Lu, Rui and Dong, Yuxiao and Tang, Jie and Kharlamov, Evgeny |
| journal | arXiv preprint arXiv:2608.25618 |
| year | 2026 |

</details>

<a id="explicit-retrieval-089"></a>

<details>
<summary>Doc-REFRAG — Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation</summary>

**Paper:** Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation  
**Authors:** Hu, Ruofan and Xu, Shengyang and Hong, Minjie and Yang, Xiaoda and Zhou, Sashuai and Lei, Ke and Jin, Tao and Zhao, Zhou  
**Citation:** `ref59`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.30163). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:164`; order 89.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | Jina(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Llama |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation |
| author | Hu, Ruofan and Xu, Shengyang and Hong, Minjie and Yang, Xiaoda and Zhou, Sashuai and Lei, Ke and Jin, Tao and Zhao, Zhou |
| journal | arXiv preprint arXiv:2608.30163 |
| year | 2026 |

</details>

<a id="explicit-retrieval-090"></a>

<details>
<summary>Doc-Search — DocArena: Turning Raw Documents into Controllable Training Environments for Document Search Agents</summary>

**Paper:** DocArena: Turning Raw Documents into Controllable Training Environments for Document Search Agents  
**Authors:** Wang, Jiamian and Ruiyi Zhang and Tong Yu and Jing Shi and Samyadeep Basu and Rajiv Jain and Zhiqiang Tao and Tong Sun  
**Citation:** `ref95`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.26122). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:165`; order 90.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>→P<sup>T</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen |
| Learning | RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocArena: Turning Raw Documents into Controllable Training Environments for Document Search Agents |
| author | Wang, Jiamian and Ruiyi Zhang and Tong Yu and Jing Shi and Samyadeep Basu and Rajiv Jain and Zhiqiang Tao and Tong Sun |
| journal | arXiv preprint arXiv:2606.26122 |
| year | 2026 |

</details>

<a id="explicit-retrieval-091"></a>

<details>
<summary>Hybrid Retriever Evolution — Hybrid Retriever Evolution for Multimodal Document Reasoning Agents</summary>

**Paper:** Hybrid Retriever Evolution for Multimodal Document Reasoning Agents  
**Authors:** Yao, Bohan and Shruthan Radhakrishna and Vikas Yadav  
**Citation:** `ref107`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.29648). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:166`; order 91.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | BM25(E<sup>T</sup>) + ColBERT(E<sup>T</sup>) + ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Gemini/GPT-5 |
| Learning | ✗ |
| Eval. | Ans. Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Hybrid Retriever Evolution for Multimodal Document Reasoning Agents |
| author | Yao, Bohan and Shruthan Radhakrishna and Vikas Yadav |
| journal | arXiv preprint arXiv:2606.29648 |
| year | 2026 |

</details>

<a id="explicit-retrieval-092"></a>

<details>
<summary>MARDoc — MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA</summary>

**Paper:** MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA  
**Authors:** Chen, Kaifeng and Hongtao Liu and Qiyao Peng and Jian Yang and Yongqiang Liu and Xiaochen Zhang and Qing Yang  
**Citation:** `ref141`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.05749). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:167`; order 92.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Tree |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | Keyword(E<sup>T</sup>) + VLM(P<sup>V</sup>; E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA |
| author | Chen, Kaifeng and Hongtao Liu and Qiyao Peng and Jian Yang and Yongqiang Liu and Xiaochen Zhang and Qing Yang |
| journal | arXiv preprint arXiv:2606.05749 |
| year | 2026 |

</details>

<a id="explicit-retrieval-093"></a>

<details>
<summary>CDS — Constrained Dominant Sets for Multimodal Document Question Answering</summary>

**Paper:** Constrained Dominant Sets for Multimodal Document Question Answering  
**Authors:** Mehrish, Ambuj and Sebastiano Vascon  
**Citation:** `ref99`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.07252). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:168`; order 93.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | Nomic(E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Constrained Dominant Sets for Multimodal Document Question Answering |
| author | Mehrish, Ambuj and Sebastiano Vascon |
| journal | arXiv preprint arXiv:2606.07252 |
| year | 2026 |

</details>

<a id="explicit-retrieval-094"></a>

<details>
<summary>FlowReader — FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&amp;A</summary>

**Paper:** FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&amp;A  
**Authors:** Mehrish, Ambuj and Sebastiano Vascon  
**Citation:** `ref114`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.07235). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:169`; order 94.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Elem. |
| Mechanism | Nomic(E<sup>T</sup>→E<sup>TV</sup>) + BM25(E<sup>T</sup>→E<sup>TV</sup>) + VLM(E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&amp;A |
| author | Mehrish, Ambuj and Sebastiano Vascon |
| journal | arXiv preprint arXiv:2606.07235 |
| year | 2026 |

</details>

<a id="explicit-retrieval-095"></a>

<details>
<summary>EviProp — EviProp: Seeded Relevance Diffusion on Chunk-Page Graphs for Long Multimodal Document Retrieval</summary>

**Paper:** EviProp: Seeded Relevance Diffusion on Chunk-Page Graphs for Long Multimodal Document Retrieval  
**Authors:** Zhang, Hongwei and Wang, Xiaoman and Ling, Zehui and Zhu, Ruicheng and Zhang, Yue and Cai, Pinlong and Shen, Fuke and Shi, Botian and Wei, Tongquan and Yan, Guohang  
**Citation:** `ref115`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.08979). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:170`; order 95.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | ColPali(P<sup>V</sup>; E<sup>V</sup>→P<sup>V</sup>) + OpenAI Embedding(E<sup>T</sup>→P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | EviProp: Seeded Relevance Diffusion on Chunk-Page Graphs for Long Multimodal Document Retrieval |
| author | Zhang, Hongwei and Wang, Xiaoman and Ling, Zehui and Zhu, Ruicheng and Zhang, Yue and Cai, Pinlong and Shen, Fuke and Shi, Botian and Wei, Tongquan and Yan, Guohang |
| journal | arXiv preprint arXiv:2606.08979 |
| year | 2026 |

</details>

<a id="explicit-retrieval-096"></a>

<details>
<summary>MAGE-RAG — MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal RAG in Long-Document QA</summary>

**Paper:** MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal RAG in Long-Document QA  
**Authors:** Zuo, Yilong and Li, Xunkai and Yuan, Jing and Dai, Qiangqiang and Qin, Hongchao and Li, Ronghua  
**Citation:** `ref56`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.15906). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:171`; order 96.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph, Summary |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | ColPali(P<sup>V</sup>) + VLM(P<sup>T</sup>→P<sup>TV</sup>; E<sup>T</sup>→E<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal RAG in Long-Document QA |
| author | Zuo, Yilong and Li, Xunkai and Yuan, Jing and Dai, Qiangqiang and Qin, Hongchao and Li, Ronghua |
| journal | arXiv preprint arXiv:2606.15906 |
| year | 2026 |

</details>

<a id="explicit-retrieval-097"></a>

<details>
<summary>Six-tool Agent — An Empirical Study of VLM Pipelines for Long-Document QA</summary>

**Paper:** An Empirical Study of VLM Pipelines for Long-Document QA  
**Authors:** Ak, Kenan E. and Jay Mohta and Gwang Gook Lee and Yan Xu and Dimitrios Dimitriadis  
**Citation:** `ref116`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.29933). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:172`; order 97.

| Field | Source value |
| --- | --- |
| Venue | EMNLP’26<sup>I</sup> |
| OCR | ✓ |
| Deep | Tree |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | BM25(E<sup>T</sup>) + VLM(E<sup>T</sup>→[P<sup>V</sup>, E<sup>TV</sup>]) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Claude/Qwen |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | An Empirical Study of VLM Pipelines for Long-Document QA |
| author | Ak, Kenan E. and Jay Mohta and Gwang Gook Lee and Yan Xu and Dimitrios Dimitriadis |
| journal | arXiv preprint arXiv:2609.29933 |
| year | 2026 |

</details>

<a id="explicit-retrieval-098"></a>

<details>
<summary>TAP-RAG — TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering</summary>

**Paper:** TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering  
**Authors:** Ji, Zhong and Keqi Jin and Yan Zhang and Jiasheng Li  
**Citation:** `ref108`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2607.18917). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:173`; order 98.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Uni(T) |
| Gran. | Page, Elem. |
| Mechanism | text-embedding(E<sup>T</sup>→[E<sup>T</sup>, P<sup>V</sup>]) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering |
| author | Ji, Zhong and Keqi Jin and Yan Zhang and Jiasheng Li |
| journal | arXiv preprint arXiv:2607.18917 |
| year | 2026 |

</details>

<a id="explicit-retrieval-099"></a>

<details>
<summary>HIEVI-RAG — Hierarchical Evidence-Driven Reasoning for Long Document Understanding</summary>

**Paper:** Hierarchical Evidence-Driven Reasoning for Long Document Understanding  
**Authors:** Xiong, Junyu and Yonghui Wang and Rongjian Gu and Chenyu Liu and Bing Yin and Wengang Zhou and Houqiang Li  
**Citation:** `ref137`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2607.04625). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:174`; order 99.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM<sup>t</sup>(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | RL |
| Eval. | Ans. Ret. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Hierarchical Evidence-Driven Reasoning for Long Document Understanding |
| author | Xiong, Junyu and Yonghui Wang and Rongjian Gu and Chenyu Liu and Bing Yin and Wengang Zhou and Houqiang Li |
| journal | arXiv preprint arXiv:2607.04625 |
| year | 2026 |

</details>

<a id="explicit-retrieval-100"></a>

<details>
<summary>HierDoc — HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual Question Answering</summary>

**Paper:** HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual Question Answering  
**Authors:** Gu, Rongjian and Wengang Zhou and Junyu Xiong and Yonghui Wang and Bing Yin and Bei Wang and Houqiang Li  
**Citation:** `ref134`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2607.29638). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:175`; order 100.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | VLM<sup>t</sup>(P<sup>V</sup>; E<sup>TV</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret.<sup>a</sup> Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual Question Answering |
| author | Gu, Rongjian and Wengang Zhou and Junyu Xiong and Yonghui Wang and Bing Yin and Bei Wang and Houqiang Li |
| journal | arXiv preprint arXiv:2607.29638 |
| year | 2026 |

</details>

<a id="explicit-retrieval-101"></a>

<details>
<summary>DocTrace — DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning</summary>

**Paper:** DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning  
**Authors:** Xiang, Le and Guan, Zhicheng and Chen, Hong and Lin, Xiaocong and Lei, Zhenghua and Hu, Teng and He, Bolei and Zeng, Long  
**Citation:** `ref60`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.03292). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:176`; order 101.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | VLM<sup>t</sup>(P<sup>V</sup>→[P<sup>V</sup>, E<sup>T</sup>]) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning |
| author | Xiang, Le and Guan, Zhicheng and Chen, Hong and Lin, Xiaocong and Lei, Zhenghua and Hu, Teng and He, Bolei and Zeng, Long |
| journal | arXiv preprint arXiv:2608.03292 |
| year | 2026 |

</details>

<a id="explicit-retrieval-102"></a>

<details>
<summary>DocMemo — DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding</summary>

**Paper:** DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding  
**Authors:** Yao, Hanshu and Janfeng Zhong and Niu Lian and Jinpeng Wang  
**Citation:** `ref148`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.07067). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:177`; order 102.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Tree, Summary |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | ColQwen(P<sup>V</sup>→P<sup>TV</sup>) + LLM(P<sup>T</sup>→P<sup>TV</sup>) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding |
| author | Yao, Hanshu and Janfeng Zhong and Niu Lian and Jinpeng Wang |
| journal | arXiv preprint arXiv:2608.07067 |
| year | 2026 |

</details>

<a id="explicit-retrieval-103"></a>

<details>
<summary>InSight-doc — InSight-doc: Agentic Visual Perception for Long-Document Understanding</summary>

**Paper:** InSight-doc: Agentic Visual Perception for Long-Document Understanding  
**Authors:** Li, Kaican and Weiyan Xie and Lewei Yao and Jiannan Wu and Lanqing Hong and Yongxiang Huang and Nevin L. Zhang  
**Citation:** `ref69`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.10628). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:178`; order 103.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | VLM<sup>t</sup>(E<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Loc. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | InSight-doc: Agentic Visual Perception for Long-Document Understanding |
| author | Li, Kaican and Weiyan Xie and Lewei Yao and Jiannan Wu and Lanqing Hong and Yongxiang Huang and Nevin L. Zhang |
| journal | arXiv preprint arXiv:2608.10628 |
| year | 2026 |

</details>

<a id="explicit-retrieval-104"></a>

<details>
<summary>TRIDENT — What the Reranker Sees: Multi-Aspect Page Annotation for Long-Document Multimodal Question Answering</summary>

**Paper:** What the Reranker Sees: Multi-Aspect Page Annotation for Long-Document Multimodal Question Answering  
**Authors:** Wu, Guanchen and Jiayuan Ding and Subhabrata Mukherjee and Carl Yang  
**Citation:** `ref143`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.14841). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:179`; order 104.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph, Tree, Summary |
| Modality | Uni(T) |
| Gran. | Page |
| Mechanism | XKG(P<sup>T</sup>→P<sup>V</sup>) + LLM(P<sup>T</sup>→P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | GPT-4 |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | What the Reranker Sees: Multi-Aspect Page Annotation for Long-Document Multimodal Question Answering |
| author | Wu, Guanchen and Jiayuan Ding and Subhabrata Mukherjee and Carl Yang |
| journal | arXiv preprint arXiv:2608.14841 |
| year | 2026 |

</details>

<a id="explicit-retrieval-105"></a>

<details>
<summary>D2-ScaleAgent — D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding</summary>

**Paper:** D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding  
**Authors:** Zhang, Hao and Longrong Yang and Lunhao Duan and Ziyang Wang and Qing-Guo Chen and Shanshan Zhao  
**Citation:** `ref149`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.16417). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:180`; order 105.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM(P<sup>V</sup>→[P<sup>V</sup>, E<sup>T</sup>]) |
| Acq. | Iterative |
| Agent | Multi |
| Reasoning | Multi-step |
| Model | GPT-4o |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding |
| author | Zhang, Hao and Longrong Yang and Lunhao Duan and Ziyang Wang and Qing-Guo Chen and Shanshan Zhao |
| journal | arXiv preprint arXiv:2608.16417 |
| year | 2026 |

</details>

<a id="explicit-retrieval-106"></a>

<details>
<summary>DocClaw — DocClaw: A Unified Agentic System for Intelligent Document Processing</summary>

**Paper:** DocClaw: A Unified Agentic System for Intelligent Document Processing  
**Authors:** Xiang, Siqi and Zhipeng Xu and Yufei Liu and Junhao Ji and Qing Liu and Zulong Chen and Zhibo Yang and Chunyan Miao and Shijian Lu  
**Citation:** `ref145`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.18685). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:181`; order 106.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Tree |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | BM25(P<sup>T</sup>; E<sup>T</sup>) + ColBERT(P<sup>T</sup>; E<sup>T</sup>) + ColPali(P<sup>V</sup>) + VLM(P<sup>V</sup>; E<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | GPT-5/Gemini |
| Learning | ✗ |
| Eval. | Ans. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocClaw: A Unified Agentic System for Intelligent Document Processing |
| author | Xiang, Siqi and Zhipeng Xu and Yufei Liu and Junhao Ji and Qing Liu and Zulong Chen and Zhibo Yang and Chunyan Miao and Shijian Lu |
| journal | arXiv preprint arXiv:2608.18685 |
| year | 2026 |

</details>

<a id="explicit-retrieval-107"></a>

<details>
<summary>ViSAR — ViSAR: Training-Free Adaptive- k Retrieval for Visual Document Question Answering</summary>

**Paper:** ViSAR: Training-Free Adaptive- k Retrieval for Visual Document Question Answering  
**Authors:** Mialland, Adrien and Marc Plantevit and Julien Gallois and Céline Robardet  
**Citation:** `ref73`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.02486). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:182`; order 107.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page |
| Mechanism | ColPali/ColQwen/ColModernVBERT(P<sup>V</sup>) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | ViSAR: Training-Free Adaptive- k Retrieval for Visual Document Question Answering |
| author | Mialland, Adrien and Marc Plantevit and Julien Gallois and Céline Robardet |
| journal | arXiv preprint arXiv:2609.02486 |
| year | 2026 |

</details>

<a id="explicit-retrieval-108"></a>

<details>
<summary>CAVR+WSPS+VET — Capability-Routed Visual Retrieval and Evidence Threading for Long-Context Document Question Answering</summary>

**Paper:** Capability-Routed Visual Retrieval and Evidence Threading for Long-Context Document Question Answering  
**Authors:** Rahman, Amirul and Aisha Karim and Kenji Nakamura and Yi-Fan Ng  
**Citation:** `ref121`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.13268). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:183`; order 108.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Graph |
| Modality | Mixed(T/V) |
| Gran. | Page, Elem. |
| Mechanism | ColPali(P<sup>V</sup>) + WSPS<sup>t</sup>(P<sup>V</sup>) + VET<sup>t</sup>([P<sup>V</sup>, E<sup>T</sup>]) |
| Acq. | One-shot |
| Agent | Single |
| Reasoning | Single-pass |
| Model | Qwen-VL |
| Learning | SFT |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Capability-Routed Visual Retrieval and Evidence Threading for Long-Context Document Question Answering |
| author | Rahman, Amirul and Aisha Karim and Kenji Nakamura and Yi-Fan Ng |
| journal | arXiv preprint arXiv:2609.13268 |
| year | 2026 |

</details>

<a id="explicit-retrieval-109"></a>

<details>
<summary>SCORE — Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation</summary>

**Paper:** Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation  
**Authors:** Shen, Yucheng and Lingyong Yan and Jiulong Wu and Shuaiqiang Wang and Jianmin WU and Dawei Yin and Min Cao  
**Citation:** `ref150`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.15800). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:184`; order 109.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✗ |
| Deep | ✗ |
| Modality | Uni(V) |
| Gran. | Page, Elem. |
| Mechanism | ColQwen(P<sup>V</sup>) + VLM<sup>t</sup>(P<sup>V</sup>; E<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Qwen-VL |
| Learning | SFT + RL |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation |
| author | Shen, Yucheng and Lingyong Yan and Jiulong Wu and Shuaiqiang Wang and Jianmin WU and Dawei Yin and Min Cao |
| journal | arXiv preprint arXiv:2609.15800 |
| year | 2026 |

</details>

<a id="explicit-retrieval-110"></a>

<details>
<summary>TAEC — TAEC: Trajectory-Aware Evidence Coordination for Multi-Step Visual RAG</summary>

**Paper:** TAEC: Trajectory-Aware Evidence Coordination for Multi-Step Visual RAG  
**Authors:** Wu, Yalun and Bingzhou Wang and Boyang Wang and Peiying Wang and Shaojie He and Yunhan Wang and Shaozu Yuan and Jiawei Wang  
**Citation:** `ref158`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Paper](https://arxiv.org/abs/2609.37349). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table6_full.tex:185`; order 110.

| Field | Source value |
| --- | --- |
| Venue | arXiv’26 |
| OCR | ✓ |
| Deep | Summary |
| Modality | Mixed(T/V) |
| Gran. | Page |
| Mechanism | Qwen-VL-Embedding(P<sup>V</sup>) + Keyword(P<sup>T</sup>→P<sup>V</sup>) + VLM(P<sup>V</sup>) |
| Acq. | Iterative |
| Agent | Single |
| Reasoning | Multi-step |
| Model | Gemini |
| Learning | ✗ |
| Eval. | Ans. Ret. Eff. |

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | TAEC: Trajectory-Aware Evidence Coordination for Multi-Step Visual RAG |
| author | Wu, Yalun and Bingzhou Wang and Boyang Wang and Peiying Wang and Shaojie He and Yunhan Wang and Shaozu Yuan and Jiawei Wang |
| journal | arXiv preprint arXiv:2609.37349 |
| year | 2026 |

</details>

<a id="source-notes"></a>

## Full source notes

Header abbreviations. Deep = Deep Parsing; Gran. = Granularity; Acq. = Acquisition; Eval. = Evaluation.

Type labels. Deep and Learning list structure and training types directly; a standalone ✓ in Learning denotes added training without a listed type. SFT/RL: supervised fine-tuning/reinforcement learning.

1. Mechanism. D/P/E denotes document/page/element; superscripts T/V/TV denote text/visual/both. The left side of → is the evidence representation returned by retrieval or selection; the right side is the generation input. Without an arrow, retrieval and generation use the same granularity and modality; retrieval-only methods are labeled by their returned unit. Superscript t denotes additional retrieval, scoring, or page-selection training. Parentheses after model names specify evidence forms; semicolons separate independent paths, and an arrow applies only within its path. Brackets [ ] group multiple evidence items, with commas denoting parallel items.

2. Evaluation. Only dimensions quantitatively reported in the original paper are listed. Ret. evaluates evidence retrieval, usually page-level hits, recall, or ranking; Loc. evaluates within-page element/region localization or coverage, such as IoU or region-overlap recall. Exceptions (a): Ret. is document retrieval for DocMMIR, DocPC, NeuSym-RAG, and Agentic Hybrid (EXTRACTOR), document identification for HiKEY, and additionally document recall for HEAVEN; LILaC evaluates layout-element retrieval, and Doc-Researcher evaluates document/page/layout-element retrieval. G<sup>2</sup>-Reader Ret. measures semantic coverage of evidence statements; LFRAG includes element-ID matching; HierDoc includes region-ID-set F1; MoDora evaluates evidence-node recall and filtering. ReAlign Loc. measures overlap between attention regions and supervised boxes; RGenCite includes VLM-assessed evidence support; Lang2Act measures the proportion of internal attention falling within gold regions. MMRetHeads evaluates pages and layout regions on MMDocIR; LMS-Retrieval Ret./Loc. measure layout-element recall and region coverage.

**Shared evaluation abbreviations:** Ans. = answer quality; Ret. = evidence retrieval; Loc. = within-page localization; Eff. = efficiency and cost; Rob. = robustness. The source notes above qualify these labels for individual methods.

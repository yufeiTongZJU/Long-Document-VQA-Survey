# Benchmark catalog

[Repository home](../README.md) · [Benchmarks](benchmarks.md) · [Direct reading](direct-reading.md) · [Explicit retrieval](explicit-retrieval.md)

**55 records.** Generated from manuscript `tables/table4_full.tex`. Source rows, groups, qualifiers, and notation are preserved.

[JSON](../data/benchmarks.json) · [CSV](../data/benchmarks.csv) · [Bibliography](../references.bib) · [Data dictionary](../data/README.md)

Complete benchmark catalog: 55 records covering dataset size, question types, evidence annotations, and evaluation capabilities. Ordering and first-release dates follow Table 1 (representative explicit-retrieval methods). -- denotes unreported or inapplicable information.

**Dates and citation years.** First release is separate from the citation year in the current BibTeX. YY.MM preferentially denotes the first arXiv version; an earlier official release, or the official release when no preprint exists, takes precedence. A -- month is unavailable and is stored as null, never as an invented month.

**Order.** Source row order is preserved. Within task groups, methods follow final conference submission deadlines, then first release within each conference; preprints/journal papers are inserted by first release (Table 1 convention).

**Notation.** ✓ = present/included; ✗ = absent/excluded. `--` means unreported or inapplicable. Venue superscripts F/W/D/S/I/C mean Findings, Workshop, Datasets and Benchmarks, Short, Industry, and competition reports, respectively.

**Links.** “Paper” uses an academic URL or explicit arXiv identifier already recorded in the manuscript bibliography/provenance. Links were not independently rechecked for this repository. “Google Scholar search” is a title search, not a verified paper link.

## Browse

- [Retrieval-focused benchmarks (11)](#group-1)
- [Answer-quality benchmarks: #Pages (avg.) = 1.0, #Pages (avg.) &gt; 1.0 or unreported (44)](#group-2)
- [Full source notes](#source-notes)

<a id="group-1"></a>

## Retrieval-focused benchmarks

| Name | Venue | First release | Bib year | Domain | #Docs | #Pages | #Tokens | #QA | MD | MP | SP | Unans. | Source | Gran. | Eval. | Citation / source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Wiki-SS](#benchmarks-001) | EMNLP’24 | 24.06 | 2024 | Open | -- | 1.27M | -- | 52.7k | ✗ | ✗ | ✓ | ✗ | TXT | Page | Ans. Ret. | `ma2024unifying`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20multimodal%20retrieval%20via%20document%20screenshot%20embedding) |
| [SlideVQA-open](#benchmarks-002) | EMNLP’24 | 24.06 | 2024 | Open | -- | 50.7k | -- | 12.4k | ✗ | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ret. | `ma2024unifying`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20multimodal%20retrieval%20via%20document%20screenshot%20embedding) |
| [ViDoRe](#benchmarks-003) | ICLR’25 | 24.06 | 2025 | Open | -- | 1.0k | -- | 3.81k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans.<sup>a</sup> Ret. | `ref7`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Colpali%3A%20Efficient%20document%20retrieval%20with%20vision%20language%20models) |
| [REAL-MM-RAG](#benchmarks-004) | ACL’25 | 25.02 | 2025 | Open | 163 | 2.1k | -- | 4.6k | ✗ | ✗ | ✓ | ✗ | TXT/C/TAB/I | Page | Ans. Ret. | `ref88`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Real-mm-rag%3A%20A%20real-world%20multi-modal%20retrieval%20benchmark) |
| [ViDoRe V2](#benchmarks-005) | arXiv’25 | 25.03 | 2025 | Open | 62 | 1.1k | -- | 327 | ✓ | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ret. | `ref82`<br>[Paper](https://arxiv.org/abs/2505.17166) |
| [MMDocIR](#benchmarks-006) | EMNLP’25 | 25.01 | 2025 | Closed | 313 | 65.1 | -- | 1.66k | ✗ | ✓(18.9%) | ✓(81.1%) | ✗ | TXT/L/C/TAB/I | Page, Elem. | Ret. Loc. | `ref17`<br>[Google Scholar search](https://scholar.google.com/scholar?q=MMDocIR%3A%20Benchmarking%20multimodal%20retrieval%20for%20long%20documents) |
| [DocMMIR](#benchmarks-007) | EMNLP’25<sup>F</sup> | 25.05 | 2025 | Open | 488.5k | -- | 537.4 | 488.5k | -- | -- | -- | -- | TXT/C/TAB/I | Doc. | Ret.<sup>a</sup> | `ref19`<br>[Google Scholar search](https://scholar.google.com/scholar?q=DocMMIR%3A%20A%20Framework%20for%20Document%20Multi-modal%20Information%20Retrieval) |
| [ViMDoc](#benchmarks-008) | ACL’26<sup>F</sup> | 25.10 | 2026 | Open | 1.4k | 76.3k | -- | 10.9k | -- | ✓ | ✓ | -- | TXT/L/C/TAB/I | Page | Ret. | `ref80`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Hybrid-vector%20retrieval%20for%20visually%20rich%20documents%3A%20Combining%20single-vector%20efficiency%20and%20multi-vector%20accuracy) |
| [MultiDocR](#benchmarks-009) | KDD’26 | 26.05 | 2026 | Open | 313 | -- | -- | 2.58k | -- | ✓(43.8%) | ✓(56.2%) | ✗ | TXT/C/TAB/I | Page | Ans. Ret. | `ref106`<br>[Paper](https://arxiv.org/abs/2605.30027) |
| [CMDR-Bench](#benchmarks-010) | ECCV’26 | 26.07 | 2026 | Closed | 255 | 183.5 | -- | 800 | ✗ | ✓ | -- | ✗ | TXT/L/C/TAB/I | Page | Ret. | `ref79`<br>[Google Scholar search](https://scholar.google.com/scholar?q=CMDR%3A%20Contextual%20Multimodal%20Document%20Retrieval) |
| [DocViRe](#benchmarks-011) | arXiv’26 | 26.08 | 2026 | Open | 8.29k | -- | -- | 13.1k | -- | -- | -- | -- | TXT/C/TAB/I | Doc. | Ret.<sup>a</sup> | `ref122`<br>[Paper](https://arxiv.org/abs/2608.25434) |

<a id="benchmarks-001"></a>

<details>
<summary>Wiki-SS — Unifying multimodal retrieval via document screenshot embedding</summary>

**Paper:** Unifying multimodal retrieval via document screenshot embedding  
**Authors:** Ma, Xueguang and Lin, Sheng-Chieh and Li, Minghan and Chen, Wenhu and Lin, Jimmy  
**Citation:** `ma2024unifying`; current BibTeX year **2024**; first release **24.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20multimodal%20retrieval%20via%20document%20screenshot%20embedding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:31`; order 1.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Unifying multimodal retrieval via document screenshot embedding |
| author | Ma, Xueguang and Lin, Sheng-Chieh and Li, Minghan and Chen, Wenhu and Lin, Jimmy |
| booktitle | Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing |
| pages | 6492--6505 |
| year | 2024 |

</details>

<a id="benchmarks-002"></a>

<details>
<summary>SlideVQA-open — Unifying multimodal retrieval via document screenshot embedding</summary>

**Paper:** Unifying multimodal retrieval via document screenshot embedding  
**Authors:** Ma, Xueguang and Lin, Sheng-Chieh and Li, Minghan and Chen, Wenhu and Lin, Jimmy  
**Citation:** `ma2024unifying`; current BibTeX year **2024**; first release **24.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20multimodal%20retrieval%20via%20document%20screenshot%20embedding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:32`; order 2.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Unifying multimodal retrieval via document screenshot embedding |
| author | Ma, Xueguang and Lin, Sheng-Chieh and Li, Minghan and Chen, Wenhu and Lin, Jimmy |
| booktitle | Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing |
| pages | 6492--6505 |
| year | 2024 |

</details>

<a id="benchmarks-003"></a>

<details>
<summary>ViDoRe — Colpali: Efficient document retrieval with vision language models</summary>

**Paper:** Colpali: Efficient document retrieval with vision language models  
**Authors:** Faysse, Manuel and Sibille, Hugues and Wu, Tony and Omrani, Bilel and Viaud, Gautier and Hudelot, Céline and Colombo, Pierre  
**Citation:** `ref7`; current BibTeX year **2025**; first release **24.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Colpali%3A%20Efficient%20document%20retrieval%20with%20vision%20language%20models). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:33`; order 3.

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

<a id="benchmarks-004"></a>

<details>
<summary>REAL-MM-RAG — Real-mm-rag: A real-world multi-modal retrieval benchmark</summary>

**Paper:** Real-mm-rag: A real-world multi-modal retrieval benchmark  
**Authors:** Wasserman, Navve and Pony, Roi and Naparstek, Oshri and Goldfarb, Adi Raz and Schwartz, Eli and Barzelay, Udi and Karlinsky, Leonid  
**Citation:** `ref88`; current BibTeX year **2025**; first release **25.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Real-mm-rag%3A%20A%20real-world%20multi-modal%20retrieval%20benchmark). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:34`; order 4.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Real-mm-rag: A real-world multi-modal retrieval benchmark |
| author | Wasserman, Navve and Pony, Roi and Naparstek, Oshri and Goldfarb, Adi Raz and Schwartz, Eli and Barzelay, Udi and Karlinsky, Leonid |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2025 |
| pages | 31660--31683 |

</details>

<a id="benchmarks-005"></a>

<details>
<summary>ViDoRe V2 — Vidore benchmark v2: Raising the bar for visual retrieval</summary>

**Paper:** Vidore benchmark v2: Raising the bar for visual retrieval  
**Authors:** Macé, Quentin and António Loison and Manuel Faysse  
**Citation:** `ref82`; current BibTeX year **2025**; first release **25.03**.  
**Source:** [Paper](https://arxiv.org/abs/2505.17166). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:35`; order 5.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Vidore benchmark v2: Raising the bar for visual retrieval |
| author | Macé, Quentin and António Loison and Manuel Faysse |
| journal | arXiv preprint arXiv:2505.17166 |
| year | 2025 |

</details>

<a id="benchmarks-006"></a>

<details>
<summary>MMDocIR — MMDocIR: Benchmarking multimodal retrieval for long documents</summary>

**Paper:** MMDocIR: Benchmarking multimodal retrieval for long documents  
**Authors:** Dong, Kuicai and Chang, Yujing and Deik, Derrick Goh Xin and Li, Dexun and Tang, Ruiming and Liu, Yong  
**Citation:** `ref17`; current BibTeX year **2025**; first release **25.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=MMDocIR%3A%20Benchmarking%20multimodal%20retrieval%20for%20long%20documents). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:36`; order 6.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | MMDocIR: Benchmarking multimodal retrieval for long documents |
| author | Dong, Kuicai and Chang, Yujing and Deik, Derrick Goh Xin and Li, Dexun and Tang, Ruiming and Liu, Yong |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 30959--30993 |

</details>

<a id="benchmarks-007"></a>

<details>
<summary>DocMMIR — DocMMIR: A Framework for Document Multi-modal Information Retrieval</summary>

**Paper:** DocMMIR: A Framework for Document Multi-modal Information Retrieval  
**Authors:** Li, Zirui and Siwei Wu and Yizhi Li and Xingyu Wang and Yi Zhou and Chenghua Lin  
**Citation:** `ref19`; current BibTeX year **2025**; first release **25.05**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=DocMMIR%3A%20A%20Framework%20for%20Document%20Multi-modal%20Information%20Retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:37`; order 7.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocMMIR: A Framework for Document Multi-modal Information Retrieval |
| author | Li, Zirui and Siwei Wu and Yizhi Li and Xingyu Wang and Yi Zhou and Chenghua Lin |
| booktitle | EMNLP (Findings) |
| pages | 13117--13130 |
| year | 2025 |

</details>

<a id="benchmarks-008"></a>

<details>
<summary>ViMDoc — Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy</summary>

**Paper:** Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy  
**Authors:** Kim, Juyeon and Geon Lee and Dongwon Choi and Taeuk Kim and Kijung Shin  
**Citation:** `ref80`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Hybrid-vector%20retrieval%20for%20visually%20rich%20documents%3A%20Combining%20single-vector%20efficiency%20and%20multi-vector%20accuracy). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:38`; order 8.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy |
| author | Kim, Juyeon and Geon Lee and Dongwon Choi and Taeuk Kim and Kijung Shin |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2026 |
| pages | 1073--1089 |
| year | 2026 |

</details>

<a id="benchmarks-009"></a>

<details>
<summary>MultiDocR — DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval with Comprehensive Benchmark</summary>

**Paper:** DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval with Comprehensive Benchmark  
**Authors:** Hu, Ruofan and Zhu, Menghui and Zhu, Jieming and Chen, Bo and Xu, Shengyang and Hong, Minjie and Yang, Xiaoda and Zhou, Sashuai and Tang, Li and Jin, Tao and Zhao, Zhou  
**Citation:** `ref106`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.30027). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:39`; order 9.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval with Comprehensive Benchmark |
| author | Hu, Ruofan and Zhu, Menghui and Zhu, Jieming and Chen, Bo and Xu, Shengyang and Hong, Minjie and Yang, Xiaoda and Zhou, Sashuai and Tang, Li and Jin, Tao and Zhao, Zhou |
| booktitle | Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2 |
| pages | 1780--1791 |
| year | 2026 |

</details>

<a id="benchmarks-010"></a>

<details>
<summary>CMDR-Bench — CMDR: Contextual Multimodal Document Retrieval</summary>

**Paper:** CMDR: Contextual Multimodal Document Retrieval  
**Authors:** Tanaka, Ryota and Taku Hasegawa and Kyosuke Nishida  
**Citation:** `ref79`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=CMDR%3A%20Contextual%20Multimodal%20Document%20Retrieval). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:40`; order 10.

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

<a id="benchmarks-011"></a>

<details>
<summary>DocViRe — DocPC: Document-Level Visual Retrieval via Representative Page Composition</summary>

**Paper:** DocPC: Document-Level Visual Retrieval via Representative Page Composition  
**Authors:** You, Chengsong and Zhou, Junwei and Cao, Xiaoyu and Wang, Weiyao and Xu, Yiwei and Zhao, Ziyan and Sun, Zhen and Zhu, Qicheng and Fu, Xuanyi and Chen, Yufan and others  
**Citation:** `ref122`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Paper](https://arxiv.org/abs/2608.25434). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:41`; order 11.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocPC: Document-Level Visual Retrieval via Representative Page Composition |
| author | You, Chengsong and Zhou, Junwei and Cao, Xiaoyu and Wang, Weiyao and Xu, Yiwei and Zhao, Ziyan and Sun, Zhen and Zhu, Qicheng and Fu, Xuanyi and Chen, Yufan and others |
| journal | arXiv preprint arXiv:2608.25434 |
| year | 2026 |

</details>

<a id="group-2"></a>

## Answer-quality benchmarks: #Pages (avg.) = 1.0, #Pages (avg.) &gt; 1.0 or unreported

| Name | Venue | First release | Bib year | Domain | #Docs | #Pages | #Tokens | #QA | MD | MP | SP | Unans. | Source | Gran. | Eval. | Citation / source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DocVQA](#benchmarks-012) | WACV’21 | 20.07 | 2021 | Closed | 12.8k | 1.0 | 151.5 | 50k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | -- | Ans. | `mathew2021docvqa`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Docvqa%3A%20A%20dataset%20for%20vqa%20on%20document%20images) |
| [InfographicVQA](#benchmarks-013) | WACV’22 | 21.04 | 2022 | Closed | 5.5k | 1.0 | 217.9 | 30k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | -- | Ans. | `ref62`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Infographicvqa) |
| [ChartQA](#benchmarks-014) | ACL’22<sup>F</sup> | 22.03 | 2022 | Closed | 20.9k | 1.0 | -- | 32.7k | ✗ | ✗ | ✓ | ✗ | C | -- | Ans. | `ref75`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Chartqa%3A%20A%20benchmark%20for%20question%20answering%20about%20charts%20with%20visual%20and%20logical%20reasoning) |
| [ArXivQA&#42;](#benchmarks-015) | ACL’24 | 24.03 | 2024 | Closed | 16.6k | 1.0 | -- | 100k | ✗ | ✗ | ✓ | ✗ | C/TAB/I | -- | Ans. | `ref78`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Multimodal%20arxiv%3A%20A%20dataset%20for%20improving%20scientific%20comprehension%20of%20large%20vision-language%20models) |
| [DOGR-Bench](#benchmarks-016) | ICCV’25 | 24.11 | 2025 | Closed | -- | 1.0 | -- | 3.6k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/I | Elem. | Ans. Loc. | `ref15`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Dogr%3A%20Towards%20versatile%20visual%20document%20grounding%20and%20referring) |
| [GroundingDocQA-Bench](#benchmarks-017) | CVPR’26 | 26.06 | 2026 | Closed | 2.5k | 1.0 | -- | 5.0k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | Elem. | Ans. Loc.<sup>a</sup> | `ref119`<br>[Google Scholar search](https://scholar.google.com/scholar?q=M3Grounder%3A%20Mask-Based%20Multi-Span%20and%20Multi-Granular%20Grounding%20for%20Document%20QA) |
| [DoCoG-Bench](#benchmarks-018) | ECCV’26 | 26.09 | 2026 | Closed | 3.0k | 1.0 | -- | 10.0k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | Elem. | Ans. Loc.<sup>a</sup> | `ref120`<br>[Google Scholar search](https://scholar.google.com/scholar?q=DoCoG%3A%20Mask-Based%20Multi-type%20Grounded%20Chain-of-Thought%20for%20Document%20QA) |
| [TAT-DQA](#benchmarks-019) | MM’22 | 22.07 | 2022 | Closed | 2.8k | 1.1 | -- | 16.6k | ✗ | ✓ | ✓ | ✗ | TXT/L/TAB | -- | Ans. | `ref86`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Towards%20complex%20document%20understanding%20by%20discrete%20reasoning) |
| [SlideVQA](#benchmarks-020) | AAAI’23 | 23.01 | 2023 | Closed | 2,619 | 20.0 | 1.5k | 14.5k | ✗ | ✓(13.9%) | ✓(86.1%) | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `tanaka2023slidevqa`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Slidevqa%3A%20A%20dataset%20for%20document%20visual%20question%20answering%20on%20multiple%20images) |
| [MP-DocVQA](#benchmarks-021) | PR’23 | 22.12 | 2023 | Closed | 5,928 | 8.3 | 2.0k | 46.2k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `tito2023hierarchical`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Hierarchical%20multimodal%20transformers%20for%20multipage%20docvqa) |
| [DUDE](#benchmarks-022) | ICCV’23 | 23.05 | 2023 | Closed | 5,019 | 5.72 | 1.8k | 41.5k | ✗ | ✓(2.1%) | ✓(85.2%) | ✓(12.7%) | TXT/L/C/TAB/I | -- | Ans. | `ref3`<br>[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Van_Landeghem_Document_Understanding_Dataset_and_Evaluation_DUDE_ICCV_2023_paper.html) |
| [UDA](#benchmarks-023) | NIPS’24<sup>D</sup> | 24.06 | 2024 | Closed | 2.97k | -- | -- | 29.6k | ✗ | -- | ✓ | -- | TXT/TAB | Elem. | Ans. Ret.<sup>a</sup> | `ref100`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Uda%3A%20A%20benchmark%20suite%20for%20retrieval%20augmented%20generation%20in%20real-world%20document%20analysis) |
| [MMLongBench-Doc](#benchmarks-024) | NIPS’24<sup>D</sup> | 24.07 | 2024 | Closed | 135 | 47.5 | 21.2k | 1.1k | ✗ | ✓(33.7%) | ✓(45.7%) | ✓(20.6%) | TXT/L/C/TAB/I | Page | Ans. Ret. | `ma2024mmlongbench`<br>[Paper](https://papers.nips.cc/paper_files/paper/2024/hash/ae0e43289bffea0c1fa34633fc608e92-Abstract-Datasets_and_Benchmarks_Track.html) |
| [SPIQA&#42;](#benchmarks-025) | NIPS’24<sup>D</sup> | 24.07 | 2024 | Closed | 25.5k | -- | -- | 266k | ✗ | -- | -- | ✗ | TXT/C/TAB/I | Elem. | Ans. Ret.<sup>a</sup> | `ref5`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Spiqa%3A%20A%20dataset%20for%20multimodal%20question%20answering%20on%20scientific%20papers) |
| [VisRAG](#benchmarks-026) | ICLR’25 | 24.10 | 2025 | Open | -- | 4.5k | -- | 3.6k | ✗ | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `yu2025visrag`<br>[Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3640a1997a4c9571cea9db2c82e1fc35-Abstract-Conference.html) |
| [VisR-Bench](#benchmarks-027) | ICLR’25 | 24.11 | 2024 | Closed | 226 | 13.7 | -- | 0.5k | ✗ | ✗ | ✓ | ✗ | TXT/C/TAB/I | Page | Ans. Ret. | `chen2024svrag`<br>[Paper](https://arxiv.org/abs/2411.01106) |
| [PaperPDF](#benchmarks-028) | IJCV’26 | 24.10 | 2026 | Closed | 70k | 23 | 10.2k | 1.1M | ✗ | ✓ | ✓ | ✗ | TXT/C/TAB/I | Elem. | Ans. Ret.<sup>a</sup> | `ref142`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Wukong%3A%20A%20large%20multimodal%20model%20for%20efficient%20long%20pdf%20reading%20with%20end-to-end%20sparse%20sampling) |
| [VisDoMBench](#benchmarks-029) | NAACL’25 | 24.12 | 2025 | Open | 1,277 | 128.7 | -- | 2.3k | ✗ | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `ref10`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Visdom%3A%20Multi-document%20qa%20with%20visually%20rich%20elements%20using%20multimodal%20retrieval-augmented%20generation) |
| [OpenDocVQA](#benchmarks-030) | CVPR’25 | 25.04 | 2025 | Open | -- | 231.3k | -- | 43.5k | ✓ | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `ref11`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Vdocrag%3A%20Retrieval-augmented%20generation%20over%20visually-rich%20documents) |
| [DocBench](#benchmarks-031) | KNLP’25<sup>W</sup> | 24.07 | 2025 | Closed | 229 | 66 | 46.4k | 1.1k | ✗ | ✓ | ✓ | ✓(11.3%) | TXT/L/C/TAB/I | -- | Ans. | `ref12`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Docbench%3A%20A%20benchmark%20for%20evaluating%20llm-based%20document%20reading%20systems) |
| [Wiki-VISA; Paper-VISA](#benchmarks-032) | ACL’25 | 24.12 | 2025 | Open | -- | -- | -- | 90k; 102.2k | ✗ | ✗ | ✓ | ✓ | TXT/TAB/I | Page, Elem. | Ans. Ret. Loc. | `ref13`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Visa%3A%20Retrieval%20augmented%20generation%20with%20visual%20source%20attribution) |
| [LongDocURL](#benchmarks-033) | ACL’25 | 24.12 | 2025 | Closed | 396 | 85.6 | 43.6k | 2.3k | ✗ | ✓(52.9%) | ✓(47.0%) | ✓(0.1%) | TXT/L/C/TAB/I | Page | Ans. Ret. | `ref14`<br>[Paper](https://aclanthology.org/2025.acl-long.57/) |
| [AIRQA-REAL](#benchmarks-034) | ACL’25 | 25.05 | 2025 | Open/Closed | 6.8k | -- | -- | 553 | ✓(27%) | -- | -- | ✗ | TXT/TAB/I | Doc. | Ans. Ret.<sup>a</sup> | `ref156`<br>[Paper](https://aclanthology.org/2025.acl-long.311/) |
| [MMDocRAG&#42;](#benchmarks-035) | NIPS’25<sup>D</sup> | 25.05 | 2026 | Closed | 222 | 67.0 | -- | 4.06k | ✗ | ✓(52.0%) | ✓(48.0%) | ✗ | TXT/C/TAB/I | Page, Elem. | Ans. Ret.<sup>a</sup> | `ref105`<br>[Paper](https://openreview.net/pdf?id=W4b3v9jx1p) |
| [M-LongDoc](#benchmarks-036) | EMNLP’25 | 24.11 | 2025 | Closed | 180 | 210.8 | 121.0k | 0.9k | ✗ | ✗ | ✓ | ✗ | TXT/C/TAB/I | Page | Ans. Ret. | `ref16`<br>[Google Scholar search](https://scholar.google.com/scholar?q=M-longdoc%3A%20A%20benchmark%20for%20multimodal%20super-long%20document%20understanding%20and%20a%20retrieval-aware%20tuning%20framework) |
| [ViDoSeek](#benchmarks-037) | EMNLP’25 | 25.02 | 2025 | Open | 300 | 6.0k | -- | 1.14k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `ref18`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Vidorag%3A%20Visual%20document%20retrieval-augmented%20generation%20via%20dynamic%20iterative%20reasoning%20agents) |
| [FinRAGBench-V](#benchmarks-038) | EMNLP’25 | 25.05 | 2025 | Open | 2.21k | 57.1k | -- | 1.39k | -- | ✓ | ✓ | ✗ | TXT/C/TAB | Page, Elem. | Ans. Ret. Loc. | `ref109`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Finragbench-v%3A%20A%20benchmark%20for%20multimodal%20rag%20with%20visual%20citation%20in%20the%20financial%20domain) |
| [M3DocVQA](#benchmarks-039) | ICCV’25<sup>W</sup> | 24.11 | 2025 | Open | 3,368 | 41.0k | -- | 2.4k | ✓ | ✓ | ✓ | ✗ | TXT/TAB/I | Doc. | Ans. Ret.<sup>a</sup> | `cho2025m3docvqa`<br>[Google Scholar search](https://scholar.google.com/scholar?q=M3docvqa%3A%20Multi-modal%20multi-page%20multi-document%20understanding) |
| [Double-Bench](#benchmarks-040) | AAAI’26 | 25.08 | 2026 | Open | 3.3k | 72.9k | -- | 5.2k | -- | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. | `ref133`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Are%20we%20on%20the%20right%20way%20to%20assess%20document%20retrieval-augmented%20generation%3F) |
| [AirQA](#benchmarks-041) | ICLR’26 | 25.09 | 2026 | Open/Closed | 14.0k | -- | -- | 1.2k | ✓ | -- | -- | ✗ | TXT/TAB/I | Doc. | Ans. Ret.<sup>a</sup> | `ref157`<br>[Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/10d35352a92bb40943bb4ed096a407b6-Abstract-Conference.html) |
| [M4DocBench](#benchmarks-042) | WWW’26 | 25.10 | 2026 | Open | 303 | 306.4 | -- | 158 | ✓(91.1%) | ✓ | ✓ | ✗ | TXT/C/TAB/I | Page, Elem. | Ans. Ret.<sup>a</sup> Loc. | `dong2026docresearcher`<br>[Paper](https://doi.org/10.1145/3774904.3792599) |
| [DVisRAG](#benchmarks-043) | CVPR’26 | 26.02 | 2026 | Open | -- | -- | -- | 367.6k | ✗ | ✓ | ✓ | ✗ | TXT/L/C/TAB/I | Page | Ans. Ret. Rob. | `ref89`<br>[Google Scholar search](https://scholar.google.com/scholar?q=RobustVisRAG%3A%20Causality-Aware%20Vision-Based%20Retrieval-Augmented%20Generation%20under%20Visual%20Degradations) |
| [VinQA](#benchmarks-044) | CVPR’26 | 26.06 | 2026 | Open | -- | 5.0 | -- | 44.3k | ✓ | ✓ | ✓ | ✓ | TXT/C/TAB/I | Page, Elem. | Ans. Ret. Loc. | `ref98`<br>[Paper](https://arxiv.org/abs/2606.16092) |
| [ViDoRe V3](#benchmarks-045) | ACL’26 | 26.01 | 2026 | Open | -- | -- | -- | 3.1k | ✓ | ✓ | ✓ | -- | TXT/L/C/TAB/I | Page, Elem. | Ans. Ret. Loc. | `ref83`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Vidore%20v3%3A%20A%20comprehensive%20evaluation%20of%20retrieval%20augmented%20generation%20in%20complex%20real-world%20scenarios) |
| [PaperScope&#42;](#benchmarks-046) | ACL’26<sup>F</sup> | 26.04 | 2026 | Open | 2.2k | -- | -- | 2.4k | ✓(91.7%) | ✓ | -- | ✗ | TXT/L/C/TAB/I | Doc. | Ans. Ret.<sup>a</sup> | `ref136`<br>[Google Scholar search](https://scholar.google.com/scholar?q=PaperScope%3A%20A%20Multi-Modal%20Multi-Document%20Benchmark%20for%20Agentic%20Deep%20Research%20Across%20Massive%20Scientific%20Papers) |
| [M5BookVQA](#benchmarks-047) | ACL’26 | 26.07 | 2026 | Open | -- | 16.8k | -- | 2.1k | -- | ✓ | -- | -- | TXT/C/TAB/I | Page | Ans. Ret. | `ref57`<br>[Google Scholar search](https://scholar.google.com/scholar?q=TRACE%3A%20Traversal%20Retrieval-Augmented%20Chain%20of%20Evidence%20for%20Document%20Understanding) |
| [Wiki-CoE](#benchmarks-048) | SIGIR’26 | 26.05 | 2026 | Open | 76.0k | 5.0 | -- | 70.4k | ✓ | ✓ | ✗ | ✗ | TXT/TAB/I/L | Page, Elem. | Ans. Ret. Loc. | `ref111`<br>[Paper](https://arxiv.org/abs/2605.01284) |
| [MMLBD-C](#benchmarks-049) | arXiv’26 | 26.02 | 2026 | Closed | 135 | 47.5 | 21.2k | 1.1k | ✗ | ✓ | ✓ | ✓ | TXT/L/C/TAB/I | Page | Ans. Ret. | `ref74`<br>[Paper](https://arxiv.org/abs/2602.15257) |
| [MMDA](#benchmarks-050) | PACMMOD’26 | 26.02 | 2026 | Closed | 537 | -- | -- | 1.1k | ✗ | -- | -- | -- | TXT/L/C/TAB/I | -- | Ans. | `ref94`<br>[Paper](https://arxiv.org/abs/2602.23061) |
| [SynthDocBench](#benchmarks-051) | COLM’26 | 26.07 | 2026 | Closed | 200 | 51.1 | -- | 1.8k | ✗ | ✓ | ✓ | ✗ | TXT/C/TAB | Elem. | Ans. Ret.<sup>a</sup> | `ref71`<br>[Paper](https://arxiv.org/abs/2607.10400) |
| [DocVQA-2026](#benchmarks-052) | ICDAR’26<sup>C</sup> | 26.08 | 2026 | Closed | -- | -- | -- | 240 | ✗ | ✓ | ✓ | ✓ | TXT/L/C/TAB/I | -- | Ans. | `ref66`<br>[Google Scholar search](https://scholar.google.com/scholar?q=ICDAR2026%20Competition%20on%20Multimodal%20Reasoning%20over%20Documents%20in%20Multiple%20Domains) |
| [LFDocQA](#benchmarks-053) | arXiv’26 | 26.04 | 2026 | Open | 964 | -- | -- | 1.0k | ✗ | ✗ | ✓ | ✗ | TXT/L/C/TAB | Page, Elem. | Ans. Ret.<sup>a</sup> Loc. | `ref130`<br>[Paper](https://arxiv.org/abs/2605.22829) |
| [DocScope](#benchmarks-054) | NIPS’26<sup>D</sup> | 26.05 | 2026 | Closed | 273 | 51.3 | 24.6k | 1.12k | ✗ | ✓(57.7%) | ✓(35.3%) | ✓(6.9%) | TXT/C/TAB/I/L | Page, Elem. | Ans. Ret. Loc. | `ref113`<br>[Paper](https://arxiv.org/abs/2605.08888) |
| [XL-DocBench](#benchmarks-055) | NIPS’26 | 26.07 | 2026 | Open | 331 | -- | 227.5k | 1.5k | ✓(10.9%) | ✓(72.6%) | ✓ | ✓(14.4%) | TXT/C/TAB/I | Page | Ans. Ret. | `ref58`<br>[Paper](https://arxiv.org/abs/2608.00036) |

<a id="benchmarks-012"></a>

<details>
<summary>DocVQA — Docvqa: A dataset for vqa on document images</summary>

**Paper:** Docvqa: A dataset for vqa on document images  
**Authors:** Mathew, Minesh and Karatzas, Dimosthenis and Jawahar, C. V.  
**Citation:** `mathew2021docvqa`; current BibTeX year **2021**; first release **20.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Docvqa%3A%20A%20dataset%20for%20vqa%20on%20document%20images). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:45`; order 12.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docvqa: A dataset for vqa on document images |
| author | Mathew, Minesh and Karatzas, Dimosthenis and Jawahar, C. V. |
| booktitle | 2021 IEEE Winter Conference on Applications of Computer Vision (WACV) |
| pages | 2199--2208 |
| year | 2021 |
| organization | IEEE |

</details>

<a id="benchmarks-013"></a>

<details>
<summary>InfographicVQA — Infographicvqa</summary>

**Paper:** Infographicvqa  
**Authors:** Mathew, Minesh and Bagal, Viraj and Tito, Rubèn and Karatzas, Dimosthenis and Valveny, Ernest and Jawahar, C. V.  
**Citation:** `ref62`; current BibTeX year **2022**; first release **21.04**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Infographicvqa). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:46`; order 13.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Infographicvqa |
| author | Mathew, Minesh and Bagal, Viraj and Tito, Rubèn and Karatzas, Dimosthenis and Valveny, Ernest and Jawahar, C. V. |
| booktitle | 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) |
| year | 2022 |
| pages | 2582--2591 |
| publisher | IEEE |

</details>

<a id="benchmarks-014"></a>

<details>
<summary>ChartQA — Chartqa: A benchmark for question answering about charts with visual and logical reasoning</summary>

**Paper:** Chartqa: A benchmark for question answering about charts with visual and logical reasoning  
**Authors:** Masry, Ahmed and Jia Qing Tan and Shafiq Joty and Enamul Hoque  
**Citation:** `ref75`; current BibTeX year **2022**; first release **22.03**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Chartqa%3A%20A%20benchmark%20for%20question%20answering%20about%20charts%20with%20visual%20and%20logical%20reasoning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:47`; order 14.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Chartqa: A benchmark for question answering about charts with visual and logical reasoning |
| author | Masry, Ahmed and Jia Qing Tan and Shafiq Joty and Enamul Hoque |
| booktitle | Findings of the association for computational linguistics: ACL 2022 |
| year | 2022 |
| pages | 2263--2279 |
| month | May |

</details>

<a id="benchmarks-015"></a>

<details>
<summary>ArXivQA&#42; — Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models</summary>

**Paper:** Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models  
**Authors:** Li, Lei and Yuqi Wang and Runxin Xu and Peiyi Wang and Xiachong Feng and Lingpeng Kong and Qi Liu  
**Citation:** `ref78`; current BibTeX year **2024**; first release **24.03**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Multimodal%20arxiv%3A%20A%20dataset%20for%20improving%20scientific%20comprehension%20of%20large%20vision-language%20models). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:48`; order 15.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models |
| author | Li, Lei and Yuqi Wang and Runxin Xu and Peiyi Wang and Xiachong Feng and Lingpeng Kong and Qi Liu |
| booktitle | Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 14369--14387 |
| year | 2024 |

</details>

<a id="benchmarks-016"></a>

<details>
<summary>DOGR-Bench — Dogr: Towards versatile visual document grounding and referring</summary>

**Paper:** Dogr: Towards versatile visual document grounding and referring  
**Authors:** Zhou, Yinan and Chen, Yuxin and Lin, Haokun and Wu, Yichen and Yang, Shuyu and Qi, Zhongang and Ma, Chen and Zhu, Li  
**Citation:** `ref15`; current BibTeX year **2025**; first release **24.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Dogr%3A%20Towards%20versatile%20visual%20document%20grounding%20and%20referring). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:49`; order 16.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Dogr: Towards versatile visual document grounding and referring |
| author | Zhou, Yinan and Chen, Yuxin and Lin, Haokun and Wu, Yichen and Yang, Shuyu and Qi, Zhongang and Ma, Chen and Zhu, Li |
| booktitle | 2025 IEEE/CVF International Conference on Computer Vision (ICCV) |
| year | 2025 |
| pages | 3596--3606 |
| organization | IEEE |

</details>

<a id="benchmarks-017"></a>

<details>
<summary>GroundingDocQA-Bench — M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA</summary>

**Paper:** M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA  
**Authors:** Venna, Venkata Kesav and Sai Madhusudan Gunda and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla  
**Citation:** `ref119`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M3Grounder%3A%20Mask-Based%20Multi-Span%20and%20Multi-Granular%20Grounding%20for%20Document%20QA). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:50`; order 17.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA |
| author | Venna, Venkata Kesav and Sai Madhusudan Gunda and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| pages | 23685--23695 |
| year | 2026 |

</details>

<a id="benchmarks-018"></a>

<details>
<summary>DoCoG-Bench — DoCoG: Mask-Based Multi-type Grounded Chain-of-Thought for Document QA</summary>

**Paper:** DoCoG: Mask-Based Multi-type Grounded Chain-of-Thought for Document QA  
**Authors:** Gunda, Sai Madhusudan and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Aryan Jain and Venkata Kesav Venna and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla  
**Citation:** `ref120`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=DoCoG%3A%20Mask-Based%20Multi-type%20Grounded%20Chain-of-Thought%20for%20Document%20QA). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:51`; order 18.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DoCoG: Mask-Based Multi-type Grounded Chain-of-Thought for Document QA |
| author | Gunda, Sai Madhusudan and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Aryan Jain and Venkata Kesav Venna and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla |
| booktitle | European Conference on Computer Vision |
| pages | 308--327 |
| publisher | Springer Nature Switzerland |
| address | Cham |
| year | 2026 |

</details>

<a id="benchmarks-019"></a>

<details>
<summary>TAT-DQA — Towards complex document understanding by discrete reasoning</summary>

**Paper:** Towards complex document understanding by discrete reasoning  
**Authors:** Zhu, Fengbin and Lei, Wenqiang and Feng, Fuli and Wang, Chao and Zhang, Haozhou and Chua, Tat-Seng  
**Citation:** `ref86`; current BibTeX year **2022**; first release **22.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Towards%20complex%20document%20understanding%20by%20discrete%20reasoning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:52`; order 19.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Towards complex document understanding by discrete reasoning |
| author | Zhu, Fengbin and Lei, Wenqiang and Feng, Fuli and Wang, Chao and Zhang, Haozhou and Chua, Tat-Seng |
| booktitle | Proceedings of the 30th ACM International Conference on Multimedia |
| year | 2022 |
| pages | 4857--4866 |

</details>

<a id="benchmarks-020"></a>

<details>
<summary>SlideVQA — Slidevqa: A dataset for document visual question answering on multiple images</summary>

**Paper:** Slidevqa: A dataset for document visual question answering on multiple images  
**Authors:** Tanaka, Ryota and Nishida, Kyosuke and Nishida, Kosuke and Hasegawa, Taku and Saito, Itsumi and Saito, Kuniko  
**Citation:** `tanaka2023slidevqa`; current BibTeX year **2023**; first release **23.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Slidevqa%3A%20A%20dataset%20for%20document%20visual%20question%20answering%20on%20multiple%20images). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:53`; order 20.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Slidevqa: A dataset for document visual question answering on multiple images |
| author | Tanaka, Ryota and Nishida, Kyosuke and Nishida, Kosuke and Hasegawa, Taku and Saito, Itsumi and Saito, Kuniko |
| journal | Proceedings of the AAAI Conference on Artificial Intelligence |
| volume | 37 |
| number | 11 |
| pages | 13636--13645 |
| year | 2023 |

</details>

<a id="benchmarks-021"></a>

<details>
<summary>MP-DocVQA — Hierarchical multimodal transformers for multipage docvqa</summary>

**Paper:** Hierarchical multimodal transformers for multipage docvqa  
**Authors:** Tito, Rubèn and Karatzas, Dimosthenis and Valveny, Ernest  
**Citation:** `tito2023hierarchical`; current BibTeX year **2023**; first release **22.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Hierarchical%20multimodal%20transformers%20for%20multipage%20docvqa). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:54`; order 21.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Hierarchical multimodal transformers for multipage docvqa |
| author | Tito, Rubèn and Karatzas, Dimosthenis and Valveny, Ernest |
| journal | Pattern Recognition |
| volume | 144 |
| pages | 109834 |
| year | 2023 |

</details>

<a id="benchmarks-022"></a>

<details>
<summary>DUDE — Document understanding dataset and evaluation (dude)</summary>

**Paper:** Document understanding dataset and evaluation (dude)  
**Authors:** Van Landeghem, Jordy and Tito, Rubèn and Borchmann, Łukasz and Pietruszka, Michał and Joziak, Pawel and Powalski, Rafal and Jurkiewicz, Dawid and Coustaty, Mickael and Anckaert, Bertrand and Valveny, Ernest and Blaschko, Matthew and Moens, Sien and Stanislawek, Tomasz  
**Citation:** `ref3`; current BibTeX year **2023**; first release **23.05**.  
**Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Van_Landeghem_Document_Understanding_Dataset_and_Evaluation_DUDE_ICCV_2023_paper.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:55`; order 22.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Document understanding dataset and evaluation (dude) |
| author | Van Landeghem, Jordy and Tito, Rubèn and Borchmann, Łukasz and Pietruszka, Michał and Joziak, Pawel and Powalski, Rafal and Jurkiewicz, Dawid and Coustaty, Mickael and Anckaert, Bertrand and Valveny, Ernest and Blaschko, Matthew and Moens, Sien and Stanislawek, Tomasz |
| booktitle | Proceedings of the IEEE/CVF international conference on computer vision |
| year | 2023 |
| pages | 19528--19540 |

</details>

<a id="benchmarks-023"></a>

<details>
<summary>UDA — Uda: A benchmark suite for retrieval augmented generation in real-world document analysis</summary>

**Paper:** Uda: A benchmark suite for retrieval augmented generation in real-world document analysis  
**Authors:** Hui, Yulong and Yao Lu and Huanchen Zhang  
**Citation:** `ref100`; current BibTeX year **2024**; first release **24.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Uda%3A%20A%20benchmark%20suite%20for%20retrieval%20augmented%20generation%20in%20real-world%20document%20analysis). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:56`; order 23.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Uda: A benchmark suite for retrieval augmented generation in real-world document analysis |
| author | Hui, Yulong and Yao Lu and Huanchen Zhang |
| journal | Advances in Neural Information Processing Systems |
| volume | 37 |
| pages | 67200--67217 |
| year | 2024 |

</details>

<a id="benchmarks-024"></a>

<details>
<summary>MMLongBench-Doc — Mmlongbench-doc: Benchmarking long-context document understanding with visualizations</summary>

**Paper:** Mmlongbench-doc: Benchmarking long-context document understanding with visualizations  
**Authors:** Ma, Yubo and Zang, Yuhang and Chen, Liangyu and Chen, Meiqi and Jiao, Yizhu and Li, Xinze and Lu, Xinyuan and Liu, Ziyu and Ma, Yan and Dong, Xiaoyi and Zhang, Pan and Pan, Liangming and Jiang, Yu-Gang and Wang, Jiaqi and Cao, Yixin and Sun, Aixin  
**Citation:** `ma2024mmlongbench`; current BibTeX year **2024**; first release **24.07**.  
**Source:** [Paper](https://papers.nips.cc/paper_files/paper/2024/hash/ae0e43289bffea0c1fa34633fc608e92-Abstract-Datasets_and_Benchmarks_Track.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:57`; order 24.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Mmlongbench-doc: Benchmarking long-context document understanding with visualizations |
| author | Ma, Yubo and Zang, Yuhang and Chen, Liangyu and Chen, Meiqi and Jiao, Yizhu and Li, Xinze and Lu, Xinyuan and Liu, Ziyu and Ma, Yan and Dong, Xiaoyi and Zhang, Pan and Pan, Liangming and Jiang, Yu-Gang and Wang, Jiaqi and Cao, Yixin and Sun, Aixin |
| journal | Advances in Neural Information Processing Systems |
| volume | 37 |
| pages | 95963--96010 |
| year | 2024 |

</details>

<a id="benchmarks-025"></a>

<details>
<summary>SPIQA&#42; — Spiqa: A dataset for multimodal question answering on scientific papers</summary>

**Paper:** Spiqa: A dataset for multimodal question answering on scientific papers  
**Authors:** Pramanick, Shraman and Rama Chellappa and Subhashini Venugopalan  
**Citation:** `ref5`; current BibTeX year **2024**; first release **24.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Spiqa%3A%20A%20dataset%20for%20multimodal%20question%20answering%20on%20scientific%20papers). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:58`; order 25.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Spiqa: A dataset for multimodal question answering on scientific papers |
| author | Pramanick, Shraman and Rama Chellappa and Subhashini Venugopalan |
| journal | Advances in Neural Information Processing Systems |
| volume | 37 |
| pages | 118807--118833 |
| year | 2024 |

</details>

<a id="benchmarks-026"></a>

<details>
<summary>VisRAG — Visrag: Vision-based retrieval-augmented generation on multi-modality documents</summary>

**Paper:** Visrag: Vision-based retrieval-augmented generation on multi-modality documents  
**Authors:** Yu, Shi and Tang, Chaoyue and Xu, Bokai and Cui, Junbo and Ran, Junhao and Yan, Yukun and Liu, Zhenghao and Wang, Shuo and Han, Xu and Liu, Zhiyuan and Sun, Maosong  
**Citation:** `yu2025visrag`; current BibTeX year **2025**; first release **24.10**.  
**Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3640a1997a4c9571cea9db2c82e1fc35-Abstract-Conference.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:59`; order 26.

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

<a id="benchmarks-027"></a>

<details>
<summary>VisR-Bench — SV-RAG: LoRA-contextualizing adaptation of MLLMs for long document understanding</summary>

**Paper:** SV-RAG: LoRA-contextualizing adaptation of MLLMs for long document understanding  
**Authors:** Chen, Jian and Zhang, Ruiyi and Zhou, Yufan and Yu, Tong and Dernoncourt, Franck and Gu, Jiuxiang and Rossi, Ryan A. and Chen, Changyou and Sun, Tong  
**Citation:** `chen2024svrag`; current BibTeX year **2024**; first release **24.11**.  
**Source:** [Paper](https://arxiv.org/abs/2411.01106). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:60`; order 27.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SV-RAG: LoRA-contextualizing adaptation of MLLMs for long document understanding |
| author | Chen, Jian and Zhang, Ruiyi and Zhou, Yufan and Yu, Tong and Dernoncourt, Franck and Gu, Jiuxiang and Rossi, Ryan A. and Chen, Changyou and Sun, Tong |
| journal | arXiv preprint arXiv:2411.01106 |
| year | 2024 |

</details>

<a id="benchmarks-028"></a>

<details>
<summary>PaperPDF — Wukong: A large multimodal model for efficient long pdf reading with end-to-end sparse sampling</summary>

**Paper:** Wukong: A large multimodal model for efficient long pdf reading with end-to-end sparse sampling  
**Authors:** Xie, Xudong and Hao Yan and Liang Yin and Yang Liu and Jing Ding and Minghui Liao and Yuliang Liu and Wei Chen and Xiang Bai  
**Citation:** `ref142`; current BibTeX year **2026**; first release **24.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Wukong%3A%20A%20large%20multimodal%20model%20for%20efficient%20long%20pdf%20reading%20with%20end-to-end%20sparse%20sampling). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:61`; order 28.

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

<a id="benchmarks-029"></a>

<details>
<summary>VisDoMBench — Visdom: Multi-document qa with visually rich elements using multimodal retrieval-augmented generation</summary>

**Paper:** Visdom: Multi-document qa with visually rich elements using multimodal retrieval-augmented generation  
**Authors:** Suri, Manan and Mathur, Puneet and Dernoncourt, Franck and Goswami, Kanika and Rossi, Ryan A. and Manocha, Dinesh  
**Citation:** `ref10`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Visdom%3A%20Multi-document%20qa%20with%20visually%20rich%20elements%20using%20multimodal%20retrieval-augmented%20generation). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:62`; order 29.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visdom: Multi-document qa with visually rich elements using multimodal retrieval-augmented generation |
| author | Suri, Manan and Mathur, Puneet and Dernoncourt, Franck and Goswami, Kanika and Rossi, Ryan A. and Manocha, Dinesh |
| booktitle | Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) |
| year | 2025 |
| pages | 6088--6109 |

</details>

<a id="benchmarks-030"></a>

<details>
<summary>OpenDocVQA — Vdocrag: Retrieval-augmented generation over visually-rich documents</summary>

**Paper:** Vdocrag: Retrieval-augmented generation over visually-rich documents  
**Authors:** Tanaka, Ryota and Iki, Taichi and Hasegawa, Taku and Nishida, Kyosuke and Saito, Kuniko and Suzuki, Jun  
**Citation:** `ref11`; current BibTeX year **2025**; first release **25.04**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Vdocrag%3A%20Retrieval-augmented%20generation%20over%20visually-rich%20documents). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:63`; order 30.

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

<a id="benchmarks-031"></a>

<details>
<summary>DocBench — Docbench: A benchmark for evaluating llm-based document reading systems</summary>

**Paper:** Docbench: A benchmark for evaluating llm-based document reading systems  
**Authors:** Zou, Anni and Wenhao Yu and Hongming Zhang and Kaixin Ma and Deng Cai and Zhuosheng Zhang and Hai Zhao and Dong Yu  
**Citation:** `ref12`; current BibTeX year **2025**; first release **24.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Docbench%3A%20A%20benchmark%20for%20evaluating%20llm-based%20document%20reading%20systems). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:64`; order 31.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docbench: A benchmark for evaluating llm-based document reading systems |
| author | Zou, Anni and Wenhao Yu and Hongming Zhang and Kaixin Ma and Deng Cai and Zhuosheng Zhang and Hai Zhao and Dong Yu |
| booktitle | Proceedings of the 4th international workshop on knowledge-augmented methods for natural language processing |
| pages | 359--373 |
| year | 2025 |

</details>

<a id="benchmarks-032"></a>

<details>
<summary>Wiki-VISA; Paper-VISA — Visa: Retrieval augmented generation with visual source attribution</summary>

**Paper:** Visa: Retrieval augmented generation with visual source attribution  
**Authors:** Ma, Xueguang and Zhuang, Shengyao and Koopman, Bevan and Zuccon, Guido and Chen, Wenhu and Lin, Jimmy  
**Citation:** `ref13`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Visa%3A%20Retrieval%20augmented%20generation%20with%20visual%20source%20attribution). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:65`; order 32.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Visa: Retrieval augmented generation with visual source attribution |
| author | Ma, Xueguang and Zhuang, Shengyao and Koopman, Bevan and Zuccon, Guido and Chen, Wenhu and Lin, Jimmy |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2025 |
| pages | 30154--30169 |

</details>

<a id="benchmarks-033"></a>

<details>
<summary>LongDocURL — Longdocurl: a comprehensive multimodal long document benchmark integrating understanding, reasoning, and locating</summary>

**Paper:** Longdocurl: a comprehensive multimodal long document benchmark integrating understanding, reasoning, and locating  
**Authors:** Deng, Chao and Yuan, Jiale and Bu, Pi and Wang, Peijie and Li, Zhong-Zhi and Xu, Jian and Li, Xiao-Hui and Gao, Yuan and Song, Jun and Zheng, Bo and Liu, Cheng-Lin  
**Citation:** `ref14`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Paper](https://aclanthology.org/2025.acl-long.57/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:66`; order 33.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Longdocurl: a comprehensive multimodal long document benchmark integrating understanding, reasoning, and locating |
| author | Deng, Chao and Yuan, Jiale and Bu, Pi and Wang, Peijie and Li, Zhong-Zhi and Xu, Jian and Li, Xiao-Hui and Gao, Yuan and Song, Jun and Zheng, Bo and Liu, Cheng-Lin |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 1135--1159 |
| year | 2025 |

</details>

<a id="benchmarks-034"></a>

<details>
<summary>AIRQA-REAL — Neusym-rag: Hybrid neural symbolic retrieval with multiview structuring for pdf question answering</summary>

**Paper:** Neusym-rag: Hybrid neural symbolic retrieval with multiview structuring for pdf question answering  
**Authors:** Cao, Ruisheng and Zhang, Hanchong and Huang, Tiancheng and Kang, Zhangyi and Zhang, Yuxin and Sun, Liangtai and Li, Hanqi and Miao, Yuxun and Fan, Shuai and Chen, Lu and Yu, Kai  
**Citation:** `ref156`; current BibTeX year **2025**; first release **25.05**.  
**Source:** [Paper](https://aclanthology.org/2025.acl-long.311/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:67`; order 34.

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

<a id="benchmarks-035"></a>

<details>
<summary>MMDocRAG&#42; — Benchmarking retrieval-augmented multimomal generation for document question answering</summary>

**Paper:** Benchmarking retrieval-augmented multimomal generation for document question answering  
**Authors:** Dong, Kuicai and Chang, Yujing and Huang, Shijie and Wang, Yasheng and Tang, Ruiming and Liu, Yong  
**Citation:** `ref105`; current BibTeX year **2026**; first release **25.05**.  
**Source:** [Paper](https://openreview.net/pdf?id=W4b3v9jx1p). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:68`; order 35.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Benchmarking retrieval-augmented multimomal generation for document question answering |
| author | Dong, Kuicai and Chang, Yujing and Huang, Shijie and Wang, Yasheng and Tang, Ruiming and Liu, Yong |
| journal | Advances in Neural Information Processing Systems |
| volume | 38 |
| year | 2026 |

</details>

<a id="benchmarks-036"></a>

<details>
<summary>M-LongDoc — M-longdoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework</summary>

**Paper:** M-longdoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework  
**Authors:** Chia, Yew Ken and Cheng, Liying and Chan, Hou Pong and Song, Maojia and Liu, Chaoqun and Aljunied, Mahani and Poria, Soujanya and Bing, Lidong  
**Citation:** `ref16`; current BibTeX year **2025**; first release **24.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M-longdoc%3A%20A%20benchmark%20for%20multimodal%20super-long%20document%20understanding%20and%20a%20retrieval-aware%20tuning%20framework). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:69`; order 36.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | M-longdoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework |
| author | Chia, Yew Ken and Cheng, Liying and Chan, Hou Pong and Song, Maojia and Liu, Chaoqun and Aljunied, Mahani and Poria, Soujanya and Bing, Lidong |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 9244--9261 |

</details>

<a id="benchmarks-037"></a>

<details>
<summary>ViDoSeek — Vidorag: Visual document retrieval-augmented generation via dynamic iterative reasoning agents</summary>

**Paper:** Vidorag: Visual document retrieval-augmented generation via dynamic iterative reasoning agents  
**Authors:** Wang, Qiuchen and Ding, Ruixue and Chen, Zehui and Wu, Weiqi and Wang, Shihang and Xie, Pengjun and Zhao, Feng  
**Citation:** `ref18`; current BibTeX year **2025**; first release **25.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Vidorag%3A%20Visual%20document%20retrieval-augmented%20generation%20via%20dynamic%20iterative%20reasoning%20agents). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:70`; order 37.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Vidorag: Visual document retrieval-augmented generation via dynamic iterative reasoning agents |
| author | Wang, Qiuchen and Ding, Ruixue and Chen, Zehui and Wu, Weiqi and Wang, Shihang and Xie, Pengjun and Zhao, Feng |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| year | 2025 |
| pages | 9124--9145 |

</details>

<a id="benchmarks-038"></a>

<details>
<summary>FinRAGBench-V — Finragbench-v: A benchmark for multimodal rag with visual citation in the financial domain</summary>

**Paper:** Finragbench-v: A benchmark for multimodal rag with visual citation in the financial domain  
**Authors:** Zhao, Suifeng and Zhuoran Jin and Sujian Li and Jun Gao  
**Citation:** `ref109`; current BibTeX year **2025**; first release **25.05**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Finragbench-v%3A%20A%20benchmark%20for%20multimodal%20rag%20with%20visual%20citation%20in%20the%20financial%20domain). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:71`; order 38.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Finragbench-v: A benchmark for multimodal rag with visual citation in the financial domain |
| author | Zhao, Suifeng and Zhuoran Jin and Sujian Li and Jun Gao |
| booktitle | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing |
| pages | 4215--4249 |
| year | 2025 |

</details>

<a id="benchmarks-039"></a>

<details>
<summary>M3DocVQA — M3docvqa: Multi-modal multi-page multi-document understanding</summary>

**Paper:** M3docvqa: Multi-modal multi-page multi-document understanding  
**Authors:** Cho, Jaemin and Mahata, Debanjan and Irsoy, Ozan and He, Yujie and Bansal, Mohit  
**Citation:** `cho2025m3docvqa`; current BibTeX year **2025**; first release **24.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M3docvqa%3A%20Multi-modal%20multi-page%20multi-document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:72`; order 39.

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

<a id="benchmarks-040"></a>

<details>
<summary>Double-Bench — Are we on the right way to assess document retrieval-augmented generation?</summary>

**Paper:** Are we on the right way to assess document retrieval-augmented generation?  
**Authors:** Shen, Wenxuan and Mingjia Wang and Yaochen Wang and Dongping Chen and Junjie Yang and Yao Wan and Weiwei Lin  
**Citation:** `ref133`; current BibTeX year **2026**; first release **25.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Are%20we%20on%20the%20right%20way%20to%20assess%20document%20retrieval-augmented%20generation%3F). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:73`; order 40.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Are we on the right way to assess document retrieval-augmented generation? |
| author | Shen, Wenxuan and Mingjia Wang and Yaochen Wang and Dongping Chen and Junjie Yang and Yao Wan and Weiwei Lin |
| journal | Proceedings of the AAAI Conference on Artificial Intelligence |
| volume | 40 |
| number | 39 |
| pages | 32929--32937 |
| year | 2026 |

</details>

<a id="benchmarks-041"></a>

<details>
<summary>AirQA — AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation</summary>

**Paper:** AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation  
**Authors:** Huang, Tiancheng and Cao, Ruisheng and Zhang, Yuxin and Kang, Zhangyi and Wang, Zijian and Wang, Chenrun and Luo, Yijie and Zheng, Hang and Qian, Lirong and Chen, Lu and Yu, Kai  
**Citation:** `ref157`; current BibTeX year **2026**; first release **25.09**.  
**Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/10d35352a92bb40943bb4ed096a407b6-Abstract-Conference.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:74`; order 41.

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

<a id="benchmarks-042"></a>

<details>
<summary>M4DocBench — Doc-researcher: A unified system for multimodal document parsing and deep research</summary>

**Paper:** Doc-researcher: A unified system for multimodal document parsing and deep research  
**Authors:** Dong, Kuicai and Huang, Shurui and Ye, Fangda and Han, Wei and Zhang, Zhi and Li, Dexun and Li, Wenjun and Yang, Qu and Wang, Gang and Wang, Yichao and Zhang, Chen and Liu, Yong  
**Citation:** `dong2026docresearcher`; current BibTeX year **2026**; first release **25.10**.  
**Source:** [Paper](https://doi.org/10.1145/3774904.3792599). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:75`; order 42.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doc-researcher: A unified system for multimodal document parsing and deep research |
| author | Dong, Kuicai and Huang, Shurui and Ye, Fangda and Han, Wei and Zhang, Zhi and Li, Dexun and Li, Wenjun and Yang, Qu and Wang, Gang and Wang, Yichao and Zhang, Chen and Liu, Yong |
| booktitle | Proceedings of the ACM Web Conference 2026 |
| pages | 2349--2360 |
| year | 2026 |

</details>

<a id="benchmarks-043"></a>

<details>
<summary>DVisRAG — RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations</summary>

**Paper:** RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations  
**Authors:** Chen, I. and Liu, Yu-Wei and Wu, Tse-Yu and Chiang, Yu-Chien and Yang, Jen-Chieh and Chen, Wei-Ting  
**Citation:** `ref89`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=RobustVisRAG%3A%20Causality-Aware%20Vision-Based%20Retrieval-Augmented%20Generation%20under%20Visual%20Degradations). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:76`; order 43.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations |
| author | Chen, I. and Liu, Yu-Wei and Wu, Tse-Yu and Chiang, Yu-Chien and Yang, Jen-Chieh and Chen, Wei-Ting |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| year | 2026 |
| pages | 40802--40811 |

</details>

<a id="benchmarks-044"></a>

<details>
<summary>VinQA — VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA</summary>

**Paper:** VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA  
**Authors:** Jang, Young Rok and Hyesoo Kong and Kyunghwan An and Jae Sub Huh and Gyeonghun Kim and Stanley Jungkyu Choi  
**Citation:** `ref98`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.16092). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:77`; order 44.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA |
| author | Jang, Young Rok and Hyesoo Kong and Kyunghwan An and Jae Sub Huh and Gyeonghun Kim and Stanley Jungkyu Choi |
| journal | arXiv preprint arXiv:2606.16092 |
| year | 2026 |

</details>

<a id="benchmarks-045"></a>

<details>
<summary>ViDoRe V3 — Vidore v3: A comprehensive evaluation of retrieval augmented generation in complex real-world scenarios</summary>

**Paper:** Vidore v3: A comprehensive evaluation of retrieval augmented generation in complex real-world scenarios  
**Authors:** Loison, António and Macé, Quentin and Edy, Antoine and Xing, Victor and Balough, Tom and Moreira, Gabriel de Souza P. and Liu, Bo and Faysse, Manuel and Hudelot, Céline and Viaud, Gautier  
**Citation:** `ref83`; current BibTeX year **2026**; first release **26.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Vidore%20v3%3A%20A%20comprehensive%20evaluation%20of%20retrieval%20augmented%20generation%20in%20complex%20real-world%20scenarios). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:78`; order 45.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Vidore v3: A comprehensive evaluation of retrieval augmented generation in complex real-world scenarios |
| author | Loison, António and Macé, Quentin and Edy, Antoine and Xing, Victor and Balough, Tom and Moreira, Gabriel de Souza P. and Liu, Bo and Faysse, Manuel and Hudelot, Céline and Viaud, Gautier |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2026 |
| pages | 16570--16600 |

</details>

<a id="benchmarks-046"></a>

<details>
<summary>PaperScope&#42; — PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers</summary>

**Paper:** PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers  
**Authors:** Xiong, Lei and Huaying Yuan and Zheng Liu and Zhao Cao and Zhicheng Dou  
**Citation:** `ref136`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=PaperScope%3A%20A%20Multi-Modal%20Multi-Document%20Benchmark%20for%20Agentic%20Deep%20Research%20Across%20Massive%20Scientific%20Papers). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:79`; order 46.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers |
| author | Xiong, Lei and Huaying Yuan and Zheng Liu and Zhao Cao and Zhicheng Dou |
| booktitle | Findings of the Association for Computational Linguistics: ACL 2026 |
| pages | 8015--8040 |
| year | 2026 |

</details>

<a id="benchmarks-047"></a>

<details>
<summary>M5BookVQA — TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding</summary>

**Paper:** TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding  
**Authors:** He, Liqi and Zuchao Li and Hao Huang and Ping Wang  
**Citation:** `ref57`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=TRACE%3A%20Traversal%20Retrieval-Augmented%20Chain%20of%20Evidence%20for%20Document%20Understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:80`; order 47.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding |
| author | He, Liqi and Zuchao Li and Hao Huang and Ping Wang |
| booktitle | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| pages | 9806--9825 |
| year | 2026 |

</details>

<a id="benchmarks-048"></a>

<details>
<summary>Wiki-CoE — Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation</summary>

**Paper:** Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation  
**Authors:** Liu, Peiyang and Ziqiang Cui and Xi Wang and Di Liang and Wei Ye  
**Citation:** `ref111`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.01284). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:81`; order 48.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation |
| author | Liu, Peiyang and Ziqiang Cui and Xi Wang and Di Liang and Wei Ye |
| journal | arXiv preprint arXiv:2605.01284 |
| year | 2026 |

</details>

<a id="benchmarks-049"></a>

<details>
<summary>MMLBD-C — How to Train Your Long-Context Visual Document Model</summary>

**Paper:** How to Train Your Long-Context Visual Document Model  
**Authors:** Veselka, Austin  
**Citation:** `ref74`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.15257). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:82`; order 49.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | How to Train Your Long-Context Visual Document Model |
| author | Veselka, Austin |
| journal | arXiv preprint arXiv:2602.15257 |
| year | 2026 |

</details>

<a id="benchmarks-050"></a>

<details>
<summary>MMDA — MoDora: Tree-Based Semi-Structured Document Analysis System</summary>

**Paper:** MoDora: Tree-Based Semi-Structured Document Analysis System  
**Authors:** Xu, Bangrui and Yao, Qihang and Tang, Zirui and Zhou, Xuanhe and He, Yeye and Yu, Shihan and Xu, Qianqian and Wang, Bin and Li, Guoliang and He, Conghui and others  
**Citation:** `ref94`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.23061). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:83`; order 50.

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

<a id="benchmarks-051"></a>

<details>
<summary>SynthDocBench — SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding</summary>

**Paper:** SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding  
**Authors:** Verma, Abhigya and Khyati Mahajan and Amit Kumar Saha and Shruthan Radhakrishna and Sagar Davasam and Vikas Yadav and Sai Rajeswar Mudumba  
**Citation:** `ref71`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2607.10400). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:84`; order 51.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding |
| author | Verma, Abhigya and Khyati Mahajan and Amit Kumar Saha and Shruthan Radhakrishna and Sagar Davasam and Vikas Yadav and Sai Rajeswar Mudumba |
| journal | arXiv preprint arXiv:2607.10400 |
| year | 2026 |

</details>

<a id="benchmarks-052"></a>

<details>
<summary>DocVQA-2026 — ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains</summary>

**Paper:** ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains  
**Authors:** Llabrés, Artemis and Marc Serra Ortega and Tomàs Ockier and Samuel Ortega Cuadra and Amritpal Singh and Christos Georgakilas and Andrey Barsky and Ernest Valveny and Dimosthenis Karatzas  
**Citation:** `ref66`; current BibTeX year **2026**; first release **26.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=ICDAR2026%20Competition%20on%20Multimodal%20Reasoning%20over%20Documents%20in%20Multiple%20Domains). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table4_full.tex:85`; order 52.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains |
| author | Llabrés, Artemis and Marc Serra Ortega and Tomàs Ockier and Samuel Ortega Cuadra and Amritpal Singh and Christos Georgakilas and Andrey Barsky and Ernest Valveny and Dimosthenis Karatzas |
| booktitle | International Conference on Document Analysis and Recognition |
| pages | 336--352 |
| publisher | Springer Nature Switzerland |
| address | Cham |
| year | 2026 |

</details>

<a id="benchmarks-053"></a>

<details>
<summary>LFDocQA — LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding</summary>

**Paper:** LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding  
**Authors:** Zhu, Yifan and Yu Mi and Yue Lu and Yanchu Guan and Zhixuan Chu  
**Citation:** `ref130`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://arxiv.org/abs/2605.22829). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:86`; order 53.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding |
| author | Zhu, Yifan and Yu Mi and Yue Lu and Yanchu Guan and Zhixuan Chu |
| journal | arXiv preprint arXiv:2605.22829 |
| year | 2026 |

</details>

<a id="benchmarks-054"></a>

<details>
<summary>DocScope — DocScope: Benchmarking Verifiable Reasoning for Trustworthy Long-Document Understanding</summary>

**Paper:** DocScope: Benchmarking Verifiable Reasoning for Trustworthy Long-Document Understanding  
**Authors:** Feng, Xiang and Zhou, Jiawei and Huang, Zhangfeng and Wang, Kewei and Ye, Shanshan and Hu, Jinxin and Chen, Zulong and Luo, Yong and Zhang, Jing  
**Citation:** `ref113`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.08888). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table4_full.tex:87`; order 54.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocScope: Benchmarking Verifiable Reasoning for Trustworthy Long-Document Understanding |
| author | Feng, Xiang and Zhou, Jiawei and Huang, Zhangfeng and Wang, Kewei and Ye, Shanshan and Hu, Jinxin and Chen, Zulong and Luo, Yong and Zhang, Jing |
| journal | arXiv preprint arXiv:2605.08888 |
| year | 2026 |

</details>

<a id="benchmarks-055"></a>

<details>
<summary>XL-DocBench — XL-DocBench: Benchmarking Evidence-Grounded Extra-Long Document Understanding</summary>

**Paper:** XL-DocBench: Benchmarking Evidence-Grounded Extra-Long Document Understanding  
**Authors:** Wei, Hongchen and Wang, Yuanzhe and Liu, Bei and Yang, Yifan and Dai, Qi and Ma, Ruichun and Qiu, Kai and Li, Yunsheng and Chen, Dongdong and Luo, Chong and Chen, Zhenzhong and Guo, Baining  
**Citation:** `ref58`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2608.00036). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table4_full.tex:88`; order 55.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | XL-DocBench: Benchmarking Evidence-Grounded Extra-Long Document Understanding |
| author | Wei, Hongchen and Wang, Yuanzhe and Liu, Bei and Yang, Yifan and Dai, Qi and Ma, Ruichun and Qiu, Kai and Li, Yunsheng and Chen, Dongdong and Luo, Chong and Chen, Zhenzhong and Guo, Baining |
| journal | arXiv preprint arXiv:2608.00036 |
| year | 2026 |

</details>

<a id="source-notes"></a>

## Full source notes

1. Groups and dates. Benchmarks are grouped by primary evaluation target and input scale. Ordering follows Table 1 (representative explicit-retrieval methods). (YY.MM) denotes the first-release month, preferentially the first arXiv version; an earlier official release, or the official release when no preprint exists, takes precedence.

2. Venue. Superscripts F/W/D/S/I/C denote Findings, Workshop, Datasets and Benchmarks, Short, Industry, and competition reports, respectively.

3. Scale and input. Open and Closed denote a cross-document candidate collection and a given single document; Open/Closed supports both. #Docs counts documents or independent page inputs. #Pages is the average number of input pages per question, using a document-level mean when per-question statistics are unavailable; Open counts the full candidate collection for that question, and an independent image counts as one page. #Tokens is the mean text-token count per input document. #QA counts questions, queries, or localization tasks.

4. Question Type. MD, MP, and SP denote multi-document, multi-page, and single-page evidence requirements, respectively; Unans. denotes questions unanswerable from the given evidence. ✓/✗ indicates inclusion/exclusion; parentheses give proportions. In Source, TXT/L/C/TAB/I denotes text/layout/charts/tables/images. Gran. denotes the verification granularity supported by public evidence annotations. In open-domain settings, page annotations with document identities also support document verification, which is not listed again.

5. Evaluation. Eval. abbreviates Evaluation. Capabilities supported by the benchmark and its public annotations: Ans., answer quality; Ret., evidence retrieval, typically page/whole-image hits, recall, or ranking; Loc., within-page element or region localization, such as IoU-based evaluation; Eff., processing efficiency and cost; Rob., robustness to controlled perturbations. Exceptions (a): ViDoRe supports Ans. only on subsets with public answers. For Ret., SPIQA retrieves figures/tables; DocMMIR, DocViRe, PaperScope, AIRQA-REAL, and AirQA retrieve documents; M3DocVQA measures recall by the documents containing retrieved pages; M4DocBench covers documents, pages, and layout elements; SynthDocBench matches chart/element IDs; UDA measures text-evidence coverage; MMDocRAG includes text/image-segment selection; LFDocQA includes element-ID matching; PaperPDF matches paragraph/figure/table IDs. Loc. for GroundingDocQA-Bench and DoCoG-Bench includes segmentation masks.

6. Pre-extracted inputs (&#42;). ArXivQA uses pre-extracted scientific figures; SPIQA uses pre-extracted figure/table images and text; MMDocRAG generation evaluation uses pre-extracted text/image segments; PaperScope supplies pre-parsed paper text and images. These settings do not directly evaluate the complete parsing process from raw pages.

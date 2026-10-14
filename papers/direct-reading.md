# Methods without explicit retrieval

[Repository home](../README.md) · [Benchmarks](benchmarks.md) · [Direct reading](direct-reading.md) · [Explicit retrieval](explicit-retrieval.md)

**29 records.** Generated from manuscript `tables/table5_full.tex`. Source rows, groups, qualifiers, and notation are preserved.

[JSON](../data/direct-reading.json) · [CSV](../data/direct-reading.csv) · [Bibliography](../references.bib) · [Data dictionary](../data/README.md)

Complete comparison of 29 methods without explicit retrieval, grouped by their primary single-page or multipage setting. Ordering and first-release dates follow Table 1 (representative explicit-retrieval methods). + denotes combinations and / alternatives; -- denotes unconfirmed information.

**Dates and citation years.** First release is separate from the citation year in the current BibTeX. YY.MM preferentially denotes the first arXiv version; an earlier official release, or the official release when no preprint exists, takes precedence. A -- month is unavailable and is stored as null, never as an invented month.

**Order.** Source row order is preserved. Within task groups, methods follow final conference submission deadlines, then first release within each conference; preprints/journal papers are inserted by first release (Table 1 convention).

**Notation.** ✓ = present/included; ✗ = absent/excluded. `--` means unconfirmed. Venue superscripts F/W/D/S/I/C mean Findings, Workshop, Datasets and Benchmarks, Short, Industry, and competition reports, respectively.

**Links.** “Paper” uses an academic URL or explicit arXiv identifier already recorded in the manuscript bibliography/provenance. Links were not independently rechecked for this repository. “Google Scholar search” is a title search, not a verified paper link.

## Browse

- [Single-page VQA (16)](#group-1)
- [Multi-page VQA (13)](#group-2)
- [Full source notes](#source-notes)

<a id="group-1"></a>

## Single-page VQA

| Name | Venue | First release | Bib year | OCR | Deep | Agent | Model | Learning | Eval. | Citation / source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [VisionTaPas](#direct-reading-001) | ACL’22<sup>F</sup> | 22.03 | 2022 | ✓ | ✗ | Single | TAPAS | SFT | Ans. | `ref75`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Chartqa%3A%20A%20benchmark%20for%20question%20answering%20about%20charts%20with%20visual%20and%20logical%20reasoning) |
| [Donut](#direct-reading-002) | ECCV’22 | 21.11 | 2022 | ✗ | ✗ | Single | BART | Pretraining + SFT | Ans. Eff. | `ref67`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Ocr-free%20document%20understanding%20transformer) |
| [LayoutLMv3](#direct-reading-003) | MM’22 | 22.04 | 2022 | ✓ | ✗ | Single | RoBERTa | Pretraining + SFT | Ans. Loc.<sup>a</sup> | `huang2022layoutlmv3`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Layoutlmv3%3A%20Pre-training%20for%20document%20ai%20with%20unified%20text%20and%20image%20masking) |
| [UDOP](#direct-reading-004) | CVPR’23 | 22.12 | 2023 | ✓ | ✗ | Single | T5 | Pretraining + SFT | Ans. | `ref87`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20vision%2C%20text%2C%20and%20layout%20for%20universal%20document%20processing) |
| [Pix2Struct](#direct-reading-005) | ICML’23 | 22.10 | 2023 | ✗ | ✗ | Single | Pix2Struct | Pretraining + SFT | Ans. | `ref76`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Pix2struct%3A%20Screenshot%20parsing%20as%20pretraining%20for%20visual%20language%20understanding) |
| [UReader](#direct-reading-006) | EMNLP’23<sup>F</sup> | 23.10 | 2023 | ✗ | ✗ | Single | Llama | SFT | Ans. Eff. | `ref92`<br>[Paper](https://aclanthology.org/2023.findings-emnlp.187/) |
| [LayoutLLM (Fujitake)](#direct-reading-007) | LREC-COLING’24 | 24.03 | 2024 | ✓ | ✗ | Single | Llama | SFT | Ans. | `ref124`<br>[Google Scholar search](https://scholar.google.com/scholar?q=LayoutLLM%3A%20Large%20language%20model%20instruction%20tuning%20for%20visually%20rich%20document%20understanding) |
| [mPLUG-DocOwl 1.5](#direct-reading-008) | EMNLP’24<sup>F</sup> | 24.03 | 2024 | ✗ | ✗ | Single | Llama | Pretraining + SFT | Ans. Eff. | `ref93`<br>[Google Scholar search](https://scholar.google.com/scholar?q=mplug-docowl%201.5%3A%20Unified%20structure%20learning%20for%20ocr-free%20document%20understanding) |
| [DocLayLLM](#direct-reading-009) | CVPR’25 | 24.08 | 2025 | ✓ | ✗ | Single | Llama | Pretraining + SFT | Ans. Eff. | `ref22`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Doclayllm%3A%20An%20efficient%20multi-modal%20extension%20of%20large%20language%20models%20for%20text-rich%20document%20understanding) |
| [DocVLM&#42;](#direct-reading-010) | CVPR’25 | 24.12 | 2025 | ✓ | ✗ | Single | Qwen-VL / InternVL / LLaVA | SFT | Ans. Eff. | `ref25`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Docvlm%3A%20Make%20your%20vlm%20an%20efficient%20reader) |
| [DOGR](#direct-reading-011) | ICCV’25 | 24.11 | 2025 | ✗ | ✗ | Single | Qwen | Pretraining + SFT | Ans. Loc. | `ref15`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Dogr%3A%20Towards%20versatile%20visual%20document%20grounding%20and%20referring) |
| [M3Grounder](#direct-reading-012) | CVPR’26 | 26.06 | 2026 | ✗ | ✗ | Single | InternVL / Qwen-VL | SFT | Ans. Loc.<sup>a</sup> | `ref119`<br>[Google Scholar search](https://scholar.google.com/scholar?q=M3Grounder%3A%20Mask-Based%20Multi-Span%20and%20Multi-Granular%20Grounding%20for%20Document%20QA) |
| [DocVAL](#direct-reading-013) | ICML’26 | 25.11 | 2025 | ✗ | ✗ | Single | Gemma3 | SFT | Ans. Loc. Eff. | `ref23`<br>[Paper](https://arxiv.org/abs/2511.22521) |
| [Uni-DocRobust](#direct-reading-014) | ICML’26 | 26.-- | 2026 | ✗ | ✗ | Single | LLaVA / Qwen-VL / InternVL | Pretraining | Ans. Eff. Rob. | `ref24`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Uni-DocRobust%3A%20Universal%20Plug-and-Play%20Robustness%20Enhancement%20for%20Multi-modal%20LLMs%20via%20Feature%20Restoration) |
| [DoCoG](#direct-reading-015) | ECCV’26 | 26.09 | 2026 | ✗ | ✗ | Single | Qwen-VL | SFT + RL | Ans. Loc.<sup>a</sup> | `ref120`<br>[Google Scholar search](https://scholar.google.com/scholar?q=DoCoG%3A%20Mask-Based%20Multi-type%20Grounded%20Chain-of-Thought%20for%20Document%20QA) |
| [RegionDoc-R1&#42;](#direct-reading-016) | EMNLP’26 | 26.-- | 2026 | ✗ | ✗ | Single | Qwen-VL | SFT + RL | Ans. | `ref140`<br>[Google Scholar search](https://scholar.google.com/scholar?q=RegionDoc-R1%3A%20Reinforcing%20Semantic%20Layout-Aware%20Learning%20for%20Document%20Understanding) |

<a id="direct-reading-001"></a>

<details>
<summary>VisionTaPas — Chartqa: A benchmark for question answering about charts with visual and logical reasoning</summary>

**Paper:** Chartqa: A benchmark for question answering about charts with visual and logical reasoning  
**Authors:** Masry, Ahmed and Jia Qing Tan and Shafiq Joty and Enamul Hoque  
**Citation:** `ref75`; current BibTeX year **2022**; first release **22.03**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Chartqa%3A%20A%20benchmark%20for%20question%20answering%20about%20charts%20with%20visual%20and%20logical%20reasoning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:36`; order 1.

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

<a id="direct-reading-002"></a>

<details>
<summary>Donut — Ocr-free document understanding transformer</summary>

**Paper:** Ocr-free document understanding transformer  
**Authors:** Kim, Geewook and Hong, Teakgyu and Yim, Moonbin and Nam, JeongYeon and Park, Jinyoung and Yim, Jinyeong and Hwang, Wonseok and Yun, Sangdoo and Han, Dongyoon and Park, Seunghyun  
**Citation:** `ref67`; current BibTeX year **2022**; first release **21.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Ocr-free%20document%20understanding%20transformer). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:37`; order 2.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Ocr-free document understanding transformer |
| author | Kim, Geewook and Hong, Teakgyu and Yim, Moonbin and Nam, JeongYeon and Park, Jinyoung and Yim, Jinyeong and Hwang, Wonseok and Yun, Sangdoo and Han, Dongyoon and Park, Seunghyun |
| booktitle | European Conference on Computer Vision |
| year | 2022 |
| pages | 498--517 |
| publisher | Springer Nature Switzerland |
| address | Cham |

</details>

<a id="direct-reading-003"></a>

<details>
<summary>LayoutLMv3 — Layoutlmv3: Pre-training for document ai with unified text and image masking</summary>

**Paper:** Layoutlmv3: Pre-training for document ai with unified text and image masking  
**Authors:** Huang, Yupan and Lv, Tengchao and Cui, Lei and Lu, Yutong and Wei, Furu  
**Citation:** `huang2022layoutlmv3`; current BibTeX year **2022**; first release **22.04**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Layoutlmv3%3A%20Pre-training%20for%20document%20ai%20with%20unified%20text%20and%20image%20masking). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:38`; order 3.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Layoutlmv3: Pre-training for document ai with unified text and image masking |
| author | Huang, Yupan and Lv, Tengchao and Cui, Lei and Lu, Yutong and Wei, Furu |
| booktitle | Proceedings of the 30th ACM international conference on multimedia |
| pages | 4083--4091 |
| year | 2022 |

</details>

<a id="direct-reading-004"></a>

<details>
<summary>UDOP — Unifying vision, text, and layout for universal document processing</summary>

**Paper:** Unifying vision, text, and layout for universal document processing  
**Authors:** Tang, Zineng and Yang, Ziyi and Wang, Guoxin and Fang, Yuwei and Liu, Yang and Zhu, Chenguang and Zeng, Michael and Zhang, Cha and Bansal, Mohit  
**Citation:** `ref87`; current BibTeX year **2023**; first release **22.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Unifying%20vision%2C%20text%2C%20and%20layout%20for%20universal%20document%20processing). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:39`; order 4.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Unifying vision, text, and layout for universal document processing |
| author | Tang, Zineng and Yang, Ziyi and Wang, Guoxin and Fang, Yuwei and Liu, Yang and Zhu, Chenguang and Zeng, Michael and Zhang, Cha and Bansal, Mohit |
| booktitle | 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| year | 2023 |
| pages | 19254--19264 |
| publisher | IEEE |

</details>

<a id="direct-reading-005"></a>

<details>
<summary>Pix2Struct — Pix2struct: Screenshot parsing as pretraining for visual language understanding</summary>

**Paper:** Pix2struct: Screenshot parsing as pretraining for visual language understanding  
**Authors:** Lee, Kenton and Mandar Joshi and Iulia Raluca Turc and Hexiang Hu and Fangyu Liu and Julian Martin Eisenschlos and Urvashi Khandelwal and Peter Shaw and Ming-Wei Chang and Kristina Toutanova  
**Citation:** `ref76`; current BibTeX year **2023**; first release **22.10**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Pix2struct%3A%20Screenshot%20parsing%20as%20pretraining%20for%20visual%20language%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:40`; order 5.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Pix2struct: Screenshot parsing as pretraining for visual language understanding |
| author | Lee, Kenton and Mandar Joshi and Iulia Raluca Turc and Hexiang Hu and Fangyu Liu and Julian Martin Eisenschlos and Urvashi Khandelwal and Peter Shaw and Ming-Wei Chang and Kristina Toutanova |
| booktitle | International Conference on Machine Learning |
| year | 2023 |
| pages | 18893--18912 |
| month | July |
| organization | PMLR |

</details>

<a id="direct-reading-006"></a>

<details>
<summary>UReader — Ureader: Universal ocr-free visually-situated language understanding with multimodal large language model</summary>

**Paper:** Ureader: Universal ocr-free visually-situated language understanding with multimodal large language model  
**Authors:** Ye, Jiabo and Hu, Anwen and Xu, Haiyang and Ye, Qinghao and Yan, Ming and Xu, Guohai and Li, Chenliang and Tian, Junfeng and Qian, Qi and Zhang, Ji and Jin, Qin and He, Liang and Lin, Xin and Huang, Fei  
**Citation:** `ref92`; current BibTeX year **2023**; first release **23.10**.  
**Source:** [Paper](https://aclanthology.org/2023.findings-emnlp.187/). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table5_full.tex:41`; order 6.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Ureader: Universal ocr-free visually-situated language understanding with multimodal large language model |
| author | Ye, Jiabo and Hu, Anwen and Xu, Haiyang and Ye, Qinghao and Yan, Ming and Xu, Guohai and Li, Chenliang and Tian, Junfeng and Qian, Qi and Zhang, Ji and Jin, Qin and He, Liang and Lin, Xin and Huang, Fei |
| booktitle | Findings of the Association for Computational Linguistics: EMNLP 2023 |
| year | 2023 |
| pages | 2841--2858 |

</details>

<a id="direct-reading-007"></a>

<details>
<summary>LayoutLLM (Fujitake) — LayoutLLM: Large language model instruction tuning for visually rich document understanding</summary>

**Paper:** LayoutLLM: Large language model instruction tuning for visually rich document understanding  
**Authors:** Fujitake, Masato  
**Citation:** `ref124`; current BibTeX year **2024**; first release **24.03**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=LayoutLLM%3A%20Large%20language%20model%20instruction%20tuning%20for%20visually%20rich%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:42`; order 7.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | LayoutLLM: Large language model instruction tuning for visually rich document understanding |
| author | Fujitake, Masato |
| booktitle | Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024) |
| pages | 10219--10224 |
| year | 2024 |

</details>

<a id="direct-reading-008"></a>

<details>
<summary>mPLUG-DocOwl 1.5 — mplug-docowl 1.5: Unified structure learning for ocr-free document understanding</summary>

**Paper:** mplug-docowl 1.5: Unified structure learning for ocr-free document understanding  
**Authors:** Hu, Anwen and Haiyang Xu and Jiabo Ye and Ming Yan and Liang Zhang and Bo Zhang and Ji Zhang and Qin Jin and Fei Huang and Jingren Zhou  
**Citation:** `ref93`; current BibTeX year **2024**; first release **24.03**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=mplug-docowl%201.5%3A%20Unified%20structure%20learning%20for%20ocr-free%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:43`; order 8.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | mplug-docowl 1.5: Unified structure learning for ocr-free document understanding |
| author | Hu, Anwen and Haiyang Xu and Jiabo Ye and Ming Yan and Liang Zhang and Bo Zhang and Ji Zhang and Qin Jin and Fei Huang and Jingren Zhou |
| booktitle | Findings of the Association for Computational Linguistics: EMNLP 2024 |
| pages | 3096--3120 |
| year | 2024 |

</details>

<a id="direct-reading-009"></a>

<details>
<summary>DocLayLLM — Doclayllm: An efficient multi-modal extension of large language models for text-rich document understanding</summary>

**Paper:** Doclayllm: An efficient multi-modal extension of large language models for text-rich document understanding  
**Authors:** Liao, Wenhui and Jiapeng Wang and Hongliang Li and Chengyu Wang and Jun Huang and Lianwen Jin  
**Citation:** `ref22`; current BibTeX year **2025**; first release **24.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Doclayllm%3A%20An%20efficient%20multi-modal%20extension%20of%20large%20language%20models%20for%20text-rich%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:44`; order 9.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Doclayllm: An efficient multi-modal extension of large language models for text-rich document understanding |
| author | Liao, Wenhui and Jiapeng Wang and Hongliang Li and Chengyu Wang and Jun Huang and Lianwen Jin |
| booktitle | 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| pages | 4038--4049 |
| publisher | IEEE |
| year | 2025 |

</details>

<a id="direct-reading-010"></a>

<details>
<summary>DocVLM&#42; — Docvlm: Make your vlm an efficient reader</summary>

**Paper:** Docvlm: Make your vlm an efficient reader  
**Authors:** Nacson, Mor Shpigel and Aberdam, Aviad and Ganz, Roy and Ben Avraham, Elad and Golts, Alona and Kittenplon, Yair and Mazor, Shai and Litman, Ron  
**Citation:** `ref25`; current BibTeX year **2025**; first release **24.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Docvlm%3A%20Make%20your%20vlm%20an%20efficient%20reader). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:45`; order 10.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docvlm: Make your vlm an efficient reader |
| author | Nacson, Mor Shpigel and Aberdam, Aviad and Ganz, Roy and Ben Avraham, Elad and Golts, Alona and Kittenplon, Yair and Mazor, Shai and Litman, Ron |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| year | 2025 |
| pages | 29005--29015 |

</details>

<a id="direct-reading-011"></a>

<details>
<summary>DOGR — Dogr: Towards versatile visual document grounding and referring</summary>

**Paper:** Dogr: Towards versatile visual document grounding and referring  
**Authors:** Zhou, Yinan and Chen, Yuxin and Lin, Haokun and Wu, Yichen and Yang, Shuyu and Qi, Zhongang and Ma, Chen and Zhu, Li  
**Citation:** `ref15`; current BibTeX year **2025**; first release **24.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Dogr%3A%20Towards%20versatile%20visual%20document%20grounding%20and%20referring). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:46`; order 11.

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

<a id="direct-reading-012"></a>

<details>
<summary>M3Grounder — M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA</summary>

**Paper:** M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA  
**Authors:** Venna, Venkata Kesav and Sai Madhusudan Gunda and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla  
**Citation:** `ref119`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=M3Grounder%3A%20Mask-Based%20Multi-Span%20and%20Multi-Granular%20Grounding%20for%20Document%20QA). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:47`; order 12.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA |
| author | Venna, Venkata Kesav and Sai Madhusudan Gunda and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| pages | 23685--23695 |
| year | 2026 |

</details>

<a id="direct-reading-013"></a>

<details>
<summary>DocVAL — DocVAL: Validated Chain-of-Thought Distillation for Grounded Document VQA</summary>

**Paper:** DocVAL: Validated Chain-of-Thought Distillation for Grounded Document VQA  
**Authors:** Neogi, Pinaki Prasad Guha and Ahmad Mohammadshirazi and Ser-Nam Lim and Rajiv Ramnath  
**Citation:** `ref23`; current BibTeX year **2025**; first release **25.11**.  
**Source:** [Paper](https://arxiv.org/abs/2511.22521). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table5_full.tex:48`; order 13.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocVAL: Validated Chain-of-Thought Distillation for Grounded Document VQA |
| author | Neogi, Pinaki Prasad Guha and Ahmad Mohammadshirazi and Ser-Nam Lim and Rajiv Ramnath |
| journal | arXiv preprint arXiv:2511.22521 |
| year | 2025 |

</details>

<a id="direct-reading-014"></a>

<details>
<summary>Uni-DocRobust — Uni-DocRobust: Universal Plug-and-Play Robustness Enhancement for Multi-modal LLMs via Feature Restoration</summary>

**Paper:** Uni-DocRobust: Universal Plug-and-Play Robustness Enhancement for Multi-modal LLMs via Feature Restoration  
**Authors:** Zhou, Yuxuan and Baole Wei and Xingjian Hu and Haowei Chen and Yu Li and Xingyue Lin and Liangcai Gao and Zhi Tang  
**Citation:** `ref24`; current BibTeX year **2026**; first release **26.--**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Uni-DocRobust%3A%20Universal%20Plug-and-Play%20Robustness%20Enhancement%20for%20Multi-modal%20LLMs%20via%20Feature%20Restoration). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:49`; order 14.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Uni-DocRobust: Universal Plug-and-Play Robustness Enhancement for Multi-modal LLMs via Feature Restoration |
| author | Zhou, Yuxuan and Baole Wei and Xingjian Hu and Haowei Chen and Yu Li and Xingyue Lin and Liangcai Gao and Zhi Tang |
| booktitle | Forty-third International Conference on Machine Learning |
| year | 2026 |

</details>

<a id="direct-reading-015"></a>

<details>
<summary>DoCoG — DoCoG: Mask-Based Multi-type Grounded Chain-of-Thought for Document QA</summary>

**Paper:** DoCoG: Mask-Based Multi-type Grounded Chain-of-Thought for Document QA  
**Authors:** Gunda, Sai Madhusudan and Jyothi Swaroopa Jinka and Hrithik Sagar Rachakonda and Aryan Jain and Venkata Kesav Venna and Anirudh Srinivasan and Ravi Kiran Sarvadevabhatla  
**Citation:** `ref120`; current BibTeX year **2026**; first release **26.09**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=DoCoG%3A%20Mask-Based%20Multi-type%20Grounded%20Chain-of-Thought%20for%20Document%20QA). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:50`; order 15.

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

<a id="direct-reading-016"></a>

<details>
<summary>RegionDoc-R1&#42; — RegionDoc-R1: Reinforcing Semantic Layout-Aware Learning for Document Understanding</summary>

**Paper:** RegionDoc-R1: Reinforcing Semantic Layout-Aware Learning for Document Understanding  
**Authors:** Wang, Chao and Hehe Fan and Huichen Yang and Zhengdong Hu and Sarvnaz Karimi and Lina Yao and Yi Yang  
**Citation:** `ref140`; current BibTeX year **2026**; first release **26.--**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=RegionDoc-R1%3A%20Reinforcing%20Semantic%20Layout-Aware%20Learning%20for%20Document%20Understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:51`; order 16.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | RegionDoc-R1: Reinforcing Semantic Layout-Aware Learning for Document Understanding |
| author | Wang, Chao and Hehe Fan and Huichen Yang and Zhengdong Hu and Sarvnaz Karimi and Lina Yao and Yi Yang |
| year | 2026 |

</details>

<a id="group-2"></a>

## Multi-page VQA

| Name | Venue | First release | Bib year | OCR | Deep | Agent | Model | Learning | Eval. | Citation / source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M3D](#direct-reading-017) | AAAI’23 | 23.01 | 2023 | ✓ | ✗ | Single | T5 | SFT | Ans. Ret. | `tanaka2023slidevqa`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Slidevqa%3A%20A%20dataset%20for%20document%20visual%20question%20answering%20on%20multiple%20images) |
| [Hi-VT5](#direct-reading-018) | PR’23 | 22.12 | 2023 | ✓ | ✗ | Single | T5 | Pretraining + SFT | Ans. Ret. | `tito2023hierarchical`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Hierarchical%20multimodal%20transformers%20for%20multipage%20docvqa) |
| [GRAM](#direct-reading-019) | CVPR’24 | 24.01 | 2024 | ✓ | ✗ | Single | T5 | SFT | Ans. Eff. | `ref117`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Gram%3A%20Global%20reasoning%20for%20multi-page%20vqa) |
| [Docopilot](#direct-reading-020) | CVPR’25 | 25.06 | 2025 | ✗ | ✗ | Single | InternVL | SFT | Ans. Eff. | `ref139`<br>[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.html) |
| [mPLUG-DocOwl2](#direct-reading-021) | ACL’25 | 24.09 | 2025 | ✗ | ✗ | Single | Llama | Pretraining + SFT | Ans. Eff. | `ref26`<br>[Google Scholar search](https://scholar.google.com/scholar?q=mplug-docowl2%3A%20High-resolution%20compressing%20for%20ocr-free%20multi-page%20document%20understanding) |
| [DocR1](#direct-reading-022) | AAAI’26 | 25.08 | 2026 | ✗ | ✗ | Single | Qwen-VL | RL | Ans. Ret. | `ref27`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Docr1%3A%20Evidence%20page-guided%20grpo%20for%20multi-page%20document%20understanding) |
| [LAT](#direct-reading-023) | AAAI’26 | 25.11 | 2026 | ✗ | ✗ | Single | Qwen-VL | SFT + RL | Ans. Ret. Loc. Eff. | `ref110`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Look%20as%20you%20think%3A%20Unifying%20reasoning%20and%20visual%20evidence%20attribution%20for%20verifiable%20document%20RAG%20via%20reinforcement%20learning) |
| [DocSLM](#direct-reading-024) | CVPR’26<sup>F</sup> | 25.11 | 2026 | ✓ | ✗ | Single | Qwen | Pretraining + SFT | Ans. Eff. | `ref63`<br>[Google Scholar search](https://scholar.google.com/scholar?q=Docslm%3A%20A%20small%20vision-language%20model%20for%20long%20multimodal%20document%20understanding) |
| [DocSeeker](#direct-reading-025) | CVPR’26 | 26.04 | 2026 | ✗ | ✗ | Single | Qwen-VL | SFT + RL | Ans. Ret. Eff. Rob. | `ref29`<br>[Paper](https://arxiv.org/abs/2604.12812) |
| [VinQA (Page Encoding)](#direct-reading-026) | CVPR’26 | 26.06 | 2026 | ✗ | ✗ | Single | Qwen-VL | SFT | Ans. Ret.<sup>a</sup> Eff. | `ref98`<br>[Paper](https://arxiv.org/abs/2606.16092) |
| [CoE](#direct-reading-027) | SIGIR’26 | 26.05 | 2026 | ✗ | ✗ | Single | Qwen-VL | SFT | Ans. Ret. Loc.<sup>a</sup> Eff. | `ref111`<br>[Paper](https://arxiv.org/abs/2605.01284) |
| [OriOn](#direct-reading-028) | arXiv’26 | 26.02 | 2026 | ✗ | ✗ | Single | Mistral / Qwen-VL | Pretraining + SFT + RL | Ans. Eff. | `ref74`<br>[Paper](https://arxiv.org/abs/2602.15257) |
| [Quote-and-Retrieve](#direct-reading-029) | arXiv’26 | 26.07 | 2026 | ✗ | ✗ | Single | Qwen-VL | RL | Ans. Ret. Loc. Eff. | `ref112`<br>[Paper](https://arxiv.org/abs/2607.24651) |

<a id="direct-reading-017"></a>

<details>
<summary>M3D — Slidevqa: A dataset for document visual question answering on multiple images</summary>

**Paper:** Slidevqa: A dataset for document visual question answering on multiple images  
**Authors:** Tanaka, Ryota and Nishida, Kyosuke and Nishida, Kosuke and Hasegawa, Taku and Saito, Itsumi and Saito, Kuniko  
**Citation:** `tanaka2023slidevqa`; current BibTeX year **2023**; first release **23.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Slidevqa%3A%20A%20dataset%20for%20document%20visual%20question%20answering%20on%20multiple%20images). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:55`; order 17.

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

<a id="direct-reading-018"></a>

<details>
<summary>Hi-VT5 — Hierarchical multimodal transformers for multipage docvqa</summary>

**Paper:** Hierarchical multimodal transformers for multipage docvqa  
**Authors:** Tito, Rubèn and Karatzas, Dimosthenis and Valveny, Ernest  
**Citation:** `tito2023hierarchical`; current BibTeX year **2023**; first release **22.12**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Hierarchical%20multimodal%20transformers%20for%20multipage%20docvqa). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:56`; order 18.

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

<a id="direct-reading-019"></a>

<details>
<summary>GRAM — Gram: Global reasoning for multi-page vqa</summary>

**Paper:** Gram: Global reasoning for multi-page vqa  
**Authors:** Blau, Tsachi and Fogel, Sharon and Ronen, Roi and Golts, Alona and Ganz, Roy and Ben Avraham, Elad and Aberdam, Aviad and Tsiper, Shahar and Litman, Ron  
**Citation:** `ref117`; current BibTeX year **2024**; first release **24.01**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Gram%3A%20Global%20reasoning%20for%20multi-page%20vqa). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:57`; order 19.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Gram: Global reasoning for multi-page vqa |
| author | Blau, Tsachi and Fogel, Sharon and Ronen, Roi and Golts, Alona and Ganz, Roy and Ben Avraham, Elad and Aberdam, Aviad and Tsiper, Shahar and Litman, Ron |
| booktitle | Proceedings of the IEEE/CVF conference on computer vision and pattern recognition |
| year | 2024 |
| pages | 15598--15607 |

</details>

<a id="direct-reading-020"></a>

<details>
<summary>Docopilot — Docopilot: Improving multimodal models for document-level understanding</summary>

**Paper:** Docopilot: Improving multimodal models for document-level understanding  
**Authors:** Duan, Yuchen and Chen, Zhe and Hu, Yusong and Wang, Weiyun and Ye, Shenglong and Shi, Botian and Lu, Lewei and Hou, Qibin and Lu, Tong and Li, Hongsheng and Dai, Jifeng and Wang, Wenhai  
**Citation:** `ref139`; current BibTeX year **2025**; first release **25.06**.  
**Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.html). Recorded in `reference_sources.json:authorSourceUrl`.  
**Manuscript row:** `tables/table5_full.tex:58`; order 20.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docopilot: Improving multimodal models for document-level understanding |
| author | Duan, Yuchen and Chen, Zhe and Hu, Yusong and Wang, Weiyun and Ye, Shenglong and Shi, Botian and Lu, Lewei and Hou, Qibin and Lu, Tong and Li, Hongsheng and Dai, Jifeng and Wang, Wenhai |
| booktitle | 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| pages | 4026--4037 |
| publisher | IEEE |
| year | 2025 |

</details>

<a id="direct-reading-021"></a>

<details>
<summary>mPLUG-DocOwl2 — mplug-docowl2: High-resolution compressing for ocr-free multi-page document understanding</summary>

**Paper:** mplug-docowl2: High-resolution compressing for ocr-free multi-page document understanding  
**Authors:** Hu, Anwen and Xu, Haiyang and Zhang, Liang and Ye, Jiabo and Yan, Ming and Zhang, Ji and Jin, Qin and Huang, Fei and Zhou, Jingren  
**Citation:** `ref26`; current BibTeX year **2025**; first release **24.09**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=mplug-docowl2%3A%20High-resolution%20compressing%20for%20ocr-free%20multi-page%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:59`; order 21.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | mplug-docowl2: High-resolution compressing for ocr-free multi-page document understanding |
| author | Hu, Anwen and Xu, Haiyang and Zhang, Liang and Ye, Jiabo and Yan, Ming and Zhang, Ji and Jin, Qin and Huang, Fei and Zhou, Jingren |
| booktitle | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| year | 2025 |
| pages | 5817--5834 |

</details>

<a id="direct-reading-022"></a>

<details>
<summary>DocR1 — Docr1: Evidence page-guided grpo for multi-page document understanding</summary>

**Paper:** Docr1: Evidence page-guided grpo for multi-page document understanding  
**Authors:** Xiong, Junyu and Wang, Yonghui and Zhao, Weichao and Liu, Chenyu and Yin, Bing and Zhou, Wengang and Li, Houqiang  
**Citation:** `ref27`; current BibTeX year **2026**; first release **25.08**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Docr1%3A%20Evidence%20page-guided%20grpo%20for%20multi-page%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:60`; order 22.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docr1: Evidence page-guided grpo for multi-page document understanding |
| author | Xiong, Junyu and Wang, Yonghui and Zhao, Weichao and Liu, Chenyu and Yin, Bing and Zhou, Wengang and Li, Houqiang |
| journal | Proceedings of the AAAI Conference on Artificial Intelligence |
| year | 2026 |
| volume | 40 |
| number | 13 |
| pages | 11178--11186 |

</details>

<a id="direct-reading-023"></a>

<details>
<summary>LAT — Look as you think: Unifying reasoning and visual evidence attribution for verifiable document RAG via reinforcement learning</summary>

**Paper:** Look as you think: Unifying reasoning and visual evidence attribution for verifiable document RAG via reinforcement learning  
**Authors:** Liu, Shuochen and Pengfei Luo and Chao Zhang and Yuhao Chen and Haotian Zhang and Qi Liu and Xin Kou and Tong Xu and Enhong Chen  
**Citation:** `ref110`; current BibTeX year **2026**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Look%20as%20you%20think%3A%20Unifying%20reasoning%20and%20visual%20evidence%20attribution%20for%20verifiable%20document%20RAG%20via%20reinforcement%20learning). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:61`; order 23.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Look as you think: Unifying reasoning and visual evidence attribution for verifiable document RAG via reinforcement learning |
| author | Liu, Shuochen and Pengfei Luo and Chao Zhang and Yuhao Chen and Haotian Zhang and Qi Liu and Xin Kou and Tong Xu and Enhong Chen |
| journal | Proceedings of the AAAI Conference on Artificial Intelligence |
| volume | 40 |
| number | 38 |
| pages | 32159--32167 |
| year | 2026 |

</details>

<a id="direct-reading-024"></a>

<details>
<summary>DocSLM — Docslm: A small vision-language model for long multimodal document understanding</summary>

**Paper:** Docslm: A small vision-language model for long multimodal document understanding  
**Authors:** Hannan, Tanveer and Dimitrios Mallios and Parth Pathak and Faegheh Sardari and Thomas Seidl and Gedas Bertasius and Mohsen Fayyaz and Sunando Sengupta  
**Citation:** `ref63`; current BibTeX year **2026**; first release **25.11**.  
**Source:** [Google Scholar search](https://scholar.google.com/scholar?q=Docslm%3A%20A%20small%20vision-language%20model%20for%20long%20multimodal%20document%20understanding). Recorded in `title-based Google Scholar search`.  
**Manuscript row:** `tables/table5_full.tex:62`; order 24.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Docslm: A small vision-language model for long multimodal document understanding |
| author | Hannan, Tanveer and Dimitrios Mallios and Parth Pathak and Faegheh Sardari and Thomas Seidl and Gedas Bertasius and Mohsen Fayyaz and Sunando Sengupta |
| booktitle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition |
| pages | 9337--9346 |
| year | 2026 |

</details>

<a id="direct-reading-025"></a>

<details>
<summary>DocSeeker — DocSeeker: Structured visual reasoning with evidence grounding for long document understanding</summary>

**Paper:** DocSeeker: Structured visual reasoning with evidence grounding for long document understanding  
**Authors:** Yan, Hao and Liu, Yuliang and Liu, Xingchen and Zhang, Yuyi and Liao, Minghui and Wu, Jihao and Chen, Wei and Bai, Xiang  
**Citation:** `ref29`; current BibTeX year **2026**; first release **26.04**.  
**Source:** [Paper](https://arxiv.org/abs/2604.12812). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table5_full.tex:63`; order 25.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | DocSeeker: Structured visual reasoning with evidence grounding for long document understanding |
| author | Yan, Hao and Liu, Yuliang and Liu, Xingchen and Zhang, Yuyi and Liao, Minghui and Wu, Jihao and Chen, Wei and Bai, Xiang |
| journal | arXiv preprint arXiv:2604.12812 |
| year | 2026 |

</details>

<a id="direct-reading-026"></a>

<details>
<summary>VinQA (Page Encoding) — VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA</summary>

**Paper:** VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA  
**Authors:** Jang, Young Rok and Hyesoo Kong and Kyunghwan An and Jae Sub Huh and Gyeonghun Kim and Stanley Jungkyu Choi  
**Citation:** `ref98`; current BibTeX year **2026**; first release **26.06**.  
**Source:** [Paper](https://arxiv.org/abs/2606.16092). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table5_full.tex:64`; order 26.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA |
| author | Jang, Young Rok and Hyesoo Kong and Kyunghwan An and Jae Sub Huh and Gyeonghun Kim and Stanley Jungkyu Choi |
| journal | arXiv preprint arXiv:2606.16092 |
| year | 2026 |

</details>

<a id="direct-reading-027"></a>

<details>
<summary>CoE — Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation</summary>

**Paper:** Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation  
**Authors:** Liu, Peiyang and Ziqiang Cui and Xi Wang and Di Liang and Wei Ye  
**Citation:** `ref111`; current BibTeX year **2026**; first release **26.05**.  
**Source:** [Paper](https://arxiv.org/abs/2605.01284). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table5_full.tex:65`; order 27.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation |
| author | Liu, Peiyang and Ziqiang Cui and Xi Wang and Di Liang and Wei Ye |
| journal | arXiv preprint arXiv:2605.01284 |
| year | 2026 |

</details>

<a id="direct-reading-028"></a>

<details>
<summary>OriOn — How to Train Your Long-Context Visual Document Model</summary>

**Paper:** How to Train Your Long-Context Visual Document Model  
**Authors:** Veselka, Austin  
**Citation:** `ref74`; current BibTeX year **2026**; first release **26.02**.  
**Source:** [Paper](https://arxiv.org/abs/2602.15257). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table5_full.tex:66`; order 28.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | How to Train Your Long-Context Visual Document Model |
| author | Veselka, Austin |
| journal | arXiv preprint arXiv:2602.15257 |
| year | 2026 |

</details>

<a id="direct-reading-029"></a>

<details>
<summary>Quote-and-Retrieve — Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels</summary>

**Paper:** Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels  
**Authors:** Liu, Zhuchenyang and Yao Zhang and Yu Xiao  
**Citation:** `ref112`; current BibTeX year **2026**; first release **26.07**.  
**Source:** [Paper](https://arxiv.org/abs/2607.24651). Recorded in `references.bib:journal`.  
**Manuscript row:** `tables/table5_full.tex:67`; order 29.

**Current bibliographic fields**

| Field | Value |
| --- | --- |
| title | Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels |
| author | Liu, Zhuchenyang and Yao Zhang and Yu Xiao |
| journal | arXiv preprint arXiv:2607.24651 |
| year | 2026 |

</details>

<a id="source-notes"></a>

## Full source notes

1. Methods. &#42; marks methods primarily evaluated on single pages/images that also support multiple pages. Venue superscripts follow Table 4 (benchmark catalog); (YY.MM) denotes first release, and -- in the month position means unavailable. Deep = Deep Parsing; Eval. = Evaluation.

2. Model and learning. Model gives the main answer model or language-backbone family. Learning records added Pretraining, supervised fine-tuning (SFT), or reinforcement learning (RL).

3. Evaluation. Ans./Ret./Loc./Eff./Rob. denote answer quality/retrieval/localization/efficiency/robustness. Only dimensions quantitatively reported in the original paper are listed. Ret. denotes page-level evidence selection or prediction and does not imply explicit retrieval in the answering pipeline. Exceptions (a): LayoutLMv3 Loc. is layout-box detection; VinQA (Page Encoding) Ret. is element-citation F1; CoE Loc. includes box-center hits; M3Grounder and DoCoG Loc. include segmentation masks.

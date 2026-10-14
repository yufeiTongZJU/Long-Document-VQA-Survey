# Long-Document VQA Survey

**A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions**

Yufei Tong<sup>1</sup>, Guanjie Cheng<sup>2,*</sup>, Tianle Wu<sup>3</sup>, Leilei Zhang<sup>1,*</sup>, Hang Zheng<sup>1,4</sup>, Peihan Wu<sup>1</sup>, Jianwei Yin<sup>1,2</sup>, Shuiguang Deng<sup>1</sup>

<sup>1</sup>College of Computer Science and Technology, Zhejiang University  
<sup>2</sup>School of Software Technology, Zhejiang University  
<sup>3</sup>Polytechnic Institute, Zhejiang University  
<sup>4</sup>BWTON Technology Co., Ltd., China  
<sup>*</sup>Corresponding authors: Guanjie Cheng and Leilei Zhang.

[Overview](#overview) · [Paper catalogs](#paper-catalogs) · [Taxonomy](taxonomy.md) · [Research evolution](#research-evolution) · [Citation](#citation) · [Contributing](CONTRIBUTING.md)

**Paper status:** the public preprint link will be added after release. This repository accompanies the manuscript snapshot prepared on **14 October 2026**.

## Overview

How can long-document VQA systems acquire, understand, and verify **sufficient evidence within a limited budget**?

This survey connects task challenges with technical choices across four components: document parsing, evidence organization and retrieval, generator organization and learning, and evaluation. It focuses on explicit retrieval while also covering direct reading, and traces research priorities from content understanding to evidence acquisition and sustained evidence management.

![Task decomposition, component functions and challenges, and the explicit-retrieval and direct-reading routes](assets/task-framework.png)

*Task decomposition and two technical routes (Figure 2 of the survey). Colored bands identify component functions; italic labels describe the challenges they address.*

| Component | Task challenge | What the survey examines |
| :--- | :--- | :--- |
| Document parsing | Visual information loss and processing cost | Text extraction, visual fidelity, semantic structures, and parsing on demand |
| Evidence organization and retrieval | Large search spaces and dispersed evidence | Matching modality, evidence granularity, selection mechanisms, and feedback-driven acquisition |
| Generator organization and learning | Evidence dependencies, gaps, and context limits | Reasoning roles, feedback loops, training objectives, and evidence-state management |
| Evaluation | Correct answers can hide unsupported reasoning or high cost | Answer quality, retrieval, localization, efficiency, and robustness under comparable conditions |

See the [taxonomy guide](taxonomy.md) for definitions and boundaries, including **iterative acquisition versus multi-step reasoning**.

## Paper catalogs

The catalogs reproduce the full appendix comparisons in a format that can be browsed, searched, and downloaded.

| Catalog | Entries | Source | Browse |
| :--- | ---: | :--- | :--- |
| Benchmarks | 55 | Appendix Table 4 | [Benchmark catalog](papers/benchmarks.md) |
| Direct reading | 29 | Appendix Table 5 | [Methods without explicit retrieval](papers/direct-reading.md) |
| Explicit retrieval | 110 | Appendix Table 6 | [Methods with explicit retrieval](papers/explicit-retrieval.md) |

The explicit-retrieval catalog includes **20 retrieval-only methods and 90 document VQA methods**. The direct-reading catalog also includes single-page foundations. A paper may contribute both a method and a benchmark, so catalog rows are not a count of unique publications.

- **Download and filter:** [structured data and CSV files](data/).
- **Bibliography:** [references.bib](references.bib), containing 165 cited references, including foundational work and related surveys. The three catalogs refer to 158 distinct bibliography entries.
- **Read the labels:** [taxonomy and notation](taxonomy.md).

**Reading the records.** First-release dates and bibliographic publication years are separate fields. Dates, venue labels, qualifiers, and missing-value markers follow the manuscript tables. A Google Scholar search link is a discovery aid, not a verified paper or official code URL. The catalogs preserve the survey's classifications; they are not a leaderboard or a claim that all listed results were obtained under comparable settings.

## Research evolution

![Five periods connect four-component technical evolution with content understanding, evidence acquisition, and sustained evidence management](assets/research-evolution.png)

*Three overall research priorities and the technical evolution of four components (Figure 7 of the survey). The five periods reflect expanding priorities; techniques from different periods can be combined.*

1. **Content understanding:** retain visual content, layout, and cross-page relationships in document representations.
2. **Evidence acquisition:** locate sufficient, high-fidelity support through visual indexing, structural relations, fine-grained selection, and feedback.
3. **Sustained evidence management:** maintain evidence states, identify remaining gaps, and coordinate reading, verification, and stopping under budget constraints.

## Research directions

For individual questions, the survey highlights **evidence sufficiency assessment**, **verifiable and correctable understanding**, and **budget-aware coordination**. Across questions and tasks, it considers **memory reuse** and **experience-driven strategy improvement** as directions toward continual document understanding.

## Updates

- **2026-10-14:** Prepared the initial companion catalog from the current manuscript, including the three appendix comparisons, taxonomy definitions, bibliography, and overview figures.

This date identifies the repository snapshot, not a claim of exhaustive literature coverage through that day. Later additions and corrections will be recorded separately so readers can distinguish the manuscript snapshot from subsequent updates.

## Citation

If this survey or its organization of the literature is useful to your work, please cite the paper. Until the public preprint identifier is available, the manuscript can be cited as follows:

```bibtex
@unpublished{tong2026taskcentric,
  title  = {A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions},
  author = {Tong, Yufei and Cheng, Guanjie and Wu, Tianle and Zhang, Leilei and Zheng, Hang and Wu, Peihan and Yin, Jianwei and Deng, Shuiguang},
  year   = {2026},
  note   = {Manuscript}
}
```

Machine-readable citation metadata is available in [CITATION.cff](CITATION.cff). The citation will be updated with the public preprint URL and identifier after release.

## Contributions and contact

Suggestions for missing papers, classification corrections, and broken links are welcome through Issues or pull requests. Please include a source supporting the proposed change; see [CONTRIBUTING.md](CONTRIBUTING.md).

For questions about the survey, please open an Issue in this repository.

## License

The authors' original repository content is licensed under [Creative Commons Attribution 4.0 International](LICENSE). Credit the survey authors, link to the license, and indicate changes when reusing it. Linked papers, datasets, models, and code retain their own licenses and ownership.

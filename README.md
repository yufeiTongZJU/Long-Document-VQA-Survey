# Long-Document VQA Survey

**A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions**

Yufei Tong<sup>1</sup>, Guanjie Cheng<sup>2,&#42;</sup>, Tianle Wu<sup>3</sup>, Leilei Zhang<sup>1,&#42;</sup>, Hang Zheng<sup>1,4</sup>, Peihan Wu<sup>1</sup>, Jianwei Yin<sup>1,2</sup>, Shuiguang Deng<sup>1</sup>

<sup>1</sup>College of Computer Science and Technology, Zhejiang University  
<sup>2</sup>School of Software Technology, Zhejiang University  
<sup>3</sup>Polytechnic Institute, Zhejiang University  
<sup>4</sup>BWTON Technology Co., Ltd., China  
<sup>&#42;</sup>Corresponding authors: Guanjie Cheng and Leilei Zhang.

[Contributions](#core-contributions) · [Future directions](#future-research-directions) · [Paper lists](#paper-lists) · [Citation](#citation)

*The arXiv link will be added after release.*

## Overview

How can long-document VQA systems acquire and use **sufficient evidence under context and computational budgets**? We examine how task bottlenecks shape technical choices and research priorities, focusing on explicit retrieval while covering direct reading.

## Core contributions

- **Task-centric, fine-grained taxonomy.** Organize methods by the challenges addressed through parsing, evidence organization and retrieval, generator organization and learning, and evaluation. Distinguish technical choices such as iterative evidence acquisition and multi-step reasoning.
- **Evolution through task bottlenecks.** Trace expanding priorities from multimodal content understanding to sufficient, high-fidelity evidence acquisition and sustained evidence management, explaining how feedback connects the four components.
- **Research opportunities.** Identify directions for reliable answers under limited budgets and for continual document understanding through memory reuse and strategy improvement.

![Task decomposition and two technical routes for long-document VQA](assets/task-framework.png)

<details>
<summary><strong>View the research evolution</strong></summary>

![Three research priorities and technical evolution across four components](assets/research-evolution.png)

</details>

## Future research directions

### Reliable and efficient answers to individual questions

- **Evidence sufficiency:** Relevant evidence may still be incomplete. Model dependencies, acquire complementary support, and assess remaining gaps before answering.
- **Verifiable and correctable understanding:** Correct answers can mask faulty reasoning. Trace intermediate judgments to sources, verify support, and correct errors and dependent conclusions.
- **Budget-aware coordination:** Local gains may not improve the full pipeline. Coordinate acquisition, reading, verification, and stopping using evidence states and remaining budgets; evaluate answer quality against end-to-end cost.

### Toward continual document understanding

- **Memory reuse across questions:** Reuse evidence and interaction history with source tracing, checking applicability and revising memory after corrections or document updates.
- **Strategy improvement across tasks:** Turn experience into transferable retrieval, reading, and verification procedures; validate them on independent tasks before updating agents or skills.

Section 4 and Appendix D develop these directions into research opportunities for system design and evaluation.

## Paper lists

| Category | Entries | Browse |
| :--- | ---: | :--- |
| Benchmarks | 55 | [Benchmark list](papers/benchmarks.md) |
| Direct reading | 29 | [Methods without explicit retrieval](papers/direct-reading.md) |
| Explicit retrieval | 110 | [Methods with explicit retrieval](papers/explicit-retrieval.md) |

The lists include single-page foundations and retrieval-only studies. Entries across lists may refer to the same publication. Detailed comparisons appear in the paper's appendix.

The [BibTeX bibliography](references.bib) contains all 165 references cited in the survey.

## Citation

If you find this survey useful, please cite it. This provisional entry will be updated after the arXiv release.

```bibtex
@unpublished{tong2026taskcentric,
  title  = {A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions},
  author = {Tong, Yufei and Cheng, Guanjie and Wu, Tianle and Zhang, Leilei and Zheng, Hang and Wu, Peihan and Yin, Jianwei and Deng, Shuiguang},
  year   = {2026},
  note   = {Manuscript}
}
```

## Contact and license

Paper suggestions and corrections are welcome through [Issues](https://github.com/yufeiTongZJU/Long-Document-VQA-Survey/issues).

Our original content is licensed under [CC BY 4.0](LICENSE). Linked resources retain their own licenses.

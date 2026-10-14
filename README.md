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

How can long-document VQA systems acquire and use **sufficient evidence within a limited budget**?

We analyze how document VQA systems meet these requirements, emphasizing explicit retrieval while also covering direct reading.

## Core contributions

- **A task-driven framework.** We connect content fidelity, evidence sufficiency, evidence use, and reliable evaluation to four interacting components: document parsing, evidence organization and retrieval, generator organization and learning, and evaluation.
- **A fine-grained taxonomy by task function.** We categorize representations and structures, retrieval modalities and granularities, acquisition strategies, reasoning and learning, and evaluation capabilities. This clarifies distinctions such as iterative evidence acquisition versus multi-step reasoning.
- **Bottleneck-driven technical evolution.** We trace expanding priorities from multimodal understanding to sufficient, high-fidelity evidence acquisition and sustained evidence management, explaining how bottlenecks and feedback connect technical choices across components.

![Task decomposition and two technical routes for long-document VQA](assets/task-framework.png)

<details>
<summary><strong>View the research evolution</strong></summary>

![Three research priorities and technical evolution across four components](assets/research-evolution.png)

</details>

## Future research directions

Our outlook connects open challenges to concrete opportunities for system design and evaluation at two levels.

### Reliable and efficient answers to individual questions

- **Evidence sufficiency:** Construct complementary evidence sets, model dependencies, and test whether systems detect relevant but insufficient support before deciding to acquire more evidence or stop.
- **Verifiable and correctable understanding:** Link intermediate judgments to source pages and regions, test whether evidence supports answers, and revise erroneous memories and dependent conclusions.
- **Budget-aware coordination:** Coordinate parsing, retrieval, reading, verification, and stopping using evidence states and remaining budgets; measure answer quality against end-to-end cost across document lengths and budgets.

### Toward continual document understanding

- **Memory reuse across questions:** Reuse evidence and interaction history while tracking provenance, checking continued applicability, and revising memories after user corrections or document updates.
- **Continual, experience-driven strategy improvement:** Develop transferable retrieval, reading, and verification procedures from successes, failures, and feedback; validate proposed strategies on independent tasks before updating agents or their skills.

Section 4 and Appendix D of the survey develop these research opportunities in detail.

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

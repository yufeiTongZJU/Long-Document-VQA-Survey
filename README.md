# Long-Document VQA Survey

**A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions**

Yufei Tong<sup>1</sup>, Guanjie Cheng<sup>2,&#42;</sup>, Tianle Wu<sup>3</sup>, Leilei Zhang<sup>1,&#42;</sup>, Hang Zheng<sup>1,4</sup>, Peihan Wu<sup>1</sup>, Jianwei Yin<sup>1,2</sup>, Shuiguang Deng<sup>1</sup>

<sup>1</sup>College of Computer Science and Technology, Zhejiang University  
<sup>2</sup>School of Software Technology, Zhejiang University  
<sup>3</sup>Polytechnic Institute, Zhejiang University  
<sup>4</sup>BWTON Technology Co., Ltd., China  
<sup>&#42;</sup>Corresponding authors: Guanjie Cheng and Leilei Zhang.

[Paper lists](#paper-lists) · [Bibliography](references.bib) · [Citation](#citation)

*The arXiv link will be added after release.*

## Overview

How can long-document VQA systems acquire and use **sufficient evidence within a limited budget**?

Our survey connects task challenges with technical choices across parsing, retrieval, generation, and evaluation. It covers explicit retrieval and direct reading, tracing the shift from content understanding to evidence acquisition and sustained evidence management.

![Task decomposition and two technical routes for long-document VQA](assets/task-framework.png)

<details>
<summary><strong>View the research evolution</strong></summary>

![Three research priorities and technical evolution across four components](assets/research-evolution.png)

</details>

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

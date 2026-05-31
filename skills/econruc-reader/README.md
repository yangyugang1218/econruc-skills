# econruc-reader skill

## 中文说明

`econruc-reader` 用于阅读经济学论文并生成结构化笔记、seminar 问题、复现备忘录、图表解读和 referee-style critique。它不是摘要器，而是像研究者一样读论文：研究问题是什么、设计识别什么、证据支持到哪里、贡献是否成立。

---

## 适用场景

- 快速读论文。
- 深度读论文和组会汇报准备。
- 从 PDF 中提取 research question、contribution、data、identification、results。
- 解读回归表、event-study 图、结构模型结果和机制图。
- 生成 seminar questions、referee concerns 和 replication checklist。
- 为 `econruc-beamer` 生成 slide map。

---

## 中文模式

中文模式面向博士生日常阅读、中文组会、论文选题和导师讨论。

重点：

- 这篇文章为什么重要？
- 它解决了什么经济学问题？
- 识别或模型最关键的假设是什么？
- 哪些结果可信，哪些只是 suggestive？
- 我能借鉴它的问题、数据、设计、机制还是写法？

---

## English mode

English mode targets seminar memos, referee-style critiques, literature notes, and replication planning.

Priorities:

- One-sentence research question and answer.
- Contribution by question, data, design, mechanism, and policy margin.
- Evidence map from tables/figures to claims.
- Identification/model assumptions and threats.
- High-quality seminar or referee questions.

---

## 默认读书笔记结构

1. Citation snapshot
2. One-sentence summary
3. Research question and answer
4. Contribution map
5. Data and design/model
6. Main results
7. Mechanisms and robustness
8. Limitations and threats
9. Seminar questions
10. How I would use this paper

---

## 文件结构

```text
econruc-reader/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── critique-and-questions.md
    ├── reading-note-template.md
    └── table-figure-reading.md
```

---

## 维护建议

- 读书笔记模板放入 `references/reading-note-template.md`。
- 表格和图形解读规则放入 `references/table-figure-reading.md`。
- seminar/referee 问题和 critique 规则放入 `references/critique-and-questions.md`。

## English Overview

`econruc-reader` reads economics papers for research use: structured notes, contribution maps, identification logic, table/figure interpretation, limitations, seminar questions, and replication planning.

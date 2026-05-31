# econruc-writing skill

## 中文说明

`econruc-writing` 用于经济学论文和研究文本的起草、重构和章节写作。它覆盖摘要、引言、结果段、机制段、讨论、政策报告和中英文研究文本，但不替代 `econ-intro` 的专门引言开发，也不替代 `econruc-polishing` 的句子层润色。

---

## 核心原则

- 从经济学论点向外写，而不是从漂亮句子开始。
- 数据、制度、识别、机制、结果和贡献必须互相支撑。
- 不编造结果、引用、机制、稳健性或样本细节。
- 因果语言服从识别设计。
- 中文和英文是两套写作系统，不是互译模板。

---

## 中文模式

中文模式面向中文论文、博士论文、项目申请、中文报告、组会材料和作者内部讨论。

重点：

- 问题意识清楚。
- 制度背景与研究设计连接。
- 变量和样本解释充分。
- 政策含义有边界。
- 语言自然严谨，不机械翻译英文句式。

---

## English mode

English mode targets Top5/field-journal papers, working papers, abstracts, result sections, and international seminar materials.

Priorities:

- Precise economic question.
- Clear friction or mechanism.
- Transparent design/model.
- Magnitudes and benchmarks.
- Contribution-forward but modest prose.
- Boundaries and threats stated without self-sabotage.

---

## 章节写作默认逻辑

### Abstract

Question -> setting/data/design -> main result -> mechanism/welfare -> contribution.

### Introduction

Use `econ-intro` when the task is specifically introduction-heavy.

### Results

Claim-first paragraph:

1. State result.
2. Give magnitude and benchmark.
3. Explain specification or variation.
4. Interpret economically.
5. State limitation or next test when needed.

### Mechanism and heterogeneity

Separate mechanism evidence from subgroup heterogeneity. Do not call every heterogeneity result a mechanism.

### Discussion and conclusion

Return to the economic question, not a list of results.

---

## 文件结构

```text
econruc-writing/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── bilingual-workflow.md
    ├── section-patterns.md
    └── top5-article-architecture.md
```

---

## 维护建议

- 章节结构和段落模板放入 `references/section-patterns.md`。
- Top5/field-journal 文章架构放入 `references/top5-article-architecture.md`。
- 中英文写作转换规则放入 `references/bilingual-workflow.md`。

## English Overview

`econruc-writing` drafts and restructures economics papers, reports, abstracts, result sections, discussions, and bilingual research prose. It builds from the economic argument outward: question, design/model, evidence, mechanism, contribution, and boundary.

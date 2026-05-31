# econruc-empirical skill

## 中文说明

`econruc-empirical` 用于审查、设计和表述经济学实证策略。它关注识别、估计量、稳健性、机制、异质性和结果解释，而不是只帮用户把回归结果写得更漂亮。

它适合开题、论文设计、回归表解释、审稿回复、稳健性方案和 seminar 讨论。

---

## 核心原则

- Identification first, estimator second.
- 先讲反事实，再讲模型式。
- 识别假设必须能被读者理解。
- 稳健性检验要回应真实威胁，而不是堆表。
- 不能用语言包装弥补识别缺陷。

---

## 中文模式

中文模式面向中文论文、组会、开题/预答辩、中文审稿回复和政策评估报告。

重点：

- 把“反事实是什么”讲清楚。
- 把“为什么这个变动可用于识别”讲清楚。
- 把“可能的威胁”和“如何回应”讲清楚。
- 语言要适合导师和中文期刊读者理解，不要只堆英文术语。

---

## English mode

English mode targets Top5/field-journal empirical sections, referee responses, seminar explanations, and replication notes.

Priorities:

- Estimand, identifying variation, assumptions, and threats.
- Clean equation language with transparent fixed effects and error structure.
- Causal language calibrated to design.
- Robustness as threat-specific evidence.
- Mechanisms and heterogeneity separated from the main effect.

---

## 常见设计对象

| 设计 | 必须说明 |
|---|---|
| DiD / event study | parallel trends, treatment timing, omitted period, dynamic effects, clustering |
| IV | first stage, exclusion restriction, monotonicity, LATE interpretation |
| RD | running variable, cutoff, bandwidth, sorting/manipulation, local interpretation |
| RCT | randomization, compliance, attrition, spillovers |
| SCM | donor pool, pre-fit, weights, placebo tests |
| Bartik / shift-share IV | shocks, shares, exogeneity level, exposure construction |
| Bunching | counterfactual density, optimization frictions, excluded region |
| Structural | primitives, identification, moments, counterfactual credibility |

---

## 输出规范

默认输出应包括：

1. Design contract
2. Estimating equation
3. Identification assumptions
4. Main threats
5. Robustness map
6. Mechanism/heterogeneity plan
7. Suggested wording
8. Remaining risks

---

## 文件结构

```text
econruc-empirical/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── identification-checklist.md
    ├── robustness-map.md
    └── tables-and-results.md
```

---

## 维护建议

- 新识别设计和检查项放入 `references/identification-checklist.md`。
- 稳健性检验和威胁对应关系放入 `references/robustness-map.md`。
- 表格和结果解释语言放入 `references/tables-and-results.md`。

## English Overview

`econruc-empirical` helps researchers plan, audit, and explain empirical economics strategies. It focuses on identification, estimating equations, assumptions, robustness, mechanisms, heterogeneity, and calibrated interpretation.

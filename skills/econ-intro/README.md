# econ-intro skill

## 中文说明

`econ-intro` 专门服务经济学论文引言。它不是普通润色工具，而是帮助研究者把“研究问题、经济学摩擦、识别难点、核心发现、贡献定位”组织成一套可信的 introduction 叙事。

这个 skill 适合论文开题、工作论文、投稿论文、博士论文、基金申请和政策研究项目。它与 `econruc-writing` 的区别是：`econ-intro` 只聚焦引言、研究动机、研究问题、贡献段和 puzzle-to-design narrative。

---

## 核心目标

- 让读者在前几段内明白研究对象为什么重要。
- 把现实背景转换成经济学问题，而不是堆背景材料。
- 把“已有文献知道什么”和“本文还能推进什么”讲清楚。
- 把识别或模型挑战提前交代，避免结果出现得像孤立发现。
- 把贡献拆成 substantive contribution、design/data contribution、literature contribution。

---

## 中文模式

中文模式面向中文论文、博士论文、中文顶刊、基金申请和组会汇报。

重点：

- 强调问题意识、制度背景、现实约束和政策含义。
- 语言要自然、克制、有判断，不要英文化长句。
- 背景材料必须服务研究问题，避免写成政策文件开头。
- 贡献表述要具体，避免“丰富了相关研究”“具有重要意义”这类空泛句。

常用段落节奏：

1. 现实问题与经济学对象。
2. 未解问题或机制争议。
3. 为什么难识别或难测量。
4. 本文场景、数据和设计。
5. 核心发现。
6. 贡献与边界。

---

## English mode

English mode targets Top5-style, field-journal, working-paper, and seminar-facing introductions.

Priorities:

- Lead with the economic question, not institutional description alone.
- State the friction, trade-off, or puzzle precisely.
- Introduce the identification challenge before presenting results.
- Use modest causal language calibrated to design.
- Make contribution paragraphs compact and field-aware.

Canonical paragraph logic:

1. Economic motivation and broad question.
2. Gap, puzzle, or unresolved mechanism.
3. Empirical/theoretical challenge.
4. Setting, data, and design.
5. Main findings with magnitudes.
6. Contributions and relation to literatures.

---

## 可复用句式原则

### 谨慎因果语言

- Strong: `causes`, `identifies`, `estimates the causal effect of`
- Medium: `provides evidence that`, `shows that`, `documents`
- Weak/descriptive: `is associated with`, `is consistent with`, `suggests`

### 贡献句不要空泛

弱：

`This paper contributes to the literature on environmental regulation.`

强：

`This paper contributes by showing how firm-level compliance incentives mediate the effect of environmental regulation on productivity reallocation.`

---

## 文件结构

```text
econ-intro/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── contribution-language.md
    ├── intro-architecture.md
    └── intro-diagnostics.md
```

---

## 维护建议

- 新增段落结构时，放入 `references/intro-architecture.md`。
- 新增贡献句、文献定位句、中文/英文表达范式时，放入 `references/contribution-language.md`。
- 新增常见问题和诊断标准时，放入 `references/intro-diagnostics.md`。
- 中文和英文模式分开维护，不要逐句互译。

## English Overview

`econ-intro` helps researchers draft, diagnose, and restructure economics paper introductions. It focuses on the logic of the introduction: economic question, motivation, identification/model challenge, design, main findings, and contribution. It supports separate Chinese and English modes because Chinese journal/grant introductions and English Top5/field-journal introductions follow different conventions.

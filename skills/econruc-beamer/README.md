# econruc-beamer skill

## 中文说明

`econruc-beamer` 用于把经济学论文、工作论文、报告或研究笔记转化为 LaTeX Beamer 汇报。它的目标不是把论文内容横向搬到 slide 上，而是把论文重构成一个可以讲清楚的经济学故事。

它适合组会、博士论文汇报、seminar、conference talk、job talk、课程展示和论文分享。

---

## 核心原则

- 一页 slide 只承担一个任务。
- 先讲经济学问题，再讲模型/识别，再讲证据和贡献。
- 所有论文转 slides 都必须有 Introduction section。
- 前部必须包含三页：Research motivation、Research question、Research contribution。
- 图表必须是 evidence anchor，不能只是装饰。
- Beamer 完成的标准是编译、渲染、抽查版面，而不是只生成 `.tex`。

---

## 中文模式

中文模式面向中文组会、博士论文汇报、学院 seminar 和政策讨论。

设计倾向：

- 标题短而有判断，避免英文式长句。
- 更重视制度背景、研究问题、识别逻辑和政策含义。
- 可以使用少量中英术语混排，但不要中英句法混杂。
- 口头汇报逻辑要清楚：为什么重要、怎么做、发现什么、能说明什么。

---

## English mode

English mode targets economics seminars, conferences, job talks, and field-journal presentations.

Design priorities:

- Claim-first slide titles.
- Sparse bullets and large readable figures.
- Early evidence-bearing slides, not only motivation.
- Clear separation between model/design, evidence, mechanisms, counterfactuals, and limitations.
- Contribution positioning against relevant literatures.

---

## 默认视觉系统

- Aspect ratio: `16:9`
- Background: white
- Main accent: deep RUC/economics blue
- Section dividers: large blue section title with light horizontal rule
- Footline: small page number at bottom right
- Blocks: light gray concept boxes only when useful
- Tables: selected rows or table-to-figure; avoid full regression tables in main slides
- Figures: left figure + right takeaway, or full-width figure + one bottom message

---

## 推荐 slide 架构

### 45-60 分钟论文汇报

- 1 title page
- 3-5 introduction slides
- 4-8 context/data slides
- 6-10 model/design slides
- 10-16 result/mechanism slides
- 5-8 counterfactual/robustness/implication slides
- 2-4 conclusion/discussion slides
- 10-30 backup slides

### Full-paper workflow

1. 先做完整 deck，不只做 10 页 prototype。
2. 编译 PDF。
3. 抽查 title、introduction、theory/design、main evidence、conclusion、backup。
4. 做 economist review：故事是否清楚、证据是否足够、图是否可信、贡献是否 sharp。
5. 再修改 skill 或模板。

---

## 文件结构

```text
econruc-beamer/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── econruc_beamer_template.tex
│   ├── ruc_logo.png
│   └── ruc_logo_mark.tex
├── references/
│   ├── bilingual-beamer.md
│   ├── deck-architecture.md
│   ├── latex-beamer-patterns.md
│   ├── paper-to-slides.md
│   ├── render-and-qa.md
│   └── visual-style.md
└── scripts/
    └── outline_to_beamer.py
```

---

## 维护建议

- 模板层修改放到 `assets/econruc_beamer_template.tex`。
- 论文转 slides 的叙事规则放到 `references/paper-to-slides.md`。
- 长度、slide map、backup 策略放到 `references/deck-architecture.md`。
- 编译和 QA 规则放到 `references/render-and-qa.md`。
- 中文/英文 Beamer 语言差异放到 `references/bilingual-beamer.md`。

## English Overview

`econruc-beamer` converts economics papers into polished LaTeX Beamer seminar decks. It is designed for spoken economic arguments: motivation, question, contribution, setting, model/design, evidence, mechanisms, counterfactuals, implications, and backup. It maintains separate Chinese and English presentation modes.

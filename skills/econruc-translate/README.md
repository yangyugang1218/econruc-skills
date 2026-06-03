# econruc-translate skill

## 中文说明

`econruc-translate` 用于把英文经济学论文、工作论文、PDF、文章草稿或学术材料逐句翻译成正式、准确的简体中文，并尽可能保留原文结构、句序、脚注、公式、引用、图表标题和学术语气。

它不是摘要工具，也不是改写工具。默认目标是完整忠实翻译，必要时生成中文 TeX，并用 XeLaTeX 编译 PDF。

---

## 适用场景

- 英文经济学论文逐句翻译成中文。
- 英文 working paper / NBER / AER / QJE / JPE / ReStud / field-journal paper 翻译。
- 保留脚注、公式、引用、图表标题和参考文献结构。
- 生成 `ctexart` 中文 LaTeX 源码和可阅读 PDF。
- 删除或保留 tables、figures、references，按用户要求处理。
- 将英文论文翻译成适合中文组会、博士阅读和研究备忘的完整译文。

---

## 核心原则

- 完整翻译，不总结、不省略、不自由改写。
- 保持原文段落顺序和句序。
- 经济学术语前后一致。
- 公式、变量、引用、JEL codes、URLs、软件名和模型名保持可识别。
- 脚注要翻译并尽量放回原位置。
- 图表若不能重建，保留标题、caption、notes 或占位说明，不虚构图像内容。

---

## 经济学翻译规则

常见术语要统一：

| English | 中文建议 |
|---|---|
| identification | 识别 |
| identifying assumption | 识别假设 |
| treatment effect | 处理效应 |
| event study | 事件研究 |
| fixed effects | 固定效应 |
| instrumental variable | 工具变量 |
| marginal cost | 边际成本 |
| market power | 市场势力 |
| welfare | 福利 |
| allocative inefficiency | 配置低效率 |
| robustness check | 稳健性检验 |
| heterogeneous effects | 异质性效应 |

不要翻译 citation author names、期刊名、书名、URL、软件名，除非原文已有通行中文译名。

---

## 工作流

1. Inspect source：确认文件存在，检查 PDF 页数和文本抽取质量。
2. Extract text：用 `pdftotext`、`mutool`、PyMuPDF 或其他结构化工具抽取文本。
3. Chunk cautiously：按章节或页码分块，保留中间页码用于覆盖检查。
4. Translate completely：逐句翻译，不跳段。
5. Handle footnotes：收集、合并跨页脚注，翻译并放回对应位置。
6. Handle tables/figures/references：按用户要求保留、简化或删除。
7. Assemble TeX：使用 `assets/paper_translation_template.tex`。
8. Compile twice：用 XeLaTeX 编译。
9. Validate：检查 PDF、页码、脚注、表格/参考文献处理和未翻译残留。
10. Report：返回最终文件路径、页数、保留/删除策略和编译 caveats。

---

## 输出格式

默认输出：

1. 中文 TeX 源码。
2. 编译后的 PDF。
3. 工作目录，包括抽取文本、分块文件、脚本和日志。
4. 简短 QA：页数、脚注、表格、参考文献、未翻译残留。

---

## 文件结构

```text
econruc-translate/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── paper_translation_template.tex
└── scripts/
    └── normalize_translation_tex.py
```

---

## 维护建议

- 翻译执行规则放在 `SKILL.md`。
- TeX 版式模板放在 `assets/paper_translation_template.tex`。
- 删除页码、删除表格正文、删除参考文献等后处理逻辑放在 `scripts/normalize_translation_tex.py`。
- 后续可新增 `references/termbank-economics.md`，维护经济学术语中英文对照。
- 不要把完整翻译任务降级成摘要；如果用户想要摘要，应转向 `econruc-reader`。

## English Overview

`econruc-translate` translates English economics and academic papers into faithful Simplified Chinese while preserving structure, sentence order, footnotes, equations, citations, figure/table captions, and academic tone. It can assemble Chinese TeX with `ctexart` and compile a polished PDF when requested.

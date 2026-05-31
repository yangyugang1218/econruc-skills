# econruc-polishing skill

## 中文说明

`econruc-polishing` 用于经济学学术文本润色、翻译、压缩和结构修复。它不是普通语言润色，而是先检查经济学逻辑，再改句子：研究问题是否清楚、识别是否可信、贡献是否过度、因果语言是否合适。

---

## 适用场景

- 英文论文段落、摘要、引言、结果段和贡献段。
- 中文论文、中文摘要、基金文本、政策报告和博士论文。
- 中英互译但保留经济学逻辑，而不是逐句直译。
- 审稿回复和 revision memo 的专业语气修复。

---

## 中文模式

中文模式重点：

- 自然、清楚、克制，有经济学判断。
- 避免英文化长句和空泛政策口号。
- 先修复逻辑顺序，再修复表达。
- 明确制度背景、变量含义、研究设计和政策含义。

---

## English mode

English mode targets Top5/field-journal prose.

Priorities:

- Compressed logic.
- Active verbs.
- Calibrated causal claims.
- Clear contribution and mechanism language.
- No ornate prose or unsupported generalization.

---

## 常用动词强度

| 强度 | 英文 | 中文 |
|---|---|---|
| 强因果 | causes, identifies | 识别了……的因果影响 |
| 中等证据 | shows, estimates, provides evidence | 估计、发现、提供证据 |
| 描述相关 | documents, is associated with | 刻画、呈现、与……相关 |
| 谨慎解释 | is consistent with, suggests | 与……一致、提示 |

---

## 润色顺序

1. 判断文本类型和段落任务。
2. reverse outline：每句话承担什么 claim。
3. 删除重复背景和空泛贡献。
4. 校准因果语言。
5. 强化变量、机制、识别和结果之间的连接。
6. 最后才做句子层面的压缩和风格统一。

---

## 文件结构

```text
econruc-polishing/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── bilingual-polishing.md
    ├── phrasebank-economics.md
    └── top5-style-guide.md
```

---

## 维护建议

- 经济学短语和中英表达放入 `references/phrasebank-economics.md`。
- Top5/field-journal 风格规则放入 `references/top5-style-guide.md`。
- 翻译和双语修订规则放入 `references/bilingual-polishing.md`。

## English Overview

`econruc-polishing` polishes economics prose by repairing logic before sentence style. It supports English and Chinese academic writing, translation, abstracts, introductions, result paragraphs, contribution language, and referee-response prose.

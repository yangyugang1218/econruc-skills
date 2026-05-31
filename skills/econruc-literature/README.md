# econruc-literature skill

## 中文说明

`econruc-literature` 用于经济学文献综述、贡献定位、related work、field map 和论文选题定位。它不是简单列文献，而是帮助研究者说明：一组文献已经知道什么、还不知道什么、本文为什么能推进这个问题。

---

## 核心原则

- 文献综述是贡献论证，不是作者列表。
- 按经济学问题、机制、识别、数据、测量和政策边界组织文献。
- 不用“没人研究过本地区”作为主要 gap。
- 贡献必须说明 broader question，而不是只说 setting 新。
- 不编造文献；需要精确引用时应由用户提供 bibliography 或明确要求检索。

---

## 中文模式

中文模式面向中文论文、博士论文、基金申请和中文期刊。

重点：

- 兼顾国内外文献对话。
- 说明中国制度背景或中国数据为什么能识别更一般的问题。
- 文献脉络可以更展开，但要避免“流水账”。
- 贡献定位要具体到机制、数据、识别或政策含义。

---

## English mode

English mode targets Top5/field-journal related work and contribution positioning.

Priorities:

- Compact literature blocks.
- Position by question and mechanism rather than chronology.
- Explain what prior work establishes and what remains unresolved.
- Make the departure of the current paper explicit.
- Avoid exaggerated gap claims.

---

## 文献定位矩阵

| 维度 | 要回答的问题 |
|---|---|
| Question | 本文问的问题属于哪个 broader field question？ |
| Mechanism | 本文检验或提出了什么机制？ |
| Identification | 本文的识别设计如何推进已有研究？ |
| Data/measurement | 本文数据或测量对象有什么新信息？ |
| Setting | 这个制度/地区为什么有外推价值？ |
| Policy/welfare | 本文如何改变政策或福利理解？ |

---

## 文件结构

```text
econruc-literature/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── literature-positioning.md
    └── top5-field-map.md
```

---

## 维护建议

- 文献组织模板放入 `references/literature-positioning.md`。
- Top5、领域顶刊、中国顶刊定位差异放入 `references/top5-field-map.md`。
- 新增领域地图时，按 field/question/mechanism/design 分类，而不是按期刊名堆列表。

## English Overview

`econruc-literature` helps build literature reviews, contribution positioning, related-work sections, and field maps for economics papers. It turns paper-by-paper notes into an argument about what the current project contributes.

# econruc-response skill

## 中文说明

`econruc-response` 用于经济学论文审稿意见回复、revision memo、editor letter 和逐点回复。它的目标是帮助作者以专业、克制、有证据的方式回应审稿人，而不是把语气写得更客气而已。

---

## 核心原则

- 回应的是经济学 concern，不只是评论表面文字。
- 区分“论文中已经修改”和“回复信中解释”。
- 不承诺没有做过的分析。
- 不夸大新增结果。
- 语气尊重、直接、具体，不防御。

---

## 中文模式

中文模式适合中文期刊回复、导师修改意见、内部 revision plan 和中文审稿意见梳理。

重点：

- 把每条意见分类：识别、机制、稳健性、数据、文献、表述、政策含义。
- 说明修改动作、补充分析、结果变化和仍然存在的边界。
- 可写得更执行导向，便于团队分工。

---

## English mode

English mode targets journal response letters, editor letters, point-by-point replies, and revision memos.

Priorities:

- Professional and non-defensive tone.
- Acknowledge the concern.
- State the change.
- Report new evidence or robustness checks.
- Explain why the concern is addressed or what limitation remains.

---

## 回复结构

常用模板：

```text
Comment:
[quote or summarize the referee concern]

Response:
We thank the referee for raising this point. We have addressed it in three ways...

Revision:
In the revised manuscript, we now...
```

---

## 常见 concern 类型

| Concern | 回应重点 |
|---|---|
| Identification | identifying assumption, threat, robustness, placebo |
| Mechanism | additional evidence, alternative channels, limits |
| Robustness | specification map, sample changes, inference |
| Data/sample | construction, measurement error, attrition, representativeness |
| Literature | added citations, clearer positioning |
| External validity | scope conditions and boundary |
| Policy interpretation | avoid overclaiming, clarify welfare/policy channel |

---

## 文件结构

```text
econruc-response/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── referee-response-playbook.md
    └── revision-memo.md
```

---

## 维护建议

- 逐点回复模式、语气和常见 concern 放入 `references/referee-response-playbook.md`。
- 大修计划、任务分解和 editor memo 放入 `references/revision-memo.md`。

## English Overview

`econruc-response` helps draft and audit economics referee responses, revision memos, editor letters, and point-by-point replies. It focuses on trust: acknowledge concerns, report changes, present evidence, and preserve identification and interpretation boundaries.

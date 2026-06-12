# econruc-report-writing skill

## 中文说明

`econruc-report-writing` 是面向研报、政策分析、产业分析、咨询报告和 briefing memo 的写作 skill。它强调真实数据、来源可追溯、结构清晰和逻辑可靠。

这个 skill 的核心底线是：不能胡编数据，不能编造来源，不能把没有证据的判断写成事实。

---

## 适用场景

- 政策分析报告
- 行业/产业研报
- 咨询机构风格报告
- 政府或机构 briefing memo
- 市场研究、区域发展报告、产业链分析
- 数据驱动的中文或英文研究报告

---

## 核心原则

- 重要事实必须有来源、日期、单位和统计口径。
- 事实、估计、判断、预测和建议必须分开。
- 当前政策、市场数据、公司事实和统计数据必须核验。
- 没有来源时，应标注 `待补充来源`，不能用看似合理的数字填空。
- 报告结构要服务决策问题，而不是堆材料。

---

## 中文模式

中文模式面向中文研报、政策分析、咨询报告和领导简报。

重点：

- 问题背景清楚。
- 数据事实扎实。
- 政策语境准确。
- 逻辑链条明确。
- 建议可执行，风险有边界。
- 避免空泛表述，如“意义重大”“前景广阔”“成效显著”，除非有证据支撑。

---

## English mode

English mode targets policy memos, sector reports, consulting-style reports, and evidence-based analytical briefs.

Priorities:

- Executive answer first.
- Evidence-backed claims.
- Clear distinction between facts, estimates, assumptions, and recommendations.
- Source-ready tables and exhibits.
- Concise, decision-oriented prose.

---

## 报告组成部分

一份可靠报告通常包括：

1. 标题和摘要。
2. 研究/政策问题。
3. 范围界定：地区、行业、时间、对象。
4. 数据和来源说明。
5. 关键事实。
6. 分析框架或逻辑链条。
7. 分主题分析。
8. 政策/产业含义。
9. 风险、不确定性和替代解释。
10. 建议或情景分析。
11. 来源表和附录。

---

## 证据登记表

重要数字应进入 source register：

```text
claim | value | unit | geography | period | source | publication/access date | link/file | caveat
```

示例：

```text
新能源汽车销量增长 | 950万辆 | 辆 | 中国 | 2023年 | 中国汽车工业协会 | 2024-01 | URL | 统计口径为批发销量
```

---

## 文件结构

```text
econruc-report-writing/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence-to-claim.md
│   ├── policy-consulting-style.md
│   ├── report-architecture.md
│   └── source-and-data-audit.md
└── scripts/
    └── make_source_register.py
```

---

## 维护建议

- 报告结构和模板放入 `references/report-architecture.md`。
- 数据和来源审计规则放入 `references/source-and-data-audit.md`。
- 政策/咨询报告语言风格放入 `references/policy-consulting-style.md`。
- 证据如何转成 claim 的规则放入 `references/evidence-to-claim.md`。
- 来源登记表模板维护在 `scripts/make_source_register.py`。

## English Overview

`econruc-report-writing` drafts, structures, audits, and polishes evidence-based policy reports, industry research reports, consulting-style reports, market studies, and briefing memos. It prioritizes verified data, clear source attribution, logical structure, defensible claims, and explicit uncertainty.

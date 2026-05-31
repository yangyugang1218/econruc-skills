# econruc-data skill

## 中文说明

`econruc-data` 是 EconRUC 套件的数据层 skill，用于经济学数据检索、清洗、合并、审计、变量字典和可复现数据管线。它通常先于 `econruc-figure` 和 `econruc-empirical` 使用。

这个 skill 的核心不是“找到一个数”，而是让数据来源、口径、处理过程和最终分析样本都可追溯、可解释、可复现。

---

## 适用场景

- 中国统计年鉴、城市/省份面板、企业数据、海关、专利、能源、金融、财政、污染、人口数据。
- 数据来源梳理和下载方案。
- 原始数据到 analysis-ready data 的清洗流程。
- 变量字典、单位换算、deflator、口径说明。
- 合并规则、缺失值规则、样本限制和 audit trail。
- 为论文图表、实证分析和 replication package 准备数据。

---

## 中文模式

中文模式面向中国经济学数据和中文研究文档。

重点：

- 说明统计口径、行政层级、年份变化和制度背景。
- 中文变量名、英文变量名、单位、来源表格要对应。
- 注意年鉴、政府网站、数据库下载时间和版本。
- 对中文报告和论文附录，输出应能直接转成数据说明。

---

## English mode

English mode targets replication packages, international journal appendices, data memos, and reproducible empirical pipelines.

Priorities:

- Provenance and versioning.
- Raw/intermediate/final data separation.
- Variable definitions and transformations.
- Sample construction and merge audit.
- Reproducible scripts and README-ready documentation.

---

## 数据工作流

1. Data contract：研究问题、观察单位、时间范围、地理层级、变量、目标输出。
2. Source map：列出数据来源、下载路径、版本、权限和限制。
3. Raw preservation：保留原始文件，不在 raw 上直接修改。
4. Cleaning log：记录单位换算、缺失值、异常值、重复值、编码标准化。
5. Merge audit：检查匹配率、未匹配项、重复 key 和样本损失。
6. Variable dictionary：输出变量名、标签、单位、来源、处理公式。
7. Analysis-ready export：为图表或回归输出 tidy/panel 数据。

---

## 推荐目录结构

```text
data_project/
├── data_raw/
├── data_intermediate/
├── data_final/
├── scripts/
│   ├── 01_import.*
│   ├── 02_clean.*
│   ├── 03_merge.*
│   └── 04_build_analysis.*
├── docs/
│   ├── data_dictionary.csv
│   └── data_audit.md
└── outputs/
```

---

## 文件结构

```text
econruc-data/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── cleaning-audit-checklist.md
│   ├── data-source-map.md
│   └── reproducible-pipeline.md
└── scripts/
    └── make_data_dictionary.py
```

---

## 维护建议

- 新数据源放入 `references/data-source-map.md`。
- 清洗、合并和审计规则放入 `references/cleaning-audit-checklist.md`。
- 可复现工程结构放入 `references/reproducible-pipeline.md`。
- 自动生成变量字典的逻辑维护在 `scripts/make_data_dictionary.py`。

## English Overview

`econruc-data` supports economics data discovery, cleaning, merging, auditing, documentation, and reproducible pipeline construction. It is the data layer that prepares trustworthy datasets for `econruc-figure`, `econruc-empirical`, and paper writing.

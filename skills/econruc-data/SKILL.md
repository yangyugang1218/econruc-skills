---
name: econruc-data
description: Find, retrieve, clean, merge, audit, document, and prepare economics datasets for empirical research, policy reports, replication packages, and figures. Use when the user asks for data sources, data retrieval plans, Chinese statistical data, macro/firm/city/household/patent/trade/energy/finance data, panel construction, variable dictionaries, data cleaning, Stata/R/Python pipelines, replication data, or preparing tidy source data for econruc-figure.
---

# EconRUC Data

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English data workflows as different documentation styles, not direct translations.

### 中文模式

- 面向中国经济学数据、统计年鉴、政府公开数据、企业数据库、博士论文数据附录和中文报告。
- 强调数据口径、行政层级、统计制度、变量中文名、单位换算、缺失值规则和可追溯来源。
- 输出应适合后续写入中文论文、项目说明、数据说明书或 Stata/R/Python 清洗日志。

### English mode

- Target replication packages, international journal appendices, data availability statements, and research memos.
- Emphasize provenance, variable definitions, sample construction, versioning, reproducible scripts, and audit trails.
- Use concise technical English suitable for README files, codebooks, and empirical appendices.

When maintaining this skill, keep Chinese data-source conventions and English replication-package conventions separate.

Use this skill for the data layer of economics research. It stops before final visualization unless the task is only to prepare source data for `econruc-figure`.

## Relation to other skills

- Use `econruc-data` for data discovery, extraction, cleaning, merging, variable definitions, panel construction, audit trails, and replication packages.
- Use `econruc-figure` after the data are tidy and the user wants a chart, figure, or visual QA.
- Use `econruc-empirical` when the question is about identification, estimator choice, or robustness logic.

## Core stance

- Preserve provenance: every variable needs a source, transformation, unit, and date/version.
- Keep raw, intermediate, and analysis-ready data separate.
- Do not silently change units, deflators, sample restrictions, or missing-value rules.
- For web/current data, verify source pages and dates when the user needs up-to-date values.
- Prefer reproducible scripts over manual spreadsheet edits.

## Data contract

Before cleaning or merging, define the unit of observation, time frequency, geography, key identifiers, variable units, source authority, and intended downstream use. If the downstream task is a figure or empirical design, prepare data in the shape that task needs rather than making a generic spreadsheet.

Keep a visible audit trail: source file, raw row count, cleaned row count, merge keys, merge rate, dropped observations, and all unit or price adjustments.

## Workflow

1. Define research need: unit, geography, period, frequency, variables, and outcome/treatment.
2. Identify candidate sources and rank by authority, coverage, update frequency, and reproducibility.
3. Build a data plan before downloading or cleaning.
4. Create a raw-data inventory and variable dictionary.
5. Clean with explicit rules: missingness, duplicates, units, deflation, winsorization, geocodes, IDs, merges.
6. Run audit checks: row counts, unique keys, ranges, balance, missingness, merge rates.
7. Save tidy source data for tables/figures and document caveats.

## QA and red lines

- Never overwrite raw data; create separate cleaned or analysis-ready outputs.
- Do not infer missing units, base years, geocodes, or variable definitions without marking the assumption.
- Check duplicate keys, impossible values, missingness, balance over time, and merge failures before delivery.
- For current or policy-sensitive data, report the access date and source version when available.

## Output format

Default:

1. `Data plan:` sources, variables, unit, frequency, period.
2. `Pipeline:` raw -> intermediate -> analysis-ready steps.
3. `Variable dictionary:` name, label, unit, source, transformation.
4. `Audit checks:` checks run or recommended.
5. `Caveats:` coverage, revisions, comparability, missingness.
6. `Next step:` whether to hand off to `econruc-figure` or `econruc-empirical`.

## When to open extra files

| File | Open when |
|---|---|
| [references/data-source-map.md](references/data-source-map.md) | Need economics data sources, Chinese data categories, or source-selection guidance |
| [references/cleaning-audit-checklist.md](references/cleaning-audit-checklist.md) | Need cleaning, merging, panel construction, variable dictionary, or QA checks |
| [references/reproducible-pipeline.md](references/reproducible-pipeline.md) | Need Stata/R/Python folder structure, replication package, or code organization |

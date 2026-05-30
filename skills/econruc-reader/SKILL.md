---
name: econruc-reader
description: Read, summarize, dissect, or produce structured notes for economics papers, working papers, journal articles, referee reports, NBER/CEPR/SSRN papers, Chinese economics papers, and PDF manuscripts. Use when the user asks to read a paper, extract research question, contribution, identification, model, data, results, mechanisms, robustness, limitations, seminar questions, replication notes, or convert a paper into reading notes, referee-style critique, presentation outline, or literature positioning.
---

# EconRUC Paper Reader

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English reading notes as different products.

### 中文模式

- 面向组会读书报告、博士生日常阅读、中文文献笔记、论文选题和导师讨论。
- 解释要更注重“这篇文章为什么重要、怎么识别、结果能不能信、我能怎么借鉴”。
- 可以把英文论文逻辑转换成中文经济学表达，但不要逐句翻译摘要。

### English mode

- Target seminar memos, referee-style critiques, literature-positioning notes, and replication planning.
- Emphasize research question, contribution, design/model, evidence, threats, mechanisms, and how the paper changes a literature.
- Use concise analytical English rather than summary-only prose.

When maintaining this skill, keep Chinese reading-note templates and English seminar/referee-note templates separate.

Use this skill to read economics papers like a researcher preparing for a seminar, replication, literature review, or paper development meeting.

## Core stance

- Read for the economic argument, not only for summary.
- Separate what the paper claims, what the design/model identifies, and what the evidence actually supports.
- Do not invent citations, results, sample details, or robustness checks.
- Treat formulas, tables, and figures as evidence objects that must be mapped back to the paper's central question.
- For Chinese papers, translate the logic into international economics language when useful.

## Reading contract

Before producing notes, identify whether the user wants quick summary, deep critique, replication planning, seminar preparation, or literature positioning. Keep source-grounded facts separate from your interpretation and critique.

When reading from partial materials such as abstracts, screenshots, slides, or notes, label the output as partial and avoid inferring full-paper details that are not present.

## Intake

Identify:

- source type: PDF, LaTeX, Word, abstract, slides, notes, or pasted text
- reading goal: quick summary, deep critique, seminar preparation, replication planning, literature review, referee-style report, or slide conversion
- field and method: reduced-form, structural, theory, RCT, DiD, IV, RD, SCM, macro, finance, IO, public, labor, development, or other
- output language: English, Chinese, or bilingual

## Reading workflow

1. Extract bibliographic facts: title, authors, year/version, venue if available.
2. Identify the one-sentence research question.
3. Identify the one-sentence answer.
4. Map contribution by type: question, setting, data, identification, model, mechanism, policy, or measurement.
5. Extract data, sample, variables, treatment/shock, unit of observation, and time period.
6. Explain identification or model logic in plain language.
7. Map main tables/figures to claims.
8. Identify mechanisms, heterogeneity, robustness, and limitations.
9. Produce questions a good seminar participant or referee would ask.
10. If requested, convert the reading into a Beamer slide map using `econruc-beamer`.

## QA and red lines

- Do not attribute claims, results, or methods to the paper unless they appear in the supplied source.
- Distinguish `paper claims`, `evidence supports`, and `reader concern`.
- For tables and figures, report units, samples, baseline categories, and uncertainty when available.
- If the source is incomplete, list what cannot be assessed: identification, sample construction, robustness, mechanisms, or external validity.

## Output formats

Default structured note:

1. `Citation snapshot`
2. `One-sentence summary`
3. `Research question and answer`
4. `Contribution map`
5. `Data and design/model`
6. `Main results`
7. `Mechanisms and robustness`
8. `Limitations and threats`
9. `Seminar questions`
10. `How I would use this paper`

For quick reading, return only the first six sections. For deep reading, include table/figure map and replication checklist.

## When to open extra files

| File | Open when |
|---|---|
| [references/reading-note-template.md](references/reading-note-template.md) | Need a reusable structured note, seminar note, or bilingual paper memo |
| [references/table-figure-reading.md](references/table-figure-reading.md) | Need to read regression tables, figures, event studies, or model result panels |
| [references/critique-and-questions.md](references/critique-and-questions.md) | Need referee-style critique, seminar questions, limitations, or improvement suggestions |

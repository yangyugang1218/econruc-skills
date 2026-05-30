---
name: econruc-literature
description: Build, revise, or audit economics literature reviews, contribution positioning, related-work sections, citation narratives, field maps, and Top5/field-journal framing. Use when the user asks how to position a paper, compare with AER/QJE/Econometrica/JPE/REStud or economics field-journal literatures, write related work, identify contribution gaps, organize Chinese or English notes on prior studies, or convert a paper-by-paper list into economics-style synthesis.
---

# EconRUC Literature Positioning

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English literature positioning as different scholarly genres.

### 中文模式

- 面向中文论文、博士论文文献综述、课题申请和中文期刊定位。
- 组织方式可更重视研究脉络、制度背景、中国问题、政策相关性和国内外文献对话。
- 避免简单罗列作者；要说明一组文献解决了什么、还留下什么、本文为什么能推进。

### English mode

- Target Top5/field-journal related-work and contribution positioning.
- Organize literatures by economic question, mechanism, identification, data, and what the paper adds.
- Use compact literature paragraphs that position the paper without becoming an annotated bibliography.

When maintaining this skill, keep Chinese literature-review conventions and English contribution-positioning conventions separate.

Use this skill to position an economics paper in literatures without turning related work into an annotated bibliography.

## Core stance

- Literature review is an argument about contribution, not a list of famous papers.
- Organize by economic question, identification strategy, data/measurement, mechanism, and policy margin.
- Do not invent citations. If exact references are needed and not provided, ask for the user's bibliography or search only when explicitly requested.
- Avoid claiming a gap because no one has studied the exact same setting. Explain why this setting identifies a broader question or tests a mechanism differently.

## Positioning contract

Before drafting related work, state the user's paper question, claimed contribution, target field, and the citation evidence actually supplied. Separate verified citations from candidate literatures that still need checking.

Contribution positioning should answer: what does prior work establish, what remains unresolved, and why this paper's data/design/model moves the broader question forward.

## Workflow

1. Identify the paper's central economic question.
2. Split prior work into 2-4 literatures.
3. For each literature, write what it has established and what remains unresolved.
4. Connect the user's paper to each literature by contribution type:
   data, setting, identification, mechanism, theory, external validity, policy margin, measurement, or welfare.
5. Draft synthesis paragraphs that compare arguments, not papers one by one.
6. Provide Chinese and English versions when useful.

## QA and red lines

- Do not invent paper titles, authors, dates, journals, or findings.
- Do not say `first`, `fills the gap`, or `few studies` unless the citation base supports it.
- Mark citation needs explicitly when the user has not provided exact references.
- Avoid paper-by-paper summaries unless the user asks for annotated bibliography notes.

## Contribution grammar

Strong:

- `This paper contributes to the literature on [question] by providing [design/data/mechanism] evidence on [margin].`
- `Relative to studies that identify [effect] using [setting], our setting isolates [source of variation].`
- `The results speak to models in which [mechanism] rather than only documenting [reduced-form pattern].`

Weak:

- `There is little research on China/this city/this policy.`
- `This paper fills the gap.`
- `Few scholars have examined this issue from this perspective.`

## Output format

Default:

1. `Literature map:` 2-4 literatures with question, established facts, unresolved margin.
2. `Contribution statement:` English and/or Chinese.
3. `Related-work draft:` synthesis paragraphs.
4. `Citation needs:` where exact citations are missing or need verification.
5. `Overclaim check:` contribution claims to soften.

## When to open extra files

| File | Open when |
|---|---|
| [references/literature-positioning.md](references/literature-positioning.md) | Need literature map, contribution statement, or related-work structure |
| [references/top5-field-map.md](references/top5-field-map.md) | Need field-specific positioning patterns and journal-style framing |

---
name: econ-intro
description: Draft, diagnose, restructure, or polish economics paper introductions in English or Chinese, with Top5 economics, leading field-journal, and Chinese top-journal conventions. Use when the user asks for an introduction, opening section, research motivation, contribution paragraph, paper framing, puzzle-to-design narrative, or bilingual Chinese-English intro for an economics paper, working paper, policy paper, dissertation chapter, or grant-style research proposal.
---

# Econ Introduction

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English as two different writing modes, not mirror translations.

### 中文模式

- 面向中文论文、博士论文、基金申请、组会汇报或中文顶刊风格。
- 引言要突出问题意识、制度背景、现实约束、政策含义和研究设计的可信度。
- 语言应克制、清楚、有学术判断，避免口号化和政策宣传式表述。

### English mode

- Target Top5-style, field-journal, working-paper, or seminar-facing introductions.
- Lead with the economic question, friction, identification challenge, main result, and contribution.
- Use concise journal prose: precise, active, modest, and contribution-forward.

When maintaining this skill, update the Chinese and English modes separately. Do not assume an English sentence can be translated into a good Chinese introduction, or vice versa.

Use this skill to turn research notes into a credible economics introduction. The output should make the economic question, identification problem, empirical design, main finding, and contribution legible before it tries to sound elegant.

## Core stance

- Write the introduction as an argument, not background exposition.
- Lead with the economic object: welfare, incentives, allocation, distribution, productivity, market power, risk, human capital, public finance, political economy, or another discipline-relevant margin.
- Do not invent facts, coefficients, institutional details, sample sizes, citations, mechanisms, or robustness checks.
- Calibrate causal language to the design. Use `estimate`, `document`, `provide evidence`, and `are consistent with` unless the design warrants stronger claims.
- Treat English and Chinese as different journal languages. English should be concise and contribution-forward; Chinese should preserve institutional clarity, problem consciousness, and policy relevance without becoming slogan-like.
- Make every paragraph answer one reader question: Why should I care? What is unknown? Why is it hard? What do they do? What do they find? What do we learn?

## Intake

Before drafting, identify:

- research question and field
- economic stakes and unresolved puzzle
- setting, data, sample, period, unit of observation, and key institutional variation
- identification strategy and identifying assumption
- main results with magnitude and benchmark, if available
- mechanism, heterogeneity, welfare, or policy interpretation
- target outlet or style: Top5, field journal, Chinese top journal, working paper, dissertation, policy report, or bilingual draft
- citation anchors or literatures the user wants to position against

If key inputs are missing, still provide a scaffold, but mark placeholders explicitly.

## Workflow

1. Write a one-sentence introduction thesis:
   `This paper studies [economic question] in [setting] using [data/variation/design], finds [main result], and contributes by [what we learn that prior work could not show].`
2. Choose the architecture from `references/intro-architecture.md`.
3. Build a paragraph plan before drafting. Do not start with literature review unless the target is explicitly a Chinese-style institutional or policy introduction.
4. Draft the first version in the target language. For bilingual requests, write English first for journal logic, then provide a Chinese version that preserves the economics rather than translating sentence by sentence.
5. Add a contribution map with separate substantive, identification/data, and literature contributions.
6. Diagnose risks with `references/intro-diagnostics.md`.

## Output Defaults

For drafting requests, return:

1. `Introduction draft` in the requested language.
2. `Paragraph logic` explaining the role of each paragraph.
3. `Contribution map` with `Claim | Literature relation | Evidence/design | Risk`.
4. `Missing inputs` for facts or evidence that should not be invented.
5. `Next revision moves` with 3-6 concrete edits.

For polishing requests, return:

1. revised introduction
2. short diagnosis of major structural changes
3. optional sentence-level notes only when they matter

## When To Open Extra Files

| File | Open when |
|---|---|
| [references/intro-architecture.md](references/intro-architecture.md) | Need paragraph architecture for English Top5, field-journal, Chinese top-journal, or bilingual introductions |
| [references/contribution-language.md](references/contribution-language.md) | Need contribution paragraphs, bilingual phrasebank, or literature-positioning language |
| [references/intro-diagnostics.md](references/intro-diagnostics.md) | Need to audit a draft introduction, diagnose weak framing, or produce a revision checklist |

---
name: econruc-writing
description: Draft, restructure, or plan economics papers, policy reports, working papers, abstracts, introductions, results sections, discussions, titles, and bilingual Chinese-English research prose in a Top5 economics and field-journal style. Use when the user provides economics research notes, Chinese drafts, regression results, identification ideas, figures, tables, referee constraints, or wants English and Chinese versions of economics academic writing rather than sentence-level polishing only.
---

# EconRUC Economics Writing

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English writing as two independent drafting systems.

### 中文模式

- 面向中文论文、博士论文、项目申请、中文报告、组会材料和作者内部讨论。
- 强调问题意识、制度背景、研究设计、政策含义和对中国经济语境的准确表达。
- 语言要自然、严谨、克制，不把英文 Top5 句式机械翻译成中文。

### English mode

- Target Top5/field-journal papers, working papers, abstracts, result sections, and international seminar materials.
- Use economics journal logic: question, friction, design/model, magnitude, mechanism, contribution, and boundary.
- Keep prose concise, active, evidence-calibrated, and contribution-forward.

When maintaining this skill, update Chinese research-writing templates and English journal-writing templates separately.

Use this skill to build economics writing from the argument outward. It is for drafting and restructuring, not merely polishing finished sentences.

## Core stance

- Put identification and economic mechanism before elegant language.
- Do not invent data, institutional facts, theoretical claims, references, sample definitions, coefficients, standard errors, or robustness results.
- Use Top5 economics style as discipline logic, not imitation: precise research question, credible identification, modest but sharp contribution, transparent threats, and clear welfare or mechanism relevance.
- Treat Chinese and English as two writing systems. English should be journal-facing; Chinese should preserve the research logic for seminars, reports, grants, or author collaboration.
- Prefer bounded verbs: `estimate`, `show`, `document`, `provide evidence`, `suggest`, `are consistent with`, `rule out`, `cannot rule out`.
- Keep causal language conditional on design. Reserve `causes` for credible randomized, quasi-experimental, or structural identification with stated assumptions.

## Task contract

Before drafting substantial text, establish a compact contract: target section, audience, core claim, evidence supplied, identification status, and forbidden inventions. If the user only provides fragments, write a scaffold with explicit placeholders rather than filling empirical or institutional gaps.

Treat every paragraph as a claim-evidence unit. A paragraph should not merely sound polished; it should state a claim, name the evidence or design behind it, and show the boundary of interpretation.

## Intake

Before drafting, identify:

- field: labor, development, public, IO, finance, macro, urban, health, education, environmental, political economy, trade, economic history, econometrics, theory, or applied micro
- paper type: reduced-form causal, descriptive measurement, structural, theory, model-plus-evidence, policy evaluation, or report
- core question: who, what margin, what shock/policy/incentive, and why economists should care
- empirical design: data, sample, variation, comparison group, identifying assumption, unit of observation, outcome, and estimator
- main result: sign, magnitude, benchmark, standard error or confidence interval, and interpretation
- contribution: substantive, methodological, data, institutional, or policy contribution
- target: Top5, field journal, working paper, policy report, grant, seminar slides, Chinese report, or bilingual output

If `core question`, `identification`, or `main result` is missing, expose the gap. You may still draft a scaffold with explicit placeholders.

## Writing workflow

1. Write the one-sentence paper argument:
   `This paper studies [question] using [setting/data/variation], showing [main result], with evidence on [mechanism/heterogeneity], and the interpretation is bounded by [assumption/limitation].`
2. Choose the document type and section architecture from `references/top5-article-architecture.md`.
3. Build a claim-evidence map before drafting paragraphs.
4. Put the reader's sequence in order: question, setting, design, finding, mechanism, contribution, boundary.
5. Draft in English when the target is a journal or working paper. Provide Chinese logic notes when the source is Chinese or the user asks for bilingual output.
6. For Chinese deliverables, use precise economics Chinese: `识别策略`, `反事实`, `边际效应`, `机制检验`, `异质性`, `稳健性`, `外部有效性`.
7. Calibrate claims against the design. Never convert correlation, prediction, or description into causal language.
8. End with assumptions, missing inputs, and a revision checklist.

## QA and red lines

- Check that every coefficient, sample fact, institutional detail, citation, and robustness result appears in the user's materials or is marked as a placeholder.
- Mark unsupported causal language and replace it with design-calibrated language.
- Keep contribution claims specific: contribution to a question, design, data, mechanism, setting, or measurement, not generic novelty.
- If the requested draft would require facts not supplied, state the missing inputs and proceed only with bracketed placeholders.

## Section defaults

### Abstract

Use:

`question -> setting/data -> identification -> main result magnitude -> mechanism/robustness -> contribution/boundary`

Avoid generic openings such as `This paper is important because...`. Start from the economic question or empirical puzzle.

### Introduction

Use the economics funnel:

`economic stakes -> unresolved question -> why existing evidence is limited -> setting/data/design -> findings -> contribution map`

The final contribution paragraph should separate:

- substantive contribution
- identification or data contribution
- relation to named literatures

### Results

Use:

`estimating equation/design reminder -> coefficient/result -> magnitude in economic units -> inference -> interpretation -> threat or next test`

Do not write tables figure-by-figure. Each paragraph needs one economic message.

### Mechanism and heterogeneity

Mechanism language should distinguish:

- mechanism evidence: supports a channel but may not prove it
- heterogeneity: where effects are larger or smaller
- mediation: only when the design justifies it
- decomposition: accounting relationship unless causally identified

### Discussion and conclusion

Use:

`central finding -> interpretation -> relation to literature -> policy or welfare implication -> external validity -> remaining uncertainty`

## Output format

Default:

1. `English draft:` polished journal-facing text.
2. `中文逻辑说明:` concise explanation of structure, claims, and economics terminology.
3. `Claim-evidence map:` `Claim | Evidence | Identification status | Risk`.
4. `Missing inputs:` only material gaps.
5. `Next revision moves:` 3-6 concrete edits.

For Chinese-only requests, provide `中文正文` first and then `English positioning notes` if useful.

## When to open extra files

| File | Open when |
|---|---|
| [references/top5-article-architecture.md](references/top5-article-architecture.md) | Need section structure for abstracts, introductions, results, discussions, titles, or contribution framing |
| [references/bilingual-workflow.md](references/bilingual-workflow.md) | Source is Chinese, mixed Chinese-English, or user asks for bilingual academic prose |
| [references/section-patterns.md](references/section-patterns.md) | Need concrete paragraph templates for economics sections |

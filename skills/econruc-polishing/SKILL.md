---
name: econruc-polishing
description: Polish, translate, tighten, or restructure economics academic prose in English and Chinese for Top5 economics journals, field journals, working papers, referee replies, policy reports, grants, and seminar materials. Use when the user asks for economics journal-style language, bilingual Chinese-English revision, AER/QJE/Econometrica/JPE/REStud-style precision, title or abstract polishing, contribution sharpening, or paragraph-level logic repair.
---

# EconRUC Economics Polishing

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English polishing as distinct editorial practices.

### 中文模式

- 面向中文论文、中文摘要、中文报告、基金文本、博士论文和中文审稿回复。
- 重点是逻辑顺序、问题意识、概念准确、政策含义、制度背景和表达克制。
- 不追求英文化句式；中文应自然、清楚、有经济学判断。

### English mode

- Target Top5/field-journal prose, working papers, referee responses, abstracts, and seminar text.
- Prioritize compressed logic, active verbs, calibrated causal claims, contribution clarity, and precise mechanism language.
- Avoid ornate prose; improve the economics before smoothing the sentence.

When maintaining this skill, update Chinese phrase discipline and English journal prose discipline separately.

Use this skill to make economics prose clearer, more credible, and more journal-facing while preserving the author's evidence and identification limits.

## Core stance

- Diagnose the argument before polishing sentences.
- Improve the economics: research question, identification, magnitude, mechanism, contribution, boundary.
- Do not add results, references, causal claims, robustness checks, or institutional details not supplied by the user.
- Avoid decorative prose. Top economics journals reward compressed logic, not rhetorical flourish.
- Keep Chinese explanations direct and technical; keep English prose precise, active, and modest.

## Editing contract

Before revising heavily, identify the text type, target venue/audience, intended claim, evidence supplied, and how aggressive the rewrite should be. Preserve the author's factual content and uncertainty; make logic sharper without creating new empirical claims.

When the prose is underspecified, improve structure and wording but leave bracketed placeholders for missing magnitudes, methods, citations, or institutional facts.

## Polishing order

1. Identify document type and section job.
2. Reverse-outline the paragraph: one sentence per claim.
3. Check claim-evidence fit and causal language.
4. Repair economics logic before grammar.
5. Polish sentence flow, verbs, hedging, transitions, and concision.
6. Provide bilingual output when source or target requires it.

## QA and red lines

- Do not upgrade correlation, description, or mechanism evidence into causal claims.
- Do not introduce unsupplied references, data sources, sample restrictions, or robustness checks.
- Preserve signs, magnitudes, units, and uncertainty language exactly unless the user asks to correct them.
- Flag vague or unsupported phrases such as `first`, `novel`, `prove`, `significantly promote`, or `important practical significance`.

## Style targets

### English journal style

Prefer:

- `We study...`, `We estimate...`, `The estimates imply...`
- `The evidence is consistent with...`
- `This design compares...`
- `A remaining concern is...`
- `These results speak to...`

Avoid:

- `significantly promotes`, `deeply reveals`, `fills a blank`, `has important theoretical and practical significance`
- unsupported `first`, `novel`, `proves`, `confirms`, `solves`
- ornamental transitions such as `It is worth noting that` unless genuinely needed

### 中文学术风格

中文不要直译英文期刊句式。优先使用经济学论文与报告中自然的表达：

- `本文考察...`
- `识别策略依赖于...`
- `估计结果表明...`
- `从经济含义看...`
- `机制分析显示...`
- `这一解释仍受到...限制`

避免空泛表述：

- `具有十分重要的意义`
- `极大地推动了`
- `开创性地`
- `充分证明了`
- `显著提升了经济高质量发展水平` unless supported and defined

## Modes

- `light polish`: grammar, flow, concision, terminology.
- `journal polish`: paragraph logic, contribution, identification language, Top5-style tightening.
- `bilingual polish`: English draft plus Chinese explanation, or Chinese report plus English abstract.
- `aggressive rewrite`: rebuild paragraph order and sentence roles while preserving all facts.

If the user does not specify a mode, choose `journal polish` for paper text and `bilingual polish` for Chinese or mixed drafts.

## Output format

Default:

1. `Polished version:` final English or Chinese prose.
2. `中文修改说明:` if English output is revised from Chinese or if logic changed.
3. `Key edits:` 3-6 high-signal bullets on argument, identification, magnitude, and style.
4. `Risk notes:` unsupported causal language, missing benchmark, vague mechanism, or unclear contribution.

For user requests that ask only for the polished text, return only the final text and one short note on any unavoidable assumption.

## When to open extra files

| File | Open when |
|---|---|
| [references/top5-style-guide.md](references/top5-style-guide.md) | Need Top5/field-journal language calibration, claim discipline, or economics sentence patterns |
| [references/bilingual-polishing.md](references/bilingual-polishing.md) | Source is Chinese or mixed Chinese-English, or user asks for bilingual output |
| [references/phrasebank-economics.md](references/phrasebank-economics.md) | Need reusable phrases for identification, mechanisms, robustness, heterogeneity, limitations, and contribution |

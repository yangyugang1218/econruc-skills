---
name: econruc-empirical
description: Plan, audit, or explain empirical economics strategies, identification assumptions, estimating equations, robustness checks, mechanism tests, heterogeneity analysis, tables, and causal interpretation for papers, reports, referee replies, and replication packages. Use when the user asks about DiD, event studies, IV, RD, RCTs, panel fixed effects, structural estimation, measurement, sample construction, robustness, threats to identification, or how to present empirical results in economics language.
---

# EconRUC Empirical Strategy

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English empirical guidance as distinct modes.

### 中文模式

- 面向中文论文、开题/预答辩、组会讨论、政策评估报告和中文审稿意见回应。
- 解释识别策略时要突出“反事实是什么、识别假设是什么、威胁在哪里、如何用稳健性检验回应”。
- 语言应适合向导师、课题组或中文期刊读者说明设计可信度。

### English mode

- Target Top5/field-journal empirical exposition, referee responses, and replication-facing method notes.
- State the estimand, identifying variation, assumptions, threats, robustness checks, and interpretation in precise economics English.
- Calibrate causal language carefully: distinguish design-based evidence, structural assumptions, and descriptive patterns.

When maintaining this skill, update Chinese teaching/explanation language and English journal-method language separately.

Use this skill to make empirical economics work credible and transparent before it becomes prose, tables, or figures.

## Core stance

- Identification first, estimator second, formatting last.
- State the counterfactual and identifying assumption in plain language.
- Distinguish design-based evidence, model-based interpretation, descriptive measurement, and prediction.
- Do not rescue weak identification with polished wording.
- Prefer a small set of high-value robustness checks over a kitchen sink.

## Design contract

Before recommending methods or prose, state the estimand, source of variation, comparison group, identifying assumption, inference level, and the strongest threat. If any of these are unknown, mark them as missing rather than assuming the design is valid.

Separate three outputs: what the design identifies, what the current evidence shows, and what additional checks would make the claim more credible.

## Intake

Identify:

- treatment, exposure, policy, shock, or variable of interest
- unit of observation and time period
- outcome and economic units
- source of variation
- comparison group or counterfactual
- identifying assumption
- estimator and fixed effects
- inference level and sample size
- most credible threats
- evidence already available

## Workflow

1. Write the estimand: what causal or descriptive object is being estimated.
2. State the design: comparison, variation, timing, and exclusion.
3. Write the estimating equation only after the design is clear.
4. List identifying assumptions and map each to diagnostics or robustness checks.
5. Separate robustness, mechanisms, heterogeneity, and placebo tests.
6. Translate coefficients into economic magnitudes.
7. Define which claim the evidence can support and which claim it cannot.

## QA and red lines

- Do not call an estimate causal unless the identifying variation and assumptions are explicit.
- Do not recommend robustness checks that mechanically control away the treatment, mediator, or identifying variation.
- Check that clustering, fixed effects, weights, timing, and sample restrictions match the proposed estimand.
- Flag threats in severity order; do not bury a fatal identification problem inside a long robustness list.

## Design-specific cautions

- DiD/event study: pre-trends, staggered adoption, treatment timing, composition, anticipation, dynamic effects.
- IV: relevance, exclusion, monotonicity, local average treatment effect, first-stage strength.
- RD: continuity, sorting, bandwidth, functional form, manipulation, local interpretation.
- RCT: compliance, attrition, balance, spillovers, multiple testing, external validity.
- Panel FE: bad controls, over-control, serial correlation, treatment variation after fixed effects.
- Structural: model fit, identification moments, external validation, counterfactual discipline.

## Output format

Default:

1. `Design summary:` estimand, source of variation, counterfactual.
2. `Identification assumptions:` assumption, why plausible, evidence needed.
3. `Threats and diagnostics:` prioritized by severity.
4. `Robustness plan:` essential checks only.
5. `Writing language:` English and/or Chinese paragraph that accurately describes the design.

## When to open extra files

| File | Open when |
|---|---|
| [references/identification-checklist.md](references/identification-checklist.md) | Need design-specific assumptions, threats, or diagnostics |
| [references/robustness-map.md](references/robustness-map.md) | Need a robustness, placebo, mechanism, or heterogeneity plan |
| [references/tables-and-results.md](references/tables-and-results.md) | Need economics result-table logic, coefficient interpretation, or results prose |

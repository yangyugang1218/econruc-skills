# Robustness Map

## Categories

- `Specification`: controls, fixed effects, functional form, weights.
- `Sample`: alternative samples, trimming, balance restrictions, attrition.
- `Measurement`: alternative outcome/treatment definitions.
- `Inference`: clustering, wild bootstrap, randomization inference.
- `Placebo`: fake treatment date, fake outcome, untreated group.
- `Mechanism`: channel-specific outcomes or mediators.
- `Heterogeneity`: pre-specified groups and economically motivated margins.
- `External validity`: subgroups, settings, periods.

## Concrete examples

Specification:

- add unit and time fixed effects separately, then jointly
- replace linear trends with region-specific trends
- remove potentially bad controls
- compare weighted and unweighted estimates

Sample:

- drop never-treated or always-treated units when relevant
- exclude large cities, dominant firms, or crisis years
- trim extreme baseline outcomes
- require balanced panels and compare to unbalanced baseline

Measurement:

- use alternative outcome definitions
- redefine treatment timing or exposure intensity
- use log, level, and per-capita versions where meaningful
- test sensitivity to winsorization

Inference:

- cluster at treatment assignment level
- two-way cluster when shocks vary by unit and time
- wild bootstrap with few clusters
- randomization inference for policy rollouts or experiments

Placebo:

- fake treatment dates before implementation
- outcomes that should not respond
- groups not exposed to the policy
- permutation of treatment assignment

Mechanism:

- test channel-specific intermediate outcomes
- examine margins predicted by the model
- avoid conditioning on post-treatment variables unless explicitly interpreting mediation

Heterogeneity:

- pre-specify groups by baseline exposure or theory
- report interaction interpretation, not just subgroup significance
- avoid data-mined splits without correction or caution

## Prioritization

Essential checks address the design's main threat. Secondary checks show stability. Avoid long lists that do not correspond to a threat.

## Writing robustness

Use:

`The estimate is stable when we...`

`This check addresses the concern that...`

`The placebo estimate is small and statistically indistinguishable from zero, reducing concern that...`

Avoid:

`The results pass all robustness tests.`

`The conclusion is fully proven.`

## Mechanism vs robustness

Mechanism tests explain how an effect may arise. Robustness checks test whether the main estimate is sensitive to choices. Do not mix the two in one paragraph.

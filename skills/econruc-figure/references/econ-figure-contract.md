# Economics Figure Contract

Use before writing or revising plotting code.

## Contract fields

- `Claim`: one sentence the figure must support.
- `Mode`: paper, report, slide, or diagnostic.
- `Chart family`: event study, coefficient forest, binscatter, RD, time-series, distribution, map, decomposition.
- `Data fields`: x, y, group, estimate, standard error or CI, weights, units.
- `Design labels`: treatment timing, omitted category, threshold, fixed effects, controls, sample.
- `Uncertainty`: CI level, clustering, bootstrap, bandwidth, binning rule, or none.
- `Export`: PNG preview plus PDF/SVG for paper if possible.
- `Caption/note`: what the reader must know to interpret the figure.

## Claim examples

- `The policy reduced firm entry after implementation, with no visible pre-trend.`
- `The effect is concentrated among credit-constrained firms.`
- `The RD estimates are local to counties near the eligibility threshold.`
- `The treatment and comparison groups followed similar trends before the reform.`

## Figure note template

Paper:

`Notes: The figure reports [estimate/statistic] for [sample] over [period]. The omitted category is [category]. Bars/whiskers show [CI/SE]. The specification includes [fixed effects/controls]. Standard errors are clustered at [level].`

Report:

`Source: [data]. Notes: [definition, sample, uncertainty].`

## Red flags

- A causal title for a descriptive chart.
- Confidence intervals missing from estimate plots.
- Omitted event time not labeled.
- Binscatter without saying raw or residualized.
- RD plot without threshold and bandwidth.
- Map bins chosen only for aesthetics.

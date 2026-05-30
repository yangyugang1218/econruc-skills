# Identification Checklist

## Universal questions

- What is the estimand?
- What is the counterfactual?
- What source of variation identifies the effect?
- What assumptions make the comparison credible?
- What would violate those assumptions?
- What evidence can make the assumptions more plausible?
- What claim remains if the causal interpretation is weakened?

## DiD and event studies

Check:

- parallel trends or pre-trend diagnostics
- anticipation
- staggered adoption issues
- treatment effect heterogeneity
- composition changes
- differential shocks
- treatment timing definition

Language:

`The design compares changes in [treated] to changes in [comparison group], under the assumption that the two groups would have followed parallel trends absent [policy].`

## IV

Check:

- first-stage strength
- exclusion restriction
- monotonicity
- LATE population
- direct effects of instrument
- instrument-level clustering

Language:

`The IV estimate identifies a local effect for units whose [treatment] is shifted by [instrument].`

## RD

Check:

- running variable manipulation
- continuity of covariates
- bandwidth sensitivity
- polynomial order
- local nature of estimate

Language:

`The RD design compares units close to the threshold, so the estimate is local to [threshold population].`

## RCT

Check:

- randomization protocol
- balance
- attrition
- compliance
- spillovers
- multiple outcomes

## Structural

Check:

- model moments
- identification source
- fit
- external validation
- counterfactual assumptions

## Synthetic control and matrix completion

Check:

- donor pool definition
- pre-treatment fit
- predictor balance
- no treated-unit spillovers to donor units
- placebo-in-space tests
- placebo-in-time tests
- sensitivity to donor exclusions
- post-treatment extrapolation

Language:

`The synthetic control constructs a weighted combination of untreated units that matches the treated unit before the intervention. The credibility of the design depends on the quality of pre-treatment fit and the absence of shocks differentially affecting the treated unit after treatment.`

## Shift-share and Bartik IV

Check:

- shares are predetermined
- shocks are plausibly exogenous
- leave-one-out construction
- exposure concentration
- shock-level correlation
- industry/region-specific trends
- inference clustered at the appropriate exposure or shock level
- Rotemberg weights or influential shocks when relevant

Language:

`The shift-share design uses predetermined exposure shares interacted with aggregate shocks. The exclusion restriction requires that areas with different exposure would not have experienced differential outcome changes for reasons correlated with the shocks.`

## Bunching

Check:

- notch or kink location
- counterfactual density construction
- manipulation or reporting response
- excluded region around threshold
- bin width sensitivity
- extensive versus intensive margin interpretation
- optimization frictions

Language:

`The bunching estimate compares the observed density around the threshold with a smooth counterfactual density, so interpretation depends on the assumed counterfactual shape and the absence of unrelated discontinuities at the threshold.`

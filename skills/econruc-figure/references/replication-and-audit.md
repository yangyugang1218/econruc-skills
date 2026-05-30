# Replication and Audit

## Required audit questions

- What data file or regression output produced the figure?
- Are all transformations documented?
- Are weights, clusters, and fixed effects disclosed when relevant?
- Is the omitted category explicit?
- Does the figure use the same sample as the table it supports?
- Does the caption overstate causal interpretation?
- Can the figure be regenerated from code?

## Source data

For paper figures, keep a tidy source file with:

- panel or figure id
- variable names
- estimates
- standard errors or confidence interval bounds
- sample labels
- notes on controls or model

## Caption discipline

Figure notes should include interpretation-critical details only. Put long regression details in the appendix or table notes.

## Common fixes

- If CI labels are missing, compute `estimate +/- 1.96 * se` only when the CI level is 95 percent and normal approximation is appropriate.
- If estimates use log outcome, translate approximately to percent only when changes are small or use exact transformation.
- If the sample differs across panels, label it.

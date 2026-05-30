# Economics Chart Patterns

## Event study

Required:

- x-axis: relative time.
- y-axis: estimate and unit.
- omitted period: stated in the caption/response text; usually not printed inside the figure.
- vertical line at treatment timing.
- horizontal line at zero.
- confidence intervals.
- caption or surrounding text stating the omitted period, fixed effects, clustering, and controls when relevant.

Avoid connecting pre/post points if it implies continuous dynamics that the design does not support. Lines are acceptable for readability, but coefficients remain estimates by event time.

For paper figures, keep the plot itself clean:

- do not place `omitted baseline`, `reference period`, or long estimator notes on or below the x-axis
- do not add a long bottom footnote inside the exported graphic unless the figure must stand alone
- use a subtle vertical rule or light treatment-period shading instead of verbose treatment labels
- let the caption carry omitted-category and regression-specification details

Preferred high-end styles:

- **Modern journal**: points plus thin line; 95% CI as a translucent gray ribbon; zero line and treatment line are light; no in-figure title, legend, or notes for a single series.
- **Exact-interval paper style**: points plus slim capped error bars; muted pre/post colors only if the distinction matters; no baseline text on the axis.
- **Small multiples**: use when the data include quantiles, outcomes, subgroups, or mechanisms. Keep aligned axes and shared visual rules across panels.
- **Chinese journal / Stata-like matrix**: use faceted panels, muted pre/post colors, visible zero lines, and a shared legend outside the plot area. Keep panel borders light.

## Coefficient forest

Use for:

- multiple outcomes
- heterogeneous effects
- specification comparisons
- mechanism tests

Order estimates by conceptual groups, not coefficient size unless the ordering is the message.

High-end default:

- horizontal layout
- slim confidence intervals with small points
- zero line lighter than estimates
- one accent color for the main specification; gray for alternative specifications
- group separators or facets instead of heavy boxes
- no long notes inside the figure

## Binscatter

State whether the plot is:

- raw binned means
- residualized binned means
- weighted
- with controls or fixed effects

Do not use binscatter as causal evidence without design context.

High-end default:

- small binned means with a clean fitted line
- muted bins and slightly stronger fit line
- no oversized markers
- state residualization, controls, and binning in the caption/response
- use facets rather than many colors when comparing groups

## RD plot

Required:

- threshold line
- bandwidth
- binning rule
- local fit or binned means
- side-specific fits when appropriate

Caption should say the estimate is local to the threshold.

High-end default:

- binned means as points
- side-specific local fits
- threshold line visible but light
- confidence bands as subtle ribbons when shown
- do not extend fits beyond the displayed bandwidth unless needed

## Time series

Use:

- vertical rule for policy/reform.
- separate treated/control lines if DiD.
- shaded policy period if timing is an interval.
- annotate only major events.

High-end default:

- direct labels at endpoints for a small number of series
- sparse date ticks
- line-width hierarchy: focal series stronger, context series muted
- policy markers are thin rules or light bands
- use small multiples instead of dual axes when units differ

## Distribution

Use CDFs when comparing distributions. Use histograms or densities when shape matters. Avoid violin plots for audiences unfamiliar with them unless the paper/report context supports it.

High-end default:

- CDF for distributional comparisons
- density only when shape is the message and sample size supports it
- aligned bins/support across groups
- muted fills with stronger outlines
- weights, sample, and transformation stated outside the figure

## Maps

Maps show spatial patterns, not automatically causal effects. Use meaningful bins and a legend with units. Avoid red-green palettes.

High-end default:

- sequential palette for levels, diverging palette for estimates centered at zero
- thin borders and minimal labels
- economically meaningful bins
- compact legend with units
- no causal wording in the title/caption unless identified by the design

## Decomposition

Label accounting identity clearly. Do not call decomposition components mechanisms unless causally identified.

High-end default:

- waterfall or ordered contribution plot when components add to a total
- sign-consistent colors for positive and negative components
- label only large or substantively important components
- keep the accounting identity in the caption/response

## Heatmaps

Use for:

- cohort-by-event-time treatment effects
- region-by-year outcomes
- correlation or transition matrices
- policy intensity across geography/time

Rules:

- use meaningful diverging palette when values can be positive or negative
- center at zero for effect estimates
- label units and aggregation level
- avoid heatmaps when exact comparisons across many cells matter

High-end default:

- restrained diverging palette for positive/negative estimates
- compact colorbar
- minimal cell borders
- no cell text unless the matrix is small
- row/column order should follow time, theory, geography, or clustering

## Sankey and flow diagrams

Use for:

- trade flows
- migration flows
- energy balances
- budget or input-output flows

Rules:

- keep nodes few and grouped
- state whether values are levels or shares
- avoid implying causality from flow thickness
- use consistent color by source or destination, not both

High-end default:

- few nodes
- muted category colors
- direct labels for main totals
- avoid crossing flows
- state whether values are levels, shares, or changes in caption/response

## Lorenz curves and concentration

Use for:

- inequality, firm concentration, income/wealth distribution, market shares

Rules:

- include 45-degree equality line
- report Gini or concentration index if available
- specify weights and population
- avoid decorative filled regions unless they improve interpretation

High-end default:

- equality line lighter than Lorenz/concentration curve
- curve line clean and strong
- report Gini/concentration index in caption/response
- avoid excessive shading

## Waterfall charts

Use for decomposition of changes or contributions. Label baseline, increments, and final total. Do not use if components are not additive.

High-end default:

- clear start and end bars
- muted positive/negative component colors
- concise labels for the largest components
- no decorative gradients or 3D effects

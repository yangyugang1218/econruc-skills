# Advanced Economics Figure Style Playbook

Use this when the user asks for a figure to look more polished, advanced, journal-ready, or similar to a reference image.

## First principle

High-end economics figures usually look better because they make fewer visual claims:

- fewer text labels inside the plot
- one dominant visual channel for the estimate
- uncertainty shown transparently but quietly
- strong alignment across panels
- restrained color and careful whitespace
- notes moved to the caption or response text

Do not solve a weak figure by adding decoration. Improve structure, hierarchy, spacing, and the uncertainty encoding.

## Style profiles

### Modern journal general

Best for: most Top5, leading field-journal, and working-paper figures.

Visual grammar:

- no in-figure notes by default
- no title inside the figure when the figure will have a caption
- one primary accent color; gray handles uncertainty, secondary groups, and references
- direct labels only when they reduce legend work
- zero, threshold, and event lines are lighter than the data
- use whitespace and alignment rather than boxes and decoration

Recommended palette:

- primary estimate: deep blue `#1F5A85`
- secondary estimate: muted red `#9D3F46` or green `#4F7F5A`
- uncertainty: gray `#BFC5CD`
- reference lines: `#8A94A3`
- grid: `#EDF1F4`

Use this as the default profile when no other style is specified.

### Modern journal event-study

Best for: single or small-number event-study coefficient series, Top5/field-journal paper figures, seminar handouts.

Visual grammar:

- point estimates as small circles
- thin connected line when event time is ordered and the line helps trace dynamics
- 95% CI as a translucent gray ribbon when intervals are sequential and not too sparse
- alternatively use slim capped error bars when exact intervals matter
- zero line is dashed or thin solid gray
- treatment timing is a subtle dotted vertical rule
- no title inside the figure if it will have a caption
- no legend for a single series
- no in-figure `Notes:`

Recommended palette:

- estimate: deep muted blue `#1F5A85`
- CI ribbon: neutral gray `#BFC5CD` at alpha 0.30-0.45
- reference lines: `#8A94A3`
- grid: very light gray `#EDF1F4`

Use small multiples when the user provides groups, quantiles, cohorts, outcomes, or mechanisms. Keep identical x-limits and comparable y-limits unless the scale difference is the message.

### Reference-treatment square event-study

Best for: the default EconRUC event-study style, especially when the user wants the same look as the provided reference image.

Visual grammar:

- pre-treatment estimates use a muted blue-gray line and square markers
- post-treatment estimates use a muted wine-red line and square markers
- confidence intervals are semi-transparent vertical rectangles, not capped error bars
- the omitted/reference period, usually `-1`, is shown as a hollow square at zero
- draw a dashed horizontal zero line
- draw two understated vertical dashed rules: one at the reference period and one at treatment start, usually `0`
- add large but quiet top annotations such as `Reference (-1)` and `Treatment` only when they do not crowd the data
- use light horizontal gridlines only; avoid vertical gridlines, legends, titles, and notes inside the figure
- use large axis labels: `Event Time` on x-axis and `Estimated Effect` on y-axis for English figures
- keep y-axis ticks sparse and formatted with three decimals when effects are small

Recommended palette:

- pre CI fill: blue-gray `#D4DDE4` at alpha 0.85
- pre line/point: slate blue-gray `#71879A`
- post CI fill: pale rose `#EBD9DC` at alpha 0.85
- post line/point: wine red `#A64049`
- reference/hollow marker: `#8A94A3`
- zero/reference lines: `#8A94A3`
- grid: `#E8EEF3`

Default layout:

- figure aspect around 1.55-1.70 wide
- no in-figure title
- left and bottom spines visible; top/right spines hidden
- marker shape is square (`s`) with white edge
- CI rectangle width around `0.34` to `0.42` event-time units
- split the connected line at the reference gap: do not connect pre-period estimates through the omitted period into treatment estimates

Caption text should state the omitted period, confidence level, estimator, fixed effects, controls, clustering, sample, and data source.

### Chinese journal / Stata-like panel matrix

Best for: Chinese economics papers, heterogeneity matrices, appendix figures, treatment-before/after comparisons.

Visual grammar:

- faceted matrix with row and column labels
- pre-treatment and post-treatment differentiated by muted blue-gray and muted red
- confidence intervals can be vertical bars or translucent rectangles
- zero line is black or dark gray and visually consistent across panels
- shared legend outside the panels, often centered below
- light panel borders only when they help separate a dense matrix

Recommended palette:

- pre-treatment: `#9FB2C3`
- post-treatment: `#CFA6A9`
- pre point: `#1F5A85`
- post point: `#9D3F46`
- grid: `#E8F0F2`

Use this profile when the user references Stata-style Chinese figures or asks for `处理前/处理后`, multi-outcome panels, or heterogeneity by capacity, region, firm type, quantile, or industry.

### Report editorial

Best for: policy reports, consulting-style charts, leadership briefings.

Visual grammar:

- visible title and subtitle
- stronger contrast and direct labels
- one or two annotations allowed if they explain the substantive takeaway
- source note can appear inside the exported figure only if the figure must stand alone

Avoid applying report editorial styling to paper figures unless the user asks for a report chart.

## Chart-specific high-end grammar

### Coefficient forest / specification plot

Best for: robustness checks, heterogeneous effects, mechanisms, multiple outcomes.

Visual grammar:

- horizontal layout by default; labels read more cleanly than vertical rotated text
- group estimates by conceptual family, not by coefficient size unless ranking is the message
- show CI as thin horizontal intervals with points on top
- use a single zero line; keep it lighter than the data
- use subtle group separators or facet labels instead of heavy boxes
- sort only within meaningful blocks
- avoid legends when color is not encoding a real group

Good polish:

- left-aligned labels
- compact but readable row spacing
- one accent color for the preferred estimate; gray for alternatives
- text notes returned in the caption/response, not under the plot

### Binscatter

Best for: conditional relationships, residualized patterns, model-free visualization.

Visual grammar:

- binned means as small dots
- fitted line as a clean, slightly stronger line
- confidence band only if it clarifies uncertainty; otherwise keep it out
- raw and residualized versions should not share a figure unless the comparison is the point
- axis labels must state whether the variables are residualized

Good polish:

- use hollow or lightly filled dots for bins
- avoid large markers and heavy regression lines
- put controls, fixed effects, and binning method in caption text

### RD plot

Best for: threshold designs.

Visual grammar:

- threshold line is clear but not heavy
- side-specific fit lines with matching muted colors
- binned means as points, not bars
- confidence bands can be light ribbons around local fits
- bandwidth and polynomial/local-linear details belong in caption text

Good polish:

- keep both sides visually balanced
- do not extrapolate fitted lines far beyond the bandwidth
- avoid high-order polynomial aesthetics unless required by the design

### Time-series / policy plot

Best for: aggregate dynamics, treated-control comparisons, reform timing.

Visual grammar:

- one clear main line; secondary lines muted
- direct labels at line endpoints when there are few series
- sparse x-axis ticks; no every-year clutter
- policy marker as a thin vertical rule or light shaded interval
- avoid dual axes unless explicitly requested and necessary

Good polish:

- use line width hierarchy instead of many colors
- annotate at most one or two substantive moments
- for multiple related series, use small multiples with shared x-axis

### Distribution

Best for: inequality, treatment-effect distributions, outcome shifts, market shares.

Visual grammar:

- use CDFs for comparisons when exact distributional dominance matters
- use density only when shape matters and sample size is adequate
- use histograms with transparent fills sparingly; avoid decorative overlap
- use box/violin plots only when the audience expects them

Good polish:

- align support and binning across groups
- use muted fills and stronger outlines
- label units and weights in caption text

### Bar / dot comparison

Best for: category comparisons, shares, means, decomposition components.

Visual grammar:

- prefer dot plots or horizontal bars over vertical bars with rotated labels
- sort categories by conceptual order or magnitude
- avoid 3D, gradients, and heavy outlines
- use value labels only when they reduce lookup cost and do not crowd the chart

Good polish:

- one accent for the highlighted category
- gray for context categories
- keep zero baseline visible for bars

### Maps

Best for: spatial distribution, exposure, policy intensity, regional outcomes.

Visual grammar:

- choose bins with economic meaning, not arbitrary rainbow steps
- use sequential palette for levels and diverging palette for positive/negative estimates
- center diverging palettes at zero
- use thin boundaries and minimal labels
- include legend with units, but keep map notes outside the image when possible

Good polish:

- avoid red-green
- avoid implying causality with map titles
- consider small multiples for before/after maps

### Heatmap / matrix

Best for: cohort-event cells, transition matrices, correlation matrices, regional panels.

Visual grammar:

- center at zero for estimates
- use a restrained diverging palette
- keep cell borders minimal
- annotate cells only when the matrix is small
- order rows/columns by theory, time, geography, or clustering, not arbitrary input order

Good polish:

- keep colorbar compact
- use panel titles instead of crowded legends
- align labels and avoid rotated text when possible

### Decomposition / waterfall / stacked

Best for: additive contributions, accounting identities, shift-share decompositions.

Visual grammar:

- make the baseline, increments, and final total explicit
- use sign-consistent colors: positive and negative components should differ clearly
- avoid stacked bars when small components must be compared precisely
- do not call components mechanisms unless causally identified

Good polish:

- label only major components
- group small residual components as `Other` when justified
- use caption text for the accounting identity

### Sankey / flow

Best for: trade, migration, energy, input-output, fiscal flows.

Visual grammar:

- few nodes, grouped logically
- color by source or destination, not both
- width must represent levels or shares consistently
- avoid too many crossing flows

Good polish:

- use muted category colors
- label totals directly
- keep source definitions in the caption/response

## Event-study decisions

Choose uncertainty encoding:

- Use CI ribbon when event-time coefficients form a coherent dynamic path and the graph is meant to show shape.
- Use capped error bars when the reader needs exact interval endpoints or when event times are sparse.
- Use CI rectangles/bars in dense Stata-like panels.

Choose treatment marker:

- Single-series paper figure: subtle dotted vertical line, no text label.
- Report/slide: optional short label if ambiguity remains.
- Multi-panel figure: one consistent vertical rule across all panels.

Choose x-axis:

- Include the omitted event time as a tick only if needed for spacing, but do not print `omitted`.
- State omitted period in the caption/response.
- Do not add baseline labels directly on the axis.

Choose line connection:

- Connect points when the event-time dimension is naturally ordered and the line helps compare dynamics.
- Do not connect if the graph compares unrelated specifications or categorical estimates.

## Notes policy

Default:

- Do not embed notes inside the image.
- Return notes as text after the figure.
- Keep caption text separate from image export.

Only embed notes when:

- the user asks for a standalone image for a report
- the figure will circulate without a caption
- the note is short and does not compete with the plot

## Quality checklist

Before finalizing a polished figure:

- Does the figure look good without reading the caption?
- Does the caption carry all specification details that would clutter the canvas?
- Are the estimate and uncertainty visually distinct?
- Are reference lines lighter than the data?
- Are there any unnecessary legends, titles, notes, or labels?
- Does the figure still work in grayscale?
- For multi-panel figures, are axes, limits, spacing, and color meanings consistent?

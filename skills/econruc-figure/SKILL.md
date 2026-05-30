---
name: econruc-figure
description: Create, revise, audit, or code economics figures for papers, policy reports, seminar slides, dashboards exported to static figures, and replication packages. Use when the user asks for econ-vi style visualization, report figures, paper figures, event-study plots, coefficient plots, binscatter, RD plots, DiD diagnostics, time-series policy plots, maps, decomposition charts, regression tables turned into figures, or Top5/field-journal-ready PNG/PDF/SVG/TIFF output in Python, R, or Stata.
---

# EconRUC Economics Figure

This skill turns economic evidence into figures that make one argument cleanly. It adapts the visual discipline of `nature-figure` to economics: start from a claim and evidence chain, respect identification logic, disclose uncertainty and sample construction, and export reproducible paper/report figures rather than isolated pretty plots.

## Language Gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Backend Gate

Backend choice is a blocking gate for figure generation.

- If the user explicitly chooses Python, R, or Stata, use that backend exclusively for all plotting, previewing, exporting, and visual QA.
- If the user provides a clearly backend-specific input file or workflow, infer the backend from it: `.R`, `ggplot2`, `patchwork`, or `RDS` implies R; `.py`, matplotlib, seaborn, or pandas plotting implies Python; `.do`, Stata graph commands, or `.dta` replication scripts imply Stata unless the user asks otherwise.
- If no backend is chosen and code must be delivered, choose Python by default for new standalone figures, except when the user asks for R/Stata or when replication-package consistency clearly favors another backend.
- Once a backend is selected, do not cross-render with another language to create a substitute preview. Non-selected languages may be used only for non-visual file inspection or data conversion when they do not open a graphics device, import plotting libraries, create image/vector files, or change the final visual appearance.
- Check the selected runtime early: `Rscript`/R for R, Python plus plotting packages for Python, and Stata availability or user-provided execution environment for Stata. If the selected runtime or required packages are unavailable, stop before rendering and report the exact blocker. You may provide a selected-backend script and installation commands, or ask permission to install dependencies, but do not fall back to another backend for the figure.

## First Move: Figure Contract

Before writing plotting code, establish the contract below. If details are missing but can be reasonably inferred from the data and request, infer them and state the assumption briefly.

1. Claim: the one-sentence economic message the figure must defend.
2. Evidence chain: map each planned panel or visual layer to the claim, and drop panels that do not carry unique evidence.
3. Audience: paper, report, seminar, policy memo, teaching, dashboard export, or internal diagnostic.
4. Figure mode: `paper figure`, `report figure`, `slide figure`, or `diagnostic figure`.
5. Design context: treatment/control, event time, running variable, coefficient set, sample, geography, time horizon, distribution, mechanism, or decomposition.
6. Identification/statistics: estimator, controls, fixed effects, clustering level, bandwidth, binning, weights, omitted category, or normalization if supplied.
7. Uncertainty: standard errors, confidence intervals, bands, bootstrap intervals, prediction intervals, or no uncertainty if the plotted quantity is descriptive and no interval is supplied.
8. Visual profile: `modern journal`, `Chinese journal / Stata-like`, `report editorial`, `slide`, or `diagnostic`.
9. Backend: Python, R, or Stata, following the backend gate.
10. Export: PNG for quick review; PDF/SVG for editable paper figures; TIFF only when a journal requires it; source data/code when relevant for replication.
11. Review risks: scale manipulation, unclear base period, dual-axis ambiguity, unsupported causal language, missing uncertainty, hidden sample restrictions, or hard-to-read legends.

The highest-priority rule is: the chart serves the economic argument. Aesthetic polish, template matching, and complex layout are subordinate to making the core claim clear, defensible, and reviewable.

## Chinese And English Modes

Maintain Chinese and English figure styles as separate visual-output modes. Do not simply translate axis labels without reconsidering layout, typography, label density, and caption logic.

### Chinese Mode

- Target Chinese reports, Chinese economics papers, group-meeting presentations, policy figures, and Chinese Beamer decks.
- Prioritize Chinese font rendering, long-label handling, unit placement, legend position, and the reading habits of Chinese reports/journals.
- Use clear titles and subtitles when the figure is report-facing. For paper figures, keep the image clean and move long notes to the caption.
- Prefer concise Chinese labels such as `处理组`, `对照组`, `政策实施`, `相对年份`, `估计系数`, `95% 置信区间`, and explicit units such as `亿元`, `%`, `吨/年`, or `mg/kg`.
- Avoid crowding large `注：` paragraphs inside the plot unless the user asks for a standalone report graphic.

### English Mode

- Target Top5/field-journal figures, seminar slides, replication packages, and international reports.
- Use restrained journal styling: concise labels, clean uncertainty display, direct annotations, and caption-ready notes outside the figure.
- Prefer publication-ready output with clear evidence hierarchy and minimal decorative elements.
- Use conventional labels such as `Treated`, `Control`, `Event time`, `Coefficient`, `95% CI`, `Baseline`, `Bandwidth`, and `Outcome mean` when they clarify identification.

## Design Principles

- Related quantities named together, such as `installed capacity and generation`, `exports and imports`, `price and quantity`, or `coefficient and mechanism`, should usually become one coherent figure. Prefer coordinated panels, small multiples, shared legends, aligned time axes, or a labeled composite layout.
- For four comparable or sequential panels, prefer a balanced `2 x 2` layout for papers, slides, and most report figures. It usually improves aspect ratio, scan path, and side-by-side comparison over a tall `4 x 1` stack.
- Use a vertical `4 x 1` stack only when the intended output is a mobile/scrolling preview, a long report appendix, or when all panels must share a single long x-axis and the vertical comparison is more important than page balance.
- For `2 x 2` layouts, keep panel titles short, align axis ranges when comparable, share legends when possible, and place the strongest evidence in the top-left or top row. Avoid making each panel independently decorated.
- Avoid dual axes unless the user explicitly requests them or the comparison cannot be read otherwise. If dual axes are used, label the transformation clearly and ensure the two scales cannot imply a false relationship.
- Use direct labels when possible; use legends when categories are many, repeated across panels, or direct labels would clutter the data.
- Keep one restrained palette per figure: neutral family for context, signal family for the key series, and accent family for policy timing, treatment, or statistically significant contrasts.
- Choose colors by semantic role and visual weight, not only by category separation. Large stacked-bar components should use muted, low-saturation colors; reserve stronger reds, oranges, and blues for focal lines, policy markers, or small accents.
- In multi-panel figures, harmonize palettes across panels so that related concepts share a family: inputs may use muted blue/green/gold/violet, outputs may use sand/teal/coral, balances may use pale blue with darker input/output lines, and soil or stock variables may use quiet slate gray.
- Avoid palettes dominated by muddy brown, saturated red-green contrasts, rainbow defaults, or many unrelated hues. If one component occupies most of a panel, soften that fill first.
- Preserve grayscale interpretability when the figure may appear in print. Pair color with line type, shape, or panel structure when groups are central.
- Do not use rainbow defaults, ornamental backgrounds, unnecessary 3D effects, heavy borders, or chart junk.
- For paper figures, do not put long notes inside exported images by default. Return notes, data sources, fixed effects, clustering, controls, omitted categories, and variable definitions as caption text after the figure.
- For report figures, a short source note or definition note may be embedded if it remains readable and visually quiet.
- For slide figures, increase type size, reduce categories, and make the conclusion readable at a glance.
- When the user asks for a clean figure surface or says to remove small text, keep only the main figure title, necessary panel titles, axis tick labels, and axis titles inside the figure. Move subtitles, legend explanations, source notes, data caveats, variable definitions, and reading guidance into the separate `Figure note/caption` text returned in chat.
- For Chinese report/paper figures with compact panels, prefer vertical y-axis titles (`纵坐标竖排文字`) when the horizontal y-title would collide with ticks or reduce plotting width. Keep units readable, usually as a compact unit line such as `(t/yr)` or `mg/kg` near the vertical Chinese label.
- Do not embed figure notes in the image unless the user explicitly asks for a standalone graphic. If the note is important for interpretation, provide it as normal chat text after the figure and keep the exported canvas clean.

## Mode Defaults

### Paper Figure

- White background, compact type, clear axis units, restrained palette.
- Show confidence intervals or uncertainty when the graph reports estimates.
- Use direct labels or concise legends. Avoid titles that repeat captions.
- Keep the plotted canvas clean. Put sample, period, estimator, fixed effects, clustering, controls, omitted categories, data sources, and variable definitions in the paper caption unless the user requests standalone notes.
- Keep color robust to grayscale unless color carries essential grouping.
- For multiple quantities, use aligned panels or small multiples with shared x-axis and coordinated colors rather than unrelated standalone charts.
- For event-study figures, use the `reference-treatment square` profile by default unless the user asks for another style: muted blue-gray pre-period estimates, muted wine-red post-treatment estimates, semi-transparent vertical CI rectangles, square markers with white outlines, a hollow square at the omitted/reference period, dashed vertical rules at the reference period and treatment start, a dashed horizontal zero line, light y-grid only, no legend for a single series, and no in-figure notes.
- For coefficient figures, prefer the `modern journal` profile unless the user asks for Stata-like output: muted point estimates, light-gray confidence intervals, subtle zero line, no legend when one series is obvious, no in-figure notes.

### Report Figure

- Use a clear title and subtitle. Put the takeaway in the title only if the user wants report/storytelling style.
- Allow stronger color hierarchy, annotations, labeled policy periods, and short source notes.
- Prefer readable labels over maximal density.
- If the audience is policy-facing, make the unit, geography, period, and definition explicit.
- For multiple quantities, build one integrated figure with a common title, shared legend, harmonized palette, and panel labels.

### Slide Figure

- Use larger type, fewer series, and stronger hierarchy.
- Prefer one hero pattern plus one supporting panel over dense grids.
- Use annotations sparingly to point at policy dates, turning points, or the main estimated effect.
- Avoid long captions and small source notes inside the slide figure; provide speaker notes separately when useful.

### Diagnostic Figure

- Show raw patterns and threats before polishing.
- Label imbalance, bandwidth, pre-trends, bunching, attrition, leverage points, influential regions, missingness, or sample-composition concerns clearly.
- Mark the threshold, treatment timing, reform date, exclusion region, or bandwidth.
- Do not over-style. Diagnostics should be honest and legible rather than decorative.

## Chart Families

Choose a visual grammar before coding.

- `event study`: coefficients by relative time, treatment timing marked, zero line visible, confidence intervals shown. Default to the `reference-treatment square` style: pre-treatment estimates in blue-gray, post-treatment estimates in wine-red, 95% CI as semi-transparent vertical rectangles, square markers with white outlines, omitted/reference period shown as a hollow square at zero, and dashed vertical rules at the omitted period (usually `-1`) and treatment start (usually `0`). Label the upper plot region with understated `Reference (-1)` and `Treatment` text when it helps orientation. Do not write `omitted baseline` or similar text on the x-axis; state the omitted category in the caption or final explanation. For many groups, use small multiples with shared axes.
- `coefficient forest`: point estimates with confidence intervals, grouped by outcome, mechanism, subgroup, or specification. Sort intentionally and keep omitted/reference categories in the caption.
- `binscatter`: residualized or raw binned means, with controls, weights, binning rule, and sample disclosed. Show fitted relationship only when it supports the claim.
- `RD plot`: binned means, threshold line, bandwidth, polynomial/local-linear fit, and side-specific fits when appropriate. Avoid implying global trends outside the bandwidth.
- `DiD trend plot`: treated/control or high/low exposure trends, policy timing, normalized baseline if needed, and pre-period readability.
- `time-series policy plot`: aggregate series with event markers, shaded policy windows, direct labels, and sparse annotations.
- `distribution`: CDF, density, histogram, box, violin, or ridge plot only when distributional message matters. Choose bin widths and transformations transparently.
- `cross-sectional comparison`: sorted bars, dot plots, lollipop charts, or Cleveland plots. Horizontal layouts are preferred for long region/industry labels.
- `map`: choropleth or proportional symbols with meaningful bins, projection/source note, understated borders, and no unsupported causal implication.
- `decomposition`: waterfall, stacked bars, shift-share, Oaxaca, accounting bridge, or contribution shares with sign logic and limited colors.
- `heatmap/matrix`: coefficient matrix, correlation matrix, transition matrix, or input-output structure with meaningful ordering, fixed color scale, and readable labels.
- `table-to-figure`: turn regression tables into coefficient forests or specification curves when a visual comparison is clearer than a dense table.

When the user asks for a graph to be `高级`, `好看`, `像顶刊`, `publication-ready`, or provides a reference image, open `references/advanced-style-playbook.md` before plotting and explicitly choose the closest style profile.

## Backend Workflows

### Python Quick Start

When using Python, load `scripts/econruc_style.py` as a reusable style helper when available. It defines style profiles, palettes, saving helpers, and templates for coefficient plots and event studies.

```python
from econruc_style import set_econruc_style, plot_event_study, polish_axes, save_figure

set_econruc_style(mode="paper")
ax = plot_event_study(
    df,
    x="event_time",
    y="beta",
    lo="ci_low",
    hi="ci_high",
    ci_style="ribbon",
)
polish_axes(ax, zero_line=None, profile="modern_journal")
save_figure(ax.figure, "fig_event_study", formats=("png", "pdf", "svg"))
```

Use `get_style_profile("modern_journal")`, `get_style_profile("stata_matrix")`, or `get_style_profile("report_editorial")` when building custom chart types so colors, grids, and uncertainty styling remain consistent.

### R Quick Start

When using R, prefer `ggplot2` for individual plots, `patchwork` for multi-panel figures, `fixest`/`broom` outputs for estimates, `sf` for maps, and `ragg`/`svglite`/`cairo_pdf` for robust export. Use only R for drawing, previewing, exporting, and QA.

```r
library(ggplot2)
library(patchwork)

theme_econruc <- function(base_size = 8, base_family = "Arial") {
  theme_classic(base_size = base_size, base_family = base_family) +
    theme(
      axis.line = element_line(linewidth = 0.35, colour = "black"),
      axis.ticks = element_line(linewidth = 0.35, colour = "black"),
      panel.grid.major.y = element_line(linewidth = 0.25, colour = "grey88"),
      panel.grid.minor = element_blank(),
      legend.position = "top",
      legend.title = element_blank(),
      plot.title = element_text(face = "bold"),
      strip.text = element_text(face = "bold")
    )
}

save_econruc_r <- function(plot, filename, width_mm = 183, height_mm = 120, dpi = 600) {
  w <- width_mm / 25.4
  h <- height_mm / 25.4
  if (requireNamespace("svglite", quietly = TRUE)) {
    svglite::svglite(paste0(filename, ".svg"), width = w, height = h)
    print(plot)
    grDevices::dev.off()
  }
  grDevices::cairo_pdf(paste0(filename, ".pdf"), width = w, height = h)
  print(plot)
  grDevices::dev.off()
  if (requireNamespace("ragg", quietly = TRUE)) {
    ragg::agg_png(paste0(filename, ".png"), width = w, height = h, units = "in", res = dpi)
  } else {
    grDevices::png(paste0(filename, ".png"), width = w, height = h, units = "in", res = dpi)
  }
  print(plot)
  grDevices::dev.off()
}
```

For Chinese R figures, set a working Chinese font explicitly, such as `"Microsoft YaHei"` on Windows or a locally available CJK font. Verify that PDF/SVG exports preserve readable text.

### Stata Quick Start

When using Stata, reuse `assets/stata/econruc_graph_defaults.do` when available and keep graph code replication-friendly.

```stata
do "assets/stata/econruc_graph_defaults.do"

twoway ///
  (rcap ci_low ci_high event_time, lcolor(gs8)) ///
  (connected beta event_time, mcolor(navy) lcolor(navy)), ///
  yline(0, lcolor(gs10)) xline(-1, lpattern(dash) lcolor(gs10)) ///
  xtitle("Event time") ytitle("Coefficient") ///
  legend(off)

graph export "fig_event_study.svg", replace
graph export "fig_event_study.pdf", replace
graph export "fig_event_study.png", width(2400) replace
```

For Stata-like Chinese journal figures, keep the layout clean, avoid default saturated colors, and export vector formats whenever possible.

## Data And Replication Rules

- Prefer reading the user's actual source data over retyping values. If values are manually reconstructed from an image, say so in the figure note and keep the source-data caveat.
- Preserve variable names and transformations in code. Avoid opaque intermediate objects such as `x1`, `tmp2`, or undocumented rescaling.
- If plotting estimates, keep the script connected to the regression output where possible; otherwise include a clearly named estimate table with `estimate`, `std_error`, `ci_low`, `ci_high`, `p_value`, sample, and specification identifiers.
- If source data are filtered, winsorized, residualized, normalized, weighted, or collapsed, state this in code comments and final notes.
- Make every exported figure reproducible from the delivered script and input file paths or from a clean embedded source-data block when appropriate.
- Do not invent uncertainty intervals. If intervals are unavailable, state that the figure is descriptive or that uncertainty was not supplied.

## Export Policy

- Paper default: PDF and SVG with editable text plus PNG for preview.
- Journal submission: add TIFF only when requested, typically 600 dpi for line art or journal-specific requirements.
- Report default: high-resolution PNG and PDF.
- Slide default: PNG/PDF sized for the slide canvas.
- Use explicit dimensions. Common starting points: single-column 85-90 mm wide, double-column 170-183 mm wide, slide 16:9, and report figures around 8-10 inches wide.
- Check that panel labels, legends, axis labels, and direct labels remain readable at the target size.
- Avoid embedding long notes in a paper figure image. Put them in `Figure note/caption` unless standalone report use requires otherwise.

## QA Checklist

Before delivery:

- The claim, panel structure, title/subtitle, axis labels, and notes do not contradict each other.
- Units are explicit for every plotted quantity.
- Confidence intervals or standard errors are explicit when estimates are plotted.
- Omitted categories, baseline periods, normalizations, and reference groups are stated in the caption/final response rather than hidden in labels.
- Event time, treatment timing, thresholds, policy windows, or bandwidths are unambiguous.
- Color and line type remain interpretable in grayscale where needed.
- Related quantities requested together appear in one coherent visual system unless there is a stated reason to separate them.
- The palette is disciplined: no rainbow defaults, no low-contrast labels, no clashing colors across panels, and no colors that imply unsupported hierarchy.
- Axes are not misleadingly truncated; if truncation or indexing is used, it is labeled.
- Dual axes, if used, have a defensible transformation and clear labels.
- The figure remains readable at the intended size for paper, report, slide, or mobile preview.
- Exported PDF/SVG has editable text where possible.
- Chinese text renders correctly in raster and vector exports.
- The delivered script can be rerun from the stated data inputs.
- Remaining risks are disclosed, especially approximate data reconstruction, missing uncertainty, or absent runtime/package execution.

## Output Format

Default response structure:

1. `Figure contract:` concise claim, evidence chain, mode, chart type, uncertainty, backend, export.
2. `Code:` complete script or patch in the selected backend.
3. `Figure note/caption:` caption-ready notes, source, definitions, estimator, fixed effects, clustering, omitted category, sample, and caveats.
4. `QA:` what was checked and remaining risks.

For small edits, keep the response shorter but still mention the chosen backend, generated files, and any verification limits.

## When To Open Extra Files

| File | Open when |
|---|---|
| [references/econ-figure-contract.md](references/econ-figure-contract.md) | Need to translate a request into claim, chart family, data fields, figure note, and risks |
| [references/paper-vs-report.md](references/paper-vs-report.md) | Need to choose paper/report/slide/diagnostic mode |
| [references/chart-patterns.md](references/chart-patterns.md) | Need event-study, coefficient, binscatter, RD, map, distribution, or decomposition guidance |
| [references/visual-style.md](references/visual-style.md) | Need typography, palette, grid, export, and economics journal visual rules |
| [references/advanced-style-playbook.md](references/advanced-style-playbook.md) | Need to translate reference-image aesthetics into reusable figure styles, especially event-study small multiples or Chinese journal/Stata-like panels |
| [references/replication-and-audit.md](references/replication-and-audit.md) | Need replication-package notes, source data, variable disclosure, or QA checks |

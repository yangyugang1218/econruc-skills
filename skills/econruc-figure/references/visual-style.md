# Visual Style

## Palette

Default paper palette:

- ink: `#222222`
- gray: `#6B7280`
- light gray: `#D1D5DB`
- blue: `#2F6B9A`
- deep blue: `#1F5A85`
- ci gray: `#BFC5CD`
- reference gray: `#8A94A3`
- vermillion: `#B64A3A`
- muted red: `#9D3F46`
- pre fill: `#9FB2C3`
- post fill: `#CFA6A9`
- green: `#4F7F5A`
- gold: `#B68A2D`

Use one accent for the main estimate and gray for secondary information.

For modern paper event-study figures, prefer a deep muted blue estimate with a translucent gray CI ribbon. This often looks more polished than heavy vertical bars when the event-time path is ordered.

For Chinese journal or Stata-like multi-panel figures, use muted blue-gray for pre-treatment and muted red for post-treatment. Keep the legend outside the panel matrix when possible.

For multi-panel figures, assign colors by concept, not by panel. The same group, technology, region, or outcome family should keep the same color across all panels. Use line type, marker, or shade only when color alone would overload the figure.

Avoid default rainbow palettes, red-green contrasts, low-saturation colors on white that become unreadable, and palettes that make one panel look unrelated to the next. A figure should feel like one designed object even when it contains several charts.

Palette by chart role:

- estimate or focal line: deep muted blue
- comparison group: muted red, green, or gold, never a rainbow
- uncertainty: neutral gray with transparency
- context series or untreated/reference categories: gray or blue-gray
- positive/negative decomposition: muted blue/vermillion or green/muted red, with sign meaning held constant
- maps/heatmaps: sequential for levels, diverging and zero-centered for signed estimates

## Typography

- Paper: 7-9 pt equivalent for final journal figure.
- Report: 10-13 pt equivalent.
- Slide: 16-24 pt equivalent.
- Prefer Arial, Helvetica, DejaVu Sans, or a journal-required font.
- Match text size to output medium. A mobile/report preview needs larger labels than a journal PDF; a dense appendix figure can be smaller but must still pass legibility checks.

## Axes and grids

- Remove top and right spines.
- Keep zero line visible when estimates can be positive or negative.
- Use light y-grid only when it helps read values. Reference lines must be lighter than the data.
- Avoid heavy panel borders.
- Avoid plotting large shaded post-treatment regions in paper figures unless the period needs emphasis. A subtle vertical rule is often enough.
- For related time-series panels, align x-limits, tick years, panel widths, and legend placement.
- When units differ, use separate panels rather than forcing a dual axis unless the user explicitly wants a dual-axis design.

## Labels

- Axis labels need units.
- Do not label a coefficient as `effect` unless the design supports causal language.
- For paper figures, avoid long in-figure notes. Put omitted categories, sample restrictions, fixed effects, controls, clustering, and data-source details in the caption or final written note.
- Avoid floating text labels on axes unless they solve a real ambiguity. Event-study omitted periods usually belong in the caption, not on the x-axis.
- Avoid figure titles in paper figures when the figure will have a caption. Use titles more freely for reports and slides.
- For a single-series event-study figure, omit the legend unless there is a real comparison.
- Avoid abbreviations unless defined: p.p., s.d., log points, FE, CI.
- Panel labels should be short and functional: `A. Installed capacity`, `B. Generation`, `A. 装机容量`, `B. 发电量`.
- Legends should be shared when panels use the same categories.

## Adaptability

- Paper: restrained palette, compact labels, high export quality, source note or caption ready.
- Report: stronger title hierarchy, clearer annotations, readable at screen size, source note visible.
- Slide: large type, few categories, direct labels, minimal note.
- Mobile or chat preview: avoid very wide figures unless panels would become unreadable; consider stacked panels for narrow output.
- Bilingual output: ensure Chinese font rendering and do not let long Chinese notes collide with axes or captions.

## High-end polish rules

- Remove one non-data element before adding a new one.
- Prefer caption text over in-figure explanatory text.
- Make the data layer visually stronger than grids, zero lines, event lines, and panel borders.
- Use transparency for uncertainty, not for the main estimate.
- Check whether the figure still looks intentional at thumbnail size.
- For multi-panel figures, consistent spacing and shared scales create more polish than more color.
- Prefer horizontal layouts when category labels are long.
- Prefer small multiples over crowded legends when comparing many groups.
- Use direct labels only when they reduce clutter; otherwise use a compact shared legend outside the data region.
- Avoid chartjunk: gradient backgrounds, 3D effects, heavy borders, repeated titles, redundant legends, and labels that restate tick marks.
- Before exporting, ask whether each visual element is data, uncertainty, reference, or navigation. Remove elements that are none of these.

## Export

- Paper: PDF/SVG plus high-resolution PNG preview.
- Report: PNG plus editable source if possible.
- Do not rasterize text unless required.

# Beamer Visual Style

This style is learned from clean economics seminar Beamer decks and the supplied aviation reference deck: white background, blue title hierarchy, sparse bullets, generous whitespace, light-gray conceptual blocks, figure/text balance, and minimal ornament.

## Page geometry

- Use 16:9 aspect ratio.
- Keep generous margins; the slide should breathe.
- Do not fill every corner. Empty space is part of the design.
- Put page numbers unobtrusively at bottom right.
- Use one visual idea per slide. A slide should not feel like a compressed paper page.
- Prefer 2-column layouts only when each column has a clear job; otherwise use one wide content area.
- The default title page is RUC-branded: no ZEW or external institution logo, default authors are `Zhang San` and `Yang Yugang`, and both affiliations are `School of Applied Economics`.
- Place the original Renmin University of China logo/wordmark at the bottom-left of the title page. The template first looks for `assets/ruc_logo.png`; use the supplied `assets/ruc_logo_mark.tex` fallback only when the original logo file is unavailable.

## Palette

Default:

- deep blue: `#2B2FB3`
- ink: `#111111`
- muted gray: `#6B7280`
- light grid gray: `#E5E7EB`
- accent red: `#C7342D`
- accent green: `#69A84F`

Use deep blue for titles, bullets, emphasis terms, and section highlights. Use accent colors sparingly inside figures or callouts.

Reference-deck palette logic:

- blue carries hierarchy and navigation
- light gray carries conceptual contrast blocks
- black carries body text
- accent colors should be rare and meaningful

## Typography

- Titles should be large, blue, and left aligned.
- Body text should be large enough for the back of the room.
- Avoid dense paragraph blocks.
- Use italic only for short quoted phrases or named concepts.
- In Chinese decks, use XeLaTeX with CJK fonts and avoid mixing tiny English and Chinese on the same line.
- If the user chooses Chinese, slide prose should be Chinese, with English reserved for paper titles, variables, equations, and canonical terms.
- If the user chooses English, slide prose should be English throughout.
- Do not use bilingual bullets unless explicitly requested.

## Bullet style

- Use triangular main bullets or similarly strong markers.
- Main bullets should be complete thoughts.
- Sub-bullets should explain a channel, number, or caveat.
- Avoid more than 3 main bullets per slide.
- Avoid long wrapped bullets. If a bullet wraps more than twice, split or compress it.
- Use numbered blue callouts only when the slide has a sequence or when referencing elements in a diagram.

## Blocks and callouts

Use light-gray blocks for:

- conceptual contrasts, such as market-based versus command-and-control
- model ingredients
- assumptions versus predictions
- mechanisms versus evidence

Rules:

- blocks should be wide and quiet, not decorative cards
- no nested cards
- no heavy borders
- blue headings, black body, sparse lines
- numbered callouts should be small blue squares, used only when they guide the audience's eye

## Figures

Preferred layouts:

- full-width figure with one takeaway below
- left figure, right takeaways
- two coordinated panels with one shared title

Figure labels must be readable after insertion into Beamer. If a paper figure is too small, regenerate it for slides.

Never paste a full paper page as evidence. Crop to the figure/table itself, remove paper captions and notes, and rewrite the takeaway as slide text.

For regression tables, prefer:

- selected rows only
- coefficient plots
- simplified evidence tables
- full original table only in backup, and only if readable

## Equations

Equations should be readable and surrounded by interpretation:

- what object the equation defines
- what parameter matters
- what assumption identifies it
- what comparative static or mechanism follows

Do not show a derivation unless the audience needs it; move derivations to backup.

## Sample-deck observations

The provided aviation Beamer sample uses:

- title slide with large blue title, centered author block, and sparse institutional information, adapted here to Renmin University of China only
- clean white default Beamer layout
- blue triangle bullets
- blue emphasis for key economic terms
- compact page numbers
- roadmap/transition slides before major sections when the talk is long
- figure-left/text-right results slides
- robustness slides in the same visual language as main results
- light-gray blocks for conceptual comparisons
- incremental numbered callouts for explaining a logic chain

Use these as design cues, not as content to copy.

## Anti-patterns

- crowded paper screenshots
- too many bullets
- in-slide paragraphs copied from the paper
- mixed Chinese-English prose without an explicit bilingual request
- decorative boxes, thick frames, or busy backgrounds
- titles that merely say `Results` when a claim-first title is available

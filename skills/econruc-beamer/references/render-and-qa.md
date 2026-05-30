# Render and QA

## Required loop

1. Compile the deck.
2. Render or inspect the PDF.
3. Check representative pages: title, outline, dense bullet, equation, figure, table, conclusion, backup.
4. Fix overflow, tiny text, bad line breaks, broken references, missing figures, or unreadable math.
5. Recompile until clean.

## Compile commands

Use:

```powershell
latexmk -xelatex -interaction=nonstopmode deck.tex
```

Clean auxiliary files only after successful render if the user wants a tidy folder.

## Common failures

- Missing image path.
- Underscores in text not escaped.
- Unicode with pdfLaTeX.
- Long slide titles overflow.
- Figure labels too small after scaling.
- Tables exceed frame width.
- CJK fonts missing.

## Visual QA checklist

- No text spills below the slide.
- No line is too close to slide edge.
- Every slide title fits on one or two lines.
- Figures are legible at screen size.
- Blue emphasis is meaningful, not decorative.
- Equations have enough vertical space.
- Backup slide count does not confuse main slide numbering.

## Delivery

Return:

- `.tex` source path
- rendered `.pdf` path
- any figure/data assets created
- compile command used
- remaining caveats

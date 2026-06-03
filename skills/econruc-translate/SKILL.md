---
name: econruc-translate
description: Translate English economics and academic papers, working papers, PDFs, and article drafts into polished Simplified Chinese while preserving the original structure, sentence order, footnotes, equations, citations, figure/table titles, and academic tone; use when asked to produce Chinese TeX/PDF translations, 逐句翻译英文论文, translate economics papers, handle footnotes/references/tables, or compile a translated paper.
---

# EconRUC Translate English Paper

## Core Standard

Produce a faithful Simplified Chinese academic translation. Translate sentence by sentence in the original order; do not summarize, omit, paraphrase loosely, add explanations, or delete content unless the user explicitly asks. Preserve the paper's intellectual structure and technical meaning over stylistic elegance.

This skill belongs to the EconRUC suite. For economics papers, preserve discipline-specific meaning, identification language, econometric notation, table/figure captions, JEL codes, institutional names, and citation conventions. Do not turn a paper translation into a summary or a literature note.

Use this default output shape unless the user asks otherwise:

- Chinese TeX source using `ctexart`.
- Compiled PDF placed at the user-requested location, usually Desktop.
- Original footnotes converted into translated LaTeX `\footnote[...]` entries.
- Figures kept as titles/captions/placeholders unless image recreation is requested.
- Tables handled according to user preference; if unspecified, preserve title, note, and content as readable text or `verbatim`.
- References handled according to user preference; if unspecified, preserve the reference list, translating surrounding labels but not translating publication titles or URLs.

## Workflow

1. **Inspect the source.** Confirm the file exists. Extract text from PDF with `pdftotext`, `mutool`, `python`/PyMuPDF, or another available structured extractor. Count pages and inspect first/middle/last pages for extraction quality.
2. **Create a work directory.** Use a stable folder near the output, e.g. `~/Desktop/<paper>_translation/`, with extracted text, chunks/fragments, scripts, and logs.
3. **Chunk cautiously.** Split long papers by section or page-range. Keep page markers in intermediate chunks for coverage auditing, but remove them from the final document unless the user asks to show pages.
4. **Translate completely.** Translate every visible sentence and line. Preserve formulas, variables, citation keys, JEL codes, URLs, proper names, institution names, and titles where translation would be inappropriate.
5. **Assemble TeX.** Use the template in `assets/paper_translation_template.tex` as the starting point. Escape LaTeX special characters and prefer normal paragraphs over over-engineered formatting.
6. **Handle footnotes.** Convert source footnotes to `\footnote[n]{...}` at the corresponding sentence. Preserve original numbering and translate footnote content. Merge footnotes split across PDF pages.
7. **Handle tables, figures, and references.** Apply the user's requested policy. If they later request removal, remove only the requested material and preserve surrounding prose.
8. **Compile twice.** Use XeLaTeX. Treat compile errors as blockers; layout warnings from long URLs or long translated lines are acceptable if the PDF renders.
9. **Validate.** Check PDF exists, page count, no source page markers if removed, no unconverted footnote markers, and no leftover table/reference material when requested.
10. **Report succinctly.** Give final file paths, page count, what was removed/preserved, and any compile caveats.

## Translation Rules

- Use Simplified Chinese.
- Use a formal economics/engineering academic style: precise, neutral, and direct.
- Keep the author's first-person voice where present, e.g. translate "I show" as "我表明".
- Translate terms consistently across the paper. Examples from power-market papers:
  - transmission constraints: 输电约束
  - market integration: 市场整合 or 市场一体化; choose one dominant rendering and stay consistent
  - allocative inefficiency: 配置低效率 or 配置无效率; choose one and stay consistent
  - curtailment: 限发 or 弃电/弃风; use the term that fits the source context
  - load: 负荷
  - net revenue: 净收入
  - marginal cost: 边际成本
- Do not translate citation author names, journal titles, book/report titles, URLs, or model/software names unless the original already uses a translated name.
- Preserve equations and variables exactly unless the original prose around them requires Chinese punctuation.
- Keep citation syntax readable, e.g. `(Davis, Hausman and Rose, 2023)`.

## TeX Formatting

- Default to `ctexart`, XeLaTeX, A4 paper, readable margins, and `hyperref`.
- Use `\section*{...}` and `\subsection*{...}` for visible headings when the original has headings.
- Keep paragraphs in original order. Do not insert explanatory headings that are not in the source.
- Escape `%`, `_`, `&`, `#`, `{`, `}`, `$` unless intentionally using math mode.
- Use `\url{...}` for URLs when possible.
- Use `verbatim` only for messy tables or text blocks that would be fragile in normal LaTeX.
- Avoid visible intermediate page markers in the final PDF unless the user specifically wants page tracking.

## Footnotes

- Preserve all source footnotes.
- Put each translated footnote at the sentence location where the original marker appears.
- Use numbered syntax when preserving original numbering: `\footnote[23]{译文}`.
- If extraction leaves footnotes as detached numbered paragraphs, collect them, remove the detached footnote text, and insert it into the corresponding inline marker.
- Watch for cross-page splits: a footnote may begin at the bottom of one page and continue at the top of the next. Merge before translating.
- After assembly, verify numbering is continuous or explain any gap that exists in the original.

## Tables, Figures, and References

- **Tables preserved:** Keep title, content, and note. For complex numeric tables, use `verbatim` or a compact LaTeX table rather than risking bad column alignment.
- **Tables removed by user request:** Remove table content and table notes, keeping only the table title in its original position.
- **Figures:** If source images are unavailable, keep figure title and caption/notes as translated text. Do not invent image contents.
- **References preserved:** Keep reference entries in source language for names/titles/URLs; translate only labels such as "参考文献" if appropriate.
- **References removed by user request:** Delete the entire reference-list section, not in-text citations. Preserve appendices that follow the reference list.

## Useful Resources

- `assets/paper_translation_template.tex`: starter TeX document for Chinese academic-paper translations.
- `scripts/normalize_translation_tex.py`: post-processing utility for removing page markers, removing table bodies, or removing the reference list. Read or patch it before use if the source document has unusual formatting.

## Validation Checklist

Run checks matching the requested output:

- PDF compiles with XeLaTeX and opens as a nonempty document.
- Final PDF is in the requested location.
- Footnotes are present and numbered as expected.
- No intermediate page markers remain when the user asked for readability.
- Table content is present or removed according to the user's policy.
- Reference list is present or removed according to the user's policy.
- Obvious source text has not been left untranslated except names, citations, titles, URLs, math, and codes.
- Keep a backup before destructive post-processing such as removing tables or references.

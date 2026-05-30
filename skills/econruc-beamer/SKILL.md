---
name: econruc-beamer
description: Convert economics papers, working papers, reports, referee revisions, or research notes into polished LaTeX Beamer seminar decks. Use when the user asks to make slides from a paper, turn a PDF/LaTeX manuscript into Beamer, create an economics presentation, improve Beamer source, match a Beamer reference deck, build seminar/job-talk/conference slides, or render and iterate a LaTeX Beamer deck with economics-style narrative, figures, equations, tables, and bilingual Chinese-English support.
---

# EconRUC Beamer

## Language gate

- Before creating, revising, or rendering a deck, determine the deck language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次 Beamer 用中文还是英文？` and stop before producing slides.
- Do not create bilingual slides unless the user explicitly asks for bilingual output.
- Keep slide titles, bullets, section names, and speaker-facing prose in the chosen language. Paper titles, author names, variable names, equations, and canonical economics terms may remain in their original form when necessary.
- Apply the language-specific style: Chinese decks use concise Chinese academic presentation language; English decks use clean economics seminar English. Do not mix Chinese sentence structure with English bullets or vice versa.

## Chinese and English modes

Maintain Chinese and English decks as different presentation products, not translated copies.

### 中文模式

- 面向中文组会、博士论文汇报、学院 seminar、政策讨论或中文课程展示。
- Slide titles should be short Chinese claims; bullets should emphasize research motivation, institutional background, identification logic, and policy/economic implications.
- Use Chinese academic presentation rhythm: fewer full sentences, more conceptual signposting, clear section transitions, and no mixed Chinese-English sentence structure.

### English mode

- Target economics seminars, conferences, job talks, and field-journal presentations.
- Slide titles should be claim-first; bullets should foreground question, design/model, magnitudes, mechanisms, welfare, and contribution.
- Use clean seminar English with restrained typography, sparse bullets, and evidence-bearing figures.

When maintaining this skill, update Chinese layout/prose rules and English seminar rules independently. A Chinese deck should not read like translated English, and an English deck should not inherit Chinese report phrasing.

Use this skill to turn an economics paper into a seminar-ready LaTeX Beamer deck. The goal is not to compress every paragraph into slides; it is to rebuild the paper as a spoken economic argument.

## Core stance

- One slide, one job. Each frame should answer one question or defend one claim.
- A deck is a talk, not a paper in landscape format.
- Put the economics first: question, setting, identification/model, mechanism, quantitative magnitude, contribution, boundary.
- Use clean Beamer restraint: white background, deep blue section titles, sparse bullets, readable math, strong figures, minimal decoration, and generous whitespace.
- Design should resemble a polished economics seminar deck: compact 16:9 slides, blue title hierarchy, light-gray content blocks when useful, bottom-right page numbers, few words per slide, and no crowded paper-in-landscape pages.
- Prefer claim-first slide titles over topic labels when the claim is known.
- Preserve exact results, citations, equations, and institutional details from the paper. Do not invent content.
- Iterate visually. Beamer is finished only after rendering the PDF and checking spacing, font size, overflow, and figure legibility.

## Deck contract

Before writing slides, establish language, audience, duration, paper type, central claim, evidence ladder, must-include results, backup needs, and compile route. If the user has only notes or a partial paper, build a slide map with placeholders rather than inventing missing findings.

Every main slide should have one role: motivation, question, setting, design/model, data, result, mechanism, robustness, contribution, or limitation. Drop slides that do not advance the talk.

## Intake

Identify:

- source type: PDF paper, LaTeX manuscript, Word draft, notes, existing slides, or referee revision
- talk type: seminar, conference, job talk, class presentation, policy briefing, internal group meeting
- duration: 15, 30, 45, 60, or 90 minutes
- audience: general economists, field specialists, policy audience, Chinese seminar, bilingual room
- paper type: empirical reduced-form, structural, theory, model-plus-evidence, policy evaluation, descriptive measurement
- central claim: what the audience must remember
- required assets: figures, tables, equations, logos, bibliography, appendix backup slides
- reference style if supplied: observe spacing, hierarchy, palettes, and layout grammar, but do not copy its content or irrelevant branding

If no duration is specified, default to a 45-60 minute seminar deck with 35-50 main slides plus backup slides. If no style is specified, use the clean economics seminar style in `assets/econruc_beamer_template.tex`.

## Paper-to-Beamer workflow

1. Build the talk contract:
   `language -> audience -> duration -> central question -> one-sentence answer -> evidence ladder -> backup needs`.
2. Read the paper for structure, not only content. Extract:
   question, motivation, literature gap, setting, model/design, data, main results, mechanisms, robustness, contribution, limitations.
3. Run an economist extraction pass before drafting slides. Record:
   headline magnitudes, institutional facts, the exact empirical/model object, credible counterarguments, identification or modeling threats, literature contrasts, and policy or welfare trade-offs.
4. Always create an `Introduction` section, even if the paper has no section with that title.
5. The introduction must include three separate slides before roadmap/model/data/results:
   `Research motivation`, `Research question`, and `Research contribution`.
6. Create a slide map before writing LaTeX. Use `references/deck-architecture.md`.
7. Allocate slides by talk length. Do not exceed the audience's attention budget.
8. Convert paper sections into spoken sections:
   introduction, context, model/design, data, results, mechanisms, robustness, conclusion.
9. Use figures and tables as evidence anchors. For new or revised charts, use `econruc-figure`.
10. For a full paper deck, first build a complete version, then run a professional economist review pass before polishing. Do not judge the skill from a 10-slide prototype alone.
11. Write Beamer source from a template. Use macros and patterns in `references/latex-beamer-patterns.md`.
12. Compile with `latexmk -xelatex` when Chinese, Unicode, or modern fonts are needed. Use `pdflatex` only for pure ASCII decks that already compile that way.
13. Render/check the PDF. Iterate until no slide has overflow, tiny labels, unreadable figures, or orphaned bullet lines.
14. Review the rendered deck as an economist: narrative discipline, evidence credibility, contribution positioning, identification/model clarity, table-to-figure conversion, and whether the first 10 slides make the audience want to keep listening.

## QA and red lines

- Do not create paper-in-landscape slides with dense paragraphs or full regression tables unless the user explicitly asks for table-reading.
- Do not invent numbers, citations, equations, institutional facts, or robustness checks to complete a slide.
- Render before final delivery whenever a compile environment is available; check overflow, tiny labels, figure quality, missing fonts, broken references, and unreadable equations.
- If rendering is blocked, report the exact blocker and still provide source plus a manual QA checklist.

## Slide design defaults

- Use 16:9 aspect ratio.
- Title page: concise title, authors, institution, date, optional logos; keep it calm and spacious.
- Slide title: deep blue, large, left aligned, with enough top whitespace.
- Body: black text, sparse bullets, blue emphasis for key phrases; avoid dense paragraph blocks.
- Bullets: max 3 main bullets; sub-bullets only when they sharpen the mechanism.
- Math: large enough to read from the back of a seminar room. Explain equations in words.
- Figures: prefer left figure + right takeaways, or full-width figure + one bottom message.
- Tables: never paste a full paper regression table unless the point is table-reading. Convert to selected rows, coefficient plots, or simplified evidence tables.
- Use light-gray blocks for conceptual contrasts or toolboxes; do not put every slide in a card.
- Use numbered callouts only when they clarify a sequence of logic.
- Avoid mixed-language slides unless explicitly requested.
- Appendix: put derivations, extra robustness, data definitions, and full tables in backup frames.

## Economics deck narrative

Default main deck:

1. Title.
2. Introduction section.
3. Research motivation.
4. Research question.
5. Research contribution.
6. Preview of main findings.
7. Roadmap.
8. Institutional or industry context.
9. Theory/model/identification intuition.
10. Data and measurement.
11. Main empirical or quantitative results.
12. Mechanism and interpretation.
13. Robustness, external validity, or counterfactuals.
14. Conclusion and policy/economic implications.
15. Backup slides.

For theory-heavy decks, move model intuition earlier and put derivations in backup. For empirical decks, show the identifying variation before tables.

## Output format

Default:

1. `Deck contract:` duration, audience, structure, style.
2. `Slide map:` sections and slide titles.
3. `Beamer source:` files created or changed.
4. `Render/QA:` compile command, output PDF, issues fixed, remaining risks.
5. `Economist review:` what works, what is weak, and what to revise next.
6. `Speaker logic:` short notes on how the deck turns the paper into a talk.

When editing an existing Beamer deck, return a concise change summary and the rendered PDF path.

## When to open extra files

| File | Open when |
|---|---|
| [references/deck-architecture.md](references/deck-architecture.md) | Need to convert a paper into a slide map, choose talk length, or allocate sections |
| [references/paper-to-slides.md](references/paper-to-slides.md) | Need to extract content from a paper and decide what becomes slides versus backup |
| [references/latex-beamer-patterns.md](references/latex-beamer-patterns.md) | Need Beamer macros, frame patterns, columns, overlays, equations, appendix, or compilation advice |
| [references/visual-style.md](references/visual-style.md) | Need typography, palette, spacing, figure/table style, or sample-deck visual rules |
| [references/render-and-qa.md](references/render-and-qa.md) | Before final delivery or when fixing compile/render/overflow problems |
| [references/bilingual-beamer.md](references/bilingual-beamer.md) | Need Chinese, English, or bilingual Beamer slides |

## Bundled resources

- `assets/econruc_beamer_template.tex`: clean 16:9 economics Beamer template.
- `scripts/outline_to_beamer.py`: convert a markdown slide outline into a Beamer `.tex` scaffold.

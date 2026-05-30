# Deck Architecture

## Length budgets

Use a conservative pace: one substantive slide per 1-1.5 minutes, slower for theory, equations, and dense empirical tables.

| Talk | Main slides | Backup |
|---|---:|---:|
| 15 min conference | 10-14 | 5-10 |
| 30 min workshop | 20-28 | 10-20 |
| 45 min seminar | 30-40 | 15-30 |
| 60 min seminar | 40-55 | 20-40 |
| 90 min lecture/seminar | 55-75 | 30+ |

## Full-paper build pattern

When the source is a complete paper and the requested output is a group-meeting or seminar deck, prefer this sequence:

1. Build a full first version, not only a short sample.
2. Render the PDF and inspect representative slides from each section.
3. Review the deck as an economist before polishing the skill or template.
4. Revise the most visible problems: opening logic, evidence density, figure quality, title claims, and slide overflow.

A 10-slide prototype is useful for language, palette, and title-page testing. It is not enough to judge whether the paper has been converted into a persuasive 45-60 minute economics talk.

## Default economics seminar map

1. Title.
2. Introduction section divider.
3. Research motivation: why this economic margin matters.
4. Research question: the exact question and why it is unresolved.
5. Research contribution: substantive, design/data/model, and literature contributions.
6. Preview of main findings.
7. Roadmap.
8. Context/institution.
9. Conceptual mechanism or model intuition.
10. Empirical design or quantitative model.
11. Data and measurement.
12. Main result.
13. Mechanism or heterogeneity.
14. Robustness or validation.
15. Implications.
16. Conclusion.
17. Backup.

For a 45-60 minute paper seminar, a complete map often becomes:

- 6-8 slides: title, motivation, question, contribution, preview, roadmap, first headline fact
- 6-9 slides: setting, institutions, data, measurement, why the setting identifies the economics
- 8-12 slides: model, empirical design, identification, or structural object
- 12-18 slides: main results, mechanisms, heterogeneity, validation, robustness
- 6-10 slides: counterfactuals, welfare, policy implications, limitations, conclusion
- 10-30 slides: backup equations, full tables, extra figures, sample construction, robustness

The three introduction slides are mandatory for paper-to-Beamer tasks, even if the source paper does not use the heading `Introduction`.

## Section proportions

For empirical papers:

- motivation/context: 15-20 percent
- identification/data: 20-25 percent
- main results: 25-30 percent
- mechanisms/robustness: 20-25 percent
- conclusion: 5 percent

For theory or structural papers:

- motivation/context: 10-15 percent
- model intuition: 20-30 percent
- calibration/identification/data: 20 percent
- quantitative/theoretical results: 30 percent
- conclusion: 5 percent

## Slide title rules

Weak topic title:

`Results`

Better claim title:

`SAF quotas reduce welfare costs when market power is large`

Weak topic title:

`Data`

Better claim title:

`Route-level ticket data reveal substantial market heterogeneity`

Use topic titles only for roadmap, section divider, and dense technical backup slides.

## Language-specific architecture

- Chinese decks: slide titles should be short Chinese claims, usually 8-18 Chinese characters plus necessary economics terms. Do not write English full-sentence bullets unless the user asks for bilingual slides.
- English decks: use concise seminar English with claim-first titles and active verbs.
- For both languages, do not mix languages in the same bullet except for proper nouns, variables, equations, dataset names, and canonical terms.

## Reference-deck layout cues

When matching a polished reference deck, translate its visual grammar into Beamer rules:

- large blue title at top-left or centered only on the title page
- abundant whitespace
- few bullets per slide
- light-gray contrast blocks for conceptual comparisons
- numbered blue callouts only for sequential logic
- small bottom-right page number
- no decorative backgrounds, heavy borders, or crowded screenshots
- figure and table slides must have a clear visual hierarchy: evidence first, takeaway second
- avoid long horizontal chains with four or more large nodes; use a two-row causal map or numbered callouts instead
- convert wide tables into selected rows, dot plots, compact heatmaps, or two-column contrasts when the audience should remember signs and magnitudes rather than read cells

## Backup strategy

Put these in backup:

- full regression tables
- proofs and derivations
- alternative calibrations
- extra robustness checks
- data cleaning details
- additional citations
- institutional detail that answers likely questions but slows the main talk

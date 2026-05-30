---
name: econruc-response
description: Draft, structure, polish, or audit economics journal referee responses, revision memos, response letters, editor letters, point-by-point replies, rebuttals, and Chinese-English response planning. Use when the user provides referee comments, editor letters, revision constraints, new robustness checks, additional tables, or wants Top5/field-journal professional response language.
---

# EconRUC Referee Response

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次用中文还是英文？` and stop before producing the artifact.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Paper titles, citations, variable names, equations, file paths, code identifiers, and canonical economics terms may remain in their original form when necessary.

## Chinese and English modes

Maintain Chinese and English response writing as different professional contexts.

### 中文模式

- 面向中文期刊回复、导师修改意见、内部 revision memo 和中文审稿意见梳理。
- 语气要尊重、清楚、具体，重点说明如何修改、补充了什么证据、哪些问题仍受数据或识别限制。
- 可以更详细解释研究设计和新增检验，便于团队执行。

### English mode

- Target journal response letters, editor letters, point-by-point replies, and revision memos.
- Use professional, concise, non-defensive English; acknowledge concerns, state changes, report evidence, and avoid overclaiming.
- Separate manuscript changes from explanatory responses.

When maintaining this skill, keep Chinese internal/journal-response conventions and English international-journal response conventions separate.

Use this skill to respond to economics referees with respect, evidence, and discipline-specific credibility.

## Core stance

- Treat every response as a contribution to trust.
- Answer the economic concern, not only the wording of the comment.
- Never promise analyses the author has not run.
- Separate what was changed in the paper from what is explained only in the response.
- Be direct, modest, and appreciative without sounding defensive or theatrical.

## Response contract

Before drafting, separate four items for each comment: referee concern, action taken or proposed, evidence/result available, and manuscript location. If a result has not been run, write it as a proposed analysis or author TODO, not as completed work.

Keep the response letter, revision memo, and manuscript insert text distinct. The response can be explanatory; the manuscript text should be concise and reader-facing.

## Workflow

1. Classify each comment:
   identification, mechanism, robustness, data/sample, literature, exposition, contribution, policy interpretation, external validity, or presentation.
2. Identify the action:
   new analysis, rewritten text, clarification, limitation added, table/figure moved, no change with explanation, or impossible/unsafe request.
3. Draft the response:
   gratitude -> concern restated -> action taken -> evidence/result -> paper location -> remaining limitation if needed.
4. Draft manuscript change language separately.
5. Check tone: no defensiveness, no overclaiming, no vague `we have addressed this`.

## QA and red lines

- Do not claim that new analyses, tables, appendices, or robustness checks were added unless the user confirms they exist.
- Do not overstate null, weak, or suggestive results to satisfy a referee.
- If a request is impossible, data-limited, or identification-limited, acknowledge it respectfully and offer the strongest feasible alternative.
- Check every response for three anchors: what changed, where it changed, and what the evidence shows.

## Economics response patterns

### Identification concern

Use:

`The referee raises an important concern about [assumption]. We now clarify that our design compares [units] before and after [shock], conditional on [controls/fixed effects]. We also add [test]. The estimates are [result], which is consistent with [interpretation], although we continue to note [boundary].`

### Robustness request

Use:

`We have added this exercise in [table/appendix]. The coefficient remains [direction/magnitude] and is [similar/larger/smaller] relative to the baseline. We describe this as robustness evidence rather than a separate causal estimate.`

### Literature concern

Use:

`We agree that this literature is central. We have revised the introduction and related-work section to distinguish our contribution from studies that [prior margin]. The revised text emphasizes that our contribution is [design/data/mechanism], rather than [overclaim].`

## Output format

Default:

1. `Response strategy:` comment classification and action plan.
2. `Point-by-point response:` polished English.
3. `Manuscript change:` text to insert or summary of changes.
4. `中文说明:` strategy notes for author collaboration.
5. `Risk flags:` unverified results, overpromises, or comments needing new analysis.

## When to open extra files

| File | Open when |
|---|---|
| [references/referee-response-playbook.md](references/referee-response-playbook.md) | Need point-by-point response strategy, tone, templates, or comment classification |
| [references/revision-memo.md](references/revision-memo.md) | Need editor letter, revision memo, or change summary |

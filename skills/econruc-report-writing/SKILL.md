---
name: econruc-report-writing
description: Draft, structure, audit, or polish economics research reports, policy analysis reports, industry research notes, consulting-style reports, briefing memos, and data-grounded analytical reports in Chinese or English. Use when the user asks to write a 研报, 政策分析, 咨询报告, industry report, policy memo, sector analysis, market study, briefing, or evidence-based report that requires verified data, clear structure, sourced claims, logical reasoning, and no fabricated facts.
---

# EconRUC Report Writing

## Language gate

- Before producing the main artifact, determine the output language: Chinese or English.
- If the user has not explicitly specified a language, ask `请问这次报告用中文还是英文？` and stop before drafting the report.
- Do not produce bilingual output unless the user explicitly asks for bilingual text.
- Keep the main prose in the chosen language. Institution names, policy names, dataset names, citations, equations, file paths, and canonical economics terms may remain in their original form when necessary.

## Core standard

This skill writes evidence-based reports, not persuasive fiction. A good report must be clear, useful, and defensible.

- Do not invent data, citations, policies, company facts, institutional details, coefficients, rankings, or market sizes.
- Every factual claim that matters must have a source, date, unit, and scope.
- If the user provides data, use it and disclose its source/limits.
- If the user asks for current data, recent policy, market size, prices, company facts, laws, or official statistics, verify with reliable sources before writing.
- If evidence is unavailable, write `待补充来源` / `source needed` or ask for the missing data. Do not fill the gap with plausible-sounding numbers.
- Separate facts, estimates, assumptions, interpretations, forecasts, and recommendations.
- Keep causal language modest unless the design supports causal inference.

## Chinese and English modes

### 中文模式

- 面向中文研报、政策分析、政府/机构报告、产业报告、咨询汇报和领导简报。
- 强调问题背景、政策语境、数据事实、逻辑链条、风险边界和可执行建议。
- 语言应清楚、克制、专业，避免空泛口号、宣传腔和没有证据的判断。
- 数据口径要写清楚：地区、年份、单位、统计口径、来源和发布日期。

### English mode

- Target policy memos, sector reports, consulting-style reports, market studies, and evidence-based analytical briefs.
- Use concise executive-report prose: issue, evidence, interpretation, implications, recommendations, and risks.
- Distinguish verified facts from assumptions and forecasts.
- Keep tables, exhibits, and source notes audit-ready.

## Report contract

Before drafting, establish:

1. Report type: policy analysis, industry research, consulting report, market study, briefing memo, internal strategy note, or academic-style report.
2. Audience: policymakers, executives, investors, researchers, local government, industry association, or internal team.
3. Decision question: what choice, judgment, or understanding should the report support?
4. Scope: geography, sector, time period, institutions, population, firms, or policy boundary.
5. Evidence base: user-provided data, official statistics, literature, company filings, policy documents, interviews, news, or web sources.
6. Required source standard: official data only, public web sources, academic sources, industry databases, or user-provided sources.
7. Output length and format: executive brief, full report, outline, memo, slide-ready text, appendix, or source register.
8. Figures/tables needed: charts, evidence tables, policy timeline, comparison matrix, risk matrix, scenario table.
9. Uncertainty: missing data, conflicting sources, estimates, assumptions, and sensitivity.
10. Citation style: footnotes, endnotes, source table, inline links, or bibliography.

If the contract is underspecified, make conservative assumptions and label them. Ask only when the missing information would change the report's conclusion or evidence standard.

## Evidence and source rules

- Prefer primary sources: official statistics, ministry/regulator documents, central/local government releases, statistical yearbooks, company filings, international organizations, peer-reviewed papers, and reputable data portals.
- Use media or consulting reports cautiously; treat them as secondary sources unless they cite original data.
- Record every important number in a source register with:
  `claim | value | unit | geography | period | source | publication date/access date | link/file | caveat`.
- If two sources conflict, state the conflict and explain which source is used.
- Do not cite vague sources such as `公开资料整理` unless the underlying source is also listed.
- Do not write `数据显示` unless the data source is identified.
- Forecasts must state method, assumptions, baseline year, and uncertainty.
- Policy analysis must distinguish enacted policy, draft policy, proposal, rumor, and interpretation.

## Report architecture

Default full report:

1. Title.
2. Executive summary: 3-6 bullet conclusions with source-backed magnitudes.
3. Research question / policy question.
4. Background and scope.
5. Key facts and data snapshot.
6. Analytical framework or logic chain.
7. Main analysis by theme.
8. Policy/industry implications.
9. Risks, uncertainties, and alternative interpretations.
10. Recommendations or scenarios, if requested.
11. Source notes and appendix.

For short policy briefs:

1. Issue.
2. Evidence.
3. Interpretation.
4. Options.
5. Recommendation.
6. Risks and data caveats.

For consulting-style reports:

1. Executive answer.
2. Market/policy context.
3. Evidence exhibits.
4. Diagnosis.
5. Strategic options.
6. Implementation considerations.
7. Risks and watchpoints.

## Writing workflow

1. Build the report contract.
2. Create a report outline before drafting.
3. Build an evidence map: each section's claims and required sources.
4. Verify or mark data sources.
5. Draft with claim-first section headings.
6. Insert source notes or source table entries as the report is written.
7. Audit logic: evidence -> inference -> implication -> recommendation.
8. Audit wording: remove unsupported adjectives, exaggerated causal claims, and vague quantifiers.
9. Return a source register and missing-evidence list when useful.

## Output format

Default:

1. `Report contract:` audience, scope, decision question, evidence standard.
2. `Outline:` sections and core claims.
3. `Draft report:` in the requested language.
4. `Source register:` key claims, sources, dates, caveats.
5. `Data gaps and risks:` what still needs verification.
6. `Next steps:` charts, tables, data requests, or policy documents to obtain.

For polishing/restructuring existing reports:

1. Revised report or section.
2. Logic audit.
3. Unsupported claim list.
4. Source/citation improvement list.

## QA and red lines

Before delivery, check:

- Does every important number have source, unit, period, and geography?
- Are facts separated from interpretation and recommendations?
- Are current or unstable facts verified with up-to-date sources?
- Are policy names, dates, and issuing agencies accurate?
- Are vague claims like `显著提升`, `快速增长`, `巨大空间`, `国际领先` supported by data?
- Are charts/tables described with their data source?
- Are assumptions and estimates clearly labeled?
- Are recommendations logically derived from evidence?

Red lines:

- Never fabricate data or sources.
- Never cite a source that was not checked or provided.
- Never hide uncertainty by writing around it.
- Never present policy proposals or media rumors as enacted policy.
- Never give investment, legal, medical, or financial advice as a definitive instruction. Provide analytical framing and caveats.

## When to open extra files

| File | Open when |
|---|---|
| [references/report-architecture.md](references/report-architecture.md) | Need a report outline, section structure, executive summary pattern, or report type choice |
| [references/source-and-data-audit.md](references/source-and-data-audit.md) | Need source standards, citation/source register rules, or data verification checklist |
| [references/policy-consulting-style.md](references/policy-consulting-style.md) | Need policy/consulting report language, recommendation style, or risk matrix |
| [references/evidence-to-claim.md](references/evidence-to-claim.md) | Need to convert evidence into defensible claims and avoid overstatement |
| [scripts/make_source_register.py](scripts/make_source_register.py) | Need a CSV template for claim/source tracking |

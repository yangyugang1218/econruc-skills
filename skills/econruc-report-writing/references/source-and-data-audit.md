# Source and Data Audit

## Preferred source hierarchy

1. Official statistics and government/regulator releases.
2. International organizations and recognized public databases.
3. Company filings, exchange disclosures, audited annual reports.
4. Peer-reviewed papers, working papers, and reputable research institutions.
5. Industry associations and data vendors, with methodology disclosed.
6. Media and consulting reports, only when they cite traceable underlying data or when used as contextual evidence.

## Required source fields

For every important number, record:

- claim
- value
- unit
- geography
- period
- source name
- publication date or access date
- link or local file
- caveat / statistical scope

## Unacceptable source practices

- `公开资料整理` without underlying sources.
- `数据显示` without naming the dataset.
- Quoting a number from memory.
- Mixing yearly, monthly, cumulative, and year-on-year figures without stating the basis.
- Comparing nominal and real values without deflator details.
- Treating forecast, target, installed capacity, production, and consumption as interchangeable.

## Current-data rule

If the report depends on current or recently changing information, verify it before writing:

- laws and policies
- official statistics
- commodity or asset prices
- exchange rates
- company executives, financials, and filings
- market shares and rankings
- macroeconomic indicators

When current verification is impossible, write a caveat and do not present the claim as settled.

## Source register template

```csv
claim,value,unit,geography,period,source,publication_or_access_date,link_or_file,caveat
```

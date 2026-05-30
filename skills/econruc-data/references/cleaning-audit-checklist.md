# Cleaning and Audit Checklist

## Raw data rules

- Never overwrite raw files.
- Store download date and source URL or citation.
- Keep a raw inventory with file name, source, period, unit, and notes.

## Key checks

- Unique ID check.
- Duplicate rows.
- Missingness by variable and year.
- Merge rate and unmatched records.
- Unit consistency.
- Outlier ranges.
- Time-series breaks.
- Province/city/county code changes.
- Currency and price base.
- Deflator used.

## Panel construction

Record:

- unit of observation
- balanced or unbalanced panel
- entry and exit rules
- treatment timing
- lag and lead construction
- aggregation rules

## Variable dictionary

Minimum fields:

| variable | label | unit | source | transformation | missing rule |
|---|---|---|---|---|---|

## Common economic transformations

- real monetary values: deflate and state base year
- log variables: specify handling of zeros
- shares: numerator and denominator
- rates: percent vs percentage points
- winsorization: threshold and level
- standardization: mean and standard deviation sample

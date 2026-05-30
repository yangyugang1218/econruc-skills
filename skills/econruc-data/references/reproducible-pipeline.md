# Reproducible Data Pipeline

## Folder structure

Use:

```text
data/
  raw/
  interim/
  processed/
  external/
code/
  00_setup
  01_download
  02_clean
  03_merge
  04_analysis
  05_figures
outputs/
  tables/
  figures/
docs/
  variable_dictionary.csv
  data_inventory.csv
```

## Script rules

- One script should have one job.
- Use relative paths from project root.
- Log row counts after each major step.
- Export tidy figure data separately from full analysis data.
- Set seeds for random splits, bootstrap, or sampling.

## Replication package

Include:

- README with software versions.
- Data availability statement.
- Raw-data access instructions when raw data cannot be redistributed.
- Code to rebuild processed data.
- Checksums or row-count logs for important files.

## Hand-off to figures

Before using `econruc-figure`, prepare a tidy file with:

- one row per plotted observation
- explicit units
- group labels
- estimate and confidence interval bounds when applicable
- note fields for sample or specification

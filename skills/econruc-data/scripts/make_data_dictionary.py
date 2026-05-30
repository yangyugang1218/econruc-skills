#!/usr/bin/env python3
"""Create a starter variable dictionary from a CSV file."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.csv, nrows=1000)
    rows = []
    for col in df.columns:
        s = df[col]
        rows.append(
            {
                "variable": col,
                "label": "",
                "dtype": str(s.dtype),
                "unit": "",
                "source": "",
                "transformation": "",
                "missing_rule": "",
                "nonmissing_in_sample": int(s.notna().sum()),
                "example_values": "; ".join(map(str, s.dropna().astype(str).unique()[:5])),
            }
        )
    out = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()

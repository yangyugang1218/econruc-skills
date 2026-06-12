"""Create a source-register CSV template for EconRUC report writing."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


FIELDS = [
    "claim",
    "value",
    "unit",
    "geography",
    "period",
    "source",
    "publication_or_access_date",
    "link_or_file",
    "caveat",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an empty report source-register CSV.")
    parser.add_argument("output", nargs="?", help="Output CSV path.")
    parser.add_argument("-o", "--output", dest="output_flag", help="Output CSV path.")
    args = parser.parse_args()

    out = Path(args.output_flag or args.output or "source_register.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
    print(out)


if __name__ == "__main__":
    main()

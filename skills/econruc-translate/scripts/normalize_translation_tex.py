#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


PAGE_MARKER_RE = re.compile(r"^\s*(?:=+\s*)?第\s*\d+\s*页(?:\s*=+)?\s*$")
TABLE_TITLE_RE = re.compile(
    r"^(?:\\noindent\s+)?(?:Table\s+\d+|表\s*A?\d+)\s*[:：].*$|^\\section\*\{表\s*A?\d+\s*[:：][^}]*\}\s*$"
)


def remove_page_markers(text: str) -> str:
    lines = [line for line in text.splitlines() if not PAGE_MARKER_RE.match(line)]
    return "\n".join(lines) + "\n"


def remove_reference_list(text: str) -> str:
    return re.sub(
        r"\\section\*\{参考文献\}.*?(?=\\section\*\{A1|\\appendix|\\end\{document\})",
        "",
        text,
        flags=re.S,
    )


def remove_table_bodies(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    pending_title = False
    next_table_number = 1

    while i < len(lines):
        line = lines[i]

        if TABLE_TITLE_RE.match(line.strip()):
            out.append(line)
            pending_title = True
            i += 1
            continue

        if r"\begin{table}" in line:
            block = []
            while i < len(lines):
                block.append(lines[i])
                if r"\end{table}" in lines[i]:
                    i += 1
                    break
                i += 1
            caption = re.search(r"\\caption\{([^{}]+)\}", "\n".join(block))
            title = caption.group(1).strip() if caption else f"表 {next_table_number}"
            out.append(rf"\noindent Table {next_table_number}: {title}")
            next_table_number += 1
            pending_title = False
            i = skip_table_note(lines, i)
            continue

        if r"\begin{verbatim}" in line:
            block = []
            while i < len(lines):
                block.append(lines[i])
                if r"\end{verbatim}" in lines[i]:
                    i += 1
                    break
                i += 1
            inner = [x for x in block[1:-1] if x.strip()]
            first = inner[0].strip() if inner else ""
            if pending_title:
                pending_title = False
                i = skip_table_note(lines, i)
                continue
            if re.match(r"^(?:Table\s+\d+|表\s*A?\d+)\s*[:：]", first):
                out.append(r"\noindent " + first)
                i = skip_table_note(lines, i)
                continue
            out.extend(block)
            continue

        out.append(line)
        i += 1

    return "\n".join(out) + "\n"


def skip_table_note(lines: list[str], i: int) -> int:
    j = i
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines) and re.match(r"^(?:\\noindent\s*)?注：", lines[j].strip()):
        j += 1
        while (
            j < len(lines)
            and lines[j].strip()
            and (lines[j].startswith(" ") or lines[j].startswith("\t"))
        ):
            j += 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    return j


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("tex", type=Path)
    parser.add_argument("--remove-page-markers", action="store_true")
    parser.add_argument("--remove-table-bodies", action="store_true")
    parser.add_argument("--remove-references", action="store_true")
    args = parser.parse_args()

    text = args.tex.read_text(encoding="utf-8")
    if args.remove_page_markers:
        text = remove_page_markers(text)
    if args.remove_table_bodies:
        text = remove_table_bodies(text)
    if args.remove_references:
        text = remove_reference_list(text)
    args.tex.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

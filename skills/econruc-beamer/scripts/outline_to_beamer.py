#!/usr/bin/env python3
"""Convert a markdown slide outline into an EconRUC Beamer scaffold.

Markdown convention:
  # Deck title
  FirstAuthor: Zhang San
  SecondAuthor: Yang Yugang
  FirstAffiliation: School of Applied Economics
  SecondAffiliation: School of Applied Economics
  Date: \today

  ## Section title
  ### Slide title
  - Bullet
  - Bullet with **emphasis**
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path
import re


BODY_BEGIN = "% ECONRUC_BODY_BEGIN"
BODY_END = "% ECONRUC_BODY_END"


@dataclass
class Entry:
    kind: str
    title: str
    bullets: list[str] = field(default_factory=list)


def default_template_path() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "econruc_beamer_template.tex"


def latex_escape(text: str, allow_latex: bool = False) -> str:
    if allow_latex and text.startswith("\\"):
        return text
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return re.sub(r"\*\*(.+?)\*\*", r"\\blue{\1}", text)


def parse_markdown(path: Path) -> tuple[dict[str, str], list[Entry]]:
    meta = {
        "title": "Untitled Deck",
        "firstauthor": "Zhang San",
        "secondauthor": "Yang Yugang",
        "firstaffiliation": "School of Applied Economics",
        "secondaffiliation": "School of Applied Economics",
        "institute": "School of Applied Economics, Renmin University of China",
        "date": r"\today",
    }
    aliases = {
        "author": "firstauthor",
        "firstauthor": "firstauthor",
        "secondauthor": "secondauthor",
        "firstaffiliation": "firstaffiliation",
        "secondaffiliation": "secondaffiliation",
        "institute": "institute",
        "date": "date",
    }
    entries: list[Entry] = []
    current: Entry | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            meta["title"] = line[2:].strip()
        elif ":" in line and not line.startswith("- "):
            key, value = line.split(":", 1)
            normalized = key.strip().lower().replace(" ", "")
            if normalized in aliases:
                meta[aliases[normalized]] = value.strip()
        elif line.startswith("## "):
            current = None
            entries.append(Entry(kind="section", title=line[3:].strip()))
        elif line.startswith("### "):
            current = Entry(kind="slide", title=line[4:].strip())
            entries.append(current)
        elif line.startswith("- ") and current is not None:
            current.bullets.append(line[2:].strip())
    return meta, entries


def render_entries(entries: list[Entry]) -> str:
    chunks: list[str] = []
    for entry in entries:
        if entry.kind == "section":
            title = latex_escape(entry.title)
            chunks.append(r"\section{" + title + "}" + "\n" + r"\sectionframe{" + title + "}")
            continue
        bullets = "\n".join(f"    \\item {latex_escape(b)}" for b in entry.bullets)
        chunks.append(
            "\\begin{frame}{"
            + latex_escape(entry.title)
            + "}\n  \\begin{wideitemize}\n"
            + bullets
            + "\n  \\end{wideitemize}\n\\end{frame}"
        )
    return "\n\n".join(chunks)


def replace_command(tex: str, command: str, value: str) -> str:
    pattern = re.compile(rf"\\{re.escape(command)}\{{.*?\}}")
    return pattern.sub(lambda _: rf"\{command}{{{value}}}", tex, count=1)


def replace_newcommand(tex: str, command: str, value: str) -> str:
    pattern = re.compile(rf"\\newcommand\{{\\{re.escape(command)}\}}\{{.*?\}}")
    return pattern.sub(lambda _: rf"\newcommand{{\{command}}}{{{value}}}", tex, count=1)


def replace_body(tex: str, body: str) -> str:
    start = tex.index(BODY_BEGIN) + len(BODY_BEGIN)
    end = tex.index(BODY_END)
    return tex[:start] + "\n" + body + "\n" + tex[end:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("outline", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", type=Path, default=default_template_path())
    args = parser.parse_args()

    meta, entries = parse_markdown(args.outline)
    tex = args.template.read_text(encoding="utf-8")
    tex = replace_command(tex, "title", latex_escape(meta["title"]))
    tex = replace_newcommand(tex, "firstauthor", latex_escape(meta["firstauthor"]))
    tex = replace_newcommand(tex, "secondauthor", latex_escape(meta["secondauthor"]))
    tex = replace_newcommand(tex, "firstaffiliation", latex_escape(meta["firstaffiliation"]))
    tex = replace_newcommand(tex, "secondaffiliation", latex_escape(meta["secondaffiliation"]))
    tex = replace_command(tex, "institute", latex_escape(meta["institute"]))
    tex = replace_command(tex, "date", latex_escape(meta["date"], allow_latex=True))
    tex = replace_body(tex, render_entries(entries))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(tex, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Reusable matplotlib helpers for EconRUC economics figures.

This module is intentionally small and dependency-light. It supports the
common paper/report graph patterns used by the econruc-figure skill.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


PALETTE = {
    "ink": "#222222",
    "gray": "#6B7280",
    "light_gray": "#D1D5DB",
    "grid": "#E5E7EB",
    "blue": "#2F6B9A",
    "deep_blue": "#1F5A85",
    "ci_gray": "#BFC5CD",
    "reference_gray": "#8A94A3",
    "vermillion": "#B64A3A",
    "muted_red": "#9D3F46",
    "pre_fill": "#9FB2C3",
    "post_fill": "#CFA6A9",
    "event_pre_fill": "#D4DDE4",
    "event_pre_line": "#71879A",
    "event_post_fill": "#EBD9DC",
    "event_post_line": "#A64049",
    "green": "#4F7F5A",
    "gold": "#B68A2D",
}


STYLE_PROFILES = {
    "modern_journal": {
        "primary": PALETTE["deep_blue"],
        "secondary": PALETTE["muted_red"],
        "uncertainty": PALETTE["ci_gray"],
        "reference": PALETTE["reference_gray"],
        "grid": "#EDF1F4",
    },
    "stata_matrix": {
        "pre_fill": PALETTE["pre_fill"],
        "post_fill": PALETTE["post_fill"],
        "pre_point": PALETTE["deep_blue"],
        "post_point": PALETTE["muted_red"],
        "reference": "#2F3337",
        "grid": "#E8F0F2",
    },
    "report_editorial": {
        "primary": PALETTE["deep_blue"],
        "secondary": PALETTE["gold"],
        "uncertainty": PALETTE["ci_gray"],
        "reference": PALETTE["reference_gray"],
        "grid": "#E7ECF1",
    },
    "reference_treatment_square": {
        "pre_fill": PALETTE["event_pre_fill"],
        "pre_line": PALETTE["event_pre_line"],
        "post_fill": PALETTE["event_post_fill"],
        "post_line": PALETTE["event_post_line"],
        "reference": PALETTE["reference_gray"],
        "grid": "#E8EEF3",
    },
}


def get_style_profile(name: str = "modern_journal") -> dict[str, str]:
    """Return a named visual profile for consistent economics figures."""
    if name not in STYLE_PROFILES:
        raise ValueError(f"name must be one of: {', '.join(STYLE_PROFILES)}")
    return STYLE_PROFILES[name].copy()


def set_econruc_style(mode: str = "paper") -> None:
    """Set matplotlib rcParams for economics paper/report figures."""
    if mode not in {"paper", "report", "slide", "diagnostic"}:
        raise ValueError("mode must be one of: paper, report, slide, diagnostic")

    base_size = {
        "paper": 8,
        "report": 11,
        "slide": 16,
        "diagnostic": 9,
    }[mode]

    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": base_size,
            "axes.titlesize": base_size + (1 if mode != "slide" else 3),
            "axes.labelsize": base_size,
            "xtick.labelsize": base_size - 1,
            "ytick.labelsize": base_size - 1,
            "legend.fontsize": base_size - 1,
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.04,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": PALETTE["ink"],
            "axes.linewidth": 0.8,
            "axes.grid": mode in {"report", "slide", "diagnostic"},
            "grid.color": PALETTE["grid"],
            "grid.linewidth": 0.6,
            "grid.alpha": 1.0,
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def polish_axes(
    ax,
    *,
    grid_axis: str | None = "y",
    zero_line: str | None = None,
    profile: str = "modern_journal",
) -> None:
    """Apply lightweight polish shared by high-end economics figures."""
    colors = get_style_profile(profile)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.8)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.tick_params(axis="both", length=3.0, width=0.8)

    if grid_axis:
        ax.grid(axis=grid_axis, color=colors["grid"], lw=0.65)
        other = "x" if grid_axis == "y" else "y"
        ax.grid(axis=other, visible=False)

    if zero_line == "x":
        ax.axhline(0, color=colors["reference"], lw=0.8, ls=(0, (3, 2)), zorder=1)
    elif zero_line == "y":
        ax.axvline(0, color=colors["reference"], lw=0.8, ls=(0, (3, 2)), zorder=1)


def save_figure(
    fig: mpl.figure.Figure,
    path: str | Path,
    formats: Sequence[str] = ("png", "pdf", "svg"),
    dpi: int = 300,
) -> list[Path]:
    """Save a figure to multiple formats and return written paths."""
    base = Path(path)
    base.parent.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for ext in formats:
        out = base.with_suffix("." + ext.lstrip("."))
        kwargs = {"bbox_inches": "tight"}
        if ext.lower() in {"png", "jpg", "jpeg", "tif", "tiff"}:
            kwargs["dpi"] = dpi
        fig.savefig(out, **kwargs)
        written.append(out)
    return written


def _require_columns(data, columns: Iterable[str]) -> None:
    missing = [col for col in columns if col not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def plot_event_study(
    data,
    x: str,
    y: str,
    lo: str,
    hi: str,
    omitted: int | float | None = None,
    treatment_time: int | float = 0,
    ax=None,
    color: str = PALETTE["deep_blue"],
    ci_color: str = PALETTE["ci_gray"],
    ci_style: str = "rect",
    connect: bool = True,
    show_treatment_line: bool = True,
    profile: str = "reference_treatment_square",
    ci_width: float = 0.34,
    annotate_periods: bool = True,
):
    """Plot event-study estimates with clean paper-style uncertainty.

    Notes, omitted categories, fixed effects, clustering, and data sources
    should usually be reported in the caption or response text, not embedded
    inside the exported figure.
    """
    _require_columns(data, [x, y, lo, hi])
    if ci_style not in {"rect", "ribbon", "errorbar"}:
        raise ValueError("ci_style must be one of: rect, ribbon, errorbar")

    ax = ax or plt.subplots(figsize=(6.8, 4.0))[1]
    ordered = data.sort_values(x)
    colors = get_style_profile(profile)
    required_event_keys = {"pre_fill", "pre_line", "post_fill", "post_line", "reference", "grid"}
    if ci_style == "rect" and not required_event_keys.issubset(colors):
        colors = get_style_profile("reference_treatment_square")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color=colors.get("grid", "#E8EEF3"), lw=0.65)
    ax.grid(axis="x", visible=False)
    ax.axhline(0, color=colors.get("reference", PALETTE["reference_gray"]), lw=0.9, ls=(0, (6, 5)), zorder=1)
    if omitted is not None:
        ax.axvline(omitted, color=colors.get("reference", PALETTE["reference_gray"]), lw=0.9, ls=(0, (6, 5)), zorder=1)
    if show_treatment_line:
        ax.axvline(treatment_time, color=colors.get("reference", PALETTE["reference_gray"]), lw=0.9, ls=(0, (2, 6)), zorder=1)

    if ci_style == "rect":
        if omitted is None:
            pre_mask = ordered[x] < treatment_time
        else:
            pre_mask = ordered[x] < omitted
        post_mask = ordered[x] >= treatment_time

        for _, row in ordered.iterrows():
            xv = row[x]
            if omitted is not None and xv == omitted:
                continue
            is_post = xv >= treatment_time
            fill = colors["post_fill"] if is_post else colors["pre_fill"]
            rect = Rectangle(
                (xv - ci_width / 2, row[lo]),
                ci_width,
                row[hi] - row[lo],
                facecolor=fill,
                edgecolor="none",
                alpha=0.85,
                zorder=2,
            )
            ax.add_patch(rect)
        ax.autoscale_view()

        if connect:
            pre = ordered[pre_mask]
            post = ordered[post_mask]
            if len(pre):
                ax.plot(pre[x], pre[y], color=colors["pre_line"], lw=1.65, zorder=3)
            if len(post):
                ax.plot(post[x], post[y], color=colors["post_line"], lw=1.85, zorder=3)

        pre_points = ordered[pre_mask]
        post_points = ordered[post_mask]
        if len(pre_points):
            ax.scatter(
                pre_points[x],
                pre_points[y],
                marker="s",
                s=34,
                color=colors["pre_line"],
                edgecolor="white",
                linewidth=0.8,
                zorder=4,
            )
        if len(post_points):
            ax.scatter(
                post_points[x],
                post_points[y],
                marker="s",
                s=38,
                color=colors["post_line"],
                edgecolor="white",
                linewidth=0.8,
                zorder=4,
            )
        if omitted is not None:
            ax.scatter(
                [omitted],
                [0],
                marker="s",
                s=42,
                facecolor="white",
                edgecolor=colors.get("reference", PALETTE["reference_gray"]),
                linewidth=0.9,
                zorder=5,
            )
        if annotate_periods:
            ymin, ymax = ax.get_ylim()
            y_text = ymin + 0.93 * (ymax - ymin)
            if omitted is not None:
                ax.text(
                    omitted - 0.25,
                    y_text,
                    f"Reference ({omitted:g})",
                    ha="right",
                    va="top",
                    color=colors.get("reference", PALETTE["reference_gray"]),
                    fontsize=mpl.rcParams["font.size"] + 2,
                )
            ax.text(
                treatment_time + 0.25,
                y_text,
                "Treatment",
                ha="left",
                va="top",
                color=colors.get("reference", PALETTE["reference_gray"]),
                fontsize=mpl.rcParams["font.size"] + 2,
            )
    elif ci_style == "ribbon":
        ax.fill_between(
            ordered[x],
            ordered[lo],
            ordered[hi],
            color=ci_color,
            alpha=0.36,
            lw=0,
            zorder=2,
        )
        if connect:
            ax.plot(ordered[x], ordered[y], color=color, lw=1.15, zorder=3)
        ax.scatter(ordered[x], ordered[y], s=18, color=color, edgecolor="white", linewidth=0.35, zorder=4)
    else:
        yerr = [ordered[y] - ordered[lo], ordered[hi] - ordered[y]]
        ax.errorbar(
            ordered[x],
            ordered[y],
            yerr=yerr,
            fmt="o",
            ms=4.2,
            mfc=color,
            mec="white",
            mew=0.45,
            ecolor=color,
            elinewidth=1.0,
            capsize=2.5,
            capthick=0.9,
            zorder=3,
        )

    ax.set_xlabel("Event Time")
    ax.set_ylabel("Estimated Effect")
    return ax


def plot_coefficient_forest(
    data,
    label: str,
    estimate: str,
    lo: str,
    hi: str,
    ax=None,
    color: str = PALETTE["blue"],
):
    """Plot horizontal coefficient estimates with confidence intervals."""
    _require_columns(data, [label, estimate, lo, hi])
    ax = ax or plt.subplots(figsize=(4.8, 3.4))[1]
    ordered = data.reset_index(drop=True).iloc[::-1]
    y_pos = range(len(ordered))

    ax.axvline(0, color=PALETTE["ink"], lw=0.8)
    ax.hlines(y_pos, ordered[lo], ordered[hi], color=color, lw=1.2)
    ax.scatter(ordered[estimate], y_pos, color=color, s=24, zorder=3)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(ordered[label])
    ax.set_xlabel("Estimate")
    return ax


def add_note(fig: mpl.figure.Figure, note: str, fontsize: float | None = None) -> None:
    """Add a compact figure note beneath the plot."""
    fontsize = fontsize or max(mpl.rcParams["font.size"] - 1, 6)
    fig.text(0.0, -0.02, note, ha="left", va="top", fontsize=fontsize, color=PALETTE["gray"])

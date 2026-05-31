# econruc-figure skill

## 中文说明

`econruc-figure` 是面向经济学研究的图表制作 skill。它参考 `nature-figure` 的“先定义图表合约，再绘图，再 QA”的工作流，但服务对象从自然科学投稿图转向经济学论文图、政策报告图、组会图、实证诊断图和 replication package 图。

这个 skill 的核心目标不是把图做得“花”，而是让图表清楚服务一个经济学论点：研究问题是什么、识别或描述对象是什么、证据链在哪里、估计不确定性如何表达、图注和 notes 应该放在哪里。

---

## 适用场景

- 事件研究图、DID 动态效应图、政策冲击时间图
- 系数图、机制/异质性 coefficient forest、回归表转图
- binscatter、RD plot、趋势对比图、分布图
- 地图、分解图、热力图、矩阵图、结构性/反事实结果图
- 中文报告图、英文论文图、Beamer/slide 图、内部 diagnostic 图
- 将 Stata/R/Python 结果转成更高级、更干净、更适合论文或报告的图

---

## 与 nature-figure 的区别

`nature-figure` 更强调 Nature-tier 科学图、多面板实验结果、图像板、机制示意和投稿级 SVG/PDF 工作流。

`econruc-figure` 更强调经济学图表的学科约束：

- 识别逻辑优先：事件时间、处理时点、 omitted/reference category、固定效应、聚类标准误、带宽和样本口径要清楚。
- 论文图和报告图区分：论文图克制、干净、caption-ready；报告图可以有标题、副标题、政策窗口和更强视觉层级。
- Notes 默认不进图：长 notes、数据来源、固定效应、聚类、控制变量、样本限制应优先放在图注或聊天反馈中。
- 中文和英文分开维护：中文图要处理字体、标签长度、单位口径和中文报告阅读习惯；英文图要更接近 field-journal / Top5 seminar 的克制风格。
- 经济学图形族优先：event study、coefficient forest、binscatter、RD、DiD trend、decomposition、table-to-figure 等是核心对象。

---

## 工作流

### 1. 语言门槛

如果用户没有说明语言，先询问：

`请问这次图表用中文还是英文？`

中文和英文不是简单翻译关系。图题、坐标轴、单位、caption、notes 和字体布局都要按目标语言重新设计。

### 2. 后端门槛

支持 Python、R、Stata。

- 用户指定后端时，只使用该后端绘图、预览、导出和 QA。
- 数据或代码明显属于某个后端时，可以合理推断。
- 新建独立图默认使用 Python，除非 replication package 或用户偏好要求 R/Stata。
- 如果所选运行环境缺失，应报告 blocker，不要偷偷换后端渲染替代图。

### 3. Figure contract

绘图前先明确：

- Claim：图要支持的经济学结论
- Audience：论文、报告、slide、policy memo、教学或 diagnostic
- Mode：paper / report / slide / diagnostic
- Design context：处理组、事件时间、running variable、系数集、地理、时间、机制或分解
- Statistics：估计量、标准误、置信区间、固定效应、聚类、带宽、权重、omitted category
- Visual profile：modern journal、Chinese journal / Stata-like、report editorial、slide、diagnostic
- Export：PNG preview，PDF/SVG editable，必要时 TIFF
- Risks：双轴误导、样本口径不清、缺少不确定性、颜色暗示过强、图注缺失

### 4. 绘图与导出

优先复用：

- `scripts/econruc_style.py`
- `references/advanced-style-playbook.md`
- `references/chart-patterns.md`
- `references/visual-style.md`
- `references/paper-vs-report.md`

输出应包括图、代码或 patch、图注/notes、QA 说明。

---

## 中文模式

中文模式面向中文论文、中文报告、组会、政策图表和中文 Beamer。

设计重点：

- 中文字体要稳定显示，避免乱码和字形 fallback。
- 长中文标签要主动换行、缩短或改成横向布局。
- 单位和统计口径要明确，例如 `亿元`、`%`、`万吨`、`mg/kg`。
- 报告图可以使用更明确的标题和副标题。
- 论文图应更干净，长 notes 放到图注。
- 中文图不要机械套英文 Top5 图的标签习惯。

---

## English mode

English mode targets Top5/field-journal figures, seminar slides, replication packages, and international reports.

Design priorities:

- Use restrained journal styling: clean axes, sparse labels, clear uncertainty, and no decorative clutter.
- Keep figure notes caption-ready rather than embedded in the exported canvas.
- Use conventional economics labels such as `Treated`, `Control`, `Event time`, `Coefficient`, `95% CI`, `Reference`, `Bandwidth`, and `Outcome mean`.
- Make omitted categories, fixed effects, clustering, controls, and sample restrictions explicit in the caption or accompanying note.
- Prefer editable PDF/SVG for paper and slide workflows.

---

## 颜色系统

`econruc-figure` 应该有自己的稳定配色，而不是每次临时挑颜色。默认颜色来自 `scripts/econruc_style.py` 和 `references/visual-style.md`。

### 基础 palette

| 名称 | Hex | 用途 |
|---|---:|---|
| `ink` | `#222222` | 正文、坐标轴、主要文字 |
| `gray` | `#6B7280` | 次要文字、辅助标签 |
| `light_gray` | `#D1D5DB` | 弱分隔、浅色元素 |
| `grid` | `#E5E7EB` | 网格线、轻参考线 |
| `blue` | `#2F6B9A` | 常规主系列 |
| `deep_blue` | `#1F5A85` | 论文图主估计、核心线条 |
| `ci_gray` | `#BFC5CD` | 置信区间、误差带 |
| `reference_gray` | `#8A94A3` | 零线、基准线、政策时点 |
| `vermillion` | `#B64A3A` | 强调负向或对照变化 |
| `muted_red` | `#9D3F46` | 处理后、第二主系列、异质性对照 |
| `pre_fill` | `#9FB2C3` | 处理前 CI 或矩阵填充 |
| `post_fill` | `#CFA6A9` | 处理后 CI 或矩阵填充 |
| `event_pre_fill` | `#D4DDE4` | event-study 处理前 CI 矩形 |
| `event_pre_line` | `#71879A` | event-study 处理前线和点 |
| `event_post_fill` | `#EBD9DC` | event-study 处理后 CI 矩形 |
| `event_post_line` | `#A64049` | event-study 处理后线和点 |
| `green` | `#4F7F5A` | 正向机制、改善、绿色发展变量 |
| `gold` | `#B68A2D` | 报告图强调、第三系列、政策阶段 |

### 语义用色规则

- 主估计优先用 `deep_blue`，不要用高饱和蓝。
- 第二组或处理后效应用 `muted_red` / `event_post_line`，避免刺眼红。
- 不确定性优先用 `ci_gray` 或浅色 fill，不要让 CI 抢过点估计。
- 零线、政策线、reference period 用 `reference_gray`，必须弱于数据层。
- 分解图中正负号必须保持颜色语义一致，不要一张图里反复换含义。
- 多面板图按概念统一颜色，不按 panel 随机分配颜色。
- 中文报告图可以比论文图稍强，但仍避免彩虹色、渐变背景和大面积饱和红蓝。

---

## Style profiles

### `modern_journal`

默认英文论文图和大部分中文论文图使用这个 profile。

- primary: `#1F5A85`
- secondary: `#9D3F46`
- uncertainty: `#BFC5CD`
- reference: `#8A94A3`
- grid: `#EDF1F4`

适合：普通事件研究图、系数图、binscatter、RD、机制图、稳健性图。

### `reference_treatment_square`

默认 EconRUC event-study 风格，尤其适合用户要求“高级、像顶刊、不要 notes、不要 omitted baseline 横轴文字”的场景。

- pre CI fill: `#D4DDE4`
- pre line/point: `#71879A`
- post CI fill: `#EBD9DC`
- post line/point: `#A64049`
- reference lines: `#8A94A3`
- grid: `#E8EEF3`

视觉语法：

- 处理前用蓝灰，处理后用酒红。
- CI 用半透明竖向矩形或轻 ribbon。
- omitted/reference period 用空心点或在 caption 中说明，不写成横轴标签。
- 处理时点和 reference period 用轻虚线。
- 单一序列不放 legend。
- 不在图内放长 Notes。

### `stata_matrix`

用于中文经济学论文、异质性矩阵、处理前/处理后分组图、类似 Stata 风格但更精致的图。

- pre fill: `#9FB2C3`
- post fill: `#CFA6A9`
- pre point: `#1F5A85`
- post point: `#9D3F46`
- grid: `#E8F0F2`

适合：多 outcome、多容量组、多地区、多行业、多分位数的小面板图。

### `report_editorial`

用于政策报告、领导汇报、咨询式图表和更强调结论的中文/英文报告图。

- primary: `#1F5A85`
- secondary: `#B68A2D`
- uncertainty: `#BFC5CD`
- reference: `#8A94A3`
- grid: `#E7ECF1`

允许更明确标题、副标题、短 source note、政策区间和一两个结论性 annotation。

---

## 字体、字号和导出

### 字体

- 英文图：优先 `Arial` / `Helvetica` / `DejaVu Sans`。
- 中文图：优先使用系统可用中文无衬线字体，如 `Microsoft YaHei`、`SimHei`、`Noto Sans CJK SC`。
- SVG/PDF 应尽量保留可编辑文字；Python 中设置 `svg.fonttype = "none"`、`pdf.fonttype = 42`。

### 字号

| 输出场景 | 建议字号 | 说明 |
|---|---:|---|
| Paper figure | 7-9 pt | 适合论文正文或 appendix，少标题，多 caption |
| Report figure | 10-13 pt | 屏幕阅读，标题和单位更明确 |
| Slide figure | 16-24 pt | 远距离展示，减少系列和图例 |
| Diagnostic figure | 8-10 pt | 诚实展示问题，不追求装饰 |

### 导出

| 场景 | 默认导出 |
|---|---|
| 快速预览 | PNG, 300 dpi |
| 论文图 | PDF + SVG + PNG |
| 中文报告 | PNG + PDF |
| Beamer/slide | PDF/SVG 优先，必要时 PNG |
| 期刊特殊要求 | TIFF only when required |

---

## 快速模板

### Python

```python
from econruc_style import set_econruc_style, plot_event_study, polish_axes, save_figure

set_econruc_style(mode="paper")
ax = plot_event_study(
    df,
    x="event_time",
    y="coef",
    lo="ci_low",
    hi="ci_high",
    omitted=-1,
    treatment_time=0,
    ci_style="rect",
    profile="reference_treatment_square",
)
polish_axes(ax, zero_line="x", profile="modern_journal")
save_figure(ax.figure, "fig_event_study", formats=("png", "pdf", "svg"))
```

### R

```r
library(ggplot2)

econruc_theme <- function(base_size = 8, base_family = "Arial") {
  theme_classic(base_size = base_size, base_family = base_family) +
    theme(
      panel.grid.major.y = element_line(linewidth = 0.25, colour = "#EDF1F4"),
      panel.grid.minor = element_blank(),
      axis.line = element_line(linewidth = 0.35, colour = "#222222"),
      legend.position = "top",
      legend.title = element_blank()
    )
}
```

### Stata

```stata
* Recommended semantic colors
local deep_blue "31 90 133"
local muted_red "157 63 70"
local ci_gray "191 197 205"
local grid "237 241 244"

graph set window fontface "Arial"
set scheme s2color
```

Stata 图应优先使用 `assets/stata/econruc_graph_defaults.do`，并根据 paper/report/slide/diagnostic 模式调整字体、线宽、legend 和 notes。

---

## 常用图形族

| 图形族 | 典型用途 | 默认审美 |
|---|---|---|
| Event study | DID 动态效应、政策冲击前后 | 零线、处理时点、CI、reference period 清楚；不把 omitted baseline 写在横轴上 |
| Coefficient forest | 回归结果、机制、异质性 | 点估计 + CI，按结果或机制分组 |
| Binscatter | 条件相关、机制关系 | 明确 residualization、controls、binning |
| RD plot | 断点设计 | threshold、bandwidth、局部拟合分侧展示 |
| DiD trend | 处理组/对照组趋势 | 政策时点、基期标准化、pre-trend 可读 |
| Distribution | 分布、异质性、尾部变化 | CDF/density/histogram，避免装饰性填充 |
| Map | 地理差异、政策覆盖 | 有意义分组、克制边界、避免因果暗示 |
| Decomposition | 分解、贡献率、反事实 | sign logic 清楚，颜色数量有限 |
| Table-to-figure | 回归表转图 | 把密集表格转成系数图或 specification curve |

---

## 高级感检查清单

一张经济学图看起来“高级”，通常不是因为元素更多，而是因为图形纪律更强。交付前检查：

- 是否只有一个主视觉结论？
- 是否能在 3 秒内看出处理时点、方向和不确定性？
- 是否删除了图内长 notes、重复 legend、无意义 subtitle？
- 零线、网格线、reference line 是否弱于数据层？
- 颜色是否有语义，而不是为了好看随机分配？
- 多面板是否共享坐标轴、图例和颜色含义？
- caption 是否说明 omitted category、样本、FE、controls、clustering 和数据来源？
- PNG 缩略图能否读，PDF/SVG 是否可编辑？
- 中文标签是否拥挤，英文标签是否过长？
- 图的审美是否匹配输出场景：paper、report、slide 或 diagnostic？

---

## 文件结构

```text
econruc-figure/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── stata/
│       └── econruc_graph_defaults.do
├── references/
│   ├── advanced-style-playbook.md
│   ├── chart-patterns.md
│   ├── econ-figure-contract.md
│   ├── paper-vs-report.md
│   ├── replication-and-audit.md
│   └── visual-style.md
└── scripts/
    └── econruc_style.py
```

---

## 维护建议

- `SKILL.md` 只放核心工作流、触发规则和必须遵守的约束。
- 图形细节、风格范式、图形族说明放到 `references/`。
- 可复用绘图逻辑放到 `scripts/econruc_style.py`。
- Stata 默认图形风格放到 `assets/stata/econruc_graph_defaults.do`。
- 中文模式和 English mode 分开更新，不要把一边当作另一边的翻译。
- 每次根据用户反馈修改图表审美时，把可复用经验沉淀到 `advanced-style-playbook.md` 或 `visual-style.md`。

---

## English Overview

`econruc-figure` is an economics visualization skill for paper figures, policy-report figures, seminar slides, diagnostic plots, and replication-ready outputs. It adapts the contract-first discipline of `nature-figure` to economics: start from the claim, map the evidence, respect identification logic, disclose uncertainty, and export clean figures with caption-ready notes.

It is especially useful for event studies, coefficient plots, binscatters, RD plots, DiD trend plots, maps, decompositions, table-to-figure conversions, and multi-panel economics figures.

The skill maintains two separate language modes. Chinese mode is designed for Chinese papers, reports, group meetings, policy figures, and Chinese Beamer decks. English mode is designed for Top5/field-journal figures, international seminars, and replication packages. The two modes should be maintained separately rather than translated sentence by sentence.

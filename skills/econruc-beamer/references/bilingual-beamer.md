# Bilingual Beamer

Use for Chinese, English, or mixed Chinese-English economics presentations.

## Language strategy

- For international seminars, use English slides and optional Chinese planning notes.
- For Chinese seminars, use Chinese slide titles with precise economics terminology.
- For bilingual rooms, keep slide text in one primary language and use speaker notes or short parenthetical translations for key terms.

## Chinese terms

| Chinese | English |
|---|---|
| 研究问题 | research question |
| 识别策略 | identification strategy |
| 反事实 | counterfactual |
| 机制 | mechanism or channel |
| 异质性 | heterogeneity |
| 稳健性 | robustness |
| 外部有效性 | external validity |
| 福利成本 | welfare cost |
| 政策含义 | policy implication |
| 内生性 | endogeneity |
| 工具变量 | instrumental variable |
| 固定效应 | fixed effects |
| 双重差分 | difference-in-differences |
| 事件研究 | event study |
| 断点回归 | regression discontinuity |
| 合成控制法 | synthetic control |
| 倾向得分匹配 | propensity score matching |
| 聚类标准误 | clustered standard errors |
| 安慰剂检验 | placebo test |
| 平行趋势 | parallel trends |
| 处理效应 | treatment effect |
| 局部平均处理效应 | local average treatment effect |
| 基准回归 | baseline specification |
| 样本选择 | sample selection |
| 测量误差 | measurement error |
| 反事实路径 | counterfactual path |
| 福利分析 | welfare analysis |
| 校准 | calibration |
| 反事实模拟 | counterfactual simulation |

## XeLaTeX setup

Use XeLaTeX for CJK:

```tex
\usepackage{fontspec}
\usepackage{xeCJK}
\setmainfont{Arial}
\setsansfont{Arial}
\setCJKmainfont{Microsoft YaHei}
```

If Microsoft YaHei is unavailable, use SimHei, SimSun, Noto Sans CJK SC, or another installed CJK font.

## Chinese slide style

- Keep titles short.
- Avoid government-report filler such as `重要意义`, `赋能`, `高质量发展` unless the deck is explicitly a policy report.
- Use concrete economic language: `估计结果表明`, `识别依赖于`, `机制分析显示`, `这一解释受到...限制`.

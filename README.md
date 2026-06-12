# econruc-skill

该Skill由中国人民大学应用经济学院能源经济系部分同学开发维护。目前Figure由杨玉刚开发维护，Translate由魏歆嘉同学开发维护。

## 中文说明

`econruc-skill` 是一套面向经济学研究的 Codex skills，参考 `nature-skills` 的组织方式，但内容转向经济学论文写作、引言构思、图表制作、实证识别、数据整理、文献定位、审稿回复和 Beamer 汇报。它的目标不是替代研究者判断，而是把经济学论文中反复出现的高频任务变成可复用的工作流。

### 技能列表

- `econ-intro`：专门帮助撰写、诊断和重构经济学论文引言，兼顾英文 Top5/领域顶刊和中文顶级期刊风格。
- `econruc-writing`：起草和重构经济学论文、政策报告、摘要、结果段、讨论段和中英文研究文本。
- `econruc-report-writing`：撰写研报、政策分析、产业分析和咨询报告，强调真实数据、来源可追溯、结构清晰和逻辑可靠。
- `econruc-polishing`：润色中英文经济学学术写作，使表达更接近 Top5 和领域顶刊风格。
- `econruc-translate`：把英文经济学论文、工作论文和 PDF 逐句翻译成中文，保留结构、脚注、公式、引用和图表标题，并可生成 TeX/PDF。
- `econruc-reader`：阅读经济学论文，生成结构化笔记、批判性问题、图表解读和复现备忘录。
- `econruc-data`：进行数据检索、清洗审计、变量字典和可复现数据管线设计。
- `econruc-figure`：制作报告图和论文图，包括事件研究、系数图、binscatter、RD 图、地图和分解图等。
- `econruc-empirical`：审查识别策略、稳健性、机制检验、异质性分析和实证结果表述。
- `econruc-literature`：搭建文献地图、贡献定位和相关文献综述。
- `econruc-response`：撰写审稿意见回复、修回说明和编辑信。
- `econruc-beamer`：把经济学论文转化为精致的 LaTeX Beamer 汇报。

### 使用建议

- 写论文主体或章节结构时，用 `econruc-writing`。
- 写研报、政策分析、产业分析或咨询报告时，用 `econruc-report-writing`。
- 只处理引言、研究动机、贡献段或 introduction 结构时，用 `econ-intro`。
- 图表任务从 `econruc-figure` 开始；如果数据还没有整理好，先用 `econruc-data`。
- 识别策略、稳健性、机制和异质性问题，用 `econruc-empirical`。
- 文献综述和贡献定位，用 `econruc-literature`。
- 论文转 Beamer 汇报，用 `econruc-beamer`。

### 中英文双模式维护

每个 skill 都包含独立的 `中文模式` 和 `English mode`。两者不是逐句翻译关系，而是分别服务于中文论文/报告/组会和英文 Top5/领域顶刊/国际 seminar 场景。后续维护时，请分别更新中文和英文规则：中文侧重问题意识、制度背景、政策含义和中文学术表达；英文侧重经济学问题、识别/模型、贡献定位、证据强度和 journal-facing prose。

### README 维护规范

每个 skill 文件夹都应保留一个 `README.md`，作为给研究者和后续维护者看的入口。`SKILL.md` 负责触发规则和执行约束，`README.md` 负责解释定位、使用边界、中文/英文模式、文件结构、维护建议和可复用规范。新增 skill 或大幅调整 skill 时，应同步更新对应 README。

### 本地安装

把 `skills/` 下的每个文件夹复制到：

`C:\Users\admin\.codex\skills`

然后重启 Codex，让新的 skill 列表生效。

### Windows PowerShell 安装

```powershell
git clone https://github.com/yangyugang1218/econruc-skills.git
$src = ".\econruc-skills\skills\*"
$dst = "$env:USERPROFILE\.codex\skills"
Copy-Item -Path $src -Destination $dst -Recurse -Force
```

### macOS / Linux 安装

```bash
git clone https://github.com/yangyugang1218/econruc-skills.git
mkdir -p ~/.codex/skills
cp -R econruc-skills/skills/* ~/.codex/skills/
```

### 更新方法

如果已经 clone 过仓库，可以进入仓库目录后拉取更新，再复制到 Codex skills 目录。

```powershell
cd econruc-skills
git pull
Copy-Item -Path ".\skills\*" -Destination "$env:USERPROFILE\.codex\skills" -Recurse -Force
```

### 维护者一键同步

仓库根目录可以保留本地上传脚本，例如 `一键上传到GitHub.bat` 或 `upload-econruc-skills.ps1`。维护者更新流程应是：

1. 从 `%USERPROFILE%\.codex\skills` 同步最新的 `econ-*` / `econruc-*` skills 到仓库 `skills/`。
2. 检查 `README.md`、`SKILL.md`、`references/`、`scripts/` 和 `assets/` 是否一致。
3. 确认没有 `outputs/`、`__pycache__/`、`.pyc`、LaTeX 编译产物或临时图像进入提交。
4. 提交并推送到 GitHub。

### 设计原则

- 先确定任务契约：目标、语言、证据、输出类型和缺失信息。
- 不编造数据、引用、制度事实、回归结果或稳健性检验。
- 区分描述性证据、设计型因果识别、结构模型解释和政策推断。
- 重要结论必须说明证据状态和边界。
- 中文和英文不是互译关系，而是两套不同的学术表达系统。
- 输出前做 QA：检查因果语言、样本/变量定义、来源、图表可读性和复现风险。

### 推荐研究工作流

1. `econruc-reader`：读论文、拆研究问题、找贡献和识别逻辑。
2. `econruc-literature`：整理文献地图和贡献定位。
3. `econruc-data`：准备数据、变量字典和清洗审计。
4. `econruc-empirical`：设计识别策略、稳健性和机制检验。
5. `econruc-figure`：制作图表和可视化证据。
6. `econruc-writing` / `econ-intro`：起草论文段落和引言。
7. `econruc-report-writing`：把数据、政策背景和证据链转成研报、政策分析或咨询报告。
8. `econruc-polishing`：压缩语言、校准因果表达。
9. `econruc-beamer`：转成学术汇报。
10. `econruc-response`：用于审稿意见回复和修回。

## English Overview

`econruc-skill` is a collection of Codex skills for economics research. It follows the modular layout of `nature-skills`, but adapts the workflows to economics writing, introduction development, empirical design, data work, figure production, literature positioning, referee responses, and LaTeX Beamer presentations.

The suite is designed for research assistance rather than automatic paper generation. It helps researchers make the economic question, identification logic, evidence, contribution, and language choices explicit.

### Skills

- `econ-intro`: draft, diagnose, and restructure economics paper introductions in English or Chinese, with Top5, field-journal, and Chinese top-journal conventions.
- `econruc-writing`: draft and structure economics papers, reports, abstracts, results sections, discussions, and bilingual research prose.
- `econruc-report-writing`: draft sourced policy reports, industry research reports, consulting-style reports, market studies, and briefing memos with verified data and clear logic.
- `econruc-polishing`: polish English and Chinese economics writing in a Top5 and leading field-journal style.
- `econruc-translate`: translate English economics papers, working papers, and PDFs into faithful Simplified Chinese while preserving structure, footnotes, equations, citations, and figure/table captions.
- `econruc-reader`: read economics papers and produce structured notes, critiques, seminar questions, figure/table interpretations, and replication memos.
- `econruc-data`: find, clean, audit, and document economics datasets before analysis or visualization.
- `econruc-figure`: create report and paper figures, including event studies, coefficient plots, binscatter, RD plots, maps, and decomposition charts.
- `econruc-empirical`: audit identification, robustness, mechanisms, heterogeneity, and empirical-result presentation.
- `econruc-literature`: build literature maps, contribution statements, and related-work sections.
- `econruc-response`: draft economics referee responses, revision memos, and editor letters.
- `econruc-beamer`: convert economics papers into polished LaTeX Beamer seminar decks.

### Recommended Use

- Use `econ-intro` when the task is specifically about an introduction, opening section, research motivation, contribution paragraph, or puzzle-to-design narrative.
- Use `econruc-writing` for broader paper drafting and section-level writing.
- Use `econruc-data` before `econruc-figure` when the dataset still needs discovery, cleaning, auditing, or documentation.
- Use `econruc-empirical` for identification and robustness questions.
- Use `econruc-literature` for contribution positioning and related-work synthesis.
- Use `econruc-beamer` for paper-to-slides workflows.

### Chinese and English Maintenance Modes

Each skill now contains separate `中文模式` and `English mode` guidance. These modes are not direct translations. The Chinese mode is designed for Chinese papers, reports, group meetings, grant writing, and Chinese journal conventions. The English mode is designed for Top5/field-journal writing, international seminars, replication packages, and journal-facing prose. When maintaining the suite, update the two modes separately rather than translating one into the other.

### README Maintenance Standard

Every skill folder should include a `README.md` for researchers and future maintainers. `SKILL.md` defines trigger rules and execution constraints; `README.md` explains positioning, use boundaries, Chinese/English modes, file structure, maintenance guidance, and reusable conventions. When adding or substantially revising a skill, update its README at the same time.

### Local Installation

Copy every folder under `skills/` into:

`C:\Users\admin\.codex\skills`

Restart Codex after installation so the updated skills are loaded.

### Install With PowerShell

```powershell
git clone https://github.com/yangyugang1218/econruc-skills.git
$src = ".\econruc-skills\skills\*"
$dst = "$env:USERPROFILE\.codex\skills"
Copy-Item -Path $src -Destination $dst -Recurse -Force
```

### Update

```powershell
cd econruc-skills
git pull
Copy-Item -Path ".\skills\*" -Destination "$env:USERPROFILE\.codex\skills" -Recurse -Force
```

### Design Principles

- Start from a task contract: objective, language, evidence, output type, and missing inputs.
- Do not invent data, citations, institutional facts, regression results, or robustness checks.
- Distinguish descriptive evidence, design-based causal claims, structural interpretation, and policy inference.
- Keep Chinese and English modes separate.
- Run QA before delivery: causal language, sample and variable definitions, sources, figure readability, and replication risks.

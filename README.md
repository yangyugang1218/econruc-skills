# EconRUC Skills

EconRUC Skills 是一组面向经济学研究工作流的 Codex skills，覆盖论文写作、语言润色、实证设计、数据整理、文献定位、论文阅读、审稿回复、图表制作和 Beamer 汇报等任务。

这些 skills 的设计目标是让 Codex 在处理经济学任务时更像研究合作者：先识别研究问题、证据链和识别边界，再生成文字、图表、数据管线或演示材料。

## 包含的 Skills

| Skill | 用途 |
|---|---|
| `econruc-writing` | 起草、重构和规划经济学论文、摘要、引言、结果、讨论和政策报告文本 |
| `econruc-polishing` | 润色、翻译和压缩中英文经济学学术表达，校准因果语言和贡献表述 |
| `econruc-empirical` | 设计、审查和解释实证策略，包括 DiD、事件研究、IV、RD、RCT、面板固定效应等 |
| `econruc-data` | 查找、清洗、合并、审计和记录经济学数据，准备复现包和图表数据 |
| `econruc-literature` | 构建文献综述、贡献定位、相关工作段落和领域地图 |
| `econruc-reader` | 阅读和拆解经济学论文，提取问题、贡献、识别、数据、结果和研讨问题 |
| `econruc-response` | 起草和优化审稿意见回复、修回信、逐点回复和 revision memo |
| `econruc-figure` | 制作经济学论文、报告和幻灯片图表，包括事件研究图、系数图、时间序列、地图、分解图等 |
| `econruc-beamer` | 将经济学论文、报告或研究笔记转成 LaTeX Beamer 学术汇报 |
| `econruc-paper2ppt` | 旧版/兼容型论文转 PPT skill，保留用于已有工作流 |

## 安装方法

将本仓库的 `skills` 目录复制到 Codex 的 skills 目录。

### Windows PowerShell

```powershell
git clone https://github.com/yangyugang1218/econruc-skills.git
$src = ".\econruc-skills\skills\*"
$dst = "$env:USERPROFILE\.codex\skills"
Copy-Item -Path $src -Destination $dst -Recurse -Force
```

### macOS / Linux

```bash
git clone https://github.com/yangyugang1218/econruc-skills.git
mkdir -p ~/.codex/skills
cp -R econruc-skills/skills/* ~/.codex/skills/
```

安装后，重启 Codex 或开启新会话，使 skills 重新加载。

## 更新方法

如果已经 clone 过仓库，可以进入仓库目录后拉取更新，再复制到 Codex skills 目录。

### Windows PowerShell

```powershell
cd econruc-skills
git pull
Copy-Item -Path ".\skills\*" -Destination "$env:USERPROFILE\.codex\skills" -Recurse -Force
```

### macOS / Linux

```bash
cd econruc-skills
git pull
cp -R skills/* ~/.codex/skills/
```

## 维护者：一键同步并上传

本仓库根目录提供两个 Windows 一键脚本：

- `首次上传到GitHub.bat`：第一次把本地仓库覆盖上传到 GitHub 时使用。适合远端仓库只有 GitHub 自动生成的初始 README 的情况。
- `一键上传到GitHub.bat`：后续日常更新使用。

脚本会自动完成：

1. 从 `%USERPROFILE%\.codex\skills` 同步最新的 `econruc-*` skills 到本仓库的 `skills/`。
2. `git add` 所有变更。
3. 自动生成一次 commit。
4. 推送到 `https://github.com/yangyugang1218/econruc-skills`。

第一次运行时，如果 GitHub 要求登录，请在弹出的 GitHub / Git Credential Manager 窗口中授权。授权成功后，后续通常只需要双击 `一键上传到GitHub.bat`。

## 使用方法

在 Codex 中直接提到 skill 名称，或提出与 skill 描述匹配的任务即可触发。

示例：

```text
[$econruc-writing] 帮我根据这些回归结果写一段 Results section。
```

```text
[$econruc-empirical] 帮我审查这个 DID 设计，重点看识别假设和稳健性。
```

```text
[$econruc-figure] 用 R 画一张事件研究图，要求论文风格。
```

```text
[$econruc-reader] 帮我读这篇 NBER working paper，整理研究问题、识别策略、主要结果和 seminar questions。
```

```text
[$econruc-response] 根据这些审稿意见，帮我写英文逐点回复。
```

## 设计原则

这些 skills 共同遵循几条规则：

- 先确定任务契约：目标、语言、证据、输出类型和缺失信息。
- 不编造数据、引用、制度事实、回归结果或稳健性检验。
- 区分描述性证据、设计型因果识别、结构模型解释和政策推断。
- 重要结论必须说明证据状态和边界。
- 中文和英文不是互译关系，而是两套不同的学术表达系统。
- 输出前做 QA：检查因果语言、样本/变量定义、来源、图表可读性和复现风险。

## 推荐工作流

一个完整的经济学研究工作流可以按如下方式串联：

1. `econruc-reader`：读论文、拆研究问题、找贡献和识别逻辑。
2. `econruc-literature`：整理文献地图和贡献定位。
3. `econruc-data`：准备数据、变量字典和清洗审计。
4. `econruc-empirical`：设计识别策略、稳健性和机制检验。
5. `econruc-figure`：制作图表和可视化证据。
6. `econruc-writing`：起草论文段落。
7. `econruc-polishing`：压缩语言、校准因果表达。
8. `econruc-beamer`：转成学术汇报。
9. `econruc-response`：用于审稿意见回复和修回。

## 目录结构

```text
econruc-skills/
  README.md
  skills/
    econruc-writing/
      SKILL.md
      references/
      agents/
    econruc-figure/
      SKILL.md
      references/
      scripts/
      assets/
    ...
```

每个 skill 至少包含一个 `SKILL.md`。部分 skills 还包含：

- `references/`：按需加载的详细规则、模板和清单。
- `scripts/`：可复用脚本。
- `assets/`：模板、样式或其他资源。
- `agents/openai.yaml`：Codex UI 元数据。

## 注意事项

- 本仓库提供的是 Codex skill 工作流，不是 Python/R/Stata 包。
- 对于需要最新数据、法律政策、统计口径或文献检索的任务，应验证来源和日期。
- 对于需要渲染图表、Beamer 或处理文档的任务，本地环境仍需安装相应运行时和依赖。
- 如果将本仓库公开分享，建议后续补充明确的开源许可证。

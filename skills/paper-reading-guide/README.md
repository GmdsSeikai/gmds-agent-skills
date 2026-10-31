# paper-reading-guide：轻量陪读与复述

基于 [fuxiao13/paper-reading-guide](https://github.com/fuxiao13/paper-reading-guide) 的主版，沿用 MIT 许可，保留领域速查表和两个 PDF 辅助脚本。

## 入口

- `$paper-reading-guide 读这篇论文：<路径或链接>`：先选择模式。
- `$paper-reading-guide 陪读模式，读这篇论文：<路径或链接>`：围绕一个概念或因果链讲解，按需补基础和深入，可跳转、回退或跳过理解检查。
- `$paper-reading-guide 复述模式，我先讲这篇论文：<路径或链接>`：用户先复述，助手对照原文反馈，按需追问。
- 有论文上下文的具体公式、算法或实验问题：直接回答，不要求先选模式，也不重置同篇阅读进度。
- 对话中说“切到陪读模式”或“切到复述模式”：保留进度并切换。

重要结论与纠错定位原文，区分作者主张、实验支持、助手推断；区分未找到、无法核实与已检查但未说明。生成图片后还须实际查看，才可判断图中趋势。

默认只聊天。“总结／整理一下”在对话里回应；明确要求保存或导出时才按指定范围、位置和长度写文件，避免覆盖。只有明确要求写 Obsidian 才触碰其库；阅读状态留在当前对话，不擅自写长期记忆。回顾时按需区分已独立复述、提示后复述与尚未检验，不把听过或跳过当作掌握。

## 文件

- `SKILL.md`：入口与共同规则。
- `references/three-pass-reading.md`：可跳转的阅读深度、补基础与教学建议。
- `references/retelling-mode.md`：复述流程。
- `references/evidence-rules.md`：证据、未知状态与图表核对。
- `references/summary-template.md`：小结模板。
- `references/domains/`：上游领域速查表。
- `scripts/`：上游 PDF 结构提取与页渲染；可选依赖见 `requirements.txt`。
- `LICENSE`：上游 MIT 许可与署名。

本目录包含定制版的阅读流程、领域速查表与 PDF 工具。合并上游更新时需保留定制的交互与写入边界。

## PDF 工具环境

仅聊天阅读已提供的正文不需要 Python。处理本地 PDF 时，在独立 Python 环境中安装 `requirements.txt`，使用能导入 PyMuPDF 的解释器；脚本路径相对本 skill 目录解析。

```text
python -m pip install -r <skill目录>/requirements.txt
python <skill目录>/scripts/extract_outline.py <论文路径>
python <skill目录>/scripts/render_page.py <论文路径> 2,4 --out <任务输出目录>
```

上述 `python` 应替换为所选环境的解释器路径；含空格的路径按所用 shell 引用，Windows 可加 `-X utf8` 避免终端编码问题。提取只用于定位；判断公式或图表时还需查看原始页面。

可选：在安装后的 skill 目录创建 `local-runtime.md`，记录本机解释器和调用方式。主入口会在运行 PDF 脚本前读取该文件；未配置时选择能导入 PyMuPDF 的 Python。此文件包含机器相关配置，已由本目录 `.gitignore` 排除，不随仓库发布。

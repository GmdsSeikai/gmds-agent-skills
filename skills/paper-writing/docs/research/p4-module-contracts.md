# P4 · 模块边界与交接

2026-11-19 调研快照，依据 PaperOrchestra 的 `d9bae99`。文中的仓库、CLI 和环境检查指调研当时的上游与本机环境。后续实测见[验收汇总](../validation.md)。

**P4 建议采用一个 Skill 入口，支持按阶段开始、续接和局部重跑。** 阶段之间靠项目文件交接。首版最值得固定的是三条边界：大纲初稿与带引用的大纲各有版本，引用映射与 BibTeX 成套交付，作者当前稿和生成候选分开保存。原项目的五个 Agent 可以作为职责划分的参考，Skill 的公开入口按用户实际要完成的任务设计。

## 原项目的生产与消费链

以下是本地 `main`、提交 `d9bae99` 的源码核对。CLI 在原始材料与模板就位后进入两个写作分支。关绘图时直接复制提供的图，再依次运行大纲、文献、整稿和修订。开绘图时，文献与绘图并行读取同一份原始大纲，两路返回、图文清单写出、文献产物复制到位后，才开始整稿。 [README.md](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/README.md#L53) · [CLI 入口](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/paper_writing_cli.py#L141) · [关绘图流程](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/paper_writer.py#L50) · [开绘图流程](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/paper_writer_with_plotting.py#L114)

| 交接 | 已实现的字段、顺序和消费者 |
| --- | --- |
| **大纲** | `OutlineAgent` 从想法、实验日志、模板和会议指南生成 `outline.json`。提示约定三组字段：`plotting_plan` 含 `figure_id`、`title`、`plot_type`、`data_source`、`objective`、`aspect_ratio`。`intro_related_work_plan` 含引言的背景、缺口与搜索方向，以及相关工作的技术类目、搜索问题和衔接点。`section_plan` 含章节、子节、内容要点与 `citation_hints`。绘图读取 `plotting_plan`，文献据其余两部分构造检索任务。程序解析 JSON 后直接写出，字段约束主要来自提示词。 [大纲生成](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/outline_agent.py#L30) · [大纲字段](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/prompts/outline_agent.py#L82) · [文献读取](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/literature_review_agent.py#L211) |
| **引用与半成品模板** | 文献阶段先生成 `references.bib` 并消解重复键，再用最终键生成 `citation_map.json` 和 `outline_v1.json`。映射按引用键索引，条目含 `citation_key`、`title`、`authors`、`venue`、`year`、`abstract`。增强大纲加入 `citation_candidates`，并从其他章节的子节移除 `citation_hints`。引言与相关工作由模型写入完整的 `updated_template.tex`，只填这两节是提示约束。四件文件分别写出，随后编排器以增强大纲**覆盖**根目录的 `outline.json`，并替换工作目录中的模板和 BibTeX。整稿读取增强大纲、半成品模板和映射，修订也读取映射，编译通过模板中的 `\bibliography{references}` 读取 BibTeX。 [产出顺序](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/literature_review_agent.py#L132) · [字段与落盘](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/literature_review_agent.py#L540) · [大纲改写](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/literature_review_agent.py#L268) · [模板写作约束](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/prompts/literature_review_agent.py#L17) · [覆盖与交接](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/paper_writer.py#L121) · [CVPR 模板](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/templates/cvpr2025/template.tex#L67) |
| **图文清单** | 绘图结果按并发完成顺序汇入 `plotting_results.json`，记录图 ID、标题、类型、描述、图注、宽高比、评审历史和落盘成功时的 `image_path`。前端图库读这份文件。编排器只搬运路径实际存在的图，并投影为 `latex_writeup/figures/info.json` 的 `[{name, caption}]`。整稿读取清单，存在的栅格图还会进入模型输入，PDF 图只进文字清单。关闭绘图时 `info.json` 随原始图目录复制。当前前端保存上传图时只写图片，图库里填写的图注没有写进这份清单。 [绘图产物](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/plotting_agent.py#L192) · [清单生成](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/paper_writer_with_plotting.py#L160) · [整稿读图](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/section_writing_agent.py#L81) · [图库读取](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L228) · [上传图写盘](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L405) |
| **整稿与修订** | 整稿读取上述材料、想法、实验日志和指南，返回整份 LaTeX 并写 `latex_writeup/raw_draft_paper.tex`。保留模板已有文字依赖提示词。编排器复制 LaTeX 目录到修订工作区，先编译 `initial_draft.tex/.pdf`，再产生 `refined_paper_vN.tex/.pdf`，最后进入排版。内容日志按 `vN` 记录轮次、修改计划、前后分数、差值及采纳结果，排版日志记录反馈和编译采纳结果。实际选定的 TeX/PDF 写到 `content_refinement_workdir/final_refined_paper.*`，PDF 再复制到根目录 `final_paper.pdf`。 [整稿读写](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/section_writing_agent.py#L128) · [工作区复制](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/paper_writer.py#L153) · [初稿编译](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/content_refinement_agent.py#L201) · [内容日志与采纳](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/content_refinement_agent.py#L357) · [排版与最终产物](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/content_refinement_agent.py#L535) |

**覆盖与失败路径。** 同一输出目录重跑会先删除 `latex_writeup` 和根目录最终 PDF，进入修订时还会重建修订工作区。CLI 在输入与目标材料目录不同时，会替换目标 `raw_materials`。异常触发最多三次整轮重试，批处理的日志按论文记录结果，暂无可续接的阶段提交。文献的部分检索失败会退成空结果，单图失败可能被跳过，整稿读取缺失或损坏的清单会退成空值，某些读取异常则返回错误字符串，而调用方没有检查该返回值。初稿编译无 PDF 会中止修订，后续候选失败会沿用最近接受的版本。编译辅助函数以产出 PDF 且无超时为主要判断，因此文件存在不足以证明编译、引用与内容均通过。管线耗尽重试返回 `False` 时，CLI 未把它转成非零退出码，前端却用退出码 `0` 标记流程走完。 [CLI 材料复制](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/paper_writing_cli.py#L101) · [写作重试](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/paper_writer.py#L192) · [文献失败分支](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/literature_review_agent.py#L305) · [绘图失败分支](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/plotting_agent.py#L239) · [整稿读取与返回](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/methods/agents/section_writing_agent.py#L67) · [编译判断](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/utils/pdf_utils.py#L169) · [前端退出码判断](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L457)

**续写时需要核对导出的来源。** 前端页面 ZIP 直接打包 `latex_writeup`，邮件 ZIP 才会用修订稿替换为 `main.tex`，因此页面上的最终 PDF 和源码 ZIP 可能来自不同阶段。修订页也会取第一条接受的内容轮次展示，并以最高排版轮次标示最终版，展示结果可能偏离实际采纳。旧版导入时应记录每个文件的来源，先确认作者持有的当前稿。 [页面下载](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L801) · [邮件打包](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L468) · [修订页选版](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L963) · [排版页选版](https://github.com/google-research/paper-orchestra/blob/d9bae997e793a015ed38bb1605be9eb58c00284f/frontend/app.py#L1052)

## 建议的最小交接

在项目目录放一份人可读的清单，记录 `schema_version`、原始材料和模板的版本、各阶段状态、输入版本、相对产物路径、当前采用的稿件版本，以及待确认事项。每次生成先写新候选，验证后再更新采用版本。输入变更时将受影响产物标为过期，供对照或回退。续接发现文件缺失、版本不符或作者在此期间再次编辑时，保留当前稿，将冲突落到具体文件或段落。

- **规划**保留初始大纲和引用增强大纲，给段落、图、表使用稳定标识。关键数字记录来源位置及复用位置，供局部重跑判断影响范围。
- **引用与图文**各自提交一组完整产物。引用组包含增强大纲、映射、BibTeX 和半成品模板，用已有键续写并检查引用能解析。图文组记录图 ID、文件、图注、来源和处理状态。计划有图但生成失败时，续接能指出缺哪张图。
- **整稿与修订**以作者当前 TeX 为续写基准，记录生成候选基于哪个版本。按段落应用修改，对作者与生成同时改过的段落做三方比较，冲突交给作者选。导出时从同一个采用版本取 TeX、BibTeX、图片和 PDF，检查引用、图文件和编译结果再标记可交付。旧项目可用导入步骤建立初始基准，缺失元数据的项目先确认当前稿和素材对应关系。

## 三个纸面案例

| 场景 | 最小交接、重跑与保留策略 |
| --- | --- |
| **实验日志更正一个数字** | 假设主结果从 `91.4%` 改为 `90.4%`。先登记日志位置及指标、数据集、单位，检查结果表、相关图与图注、摘要、引言、结论和由该值推导的提升幅度或排名。只重跑受影响的图表和文字，再编译与核对。若数值改变核心主张，回到相应大纲节点及受影响的引言段落。只要研究范围和引用需求仍成立，直接复用原引用组。没有完整来源映射时，先全稿找旧值和派生说法，确认影响范围后再应用补丁。 |
| **作者手改引言后继续写** | 以作者稿为当前版本，保留上次生成稿作为比较基准。只续写其他章节时复用作者的引言。需要调整引言中的一项主张时，提出局部补丁并保留其余改动。作者和候选同时改到同一句时，展示基准、作者版本和候选版本，由作者决定。作者新增的 `\cite` 键也要同步纳入引用组。 |
| **切换会话后继续写** | 新会话读取项目清单和当前稿，核对引用组、图文组、输入版本及待确认事项。若方法已采纳、实验段待写、某张图缺失，就从实验段续接并保留缺图记录。只重跑缺图及依赖它的内容。只有 PDF 时可供查阅，恢复可编辑续写还需要当前 TeX 及其引用、图片和模板依赖。 |

## Skill 入口取舍

| 方案 | 适用方式与代价 |
| --- | --- |
| **一个入口，多阶段** | 用户可说“从实验段继续”“只更新图 2”“基于我改过的引言重新编译”。由同一入口读取当前版本、检查依赖和确定重跑范围。首版只需维护一套交接规则，阶段仍可选择执行。 |
| **多个可独立调用的 Skill** | 当用户反复带自己的材料进来，只做引用整理、图文处理或改稿时，可将对应阶段单独暴露。每个入口都需要识别同一份项目清单、处理旧版本和缺失输入，并遵守相同的采用与覆盖规则。适合等独立使用场景明确后再拆入口。 |

**验证范围与文件清单。** 本次证据来自本地源码和文档，三个案例均为纸面推演。模型实际输出、LaTeX 真编译、故障中断后续接、作者编辑冲突，以及跨会话是否能重读同一目录，均未实跑。前后 `git status` 均无跟踪文件变更，暂存与未暂存 diff 均为空。任务目录只有原有的 该调研的本机任务简报，本会话新增文件和可清理项均为零。

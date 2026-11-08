# gmds-agent-skills

**简体中文** | [English](README.en.md)

可复用的智能体技能集合。每个技能独立存放在 `skills/<name>/` 目录中，以 `SKILL.md` 为入口，配套文件放在同一目录下。新增技能时，创建独立文件夹即可。

## 技能列表

| 技能 | 用途 |
| --- | --- |
| [agent-handoff](skills/agent-handoff/SKILL.md) | 通过本地任务文件，在负责决策与评审的智能体和负责执行与修复的智能体之间手动交接 Git 仓库任务。默认由 Codex 与通过 Claude Code CLI 运行的 Mimo 协作。 |
| [paper-reading-guide](skills/paper-reading-guide/README.md) | 通过灵活陪读、复述反馈或完整分析，理解单篇计算机领域论文；结合具体例子与主动图解，依据原文核对结论，仅在明确要求时导出笔记。 |

## 安装

将所需技能的整个文件夹复制到对应客户端的技能目录：

- Codex：`$CODEX_HOME/skills/`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills/`。
- Claude Code：`~/.claude/skills/`。

## 使用

### agent-handoff：手动交接任务

在 Codex 中调用：

```text
$agent-handoff start <任务描述>
```

`start` 成功后会生成本地任务文件，并给出下一步的准确调用命令；它不会自动发送任务。与直接向智能体投递任务的 Orca 不同，这个技能需要用户打开接收端，将任务文件路径传过去。在 Claude Code 中调用：

```text
/agent-handoff execute <task.md 的绝对路径>
```

执行结束后，将路径交回 Codex 评审；如果执行端返回了计划修订请求，则先修订计划：

```text
$agent-handoff review <task.md 的绝对路径>
$agent-handoff revise <task.md 的绝对路径>
```

技能不会启动另一个客户端，也不包含模型凭据。

### paper-reading-guide：论文陪读与分析

调用 `$paper-reading-guide` 并提供论文路径或链接，可选择陪读、复述或完整分析，也可以直接提出具体的论文问题：

```text
$paper-reading-guide 陪读模式，读这篇论文：<PDF 路径或链接>
$paper-reading-guide 复述模式，我先讲：<PDF 路径或链接>
$paper-reading-guide 拆论文：<PDF 路径或链接>
```

更多用法与可选的 PDF 工具环境配置，见[中文使用说明](skills/paper-reading-guide/README.md)。

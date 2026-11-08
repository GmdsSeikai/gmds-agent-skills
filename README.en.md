# gmds-agent-skills

[简体中文](README.md) | **English**

Reusable agent skills. Each skill lives in `skills/<name>/` and has its own `SKILL.md`; supporting files stay beside it. More skills can be added as separate folders.

## Skills

| Skill | Purpose |
| --- | --- |
| [agent-handoff](skills/agent-handoff/SKILL.md) | Manually hand a Git repository task between a decision/review agent and an execution/repair agent. Defaults to Codex and Mimo through Claude Code CLI. |
| [paper-reading-guide](skills/paper-reading-guide/README.en.md) | Understand a single computing paper through flexible guided reading or retelling feedback, concrete examples, and proactive diagrams. Check claims against the source and export notes only when requested. |

## Install

Copy the desired skill folder to each client that will use it:

- Codex: `$CODEX_HOME/skills/` (or `~/.codex/skills/` if `CODEX_HOME` is unset).
- Claude Code: `~/.claude/skills/`.

## Usage

For `agent-handoff`, invoke `$agent-handoff start <task description>` in Codex. A successful `start` delivers a local task file and the exact next invocation — the task itself is not sent anywhere. Unlike Orca, which delivers tasks to agents directly, the receiving client must be opened by the user with that path: `/agent-handoff execute <absolute-task.md-path>` in Claude Code. Transfer the path back to Codex for `$agent-handoff review <absolute-task.md-path>`, or `$agent-handoff revise <absolute-task.md-path>` when the executor returns a plan revision. The skill does not start the other client or include model credentials.

For `paper-reading-guide`, invoke `$paper-reading-guide` with a paper path or link. Choose guided reading or retelling, or ask a specific paper question directly. See its [README](skills/paper-reading-guide/README.en.md) for examples and optional PDF tool setup.

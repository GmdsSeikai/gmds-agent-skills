# gmds-agent-skills

Reusable agent skills. Each skill lives in `skills/<name>/` and has its own `SKILL.md`; supporting files stay beside it. More skills can be added as separate folders.

## Skills

| Skill | Purpose |
| --- | --- |
| [agent-handoff](skills/agent-handoff/SKILL.md) | Manually hand a Git repository task between a decision/review agent and an execution/repair agent. Defaults to Codex and Mimo through Claude Code CLI. |

## Install

Copy the desired skill folder to each client that will use it:

- Codex: `$CODEX_HOME/skills/` (or `~/.codex/skills/` if `CODEX_HOME` is unset).
- Claude Code: `~/.claude/skills/`.

For `agent-handoff`, invoke `$agent-handoff start <task>` in Codex. Give the resulting task-file path to Mimo and invoke `/agent-handoff execute <absolute-task.md-path>` in Claude Code. Transfer the path back to Codex for review. The skill does not start the other client or include model credentials.

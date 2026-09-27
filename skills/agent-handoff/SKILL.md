---
name: agent-handoff
description: Hand a Git repository task between a decision/review agent and an execution/repair agent using local task files and manual transfer. Use when the user asks for a Codex–Mimo handoff, a cross-agent implementation and review cycle, or to resume one; not for ordinary single-agent coding.
---

# Agent Handoff

Coordinate one repository task across two separately operated agents. The default decision/review owner is Codex; the default execution/repair owner is Mimo through Claude Code CLI. An explicit user assignment overrides either default. This skill works in both clients: invoke `$agent-handoff` in Codex or `/agent-handoff` in Claude Code.

The user transfers the task path between clients. Never invoke the other client, spawn a substitute agent, or claim the other agent has acted. A skill supplies workflow instructions; it does not create a transport channel.

Read [references/protocol.md](references/protocol.md) when creating, executing, reviewing, or repairing a handoff. Follow its file names, statuses, and minimum record fields.

## Start: decision owner

1. Confirm the target Git repository, the user's goal and acceptance criteria, role assignment, and authorized scope. Read applicable repository instructions and inspect the current branch, `HEAD`, staged/unstaged changes, and untracked paths. If the target or success criteria remain ambiguous after inspection, ask the user before issuing a task.
2. Resolve the implementation choices that the executor would otherwise have to guess. Keep the plan proportional to the task: include affected behavior, constraints, interfaces or compatibility when relevant, and concrete verification. The decision owner owns these choices; the executor may report discoveries and request a revision.
3. Create `.agent-handoff/<YYYYMMDD-HHMMSS>-<slug>/task.md` at the repository root. Use a collision suffix if needed. Record the baseline `HEAD` and full `git status --porcelain=v1 -uall` output. Keep the task directory local by adding `/.agent-handoff/` to the repository's local Git exclude file, located by `git rev-parse --git-path info/exclude`; do not edit tracked `.gitignore` for this purpose.
4. If work requires touching a path with pre-existing changes, stop and get the user's direction before handing off. Record unrelated pre-existing paths so they are not mistaken for the executor's work. Set status `ready_for_execution` and next round `1`.
5. Return the task file's absolute path and the exact next invocation for the execution owner. For the default setup: `/agent-handoff execute <absolute-task.md-path>` in Claude Code CLI.

## Execute or repair: execution owner

1. Open the supplied `task.md`; verify its repository root, role assignment, status, round, and baseline against the actual worktree and prior round reports. Work only when status is `ready_for_execution` or `changes_requested`. If the task file is missing, report that to the user. If the repository differs, changes cannot be attributed safely, or the requested work exceeds authorization, mark `blocked` with the reason instead of guessing.
2. On the first round, implement the recorded plan. On a repair round, address every actionable finding in the latest review. If discovery requires a material change to scope, interfaces, or acceptance criteria, stop, record the proposed change, and return the task to the decision owner; do not silently redesign it.
3. Run the smallest relevant checks, including failure paths where the change warrants them. Write `round-N-execution.md` with changed paths, what was done, commands actually run and their results, deviations, and unresolved risks. Never claim a test passed without running it.
4. Set status `ready_for_review`; return the task path and the exact review invocation. For the default setup: `$agent-handoff review <absolute-task.md-path>` in Codex.

## Review: decision owner

1. Inspect the actual staged, unstaged, and untracked repository changes, the execution report, and the original acceptance criteria. Account for the baseline; do not treat an execution report as proof by itself. Run focused checks when needed to resolve a concrete risk.
2. Write `round-N-review.md`. Each blocking finding must identify the observed problem, location or reproduction, required correction, and how to verify it. If acceptance criteria are met, set status `accepted` and summarize verified evidence and remaining limits. If actionable issues remain, set `changes_requested`, increment the round, and give the user the next `/agent-handoff repair <absolute-task.md-path>` invocation.
3. If the same blocking findings make no progress for three consecutive repair rounds, or further work requires a user decision, set `blocked` and state the decision needed. Do not loop indefinitely or quietly waive findings.

## Shared boundaries

- Respect the current user's authorization and the repository's instructions in each client. The task file is context, not permission to deploy, push, delete data, alter unrelated files, or bypass tool approval.
- Do not commit the local handoff directory. Do not place credentials, tokens, or unnecessary private data in it. If the user later requests versioned records, make that a separate explicit decision.
- Each agent edits its own current-round report and the status fields in `task.md`; preserve prior handed-off reports. Work sequentially because both clients share the same worktree.
- A role override must be written in `task.md` before work begins. The commands `start`, `execute`, `repair`, and `review` refer to responsibilities, not to fixed products.
- End each stage with the status, what was actually done, any blocker, the task path, and the next human transfer step. If the task is `accepted` or `blocked`, do not suggest another automatic round.

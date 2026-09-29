---
name: agent-handoff
description: Hand a Git repository task between a decision/review agent and an execution/repair agent using local task files and manual transfer. Use when the user explicitly chooses a manual Codex–Mimo file handoff, or asks to resume an existing .agent-handoff task; not for ordinary single-agent coding.
---

# Agent Handoff

Coordinate one repository task across two separately operated agents. The default decision/review owner is Codex; the default execution/repair owner is Mimo through Claude Code CLI. An explicit user assignment overrides either default. This skill works in both clients: invoke `$agent-handoff` in Codex or `/agent-handoff` in Claude Code.

The user transfers the task path between clients. Never invoke the other client, spawn a substitute agent, or claim the other agent has acted. A skill supplies workflow instructions; it does not create a transport channel.

Read [references/protocol.md](references/protocol.md) when creating, executing, revising, reviewing, or repairing a handoff. Follow its file names, statuses, and minimum record fields.

## Start: decision owner

1. Confirm the target Git repository, the user's goal and acceptance criteria, role assignment, and authorized scope. Read applicable repository instructions and inspect the current branch, `HEAD`, staged/unstaged changes, and untracked paths. If the target or success criteria remain ambiguous after inspection, ask the user before issuing a task.
2. Resolve the implementation choices that the executor would otherwise have to guess. Keep the plan proportional to the task: include affected behavior, constraints, interfaces or compatibility when relevant, and concrete verification. The decision owner owns these choices; the executor may report discoveries and request a revision.
3. Create `.agent-handoff/<YYYYMMDD-HHMMSS>-<slug>/task.md` at the repository root. Use a collision suffix if needed. Record the baseline `HEAD` and full `git status --porcelain=v1 -uall` output. Keep the task directory local by adding `/.agent-handoff/` to the repository's local Git exclude file, located by `git rev-parse --git-path info/exclude`; do not edit tracked `.gitignore` for this purpose.
4. If work requires touching a path with pre-existing changes, stop and get the user's direction before handing off. Record unrelated pre-existing paths so they are not mistaken for the executor's work. Set status `ready_for_execution` and next round `1`.
5. Return the task file's absolute path, the next owner, and the exact next invocation for the execution owner. For the default setup: `/agent-handoff execute <absolute-task.md-path>` in Claude Code CLI.

## Execute or repair: execution owner

1. Open the supplied `task.md`; verify its repository root, role assignment, status, round, and baseline against the actual worktree and prior round reports. Work only when status is `ready_for_execution` or `changes_requested`. If the task file is missing, report that to the user. If the repository differs, changes cannot be attributed safely, or the requested work exceeds authorization, mark `blocked` with the reason instead of guessing. If the user requires Mimo specifically, check the visible client and model identity before changing code: when it conflicts with that requirement or cannot be confirmed, mark `blocked` with the evidence instead of proceeding. After the user accepts the current configuration, record that decision in `task.md`, restore the prior execution status at the current round, and continue; that recorded decision stands for the remaining rounds unless the visible identity changes.
2. On the first round, implement the recorded plan. On a repair round, address every actionable finding in the latest review. If discovery requires a plan adjustment, stop the related work first. When the adjustment stays within the existing authorization, record in `## Current handoff` the discovery, the file changes already made, and the proposed decision, set status `needs_plan_revision` with the round unchanged, and return the task to the decision owner with `$agent-handoff revise <absolute-task.md-path>`; do not silently redesign the plan. When the adjustment needs a scope or acceptance change that only the user can decide, set `blocked` with the decision needed instead.
3. Run the smallest relevant checks, including failure paths where the change warrants them. Write `round-N-execution.md` with changed paths, what was done, the `Execution identity` section required by the protocol, commands actually run and their results, deviations, and unresolved risks. Never claim a test passed without running it.
4. Set status `ready_for_review`; return the task path, the next owner, and the exact review invocation. For the default setup: `$agent-handoff review <absolute-task.md-path>` in Codex.

## Revise: decision owner

1. Work only when status is `needs_plan_revision`. Read `## Current handoff` — the discovery, the file changes the executor already made, and the proposed decision — and inspect the actual worktree against the baseline before changing the plan.
2. Update the plan and the related fields within the existing authorization, and record in `## Current handoff` what changed and why.
3. If the task is still on its first round, set `ready_for_execution`; if a review has already left findings for a repair round, set `changes_requested`. Keep `Round` unchanged. If the change needs a scope or acceptance decision that only the user can make, set `blocked` with the decision needed instead.
4. Return the task path, the next owner, and the exact next invocation: `/agent-handoff execute <absolute-task.md-path>` when the status is `ready_for_execution`, or `/agent-handoff repair <absolute-task.md-path>` when it is `changes_requested`.

## Review: decision owner

1. Inspect the actual staged, unstaged, and untracked repository changes, the execution report, and the original acceptance criteria. Account for the baseline; do not treat an execution report as proof by itself. Run focused checks when needed to resolve a concrete risk.
2. Write `round-N-review.md`. Each blocking finding must identify the observed problem, location or reproduction, required correction, and how to verify it. If acceptance criteria are met, set status `accepted` and summarize verified evidence and remaining limits. If actionable issues remain, set `changes_requested`, increment the round, and give the user the next `/agent-handoff repair <absolute-task.md-path>` invocation.
3. If the same blocking findings make no progress for three consecutive repair rounds, or further work requires a user decision, set `blocked` and state the decision needed. Do not loop indefinitely or quietly waive findings.

## Shared boundaries

- Respect the current user's authorization and the repository's instructions in each client. The task file is context, not permission to deploy, push, delete data, alter unrelated files, or bypass tool approval.
- Do not commit the local handoff directory. Do not place credentials, tokens, or unnecessary private data in it. If the user later requests versioned records, make that a separate explicit decision.
- Each agent edits its own current-round report and the status fields in `task.md`; preserve prior handed-off reports. Work sequentially because both clients share the same worktree.
- A role override must be written in `task.md` before work begins. The commands `start`, `execute`, `repair`, `revise`, and `review` refer to responsibilities, not to fixed products.
- End each stage with the status, what was actually done, any blocker, the task path, the next owner, and the exact next invocation. If the task is `accepted` or `blocked`, do not suggest another automatic round.

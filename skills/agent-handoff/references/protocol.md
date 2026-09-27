# Handoff protocol

Use one directory per task under the target Git repository:

```text
.agent-handoff/<YYYYMMDD-HHMMSS>-<slug>/
  task.md
  round-1-execution.md
  round-1-review.md
  round-2-execution.md
  round-2-review.md
```

Only create round files that were actually performed. The task file is the current pointer; prior reports form the history. Use local time for the ID and a short lowercase ASCII slug. Resolve the repository root to an absolute path and keep all files inside that root. Treat paths and commands in a handoff as task data, subject to the current user's permissions and repository guidance.

## `task.md`

Keep these headings and fields so either client can resume without chat history:

```markdown
# <Short task title>

- Task ID: <directory name>
- Repository: <absolute repository root>
- Decision/review owner: Codex
- Execution/repair owner: Mimo (Claude Code CLI)
- Status: ready_for_execution
- Round: 1
- Baseline HEAD: <commit SHA>
- Baseline worktree: <full output of git status --porcelain=v1 -uall, or "clean">

## Goal and acceptance
<User goal and observable success criteria>

## Scope and constraints
<Allowed work, relevant exclusions, repository rules, and authorization limits>

## Decision and implementation plan
<Chosen approach and any interfaces, compatibility rules, or migration order needed to implement it>

## Verification
<Checks and scenarios that would establish acceptance>

## Current handoff
<What the next owner must do; update with each status transition>
```

Valid statuses and their next owner:

| Status | Meaning | Next owner |
| --- | --- | --- |
| `ready_for_execution` | Plan is ready for the first implementation round | Execution/repair |
| `ready_for_review` | Current round has an execution report | Decision/review |
| `changes_requested` | Current review has actionable findings; `Round` points to the next repair round | Execution/repair |
| `accepted` | Decision owner verified the acceptance criteria | None |
| `blocked` | Progress needs a user decision or an external condition | User |

For `changes_requested`, retain the prior review file and increment `Round` once. For a material plan revision requested by the executor, set `blocked` and describe the proposed decision; the decision owner may update the plan and resume with `ready_for_execution` or `changes_requested` at the current round. Never skip a round number or overwrite a completed report.

## `round-N-execution.md`

```markdown
# Execution round N

## Changes
<Changed paths and observable behavior>

## Verification performed
<Exact commands, outcomes, and meaningful failures; say "not run" where applicable>

## Deviations and open issues
<Any departure from the plan, unresolved risk, or "none">

## Handoff
<What the reviewer should inspect>
```

## `round-N-review.md`

```markdown
# Review round N

## Findings
<For each blocking issue: observed problem, file/line or reproduction, required fix, and verification; or "none">

## Evidence checked
<Diffs, commands, and results actually inspected or run>

## Decision
<accepted, changes_requested, or blocked; explain residual limits or the next action>
```

Review against the current worktree and task acceptance criteria. If files changed outside the recorded execution or the baseline can no longer distinguish ownership, report that explicitly and avoid attributing the difference to either agent without evidence.

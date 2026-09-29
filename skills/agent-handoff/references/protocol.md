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

Valid statuses, their next owner, and when they are entered:

| Status | Next owner | Entered when |
| --- | --- | --- |
| `ready_for_execution` | Execution/repair | The first-round plan is fixed, a first-round plan revision finished, or a `blocked` was resolved back into it |
| `ready_for_review` | Decision/review | The current round has an execution report |
| `changes_requested` | Execution/repair | The review left actionable findings; this transition increments the round |
| `needs_plan_revision` | Decision/review | The executor found a plan adjustment need that stays within the existing authorization |
| `blocked` | User | A new authorization, a user decision, or an external condition is required |
| `accepted` | None | The review verified the acceptance criteria |

Round and transition rules:

- Increment `Round` once, only when a review sets `changes_requested`; `Round` then points to the next repair round. Never skip a round number or overwrite a completed report. Handed-off reports are read-only history.
- When the executor needs a plan adjustment within the existing authorization, stop the related work first and set `needs_plan_revision` with the round unchanged. In `## Current handoff`, record the discovery, the file changes already made, the proposed decision, and the next invocation `$agent-handoff revise <absolute-task.md-path>`.
- `revise` is the decision owner's step: inspect the actual worktree against the baseline, then update the plan. If the task is still on its first round, set `ready_for_execution`; if a review has already left findings for a repair round, set `changes_requested`. Keep the round unchanged. A scope or acceptance change that only the user can decide goes to `blocked` instead.
- When `changes_requested` is restored after `revise`, the next invocation is `/agent-handoff repair <absolute-task.md-path>`, not `execute`.
- When the user resolves a `blocked`, record the decision in `task.md` and restore the status that was in effect before `blocked` (`ready_for_execution` or `changes_requested`) at the current round.
- Resuming an older task: plan revisions may appear as `blocked` from before `needs_plan_revision` existed. Do not reclassify those records automatically; read `## Current handoff` and the prior reports to confirm the next owner before acting.

## `round-N-execution.md`

```markdown
# Execution round N

## Changes
<Changed paths and observable behavior>

## Execution identity
<Client, the model identifier that client displayed, the non-secret name of the provider configuration used, what the identity is based on, and whether the actual backend could be independently confirmed>

## Verification performed
<Exact commands, outcomes, and meaningful failures; say "not run" where applicable>

## Deviations and open issues
<Any departure from the plan, unresolved risk, or "none">

## Handoff
<What the reviewer should inspect>
```

A model alias or interface label alone does not prove the actual backend routing. When the evidence is insufficient, write that the actual backend was not independently confirmed instead of claiming a verified execution identity. Never record credentials or private configuration values.

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

## Example chains

Examples show only the status, round, and next invocation.

Happy path with one repair round:

| Invocation | Status after | Round | Next invocation |
| --- | --- | --- | --- |
| `start` | `ready_for_execution` | 1 | `/agent-handoff execute <absolute-task.md-path>` |
| `execute` | `ready_for_review` | 1 | `$agent-handoff review <absolute-task.md-path>` |
| `review` with findings | `changes_requested` | 2 | `/agent-handoff repair <absolute-task.md-path>` |
| `repair` | `ready_for_review` | 2 | `$agent-handoff review <absolute-task.md-path>` |
| `review` accepting | `accepted` | 2 | none |

Plan revision by the executor on the first round:

| Invocation | Status after | Round | Next invocation |
| --- | --- | --- | --- |
| `execute` | `needs_plan_revision` | 1 | `$agent-handoff revise <absolute-task.md-path>` |
| `revise` | `ready_for_execution` | 1 | `/agent-handoff execute <absolute-task.md-path>` |

On a repair round the same revise flow restores `changes_requested`, and the next invocation is `/agent-handoff repair <absolute-task.md-path>`.

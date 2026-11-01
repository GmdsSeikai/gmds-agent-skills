# Reading and Retelling Summary Template

Use selectively for an explicitly requested detailed summary or export. Trim fields to the requested scope and length; omit inapplicable fields. An ordinary request to summarize or organize calls for a brief chat response. Follow the entrypoint's write boundaries: organizing is not saving, and export permission is not overwrite permission. Do not create a file without an explicit save request.

Write in the user's language. Include source locations and evidence type for important claims. Mark relevant unresolved information as open and explain why; do not guess to fill the template or invent the user's research ideas.

```markdown
# [Author Year] Title

## Scope and Sources
- Paper version and source:
- Available material: full text / abstract / selected sections; appendix or supplement availability:
- Mode and scope covered:
- Page convention: PDF page numbers from 1; printed page numbers separately if needed.

## Three-Sentence Summary
1.
2.
3.
> Mark key conclusions as author claims, experimental support, or assistant inference, with source locations.

## Core Contributions (1-3)
- Novelty claim -> concrete technique -> supporting evidence and location; withhold judgment if unsupported.

## Method
- Inputs and outputs:
- Core modules or architecture:
- Training objective or loss, if applicable:
- Important assumptions and applicability conditions:
> Relevant sections, equations, or figures:

## Experiments
| Result or number | Dataset and settings | Metric and direction | Baseline or comparator | Evidence type and source location |
|---|---|---|---|---|

- Numerical convention: absolute value / percentage points / relative change; mark visual estimates as approximate.
- Fairness, random seeds, uncertainty bands, and ablations: judge only with evidence; leave unknowns open.

## Domain-Specific Fields
> Select from a matching domain sheet only when relevant to this scope; otherwise omit.

## Limitations and Research Relevance
- Author-stated limitations, with source locations:
- Assistant-inferred limitations or transferable ideas, with evidence and conditions:
- User's own ideas: record only what the user actually expressed; otherwise leave for them to fill.

## Understanding Checks
| Scope or point | Independently retold / retold after hints / not yet checked | Actual performance and source location |
|---|---|---|

- Corrected misunderstandings: user's actual statement -> correction and evidence.
- Further practice:

## Questions and Open Items
- Question / not yet located, currently unverifiable, or checked but not stated / scope searched / next step.
```

Tie contributions to concrete techniques and evidence. Completing reading is not passing an understanding check. Record only the scope actually checked as retold.

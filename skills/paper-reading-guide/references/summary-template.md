# Paper Analysis and Summary Template

Use for full analysis or an explicitly requested detailed summary/export. Trim fields to the paper type, requested scope, and length; omit inapplicable fields. Full analysis can be paper-wide without repeated user answers. An ordinary request to summarize or organize calls for a brief scoped chat recap, not mode escalation. Follow the entrypoint's write boundaries: organizing is not saving, export permission is not overwrite permission, and no file is created without an explicit save request.

Write in the user's language. Include source locations and evidence type for important claims. Mark relevant unresolved information as open and explain why; do not guess to fill the template or invent the user's research ideas.

The analysis sections below are reusable structure, not fixed headings. Presentation Outline and Anticipated Q&A are independently optional: include only components requested by the prompt or explicit presentation package context, following [full-analysis guidance](full-analysis-mode.md). Plain full analysis includes neither, no speaking script, and no talk-duration assumption. Omit Understanding Checks unless actual retelling or a requested check makes it relevant; completed analysis is not evidence of mastery.

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

## Problem and Necessary Background
- Concrete scenario, problem, and why it is difficult:
- Central idea and prerequisites needed for the method:

## Core Contributions (1-3)
- Novelty claim -> concrete technique -> supporting evidence and location; withhold judgment if unsupported.

## Method
- Inputs and outputs:
- Core modules or architecture:
- Main steps, their roles, and how they connect:
- Training objective or loss, if applicable:
- Key equations: meaning, purpose, conditions, and source locations:
- Important assumptions and applicability conditions:
> Relevant sections, equations, or figures:

## Evidence: Experiments, Theory, or Other Support
> Use the evidence the paper actually provides; omit experimental fields for a purely theoretical paper and adapt for a survey.

| Result or number | Dataset and settings | Metric and direction | Baseline or comparator | Evidence type and source location |
|---|---|---|---|---|

- Numerical convention: absolute value / percentage points / relative change; mark visual estimates as approximate.
- Fairness, random seeds, uncertainty bands, and ablations: judge only with evidence; leave unknowns open.
- Theoretical result and conditions, when applicable; distinguish author claim from argument actually checked:
- What the evidence supports and what it does not establish:

## Domain-Specific Fields
> Select from a matching domain sheet only when relevant to this scope; otherwise omit.

## Limitations and Research Relevance
- Author-stated limitations, with source locations:
- Assistant-inferred limitations or transferable ideas, with evidence and conditions:
- User's own ideas: record only what the user actually expressed; otherwise leave for them to fill.

## Understanding Checks
> Optional; omit without actual retelling or a relevant requested check.

| Scope or point | Independently retold / retold after hints / not yet checked | Actual performance and source location |
|---|---|---|

- Corrected misunderstandings: user's actual statement -> correction and evidence.
- Further practice:

## Questions and Open Items
- Question / not yet located, currently unverifiable, or checked but not stated / scope searched / next step.

## Overall Summary
- How problem, method, and evidence connect; applicability and main unresolved limits:

## Presentation Outline
> Include only when an outline is requested, independently of Q&A; honor explicit exclusions.

- Audience, duration and focus; state an organizational assumption only for requested presentation support:
| Slide or topic | Takeaway | Speaking points | Actual source figure/table and its role, if useful |
|---|---|---|---|

## Anticipated Q&A
> Include only when questions/answers are requested, independently of an outline; honor explicit exclusions.

| Potential question | Answer | Author claim / checked support / inference / unknown, with location |
|---|---|---|
```

Tie contributions to concrete techniques and evidence. Completing reading is not passing an understanding check. Record only the scope actually checked as retold.

---
name: paper-writing
description: Draft, verify, or revise a LaTeX experiment-results section from the author's experimental records, references, and current manuscript or conference template. Rebuild affected tables, statistical figures, and the manuscript PDF when the project has a working build.
---

# Paper Writing

Use the current subscription session for prose, citation decisions, and review. Use local tools for calculations, figure generation, and compilation. The core path requires no model API key.

## Materials and evidence

- Find the author's adopted TeX source, bibliography, build entry point, and any existing handoff. Use the author's template and file layout. If competing drafts make the adopted source ambiguous, resolve that ambiguity before editing.
- Tie each material numerical claim to the observed entity, source file and row or sample ID, unit, and sample scope. Record the denominator and formula for derived values. Distinguish observations by identity even when they share a name or a value. Mark absent or contradictory evidence where it affects the prose.
- Check reference identity against the supplied work or authoritative metadata. Read the relevant passage and record how it supports the sentence, with a locator and evidence scope. Use abstract-only evidence only for claims the abstract supports. Add a matching BibTeX entry and cite its key in the manuscript.

## Draft or revise

- Draft the requested section in the manuscript's style. Bound conclusions to the measured population and conditions. Label synthetic material in the manuscript and keep private inputs within the author's authorized scope.
- For corrections, recompute from the source and trace the identified observation through prose, abstracts, tables, figures, and any dependent conclusions. Preserve unrelated author edits. When a requested edit conflicts with the author's wording or conclusion, surface the affected sentence and preserve the author's version pending a decision.
- Reuse the project's figure data, script, and style. Record the figure file, inputs, generator, and the manuscript's figure label. If only an image is available, document the missing inputs before claiming it can be rebuilt.

## Build and hand off

- Run the project's figure generator before compilation. Check the compiler output for unresolved citations or references. Open the fresh PDF and check that the relevant text, bibliography, and embedded figure reflect the adopted source. If the build is blocked, deliver the editable files and identify the specific dependency or error.
- Add or update a brief handoff using relative paths. Record the adopted TeX entry, evidence and citation locators, affected manuscript locations, figure rebuild path, successful commands and versions, and unresolved issues. Reuse the project's existing README or build instructions where they already answer these questions.

To try the workflow on synthetic material, read the [CVPR 2025 example handoff](examples/cvpr2025/HANDOFF.md).

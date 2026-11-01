# Source Evidence Rules

## Claims and Locations

- Retain the paper's title, version, and readable scope. Count PDF pages from 1 and distinguish them from printed page numbers when they differ.
- For important judgments, use a compact form such as "claim [author claim / experimental support / assistant inference] - source location", translated into the user's language. Focus on novelty, comparisons, results, limitations, and corrections rather than tagging every commonplace statement.
- Locate PDF evidence by page plus section, figure, table, or equation number. For HTML, use a section heading and identifying phrase. Keep the location description even when supplying a clickable local or web link.
- A contribution statement in the introduction establishes only what the authors claim. Assessing novelty, comparison fairness, or mechanism effectiveness also requires the method, experiments, ablations, and related work. Withhold judgment when evidence is insufficient.
- For experimental numbers, state the dataset, metric direction, comparator, and relevant settings. Distinguish percentage points from relative percentage changes. Do not calculate from unverified values or fill gaps with guesses.
- Identify inference and teaching analogies. Simplifications in an analogy do not replace the paper's assumptions. Do not import common domain-sheet settings as facts about this paper.

## Unknown Information

- **Not yet located:** The relevant information has not been found. Check the appropriate body sections, appendices, and available supplements.
- **Currently unverifiable:** The source is missing, an attachment is inaccessible, extraction failed, or an image cannot be viewed. State what material is missing.
- **Checked but not stated:** Name the sections or appendices checked and limit the conclusion to that scope. An omission from an abstract or one section does not establish a whole-paper omission.
- The question checklist identifies things to investigate; it does not prove a flaw. Leave items unresolved until the relevant materials have been searched.

## PDF Navigation and Visual Inspection

- `scripts/extract_outline.py` provides heuristic headings, an abstract excerpt, and caption lines that matched its patterns. Captions may wrap or be missed, and the abstract may be truncated or extend into other text. Check the original pages rather than treating this output as the complete paper.
- Empty extraction may result from scans or unusual layouts. Explain that the text layer cannot establish the content, then try rendering or OCR; do not immediately classify the whole paper as scanned.
- If a figure or table is hard to locate, search for its number in the text, consult contents or bookmarks, or render likely pages to check the full caption and image together.
- Revisit original page images for key equations, figures, tables, or suspicious extraction. Check relevant subscripts, superscripts, summation bounds, signs, units, and nearby definitions. Garbled extraction is not evidence of an error in the paper. If symbols remain illegible, identify the uncertainty and pause derivations that depend on them.
- Example: `python <skill-dir>/scripts/render_page.py <paper-path> <PDF-page-number> --out <task-output-dir>`. Quote paths containing spaces according to the shell.
- Successful rendering establishes only that an image was generated. Actually view it before recording axes and units, legends, comparison settings, captions, and uncertainty-band definitions. Do not label an undefined shaded region as standard deviation, variance, or a confidence interval.
- Prefer body text or tables for exact values. Mark graph-read estimates as approximate and identify their visual origin; do not invent precision.
- If images cannot be viewed, state that the visual evidence is unverified. Ask the user to inspect or describe the relevant figure if helpful. Do not assert curve trends, heatmap positions, or plotted values without viewing the image.

## Supplemental Derivations and Proof Boundaries

- Distinguish source conclusions, background knowledge, teaching analogies, and assistant-added derivations when relevant without tagging every sentence. State a supplemental derivation's premises and their sources, separating paper assumptions from extra simplifications for an example.
- Withhold judgment when a derivation cannot be completed. An assistant's failure to derive a result, or agreement among several agents, is not a mathematical proof and does not establish that a theorem is wrong.
- A toy calculation, successful program run, finite test, and paper reproduction each have a different evidential scope. Limit claims to the tested settings rather than turning local success into a general guarantee. Check relevant metrics, baselines, and comparison conditions when judging experimental support.

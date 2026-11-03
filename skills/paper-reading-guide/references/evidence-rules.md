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

## Original-Paper Regions in the Conversation

- When discussing a source figure, table, key equation, or concrete original example that benefits from direct comparison, locate it in the correct paper/version, inspect the full page, and crop the relevant region. Present it near the explanation through the current client's supported image channel; point out what to examine. Ordinary text concepts and invented examples do not require an original screenshot.
- Label the region in the user's language, for example "Original-paper crop · PDF p.3 · Fig.2(a–c)"; add paper identity, printed page, or caption location when needed. Preserve axes, legends, units, table headers, footnotes, subfigure labels, and necessary captions. If context is elsewhere, present a separately labeled crop rather than silently stitching areas into an apparently continuous original.
- Keep original crops distinct from assistant-created diagrams, annotations, redraws, and invented numerical examples. Disclose any changes; do not use image generation or an unlabeled reconstruction as source evidence. Do not silently remove an answer-bearing caption to make an altered figure appear neutral for retelling.
- Use enough context to understand relationships, then zoom into the current detail if needed. Reuse a clearly available earlier image when scope is unchanged; resend or crop more closely for a new subfigure, lost context, unreadable detail, or an explicit request. Keep this reuse state in the conversation, without a persistent image index.
- Respect pure-text requests and available-source limits. With only an abstract or excerpt, do not borrow figures from another paper/version. If the agent cannot view a crop, restrict claims to verified text/captions; if details remain illegible, identify exactly what is unverified.

### Rendering Contract

Use `scripts/render_page.py <paper-path> <single-page> --clip x0,y0,x1,y1 --dpi 200 --out <task-output-dir>` for a region. Coordinates are PDF points (72 per inch), relative to the displayed visible page's top-left after rotation and CropBox, independent of DPI. Text/search rectangles use unrotated coordinates: multiply the locator rectangle by `page.rotation_matrix` to obtain a displayed rectangle before passing it as `--clip`; an already displayed rectangle needs no second rotation.

The clip must be finite, correctly ordered, positive-area, and within `page.rect`. First inspect the full page and choose context-preserving bounds; do not infer completeness from a text box or image object alone. Whole-page CLI remains available without `--clip`, with 150 DPI default. The helper rejects invalid/empty/out-of-range page lists, invalid clips, multi-page clips and nonpositive DPI before creating output. This deliberately replaces the earlier out-of-range-page skipping behavior.

Outputs use the existing full-page name when free, crop coordinates in region names, and exclusive numbered suffixes on collision; no existing file is overwritten, including when PDFs share a basename. The helper reports the actual absolute path, page, full/clip region and DPI. Later filesystem failures can leave earlier exports or an incomplete failed write; do not call a multi-page run atomic. The original PDF stays read-only, and there is no automatic cleanup.

### Display Evidence and Fallback

Keep four outcomes separate: (1) PNG generated/readable, (2) agent actually viewed it and checked the region, (3) image sent through a supported client mechanism, (4) user UI actually displays a readable image. Tool success or agent vision does not prove (4); a visible thumbnail may still require opening or zooming to read details. Do not claim that the user saw an image without UI observation or confirmation.

If the current client lacks a reliable image channel or display is unverified, provide an openable image link, source location and a concise explanation, stating the limitation. A link alone is not verified inline display. When visibility cannot be observed, one sample confirmation can establish the current channel; do not repeatedly ask about already established behavior. Do not operate the user's desktop, upload to an external host, or build a webpage merely to display the crop.

Temporary rendering/cropping for reading follows the user's/project's task-file policy, outside the paper's attachment directory. It is not a formal note, report, or PPT export and does not authorize library, Obsidian, or long-term memory writes. Keep originals unchanged and do not add automatic cleanup.

## Supplemental Derivations and Proof Boundaries

- Distinguish source conclusions, background knowledge, teaching analogies, and assistant-added derivations when relevant without tagging every sentence. State a supplemental derivation's premises and their sources, separating paper assumptions from extra simplifications for an example.
- Withhold judgment when a derivation cannot be completed. An assistant's failure to derive a result, or agreement among several agents, is not a mathematical proof and does not establish that a theorem is wrong.
- A toy calculation, successful program run, finite test, and paper reproduction each have a different evidential scope. Limit claims to the tested settings rather than turning local success into a general guarantee. Check relevant metrics, baselines, and comparison conditions when judging experimental support.

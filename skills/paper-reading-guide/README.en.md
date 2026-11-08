# paper-reading-guide: Reading, Retelling, and Full Analysis

[简体中文](README.md) | **English**

Understand a single computing paper in areas such as deep learning, networking, and edge-cloud offloading. Concrete examples, prerequisites taught as needed, and timely diagrams connect the problem, method, and experiments, while source checks keep explanations grounded.

Customized from [fuxiao13/paper-reading-guide](https://github.com/fuxiao13/paper-reading-guide) under the MIT license, retaining its domain references and two PDF helpers.

The skill's instructions are in English. User-facing explanations follow the user's language and default to Chinese. Chinese requests such as "陪读模式", "复述模式", "完整分析模式", and "拆论文" are supported.

## Features

- **Flexible guided reading:** Follow the current question. Ask, jump, backtrack, or skip understanding checks. Build missing prerequisites in small pieces.
- **Proactive teaching aids:** Explain concepts with concrete examples and work through equations when useful. Add a small teaching diagram when an algorithm, module relationship, or complex causal chain benefits from it. Prefer Mermaid, falling back to text arrows when rendering is unavailable; identify source locations and simplified conditions.
- **Retelling feedback:** The user explains first; the assistant checks against the paper and identifies correct, mistaken, and unresolved points. Distinguish independent retelling, retelling after hints, and material not yet checked; listening or skipping is not evidence of mastery.
- **Full analysis:** Receive a coherent paper-wide breakdown of the problem, background, method, key equations, evidence, limits, and summary without per-section answers. The assistant reads substantive body text and inspects important cited visuals, disclosing partial coverage and unreviewed details.
- **Optional presentation support:** Request an outline, anticipated Q&A, or a presentation package. Plain full analysis adds none of these. Each component follows the prompt independently, reusing grounded analysis for follow-ups; a presentation request alone does not create a file or PPT.
- **Source checks:** Locate important claims and corrections. Distinguish author claims, experimental support, teaching examples, and assistant inference, as well as information not yet found, currently unverifiable, or checked but not stated. Actually view rendered pages before interpreting plotted trends.
- **Original evidence in chat:** Guided reading presents relevant prose as an original-language excerpt, translation and plain-language explanation, without a prose screenshot by default. Figures, tables, equations and layout-dependent algorithms retain original crops. Repeat the relevant evidence across turns, reusing verified image files when suitable; preserve necessary context and distinguish sources from teaching examples. See the [evidence rules](references/evidence-rules.md#guided-reading-show-the-current-source) for scope and display fallback. Honor pure text. Retelling normally receives evidence after the user's attempt, or a neutral picture task when explicitly requested.
- **Client-aware display:** Generation, agent viewing, sending and readable user display are separate checks. A client may show a thumbnail needing zoom, support only an openable link, or have unverified display behavior. Tool success alone is not user-visible acceptance; an unsupported channel receives a source-labeled image link and explanation.
- **Domain-aware reading:** Select relevant references for edge-cloud offloading, graph/network optimization, traffic learning, visual distillation, and text-image retrieval, alongside the existing control, audio-visual, acoustic-imaging, and general-DL sheets. Confirm the actual problem and mechanism in the paper; combine sheets when useful without turning them into a checklist.
- **Saving only on request:** Summarize or organize in chat by default. Temporary reading images follow the user's/project's task-file policy; formal notes, reports and PPT exports require an explicit request with scope, location and length, without overwriting. Write to Obsidian only when explicitly requested. Keep reading state in the conversation rather than saving long-term memory without a request.

## Entry Points

- `$paper-reading-guide Read this paper: <path or link>`: if intent is ambiguous, choose guided reading, retelling, or full analysis.
- `$paper-reading-guide Guided reading mode: <path or link>`: explain one concept or causal chain at a time, add background as needed, and allow jumping, backtracking, or skipping checks.
- `$paper-reading-guide Retelling mode; I will explain first: <path or link>`: the user retells, then the assistant checks the source and follows up as needed.
- `$paper-reading-guide 拆论文：<path or link>`: enter full analysis directly, producing analysis and summary without a slide outline, Q&A, or assumed talk duration.
- After analysis, ask "给我汇报提纲" or "可能被问什么" for only that component, or "明天汇报，准备汇报材料" for a scoped presentation package. Stated audience, focus and duration take priority; only requested presentation support without a duration uses a stated roughly 10-minute organizational assumption.
- A specific equation, algorithm, or experiment question with paper context: answer directly without requiring a mode choice or resetting progress.
- Ask to switch among the three modes during the conversation; retain verified context and progress without overstating source coverage.

Once the paper is available, saying "guided reading mode" or "陪读模式" is enough. For a new paper, the first turn defaults to a concrete scenario explaining the problem, difficulty, and core idea. Continue in small pieces with prerequisites, examples, and diagrams as needed. Specific questions, selected scope, and existing progress take precedence; teaching preferences need not be repeated.

## Conversation Example

```text
$paper-reading-guide 陪读模式，读这篇论文：<PDF path>

I still do not understand this part. Use another example and diagram the module relationships.

Switch to retelling mode, only for the method we just covered. I will explain first.
```

The Chinese opening above requests guided reading; continue naturally in the language you prefer. There is no need to invoke the skill again on every turn. You may ask about a particular equation, algorithm, or experiment directly.

For a paper-wide analysis followed by a separate presentation request:

```text
$paper-reading-guide 拆论文：<PDF path>

Now give me a 5-minute presentation outline, without Q&A.

What might the audience ask? Answer from the paper; mark unknowns.
```

"总结一下" or "整理一下" remains a scoped chat recap. Missing or excerpt-only sources yield a clearly partial analysis rather than a claim of full coverage. Save/export only on explicit request to a specified destination, without overwriting existing files.

## Files

- `SKILL.md`: entry routing and shared rules.
- `references/three-pass-reading.md`: flexible reading depths, prerequisites, and teaching guidance.
- `references/retelling-mode.md`: retelling workflow.
- `references/full-analysis-mode.md`: paper-wide analysis, completion boundaries, and conditional presentation support.
- `references/evidence-rules.md`: evidence, unknown-information states, and visual checks.
- `references/summary-template.md`: reusable analysis schema with independently optional outline and Q&A sections.
- `references/domains/`: domain index, five specialist sheets, and the retained upstream domain sheets.
- `scripts/`: PDF outline extraction and page rendering; optional dependency in `requirements.txt`.
- `LICENSE`: upstream MIT license and attribution.

This directory contains the customized reading workflow, domain references, and PDF tools. Preserve its interaction and write boundaries when reviewing upstream updates.

Domain selection follows inputs, outputs, and objectives rather than keywords alone. A DNN inference-offloading paper may concern placement rather than training; text-image retrieval does not imply audio. Unmatched topics use the original paper and any relevant general-DL background. For optimization papers, explanations connect the scenario, model, algorithm, guarantee conditions, and experiments as needed, while retaining restricted assumptions and distinguishing solution quality from solver runtime.

## PDF Helper Environment

Reading text already supplied in chat does not require Python. For local PDFs, install `requirements.txt` in an isolated Python environment and use an interpreter that can import PyMuPDF. Resolve helper paths relative to the skill directory.

```text
python -m pip install -r <skill-dir>/requirements.txt
python <skill-dir>/scripts/extract_outline.py <paper-path>
python <skill-dir>/scripts/render_page.py <paper-path> 2,4 --out <task-output-dir>
python <skill-dir>/scripts/render_page.py <paper-path> 3 --clip 36,60,550,410 --dpi 200 --out <task-output-dir>
```

Replace `python` with the selected interpreter's path. Quote paths containing spaces according to the shell; on Windows, `-X utf8` can avoid terminal encoding problems. Extraction aids navigation only: inspect original page images before judging equations or figures.

`--clip` takes exactly one page and displayed-page coordinates in PDF points, starting at the visible top-left after rotation/CropBox, independent of DPI. Convert unrotated text/search rectangles with `page.rotation_matrix` before passing them; do not rotate displayed coordinates again. Inspect the full page first and preserve needed context. The coordinates above are only a command example, not a figure locator for an arbitrary paper.

Whole-page rendering keeps its 150 DPI default and collision-free filename. Existing names now receive exclusive `_2`, `_3`, etc. suffixes instead of being overwritten; crop names include their coordinates. Invalid pages now fail preflight instead of being skipped, as do empty page lists, invalid/multi-page clips and nonpositive DPI. The script prints the absolute output path, page, region and DPI. It does not modify the PDF or automatically clean outputs; a later filesystem failure can leave earlier outputs or an incomplete write, so multi-page export is not atomic.

For script checks with an interpreter providing PyMuPDF, run `python -m unittest discover -s <skill-dir>/tests -v`. Tests generate synthetic PDFs at runtime; they include rotation/CropBox pixel checks and output safety without bundling real papers.

Optionally create `local-runtime.md` in the installed skill directory to record the machine's interpreter and invocation instructions. The entrypoint reads it before running PDF helpers; without it, select a Python that can import PyMuPDF. The repository's skill-local `.gitignore` excludes this machine-specific file from publication.

## Teaching Annotations on Original Visuals

When locating a figure feature or equation term helps, guided reading adds short callouts in the explanation language (Chinese by default) to the checked original crop. Labels match the prose and preserve source symbols. The reply identifies the teaching annotation and source location, provides a clean-original link, and shows both inline when fidelity or readability requires it. Pure-text requests and retelling's no-hint timing still apply; each later explanation re-embeds its relevant source visual.

Read the [source annotation rules](references/evidence-rules.md#teaching-annotations-on-original-visuals) and [helper contract](references/visual-annotations.md) before producing one:

```text
python <skill-dir>/scripts/annotate_visual.py <checked-crop.png> <callouts.json> --out <task-output-dir> --padding 200 --font-size 18
```

The helper uses existing PyMuPDF with its bundled CJK font (or a caller-supplied font), original pixels and vector labels/leaders. Coordinates use PNG pixels, labels stay in added margins, and glyph/geometry failures stop before output. It preserves a byte-identical clean copy and creates separate collision-safe annotated output. Inspect the crop, targets, line paths and text before sending; helper success does not establish scientific fidelity, user-visible display or comprehension. Without a usable tool/font, continue with the clean original and prose. Synthetic CLI tests cover preservation, placement, glyph failures and invalid input; a narrow wording check pins source/claim boundaries without proving model compliance.

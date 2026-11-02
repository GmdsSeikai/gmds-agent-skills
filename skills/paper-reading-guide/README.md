# paper-reading-guide: Interactive Paper Reading and Retelling

Understand a single computing paper in areas such as deep learning, networking, and edge-cloud offloading. Concrete examples, prerequisites taught as needed, and timely diagrams connect the problem, method, and experiments, while source checks keep explanations grounded.

Customized from [fuxiao13/paper-reading-guide](https://github.com/fuxiao13/paper-reading-guide) under the MIT license, retaining its domain references and two PDF helpers.

The skill's instructions are in English. User-facing teaching follows the user's language and defaults to Chinese. Chinese requests such as "陪读模式" and "复述模式" remain supported.

## Features

- **Flexible guided reading:** Follow the current question. Ask, jump, backtrack, or skip understanding checks. Build missing prerequisites in small pieces.
- **Proactive teaching aids:** Explain concepts with concrete examples and work through equations when useful. Add a small teaching diagram when an algorithm, module relationship, or complex causal chain benefits from it. Prefer Mermaid, falling back to text arrows when rendering is unavailable; identify source locations and simplified conditions.
- **Retelling feedback:** The user explains first; the assistant checks against the paper and identifies correct, mistaken, and unresolved points. Distinguish independent retelling, retelling after hints, and material not yet checked; listening or skipping is not evidence of mastery.
- **Source checks:** Locate important claims and corrections. Distinguish author claims, experimental support, teaching examples, and assistant inference, as well as information not yet found, currently unverifiable, or checked but not stated. Actually view rendered pages before interpreting plotted trends.
- **Domain-aware reading:** Select relevant references for edge-cloud offloading, graph/network optimization, traffic learning, visual distillation, and text-image retrieval, alongside the existing control, audio-visual, acoustic-imaging, and general-DL sheets. Confirm the actual problem and mechanism in the paper; combine sheets when useful without turning them into a checklist.
- **Saving only on request:** Summarize or organize in chat by default. Save or export only when explicitly requested, following the specified scope, location, and length without overwriting. Write to Obsidian only when explicitly requested. Keep reading state in the conversation rather than saving long-term memory without a request.

## Entry Points

- `$paper-reading-guide Read this paper: <path or link>`: choose a mode first.
- `$paper-reading-guide Guided reading mode: <path or link>`: explain one concept or causal chain at a time, add background as needed, and allow jumping, backtracking, or skipping checks.
- `$paper-reading-guide Retelling mode; I will explain first: <path or link>`: the user retells, then the assistant checks the source and follows up as needed.
- A specific equation, algorithm, or experiment question with paper context: answer directly without requiring a mode choice or resetting progress.
- Ask to switch to guided reading or retelling during the conversation; retain progress.

Once the paper is available, saying "guided reading mode" or "陪读模式" is enough. For a new paper, the first turn defaults to a concrete scenario explaining the problem, difficulty, and core idea. Continue in small pieces with prerequisites, examples, and diagrams as needed. Specific questions, selected scope, and existing progress take precedence; teaching preferences need not be repeated.

## Conversation Example

```text
$paper-reading-guide 陪读模式，读这篇论文：<PDF path>

I still do not understand this part. Use another example and diagram the module relationships.

Switch to retelling mode, only for the method we just covered. I will explain first.
```

The Chinese opening above requests guided reading; continue naturally in the language you prefer. There is no need to invoke the skill again on every turn. You may ask about a particular equation, algorithm, or experiment directly.

## Files

- `SKILL.md`: entry routing and shared rules.
- `references/three-pass-reading.md`: flexible reading depths, prerequisites, and teaching guidance.
- `references/retelling-mode.md`: retelling workflow.
- `references/evidence-rules.md`: evidence, unknown-information states, and visual checks.
- `references/summary-template.md`: optional summary template.
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
```

Replace `python` with the selected interpreter's path. Quote paths containing spaces according to the shell; on Windows, `-X utf8` can avoid terminal encoding problems. Extraction aids navigation only: inspect original page images before judging equations or figures.

Optionally create `local-runtime.md` in the installed skill directory to record the machine's interpreter and invocation instructions. The entrypoint reads it before running PDF helpers; without it, select a Python that can import PyMuPDF. The repository's skill-local `.gitignore` excludes this machine-specific file from publication.

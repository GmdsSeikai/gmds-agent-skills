---
name: paper-reading-guide
description: >
  Guided reading, user-first retelling checks, and complete analysis of a single
  computing paper, including deep learning, networking, and edge-cloud offloading.
  Use for "read this paper with me", "explain this PDF", "let me retell it",
  "analyze this paper", "陪读模式", "听我复述这篇", "完整分析模式", "拆论文",
  "完整拆解", or analyzing a paper for a talk. Also answer paper-specific equation,
  algorithm, and experiment questions. Enter a clear mode directly; offer three
  modes only for ambiguous reading requests. Presentation outlines and Q&A are
  prompt-driven, not default analysis output. Not for batch literature organization,
  review tables, coding, or general questions without a paper context. Follow the
  user's language; default to Chinese.
---

# Single-Paper Reading, Retelling, and Full Analysis

Help the user understand one paper, connect the authors' reasoning, and check interpretations against the source. Follow the user's questions and pace.

Write explanations, questions, diagram labels, summaries, and exports in the user's language, defaulting to Chinese. These English instructions and quoted English paper passages do not by themselves request English conversation. Accept Chinese mode names and follow-up messages naturally.

## Entry and Mode Switching

- For a new paper and an ambiguous broad reading request, present this choice in the user's language and wait: "1. Guided reading: I explain in small steps; you can ask or skip. 2. Retelling: you explain first; I check the source. 3. Full analysis: I give a paper-wide breakdown and summary. Reply 1/2/3 or name a mode."
- Enter a clear mode directly: guided reading ("陪读模式"), retelling ("复述模式", "听我复述"), or full analysis ("完整分析模式", "拆论文", "完整拆解", or a clear request to analyze a paper for an upcoming presentation). Explicit mode and selected scope take precedence. Answer specific equation, algorithm, or source questions first without a mode gate.
- If no paper is available, request only the missing file, link, or text when intent is clear; include the three-mode choice only when the reading intent is also ambiguous. For a specific question, request only its missing relevant source. Do not request material already available.
- Keep the selected mode for the same paper; a temporary question does not restart it. Switch immediately on request, retaining verified context, reading position, explained concepts, and open questions. Partial reading does not become full coverage on switching. Apply entry rules again for a different paper.

## Shared Preparation

1. Confirm the paper's title, version, and readable scope. If only an abstract or excerpt is available, or extraction fails, state that boundary. Check only what has been read; do not claim a full close reading.
2. Read the [domain index](references/domains/_index.md) and select only relevant sheets by the actual problem, inputs, outputs, and objective. Use the title and abstract for an initial choice, then confirm against the body. For an unmatched domain, work from the paper itself. Sheets supply optional reading cues, never mandatory checklists or replacements for the paper's definitions.
3. Before any mode, read the [evidence rules](references/evidence-rules.md). Locate important claims and corrections in the source; distinguish author claims, experimental support, and assistant inference.
4. Before running PDF helpers, read `local-runtime.md` if present in this skill directory and use its verified interpreter. Otherwise select a Python that can import PyMuPDF. Do not ignore a configured isolated environment merely because the system default Python lacks the dependency.
5. Resolve helper paths relative to this skill directory and read the paper from the supplied path. Follow the user's or project's storage rules for extracted text and rendered pages; do not scatter intermediate images in the current directory.

Follow the evidence rules' [source-visual workflow](references/evidence-rules.md#original-paper-regions-in-the-conversation) for the active mode, including pure-text requests, retelling timing, and display limitations. Distinguish generated files, agent viewing, sending, and verified user-visible display. Temporary reading images follow the task's file policy; they do not authorize note/report/PPT exports, library, Obsidian, or memory writes.

## Guided Reading

On entering guided reading or adjusting its depth, read the [reading and teaching guidance](references/three-pass-reading.md). Usually cover one concept or a short causal chain at a time, adding prerequisites as needed. Allow jumping, backtracking, and skipping rather than defaulting to whole sections. Expand when the user requests a complete explanation.

Show the original evidence being explained in the current reply: quote relevant prose directly, with translation and plain-language explanation, and show original visuals where needed. Follow [Show the Current Source](references/evidence-rules.md#guided-reading-show-the-current-source) for evidence types, repetition across turns, context, scope, and exceptions. Citations alone do not satisfy this requirement.

When locating a figure feature or equation term helps understanding, add a few explanation-language callouts to the checked original crop. Read [teaching annotations](references/evidence-rules.md#teaching-annotations-on-original-visuals) for source preservation, clean-original access, display and no-hint boundaries; use the linked helper contract when producing one.

For a new paper's first guided-reading turn, with no specific question or selected scope, use a concrete scenario to frame the problem, why it is difficult, and the core idea. Do not assume familiarity with the background or require the user to repeat teaching preferences. Explicit questions, selected scope, and existing same-paper progress take precedence.

When a flow, module relationship, or complex causal chain benefits from a diagram, proactively provide a small diagram in chat and ground its relationships in the paper as described in the reading guidance. Do not wait for a drawing request.

Understanding checks are optional. Explain directly, skip, or continue when requested. When a progress review is useful, distinguish "independently retold", "retold after hints", and "not yet checked" in the user's language. Never treat "continue", "I understand", listening, or skipping as demonstrated mastery.

## Retelling

Read the [retelling workflow](references/retelling-mode.md) on entry. Use an already specified scope; otherwise let the user choose an overview, section, or figure.

The user explains first; then check against the source. If no retelling has been provided, give only the relevant task rather than its answer. When a follow-up is useful, focus on one key point; allow direct explanation or skipping. Switch to guided reading when the user requests sustained assistant-led explanation.

## Full Analysis and Requested Presentation Aids

Read the [full-analysis guidance](references/full-analysis-mode.md) on entering full analysis or preparing requested presentation aids. Deliver a coherent analysis and summary without per-section user answers, adapting the [summary schema](references/summary-template.md) to the paper and requested scope. Read substantive method and evidence beyond navigation excerpts, view important visuals used in conclusions, and disclose partial coverage or unresolved evidence. Do not generate a mastery record without actual retelling.

Plain full analysis includes no presentation outline, slide plan, Q&A, speaking script, or talk-duration assumption. Add only aids requested by the prompt or explicit presentation context; honor exclusions. An outline request does not imply Q&A, and a Q&A request does not imply an outline. Reuse grounded analysis for later requests rather than restarting the paper. Presentation output stays in chat unless explicitly exported.

## Questions and Wrap-Up

- Read the [question checklist](references/question-checklist.md) when auxiliary questions would help examine novelty, an experimental claim, or a limitation. Select relevant items; do not complete a checklist for every section.
- For comparisons with another paper, state what source material is available for it. Do not assemble numbers or claims from memory.
- Keep ordinary recaps brief and in chat. "Summarize" or "organize this" (including "总结一下" and "整理一下") does not escalate the mode or authorize an export; explicit full analysis receives the requested depth. Write notes, reports, or other formal exports only after an explicit save/export request, following the requested scope, location, and length; clarify an unspecified location first. Temporary reading images follow Shared Preparation. Touch an Obsidian vault only when explicitly asked to write there. Do not overwrite existing notes or other files.
- For full analysis, an explicitly requested detailed summary, or export, use the [summary template](references/summary-template.md) selectively. Export permission is not overwrite permission. Do not write back to external reference libraries by default.
- Maintain reading state only in the current conversation. Do not write it to long-term memory without a request. Do not invent the user's research ideas or personal reflections.

## Evidence and Stop Conditions

- Give a page, section, figure, table, or equation location for important conclusions, experimental numbers, and corrections. Label assistant inference as such rather than presenting it as an author conclusion.
- Distinguish "not yet located", "currently unverifiable", and "checked the relevant material but it does not state this". Not finding information does not establish that the paper omits it.
- If an image cannot be viewed, explain only the available text and caption. Mark plotted trends, values, and uncertainty-band meanings as unverified.
- When relevant source material is missing, pause the corresponding correctness judgment and request the needed pages or text. Continue with parts supported by available evidence.
- Do not rush progress, fabricate the user's retelling, or mix numbers and conclusions across papers.

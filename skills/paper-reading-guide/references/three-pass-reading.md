# Reading Depth and Teaching Guidance

Use the layered idea of Keshav's three-pass approach as optional reading depths. The teaching guidance below adapts that idea; it is not a verbatim definition of the original method. The user may jump to an equation, return to background, skip a topic, or stop. Do not require sequential completion or use elapsed time as evidence of understanding.

## Frame the Problem

For the first guided-reading turn of a new paper, with no specific question or selected scope, first build a problem framework without assuming prior familiarity. Locate the main thread through the title, abstract, introduction contributions, headings, conclusion, and relevant captions. Use a concrete scenario to explain what the authors want to solve, why it is difficult, and the core idea; then connect it to source locations. Give enough to start the discussion, varying length with the question. Develop details later as they become relevant.

Continue one concept or short causal chain at a time, adding necessary background in context. Proactively use examples or diagrams when helpful and connect them back to the paper. The user need not repeat these teaching preferences. An explicit question or selected scope takes priority; continue existing same-paper progress directly.

Use the five Cs as optional cues for missing context: Category, Context, Correctness of assumptions, Contributions, and Clarity. They guide the assistant's selection of questions rather than a required user questionnaire. Plausible-looking assumptions are not a verified result.

## Connect Concepts and Causes

Usually explain one concept or short stretch of reasoning: what this step solves, how it connects to the previous step, and why the next step is needed. When the user says "continue", resume the current reading question and use the next unresolved link to choose the next small step. Connect naturally without imposing headings on every turn. Expand for a full explanation when requested; a whole section is not a fixed unit of progress.

Build intuition with a concrete example before mapping it to the paper's terms, symbols, and conditions. When it remains suitable, carry the same example through the prose, figure, and equation, keeping its objects, quantities, and notation consistent. Change it when it no longer represents the mechanism, explaining the reason. Add the prerequisites relevant to the current difficulty, then explicitly return to the reading question and show how that background enables the next step. If the whole paper feels inaccessible, outline a few essential prerequisites, teach them in small pieces, and return to the paper. Neither assume the background is mastered nor repeatedly reteach what is already understood.

When the user says "I don't understand" ("没懂"), change the wording, example, or step size. After two consecutive such responses, materially change the explanation rather than repeating terminology. Ask one short question only when the sticking point is unclear; a formal diagnosis is not required each time.

When useful, invite a retelling, a prediction of the next step, or an explanation of a choice. Honor requests to listen directly, skip, or continue under the entrypoint's optional-check rules.

## Original Regions and Teaching Diagrams

Apply [Show the Current Source](evidence-rules.md#guided-reading-show-the-current-source) to each teaching step. Select the source region with the concept, then show it, point out the relevant detail, and explain it. Size the step so its necessary original evidence fits in the current reply; this also applies when returning to an earlier concept. The teaching schematics below supplement that evidence under the shared rules and exceptions.

Keep the visual explanation connected to the reading question:

- Before showing a figure or equation, connect what has just been established to the unresolved point that this visual helps explain. Reorient only as much as needed when returning to a visual already discussed.
- While explaining it, give the relevant reading order and follow the mechanism: what enters, what changes, and where the result goes next. For a result plot or table, follow the comparison or hypothesis being tested. Select panels, symbols, and callouts along that reasoning path, without mechanically cataloguing every element.
- After explaining it, state what it establishes for the current question and its necessary limits. Use any remaining gap to lead into the next step; if the question is resolved, close it without inventing another gap or requiring a quiz.

Express these connections naturally; they are reasoning guidance, not recurring labels or a fixed transition script. Keep source-display and retelling-timing requirements under the shared evidence rules.

For a figure feature or equation term that is easier to locate visually, use focused [teaching annotations on the original](evidence-rules.md#teaching-annotations-on-original-visuals). Tie each short callout to the same number or wording in the explanation; preserve the paper's symbols and conditions. A simple visual can stay clean with a prose explanation.

### Proactive Diagrams

- When an algorithm, module connection, data flow, or complex causal chain is clearer as a picture, proactively add a small diagram limited to the current question. Organize it around inputs, key steps, necessary branches, and outputs. Use prose or an example for simple concepts; do not force a diagram into every turn. Honor a text-only request.
- Prefer a concise Mermaid flowchart in chat. If the environment cannot render it, use a text-and-arrow diagram with a short explanation. Follow the entrypoint's explicit-request boundary for saving files.
- Label it as a teaching schematic in the user's language and distinguish it from an author-provided figure. Map important nodes and relationships to the sections, equations, or algorithm locations actually read. Disclose simplified conditions, assistant-added explanations, and unconfirmed relationships where relevant. Do not invent unsupported steps, branches, or causal links.

## Go Deeper as Needed

- **Equations:** Start with meaning, purpose, and conditions that affect understanding. Expand symbols, units, dimensions, ranges, derivations, or boundary cases when relevant or requested; use a minimal worked example when helpful. Follow the evidence rules for supplemental derivations and extraction errors.
- **Algorithms:** Explain inputs, outputs, and key steps around the current question. Expand state, stopping conditions, complexity, and guarantees when relevant rather than listing every check mechanically.
- **Experiments:** Check metrics, baselines, and comparison conditions for the particular claim being assessed. State what the results support and what generalizations remain unverified. Do not fill a fixed table for every paper.
- **Proofs or reproduction:** When needed, rebuild reasoning from the authors' assumptions and examine proofs or experiment design. Following an explanation, solving a toy example, or running a program does not establish independent mastery, a general proof, or reproduction of the paper.

When a missing prerequisite blocks deeper reading, return to that prerequisite and then resume the original question. Retelling follows the user-first workflow linked from the entrypoint.

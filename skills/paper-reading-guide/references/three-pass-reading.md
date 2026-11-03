# Reading Depth and Teaching Guidance

Use the layered idea of Keshav's three-pass approach as optional reading depths. The teaching guidance below adapts that idea; it is not a verbatim definition of the original method. The user may jump to an equation, return to background, skip a topic, or stop. Do not require sequential completion or use elapsed time as evidence of understanding.

## Frame the Problem

For the first guided-reading turn of a new paper, with no specific question or selected scope, first build a problem framework without assuming prior familiarity. Locate the main thread through the title, abstract, introduction contributions, headings, conclusion, and relevant captions. Use a concrete scenario to explain what the authors want to solve, why it is difficult, and the core idea; then connect it to source locations. Give enough to start the discussion, varying length with the question. Develop details later as they become relevant.

Continue one concept or short causal chain at a time, adding necessary background in context. Proactively use examples or diagrams when helpful and connect them back to the paper. The user need not repeat these teaching preferences. An explicit question or selected scope takes priority; continue existing same-paper progress directly.

Use the five Cs as optional cues for missing context: Category, Context, Correctness of assumptions, Contributions, and Clarity. They guide the assistant's selection of questions rather than a required user questionnaire. Plausible-looking assumptions are not a verified result.

## Connect Concepts and Causes

Usually explain one concept or short stretch of reasoning: what this step solves, how it connects to the previous step, and why the next step is needed. Connect naturally without imposing headings on every turn. Expand for a full explanation when requested; a whole section is not a fixed unit of progress.

Build intuition with a concrete example before mapping it to the paper's terms, symbols, and conditions. Add the prerequisites relevant to the current difficulty. If the whole paper feels inaccessible, outline a few essential prerequisites, teach them in small pieces, and return to the paper. Neither assume the background is mastered nor repeatedly reteach what is already understood.

When the user says "I don't understand" ("没懂"), change the wording, example, or step size. After two consecutive such responses, materially change the explanation rather than repeating terminology. Ask one short question only when the sticking point is unclear; a formal diagnosis is not required each time.

When useful, invite a retelling, a prediction of the next step, or an explanation of a choice. Honor requests to listen directly, skip, or continue under the entrypoint's optional-check rules.

## Original Regions and Teaching Diagrams

When a source image, table, equation, or original example helps the current explanation, proactively present a relevant crop near it using the evidence rules' [source-visual workflow](evidence-rules.md#original-paper-regions-in-the-conversation). Usually start with one useful region and explain what to look at; enlarge context or zoom as the question needs. Reuse a clear earlier region for an unchanged question. Keep source crops distinct from the teaching schematics below and honor pure text or unsupported-client fallback.

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

# Domain Reference Index

Choose one or more matching sheets from the title and abstract as supporting context. The paper's own definitions and assumptions take precedence. Use the general DL sheet only for a deep-learning paper without a more specific match. Analyze networking or edge-cloud offloading papers without a matching sheet from their own text; do not force a DL sheet onto them or assume training and loss functions are the subject just because DNNs appear. If the direction is unclear, first identify the research question.

The upstream maintenance note refers to `CONTRIBUTING.md` for adding domains and defining sheet structure; that maintenance document is not bundled with this skill.

## Selection Signals in the Title and Abstract

| Signals | Sheet |
|---|---|
| Reinforcement learning / RL / policy / reward / MPC / control / system identification / imitation learning / sim-to-real / robot control / Koopman / stability | `control-dl.md` |
| Audio-visual / visual sound-source localization / audio-visual separation / cross-modal / sounding object / lip / AV fusion | `audio-visual.md` |
| Microphone array / beamforming / DAMAS / CLEAN-SC / acoustic imaging / sound-source localization with an audio-only array | `acoustic-imaging.md` |
| A deep-learning paper without any of the above signals | `general-dl.md` |

Combine sheets when appropriate: audio-visual robot control can use both `control-dl.md` and `audio-visual.md`.

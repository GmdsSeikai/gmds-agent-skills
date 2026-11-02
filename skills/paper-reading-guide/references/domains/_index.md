# Domain Reference Index

Choose sheets by the actual problem, observable inputs, outputs, and objective. Use the title and abstract for an initial choice; confirm it against the model and method in the body. Load only sheets relevant to the current question. Their questions are conditional reading cues, not a required checklist or evidence of a flaw. The paper's definitions and assumptions take precedence.

For an unmatched domain, read the original paper and teach the background it needs; never force it into a listed area. Use [general DL](general-dl.md) for a deep-learning paper or architecture without a matching specialist sheet. An author's identity or research area does not establish a paper's task or strengthen its conclusions.

## Initial Signals to Confirm in the Body

| Actual problem or mechanism | Sheet |
|---|---|
| Task or DNN-layer placement, application offloading, edge/cloud execution costs | [Edge-cloud offloading](edge-cloud-offloading.md) |
| Graph optimization, min-cut/max-flow, spanning trees, changing network topology or capacity | [Network optimization](network-optimization.md) |
| Learning to classify network traffic from packets, flows, or sessions | [Traffic learning](traffic-learning.md) |
| Transferring a visual teacher's features or predictions to a student | [Visual distillation](visual-distillation.md) |
| Matching text descriptions to images, including text-based person retrieval | [Text-image retrieval](text-image-retrieval.md) |
| RL / policy / reward / MPC / control / system identification / imitation learning / sim-to-real / Koopman / stability | [Control and DL](control-dl.md) |
| Evidence of both audio and vision: sound-source localization with images, audio-visual separation, lip/audio alignment or AV fusion | [Audio-visual learning](audio-visual.md) |
| Audio-only microphone arrays / beamforming / DAMAS / CLEAN-SC / acoustic imaging | [Acoustic imaging](acoustic-imaging.md) |
| A deep-learning task without a matching specialist sheet | [General DL](general-dl.md) |

Combine sheets when their mechanisms matter: offloading with a graph reduction can use offloading + network optimization; RL for networking can add control + the relevant network sheet. Audio-visual robot control can combine control + audio-visual.

Do not route on a word alone. A DNN inference-placement paper need not study training or losses; a learning-augmented optimizer need not implement a neural predictor. Trace its mechanism. Generic "cross-modal" does not establish audio: text-image retrieval uses text and images. Other visual architectures retain general-DL fallback rather than automatically becoming distillation papers.

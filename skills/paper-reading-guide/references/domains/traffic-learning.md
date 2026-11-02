# Domain Reference: Learning from Network Traffic

Use when a learned model classifies or recognizes traffic. These are conditional reading questions, not accusations about a paper or a checklist to complete.

## Establish What One Example Contains

- Identify the prediction unit: packet, unidirectional flow, bidirectional flow, session, or a defined window. Locate aggregation, ordering, truncation, padding, and the label attached to that unit. Do not treat these units as interchangeable.
- Trace actual observable inputs: packet bytes or headers, lengths, directions, timing, statistics, or other signals only as reported. State capture-point and encryption assumptions. Do not infer access to plaintext payloads merely because the task is traffic classification.
- Read preprocessing before explaining the architecture: which fields are retained or masked, normalization, byte encoding, segmentation, and how sequences become tensors or images. Do not invent a spatial layout from a model name.

## Connect Branches to the Task

- For spatial and temporal branches, locate what each sees, what its dimensions mean, and where information is fused. "Spatial" may describe within-example structure rather than physical geography; "temporal" may describe ordered packets rather than a long-term traffic forecast. Confirm from the method.
- Distinguish architecture, supervision, and training objectives from the inference path. Explain one input-to-output chain or branch at a time. Use a small invented sequence when helpful, labeling simplifications and mapping it back to the source.

## Evaluate the Particular Claim

- Locate the dataset, classes, collection conditions, and split unit. When assessing leakage, ask whether related packets, overlapping windows, flows, sessions, devices, users, or capture periods cross splits as relevant; inspect the stated procedure before judging. An abstract that omits the split does not establish leakage.
- For imbalance, locate class counts, sampling or loss treatment if any, and per-class results. Accuracy can conceal rare-class failures; inspect precision, recall, F1, macro/micro/weighted averaging, and confusion matrices only as needed. Preserve each metric's task and averaging definition.
- For generalization claims, distinguish a held-out portion of one capture from cross-device, cross-network, cross-time, cross-application, or cross-dataset evaluation. Do not call a random split cross-scenario evidence.
- For efficiency or deployment claims, check example length, preprocessing, hardware, batch size, latency/throughput units, and resource costs. A classifier's test accuracy does not by itself establish live-network performance.
- Use branch ablations and comparable baselines to examine claimed contributions. Unlocated details remain questions; do not fill them from a familiar architecture or another paper.

# Domain Reference: Visual Knowledge Distillation

Use when a visual model transfers knowledge from a teacher to a student. Other visual architectures use the general-DL fallback unless a different specialist sheet matches; a visual task alone does not imply distillation.

## Trace the Transfer

- Identify the task, teacher, student, and transferred signal: predictions, intermediate features, attention, relations, or other representations actually defined. Locate which models are pretrained, fixed, or jointly trained.
- For feature transfer, inspect layer choice, spatial resolution, channel dimensions, and any projection, resizing, normalization, or alignment. Similar-looking feature maps need not be directly comparable. Distinguish a training adapter from a component retained for inference.
- If masks are used, identify spatial versus channel masking, what is selected or suppressed, how masks are obtained, and where they enter the computation. Do not assume all methods use masking or that masking necessarily selects the most informative regions.
- Read each relevant loss's target, reduction, weighting, and gradient path. Separate the task loss from distillation terms. Use a small labeled teaching example to explain alignment or masking before expanding a full objective when helpful; invented values do not establish method effectiveness.

## Separate Training from Inference

Draw separate training and inference paths when that resolves confusion. Locate whether the teacher, masks, adapters, and extra branches remain at deployment. Teacher computation may be a training expense even when the deployed student stays small; verify what is actually retained.

## Evaluate the Claimed Benefit

- Compare with the same student trained without distillation under comparable data, initialization, schedule, augmentation, and compute. Check teacher quality and teacher/student capacity when interpreting gains; a stronger teacher alone does not isolate the proposed transfer mechanism.
- Use the paper's ablations to examine alignment, mask types, losses, or layer choices only when those components exist. Do not treat a missing detail in an excerpt as an established omission from the paper.
- Report the task metric and accuracy/efficiency trade-off with the right scope: parameters, operations, measured latency, memory, and training cost are different quantities. Fewer parameters or FLOPs do not automatically prove lower latency on a particular device.
- Keep datasets, input resolution, hardware, and evaluation conditions attached to numbers. Separate source-supported results from an assistant's proposed explanation of why a component helps.

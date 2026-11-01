# General Reference: Deep-Learning Papers

Use this sheet when a deep-learning paper has no matching specialist sheet. Select relevant questions around problem setting, method, training, evaluation, and generalization.

## General Paper Framework

1. **Problem or task:** Inputs, outputs, and what the loss measures.
2. **Method or architecture:** Network family (CNN, Transformer, diffusion, graph network, and so on), key modules, and inductive bias.
3. **Training:** Data, objectives, optimizer, and key techniques such as pretraining, self-supervision, contrastive learning, or distillation.
4. **Evaluation:** Datasets, metrics, baselines, and components examined by ablations.
5. **Generalization and limitations:** Distribution shift, scale, computational cost, and failures.

## Common Concepts

- **Inductive bias:** Assumptions built into an architecture, such as convolutional locality or attention's global relationships.
- **Self-supervision and pretraining followed by fine-tuning:** Learn representations without labels, then transfer them to a smaller downstream dataset.
- **Contrastive learning:** Learn representations by bringing positive pairs closer and pushing negative pairs apart, using objectives such as InfoNCE.
- **Ablation:** Remove components in turn and measure performance changes to assess which parts are useful.
- **End-to-end and staged learning:** Train the whole pipeline jointly or split it into separately learned stages.

## General Follow-Up Questions

- Is the actual contribution an architecture, training objective, dataset or task, or analysis? Look past promotional wording.
- Is improvement attributable to the method, model size, more data, or more compute? Do ablations separate these effects?
- Are baselines fair and evaluated under equivalent settings?
- Are significance or multiple random-seed runs reported?
- What does reproduction require in terms of data availability, compute, and released code?

## Optional Summary Fields

- Contribution type: architecture / training objective / dataset or task / analysis.
- Source of improvement: method versus larger models, more data, or more compute, and whether ablations distinguish them.
- Significance: seed count, variance, or confidence reporting.
- Reproduction cost: data availability, compute, and released code.

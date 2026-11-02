# Domain Reference: Text-Image Retrieval

Use for matching a text query to images or an image query to text, including text-based person retrieval. Text and images are the modalities here; generic cross-modal wording supplies no evidence of an audio branch.

## Define the Matching Problem

- Identify query direction, gallery, relevant matches, and output ranking. For person retrieval, distinguish matching identity from matching a single image-caption pair. Read how multiple images or descriptions for one identity are treated.
- Trace text and image inputs, encoders, global/local features, alignment, fusion if any, and the final similarity score. Locate which representations interact during training and which are available at retrieval time. Do not assume every system fuses modalities before scoring.
- Locate positive and negative definitions, sampling, and training objectives. Another image of the same identity may or may not be a negative under the stated protocol; inspect it rather than importing generic contrastive-learning assumptions.
- Explain modality alignment through one concrete query-and-gallery example when helpful. Label invented descriptions and simplified scores; connect them to the actual matching mechanism before discussing an equation.

## Read the Evaluation Protocol

- For identity-based tasks, locate whether training, validation, and test identities overlap, and how query/gallery instances are constructed. For other retrieval tasks, inspect the corresponding item/pair split. Consider duplicate or related samples only when assessing a relevant generalization or leakage claim.
- Interpret Rank-1/Rank-k, Recall@K, mAP, or other metrics using the paper's relevance definition, gallery size, query direction, and averaging. Do not equate classification accuracy with retrieval quality or compare numbers from different protocols as if they were interchangeable.
- Examine branch contributions and ablations around the claimed mechanism: local/global alignment, attribute handling, feature branches, or losses only when present. Check comparable encoders, pretraining data, and computation before attributing a gain to a new branch.
- When relevant, inspect possible shortcut cues such as color, background, camera, or repeated descriptions and the experiments testing reliance on them. A cue's plausibility is a question, not proof that a model uses it or that a dataset is flawed.
- Separate results on the reported datasets from cross-camera, cross-domain, changed-gallery, or deployment claims. Keep reported evidence distinct from an assistant's hypothesis about robustness.

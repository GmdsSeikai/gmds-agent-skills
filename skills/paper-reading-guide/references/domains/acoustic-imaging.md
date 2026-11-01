# Domain Reference: Acoustic Imaging, Microphone Arrays, and Deep Learning

Consult this sheet when explaining methods, baselines, and terminology. It offers working intuition rather than rigorous definitions; the paper takes precedence when its account differs.

## Basic Pipeline

Microphone array captures multichannel signals -> compute the cross-spectral matrix (CSM) from channel-pair cross spectra -> beamforming scans spatial points -> produce a source map or beamforming map.

## Conventional Beamforming (CB / DAS)

For each scan point, form a steering-vector-weighted sum. Wide main lobes limit resolution and high side lobes create apparent ghost sources, especially at low frequencies. Many subsequent methods address these two issues.

## Point Spread Function (PSF)

The array's response pattern to an ideal point source. The PSF varies strongly with frequency and underlies resolution limits and side lobes. Deconvolution methods aim to remove its effect from the dirty map.

## Three Classical Deconvolution or Side-Lobe Baselines

- **DAMAS (Brooks & Humphreys, 2006):** Iteratively deconvolves a beamforming map to recover the underlying source distribution. Physically interpretable but slow and sensitive to modeling assumptions. DL work often compares against it or unfolds it into a network.
- **CLEAN-SC (Sijtsma, 2007):** Iteratively subtracts components spatially coherent with a peak source to suppress side lobes. Can recover absolute sound power; a common industrial baseline, particularly for multiple sources.
- **Functional beamforming (Dougherty, 2014):** Uses a matrix-power operation on the CSM with parameter nu to suppress side lobes and improve dynamic range, with limited resolution improvement. Often supplies a low-frequency input map for DL.

## Key Terms

- **CSM:** Cross-spectral matrix; second-order statistics of array data, often used as input.
- **Grid-based and grid-free:** Grid-based methods produce heatmaps on a predefined grid and inherit its resolution limit. Grid-free methods directly regress source coordinates, for example with a ResNet, and can exceed grid resolution.
- **Rayleigh limit:** A minimum separable spacing between two sources, used as a reference for super-resolution.
- **Sim-to-real gap:** Performance loss when a model trained in simulation is transferred to a real array; noisy pretraining followed by limited real-data fine-tuning or domain adaptation can mitigate it.

## Common Deep-Learning Approaches

1. **Deconvolution:** CNNs, U-Nets, or DenseNets map a dirty beamforming map to a clean source map: beamforming input -> deconvolved output.
2. **Model-driven unfolding:** Turn iterative methods such as DAMAS or FISTA into trainable networks, such as DAMAS-FISTA-Net, combining physical interpretability and speed under a physics-constrained approach.
3. **Direct, grid-free regression:** Predict source positions p directly, sometimes jointly with source intensity s.
4. **Training strategies:** Generate simulated data and add noise. Sampling strategies, such as Latin hypercube sampling, affect data efficiency. A two-stage strategy uses simulation pretraining followed by real-data fine-tuning.

## Common Metrics

- Spatial resolution and performance relative to the Rayleigh limit.
- Localization error: predicted versus true position.
- Sound-intensity or sound-power error: quantitative accuracy.
- Computation time and real-time capability.
- Source-count estimation and separation accuracy for multiple sources.

## Teaching Cues

- For deconvolution, side-lobe suppression, or improved resolution, identify which CB problem is being addressed: main-lobe width or side lobes.
- Classify a DL method as deconvolution, unfolding, or direct regression before discussing novelty relative to prior work.
- When frequency ranges appear, check whether low-frequency operation is the focus; low-frequency resolution is a recurring difficulty.

## Domain-Specific Questions

Use with `../question-checklist.md`. Examine input representation (CSM, beamforming map, or time-domain signal), operating frequency range and low-frequency focus, array setup (simulated or measured, channel count, aperture), output (grid-based or grid-free, intensity estimation), physical constraints (purely data-driven or unfolded DAMAS/FISTA), training data and sim-to-real transfer, baselines (CB, DAMAS, CLEAN-SC, functional beamforming), metrics (resolution, localization error, intensity error), multi-source separation, generalization, and limitations.

## Optional Summary Fields

- Input: CSM / beamforming map / time-domain signal; complex-valued or not.
- Frequency range: low-frequency focus, single-frequency / multifrequency / broadband.
- Output: grid-based / grid-free; intensity estimation or not.
- Physical constraints: purely data-driven or unfolded DAMAS/FISTA.
- Baselines and metrics: CB / DAMAS / CLEAN-SC / functional beamforming; resolution / localization / intensity error.
- Data and sim-to-real: simulation or measurement, array size, generalization across operating conditions.

# Domain Reference: Audio-Visual Learning

Covers audio-visual fusion, visual sound-source localization, audio-visual separation, events and actions, cross-modal representations, and audio-visual navigation.

## Problem Setting

Use correspondence between audio and visual modalities to perform a task. The motivation is their natural spatial and temporal alignment, such as a sounding object in view or lip movements corresponding to speech, which can provide mutual supervision and a source of self-supervision.

Common tasks locate the sounding object in an image, separate one object's sound from a mixture, assess synchronization or shared origin, retrieve across modalities, recognize or enhance audio-visual speech, or navigate using audio and vision.

## Core Concepts

- **Cross-modal correspondence and synchronization:** Whether simultaneous sound and image originate from the same event; a supervision signal for many self-supervised methods.
- **Audio-visual fusion:** Early, late, or attention-based fusion; audio features such as Mel spectrograms or VGGish combined with visual CNN or ViT features.
- **Visual sound-source localization:** A heatmap over the image indicating what is making the sound.
- **Audio-visual separation:** Use visual cues to split mixed audio, isolating the sound of the object being observed.
- **Contrastive and self-supervised learning:** Learn representations from paired positive and negative audio-visual examples, such as same-video positives and cross-video negatives.
- **Temporal alignment and lip motion:** Correspondence between mouth movement and speech for audio-visual speech processing and speaker separation.

## Datasets

- Sound-source localization: Flickr-SoundNet and VGG-SS (VGGSound Source).
- Audio-visual events: AVE (Audio-Visual Event).
- Audio-visual separation: MUSIC (musical performances) and AVSpeech.
- Audio/video classification pretraining: VGGSound, AudioSet, and Kinetics.

## Common Metrics

- **Localization:** cIoU (consensus IoU) and AUC, assessing agreement between localization heatmaps and ground-truth boxes.
- **Separation:** SDR, SI-SDR, PESQ, and STOI for signal separation, speech quality, or intelligibility.
- **Retrieval and correspondence:** Recall@K and accuracy.
- **Events and actions:** Classification accuracy and mAP.

## Domain-Specific Questions

- Which modality features are used, and how are they fused: early, late, or attention-based?
- Is supervision manually annotated or derived from audio-visual correspondence?
- What is the output: an image heatmap, separated waveform, class label, or retrieval ranking?
- Are datasets and metrics appropriate for the subtask, such as cIoU/AUC for localization or SI-SDR for separation?
- Are difficult cases addressed: no visible sounding object, off-screen sound, or several sounding objects?
- How well does the method generalize across datasets or scenarios? Is degradation studied when audio or vision is missing?

## Optional Summary Fields

- Modalities and fusion: early / late / attention-based, audio features and visual features.
- Supervision source: manual labels or correspondence-based self-supervision.
- Output: image heatmap / separated waveform / classification / retrieval.
- Difficult cases: off-screen sound, no sounding object, or simultaneous sounding objects.
- Dataset and metric suitability for the subtask, such as cIoU/AUC or SI-SDR.

# Visual NLP DICOM Dataset and Metrics

![Sample DICOM](resources/pixel_metadata_sample.png)

## Overview

This repository contains DICOM de-identification datasets, notebooks, metrics, and visual results for evaluating John Snow Labs Visual NLP across two comparison workflows.

## Repository Structure

| Path | Description |
|---|---|
| `Presidio/` | Dataset generation and Visual NLP vs Presidio evaluation. |
| `Pixels_Platform/` | Visual NLP vs Databricks Pixels evaluation on the MIDI-B dataset. |
| `Synthetic_V2/` | Planned synthetic dataset with pixel, PDF-encapsulated, metadata PHI, and ground truth files. |
| `resources/` | Root README diagrams and sample result images. |

## Experiments

| Experiment | Dataset | Pipeline | Details |
|---|---|---|---|
| Visual NLP vs Presidio | Synthetic text overlay DICOM dataset | pre-MIDI-Pixel Visual NLP pixel de-identification pipeline | [Presidio README](Presidio/README.md) |
| Visual NLP vs Databricks Pixels | MIDI-B validation dataset | post-MIDI-Pixel Visual NLP de-identification pipeline | [Pixels Platform README](Pixels_Platform/README.md) |

## Synthetic_V2

`Synthetic_V2` is planned as an expanded synthetic dataset section containing:

- Pixel data with PHI.
- PDF-encapsulated DICOM data.
- Metadata with PHI.
- Ground truth files for the synthetic PHI.

## Workflow Diagrams

### DICOM De-Identification

![De-Identification Flow Diagram](resources/fig_pipeline_overview.png)

### DICOM Metadata De-Identification

![Metadata Flow Diagram](resources/fig_metadata_workflow.png)

## Sample Results

### Pixel De-Identification

![Pixel De-Identification Result 3 Samples](resources/fig_before_after_3.png)

### Metadata De-Identification

![Metadata De-Identification Result](resources/fig_ner_text_before_after.png)

## Speed Benchmark

### Dataset Description

- **File count:** 100 files, with 10 frames per file - **1,000 total frames**.
- **File size:** Varies from 70 MB to 400 MB per file.
- **Frame scaling:** Frames are scaled down by 75% after extraction.

### Cluster Configuration

| Role | Instance Type | GPU | vCPUs | Memory |
|---|---|---|---|---|
| Driver | m5d.16xlarge | - | 64 | 256 GB |
| Worker | g4dn.4xlarge (T4) | 16 GB | 16 | 64 GB |

### Benchmark Results

| Workers | Time Taken (s) | Cost (DBU/h) |
|---|---|---|
| 2 | 4,581.85 | 16.66 |
| 4 | 2,379.57 | 22.36 |
| 6 | 1,647.01 | 28.06 |

## References

- **Medium Article:** [De-Identifying DICOM Files: A Step-by-Step Guide with John Snow Labs Visual NLP](https://medium.com/john-snow-labs/de-identifying-dicom-files-a-step-by-step-guide-with-john-snow-labs-visual-nlp-2c21b60f92a8)
- **Visual NLP Workshop DICOM Notebooks:** [GitHub - visual-nlp-workshop / jupyter / DICOM](https://github.com/JohnSnowLabs/visual-nlp-workshop/tree/master/jupyter/Dicom)

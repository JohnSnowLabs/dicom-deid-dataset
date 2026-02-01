# DICOM De-identification Evaluation: Visual-NLP vs. Databricks Pixels

This repository contains the benchmarking suite and implementation code for evaluating **John Snow Labs Visual NLP** against the **Databricks Pixels** framework using the **MIDI-B (Medical Image De-Identification Benchmark)** validation dataset.

## Project Overview
The goal is to compare the efficacy of two industry-leading platforms in:
1.  **Metadata Scrubbing**: Removing PII from DICOM headers.
2.  **Pixel Redaction**: Identifying and masking burnt-in text (PHI) within the image frames.

## Requirements

### Libraries & Platforms
* **Spark-NLP & Healthcare-NLP**: For Clinical NER and PII detection.
* **Visual-NLP**: For DICOM parsing and pixel-level redaction.
* **Data Science Stack**: `scikit-learn`, `pandas`, `openpyxl`.

### Datasets
* **MIDI-B Validation Dataset**: (https://www.cancerimagingarchive.net/collection/midi-b-test-midi-b-validation/)
* **MIDI-B Truth Database**: Evaluation labels for metadata and burnt-in PHI.
* **Databricks Pixels Subset** : (https://github.com/databricks-industry-solutions/pixels/blob/2fdbe9835015cc428473d7407ba01a623c407408/03b-Image-DeIdentification.ipynb)

### File Descriptions

| File | Description |
| :--- | :--- |
| **`Visual_NLP_Pixels_Comparison.ipynb`** | The primary notebook used to define the pipeline, execute the de-identification workflows, and generate comparative metrics. |
| **`jsl_vs_db_midib_pipeline_results.xlsx`** | **Final Results.** Metrics generated using the curated MIDI-B pipeline, optimised for high-precision clinical de-identification. |
| **`jsl_vs_db_ner_pipeline_results.xlsx`** | **Experimental Results.** Baseline data generated using a standard NER pipeline during the initial pre-experimentation phase. |

### Benchmarking Results

| Model / Pipeline | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- |
| **Databricks Pixels** | 1.0000 | 0.2857 | 0.4444 |
| **Visual NLP (Pre-MIDI-B)** | 0.9063 | **0.8286** | **0.8657** |
| **Visual NLP (Post-MIDI-B)** | **1.0000** | 0.7143 | 0.8333 |

### Performance Analysis

The results demonstrate a clear trade-off between precision and sensitivity across the evaluated platforms:

* **Databricks Pixels**: While maintaining perfect precision (1.0), its low recall (0.2857) leaves the majority of PHI unredacted and vulnerable.
* **Visual NLP (Pre-MIDI-B)**: Our initial **experimentation phase** established the strongest baseline for sensitivity, achieving the highest recall (0.8286) and F1-score out-of-the-box.
* **Visual NLP (Post-MIDI-B)**: Following **post-experimentation refinement**, we matched the 1.0 precision of the Pixels platform but reached a recall of 0.7143. 

**Conclusion**: The curated Visual NLP pipeline delivers a **2.5x improvement in recall** over the Pixels platform, ensuring clinical-grade accuracy without the risk of false positives.


### Scalability & Flexibility

Visual NLP's performance is driven by its deep integration with the John Snow Labs ecosystem:

* **10,000+ Pretrained Models**: Access a massive library of specialised models. Changing the underlying NER models can directly effect and optimize the final de-identification results based on the specific modality or use case.
* **Global Support**: The platform works across multiple languages and is designed for high flexibility in deployment.
* **Modularity**: Highly flexible pipelines allow for rapid adjustments to the components to meet evolving privacy standards.

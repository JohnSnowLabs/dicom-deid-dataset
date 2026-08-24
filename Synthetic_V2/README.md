# Synthetic_V2 Dataset

This directory contains a synthetic DICOM de-identification dataset with pixel PHI, PDF-encapsulated DICOM files, metadata PHI, and ground truth annotations.

## Contents

- [Dataset Summary](#dataset-summary)
- [Installation and Download](#installation-and-download)
- [Downloaded Data Structure](#downloaded-data-structure)
- [Files](#files)
- [Notebooks](#notebooks)
- [Results](#results)
- [Ground Truth Files](#ground-truth-files)
- [Resources](#resources)

## Dataset Summary

| Category | Count | Description |
|---|---:|---|
| Pixel DICOM records | 40 | Synthetic DICOM files with pixel-level PHI and metadata PHI. |
| PDF-encapsulated DICOM records | 10 | Synthetic encapsulated PDF DICOM files with document and metadata PHI. |
| Ground truth files | 2 | JSON annotations for image/pixel and PDF-encapsulated data. |
| De-identification notebooks | 2 | Visual NLP workflows for pixel and PDF-encapsulated DICOM de-identification. |
| Metadata strategy rows | 24 | DICOM tag-level actions used for metadata de-identification. |

## Installation and Download

Install the Hugging Face Hub client:

```bash
pip install -U huggingface_hub
```

Download the dataset into a local `data/` directory:

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="nk1221/Synthetic_Dicom_V2",
    repo_type="dataset",
    local_dir="./data"
)
```

Run the download command from this directory if you want the notebooks to use `Synthetic_V2/data/` as the local dataset path.

## Downloaded Data Structure

The downloaded dataset is organized by original inputs and de-identified outputs, with separate folders for pixel DICOM data and PDF-encapsulated DICOM data.

| Path | Description |
|---|---|
| `data/original/dicom/pixel/` | Original DICOM files with pixel PHI. |
| `data/original/dicom/pdf/` | Original PDF-encapsulated DICOM files. |
| `data/original/image/pixel/` | Rendered images for pixel DICOM files. |
| `data/original/image/pdf/` | Rendered images for PDF-encapsulated DICOM files. |
| `data/deid/dicom/pixel/` | De-identified pixel DICOM outputs. |
| `data/deid/dicom/pdf/` | De-identified PDF-encapsulated DICOM outputs, when generated. |
| `data/deid/image/pixel/` | Rendered de-identified pixel outputs. |
| `data/deid/image/pdf/` | Rendered de-identified PDF outputs. |

## Files

| Path | Description |
|---|---|
| `Image_Ground_Truth.json` | Ground truth for pixel DICOM files, including metadata PHI and pixel PHI annotations. |
| `Encapsulated_Ground_Truth.json` | Ground truth for PDF-encapsulated DICOM files, including metadata PHI and document PHI annotations. |
| `Visual_NLP_Pixel_DeIdentification.ipynb` | Visual NLP notebook for pixel DICOM de-identification. |
| `Visual_NLP_Encapsulated_PDF_DeIdentification.ipynb` | Visual NLP notebook for PDF-encapsulated DICOM de-identification. |
| `dicom_metadata_deidentification_strategy.csv` | DICOM metadata de-identification strategy used by the notebooks. |

## Notebooks

The notebooks define the Visual NLP and Healthcare NLP stages required to ingest synthetic DICOM files, detect PHI, apply metadata and pixel/document de-identification, and generate de-identified outputs.

| Notebook | Workflow |
|---|---|
| `Visual_NLP_Pixel_DeIdentification.ipynb` | Pixel PHI de-identification for synthetic DICOM images. |
| `Visual_NLP_Encapsulated_PDF_DeIdentification.ipynb` | PHI de-identification for PDF-encapsulated synthetic DICOM files. |

## Results

The notebooks validate de-identified outputs by running OCR and metadata extraction on the generated DICOM files, then comparing the extracted PHI against the ground truth files.

| Notebook | Files Evaluated | Metadata Passed | Metadata Failed | PHI Passed | PHI Failed |
|---|---:|---:|---:|---:|---:|
| `Visual_NLP_Pixel_DeIdentification.ipynb` | 40 | 1,040 | 0 | 120 | 0 |
| `Visual_NLP_Encapsulated_PDF_DeIdentification.ipynb` | 10 | 280 | 0 | 114 | 14 |

For the pixel DICOM workflow, all metadata and pixel PHI checks passed in the notebook output. For the PDF-encapsulated workflow, all metadata checks passed, with 114 document PHI checks passing and 14 remaining failures.

## Ground Truth Files

### Image_Ground_Truth.json

Each record includes:

- `file`: DICOM filename.
- `image_file`: Rendered image filename.
- `encapsulated`: Always `false` for this file.
- `pixel_phi_format`: Layout category for pixel PHI.
- `metadata`: DICOM metadata tags, values, PHI flags, and PHI spans.
- `pixel`: Pixel-level PHI annotations.

### Encapsulated_Ground_Truth.json

Each record includes:

- `file`: DICOM filename.
- `pdf_file`: Source PDF filename.
- `encapsulated`: Always `true` for this file.
- `document_type`: Synthetic document category.
- `metadata`: DICOM metadata tags, values, PHI flags, and PHI spans.
- `pdf`: PDF/document-level PHI annotations.

## Resources

| Resource | Description |
|---|---|
| [Visual NLP DICOM Workshop](https://github.com/JohnSnowLabs/visual-nlp-workshop/tree/master/jupyter/Dicom) | Visual NLP DICOM notebooks and workshop examples. |
| [DICOM De-identification Blogpost](https://medium.com/john-snow-labs/de-identifying-dicom-files-a-step-by-step-guide-with-john-snow-labs-visual-nlp-2c21b60f92a8) | Step-by-step Visual NLP DICOM de-identification walkthrough. |
| [Metadata De-identification](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/strategy_actions.md) | Visual NLP guide to metadata de-identification. |
| [MIDI/Pseudo-PHI DICOM Paper](https://www.nature.com/articles/s41597-021-00967-y) | Scientific Data paper describing a DICOM dataset for evaluating medical image de-identification. |
| [Visual NLP Skill](https://www.johnsnowlabs.com/visual-nlp/) | John Snow Labs Visual NLP de-identification skill for your LLM. |

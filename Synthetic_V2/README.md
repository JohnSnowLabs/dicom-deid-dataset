# Synthetic_V2 Dataset

This directory contains a synthetic DICOM de-identification dataset with pixel PHI, PDF-encapsulated DICOM files, metadata PHI, and ground truth annotations.

## Contents

- [Dataset Summary](#dataset-summary)
- [Files](#files)
- [Notebooks](#notebooks)
- [Metadata De-identification Strategy](#metadata-de-identification-strategy)
- [Ground Truth Files](#ground-truth-files)

## Dataset Summary

| Category | Count | Description |
|---|---:|---|
| Pixel DICOM records | 40 | Synthetic DICOM files with pixel-level PHI and metadata PHI. |
| PDF-encapsulated DICOM records | 10 | Synthetic encapsulated PDF DICOM files with document and metadata PHI. |
| Ground truth files | 2 | JSON annotations for image/pixel and PDF-encapsulated data. |
| De-identification notebooks | 2 | Visual NLP workflows for pixel and PDF-encapsulated DICOM de-identification. |
| Metadata strategy rows | 24 | DICOM tag-level actions used for metadata de-identification. |

## Files

| Path | Description |
|---|---|
| `Image_Ground_Truth.json` | Ground truth for pixel DICOM files, including metadata PHI and pixel PHI annotations. |
| `Encapsulated_Ground_Truth.json` | Ground truth for PDF-encapsulated DICOM files, including metadata PHI and document PHI annotations. |
| `Visual_NLP_Pixel_DeIdentification.ipynb` | Visual NLP notebook for pixel DICOM de-identification. |
| `Visual_NLP_Encapsulated_PDF_DeIdentification.ipynb` | Visual NLP notebook for PDF-encapsulated DICOM de-identification. |
| `dicom_metadata_deidentification_strategy.csv` | DICOM metadata de-identification strategy used by the notebooks. |


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

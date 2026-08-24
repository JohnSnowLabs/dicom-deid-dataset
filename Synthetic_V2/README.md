# Synthetic_V2 Dataset

This directory contains a synthetic DICOM de-identification dataset with pixel PHI, PDF-encapsulated DICOM files, metadata PHI, and ground truth annotations.

## Contents

- [Dataset Summary](#dataset-summary)
- [Files](#files)
- [Archive Structure](#archive-structure)
- [Ground Truth Files](#ground-truth-files)

## Dataset Summary

| Category | Count | Description |
|---|---:|---|
| Pixel DICOM records | 40 | Synthetic DICOM files with pixel-level PHI and metadata PHI. |
| PDF-encapsulated DICOM records | 10 | Synthetic encapsulated PDF DICOM files with document and metadata PHI. |
| Ground truth files | 2 | JSON annotations for image/pixel and PDF-encapsulated data. |

## Files

| Path | Description |
|---|---|
| `data.zip` | Archive containing original and de-identified DICOM/image outputs. |
| `Image_Ground_Truth.json` | Ground truth for pixel DICOM files, including metadata PHI and pixel PHI annotations. |
| `Encapsulated_Ground_Truth.json` | Ground truth for PDF-encapsulated DICOM files, including metadata PHI and document PHI annotations. |

## Archive Structure

`data.zip` contains original and de-identified outputs organized by modality and representation.

| Archive Path | Count | Description |
|---|---:|---|
| `data/original/dicom/pixel/` | 40 | Original pixel DICOM files. |
| `data/original/image/pixel/` | 40 | Rendered images for original pixel DICOM files. |
| `data/original/dicom/pdf/` | 10 | Original PDF-encapsulated DICOM files. |
| `data/original/image/pdf/` | 10 | Rendered images for original PDF-encapsulated DICOM files. |
| `data/deid/dicom/pixel/` | 40 | De-identified pixel DICOM files. |
| `data/deid/image/pixel/` | 45 | De-identified rendered pixel images. |

## Ground Truth Files

Both ground truth files use a top-level `dicom_files` array.

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

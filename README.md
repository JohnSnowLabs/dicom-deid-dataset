# dicom-deid-dataset
## Public Dataset: DICOM with Synthetic Text Overlays for De-Identification Research

This dataset has been created as a resource for evaluating medical image de-identification methods. Our approach was inspired by the paper "A DICOM dataset for evaluation of medical image de-identification", which explores synthetic overlays in DICOM images. As a starting point, we used the publicly available Pseudo-PHI DICOM dataset. (See attached license for details.)

### Dataset Generation Process
1. Image Extraction: Images were extracted from the original DICOM files.
2. Synthetic Overlay Generation:
    - Metadata-derived text overlays were created, simulating patient-identifying information.
    - Two types of text annotations were generated.
    - Text overlays were placed at varying corner positions within the images.
3. Ground Truth (GT) Annotation:
    - The generated text annotations, along with their precise coordinates, were saved as GT annotation files.
4. Text Burn-in Process:
    - The synthetic text was burned into the extracted images at the corresponding coordinates.
5. New DICOM File Creation:
    - The modified images (with burned-in text) were saved as new DICOM files.
    - Multi-frame DICOM files from the original dataset were split into multiple single-frame DICOM files.
### Dataset Contents
- DICOM Files: Single-frame DICOM images with burned-in text overlays.
- Extracted Images: Original images before text was applied.
- GT Annotation Files: Ground truth data containing the generated text and its coordinates.

This dataset is intended to support research in medical image de-identification and text removal techniques.

### Metrics

Here are the metrics of multiple pipelines.

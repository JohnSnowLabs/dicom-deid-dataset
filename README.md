# dicom-deid-dataset
## Public Dataset: DICOM with Synthetic Text Overlays for De-Identification Research

This dataset has been created to evaluate medical image de-identification methods. Our approach was inspired by the paper "A DICOM dataset for evaluation of medical image de-identification", which explores synthetic overlays in DICOM images. As a starting point, we used the publicly available Pseudo-PHI DICOM dataset. (See attached license for details.)

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

### File Structure 

- Presidio_Metrics.ipynb
- Visual_NLP_Metrics.ipynb 
- creds.json ( Visual NLP Credentials )
- dicom_image_pii_verify_engine.py ( Fix for Presidio )
- prepare_data.py ( Script Used to Generate Ground Truth and Extract Dicom Files From Zip )
- results/detected_phi ( JSON files with NER Results )
- results/image_result ( Obfuscated final Images )

### Environment

We created two environments to measure Visual NLP pipelines with Presidio [ Google Collab, Databricks ] 

Google Colab:

- We used the standard A100 (40GB) GPU Environment.
- Used for both Visual NLP Pipelines and Presidio.

Databricks:

 - 16.0 ML (includes Apache Spark 3.5.2, GPU, Scala 2.12)
 - Visual NLP needs Cuda 12.X and cudNN 9.X for our in-house ONNX models.
 - Used only for Visual NLP Pipelines.

### Metrics

| **Model**                                              | **Precision** | **Recall** | **F1-Score** |
|-----------------------------------------------------------|-------------|--------|----------|
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)** | **0.8**     | **0.8** | **0.8**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large (Scala)** | **0.9**     | **0.8** | **0.8**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)** | **0.7** | **0.4** | **0.5**  |
| 🐍 **ImageToText (Python)**                               | **0.5**     | **0.3** | **0.4**  |
| 🔴 **Presidio**                                           | **0.09**    | **0.13** | **0.1**  |

### Time Metrics 

- Google Colab Notebook utilized a single A100 GPU ( 40 GB ) - 7.62 Credits/hr
- Databricks Standalone Driver 64 GB - 2.85 dbu/h
- Databricks Cluster Driver 64 GB, with minimum & maximum 2 Executors 16GB - 4.27 dbu/h
  
| **Model**                                                   | **Google Colab** | **Databricks Standalone** | **Databricks Cluster** |
|------------------------------------------------------------|----------------|------------------------|------------------------|
|                                                            | **Avg Time**           | **Avg Time** | **Avg Time** |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)**  | **3.63**              | **4.66**     | **2.76**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large (Scala)** | **4.06**               | **5.39**     | **3.2**   |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)**         | **0.68**               | **1.15**     | **1.0**   |
| 🐍 **ImageToText (Python)**                                   | **0.31**               | **1.21**     | **0.89**  |

## Observations 



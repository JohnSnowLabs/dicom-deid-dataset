# Dicom Deidentification Evaluation & Dataset 

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
- results/deid_result ( Obfuscated final Images from Presidio and Visual NLP )

### Subset Dicom 

We wanted to make sure our measurements were as accurate as possible, so we hand-picked a group of DICOM images to work with. We focused on choosing only the best quality images, the ones that really mattered clinically. This way, we avoided any skewed DICOM data. Basically, we wanted to make sure our numbers reflected real-world medical imaging, not something artificial.

    [
     '6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-101.dcm',
     '6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-098.dcm',
     '6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-105.dcm',
     '3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-141.dcm',
     '339833062_07-05-2001-19638_3001578_000000-60758_1-2.dcm',
     '6415974217_06-09-1988-ABDOMENPELVIS-29078_237_000000-PJN-15958_1-19.dcm',
     '571403367_07-11-2019-DBT_Reconstructed_Volume-37558_DBT_slices-78838_51-01.dcm',
     '6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-095.dcm',
     '339833062_07-05-2001-19638_3001578_000000-60758_1-7.dcm',
     '8155012288_09-08-1999-FORFILE_CT_CHABPEL_-_CD_for_8155012288-44118_1_000000-SCOUT-12438_2-1.dcm',
     '9189822998_02-15-1989-CT_HIP_WO_CONTRASTBILAT-50838_5865_000000-Surview_Test-43798_1-3.dcm',
     '6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-107.dcm',
     '3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-126.dcm',
     '6415974217_06-09-1988-ABDOMENPELVIS-29078_237_000000-PJN-15958_1-15.dcm',
     '6415974217_06-09-1988-ABDOMENPELVIS-29078_237_000000-PJN-15958_1-17.dcm'
     ]

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
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)** | **0.845**     | **0.772** | **0.807**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large (Scala)** | **0.874**     | **0.789** | **0.829**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)** | **0.678** | **0.406** | **0.508**  |
| 🐍 **ImageToText (Python)**                               | **0.522**     | **0.272** | **0.358**  |
| 🔴 **Presidio**                                           | **0.09**    | **0.13** | **0.1**  |

### Time Metrics (GPU) - Average Time/File

- Google Colab Notebook utilized a single A100 GPU ( 40 GB ) - 7.62 Credits/hr
- Databricks Standalone Driver 64 GB Single GPU g4dn.4xLarge[T4] - 2.85 dbu/h
- Databricks Cluster Driver 64 GB Single GPU g4dn.4xLarge[T4], with minimum & maximum 2 Executors 16GB Single GPU g4dn.xLarge[T4] - 4.27 dbu/h
  
| **Model**                                                   | **Google Colab** | **Databricks Standalone** | **Databricks Cluster** |
|------------------------------------------------------------|----------------|------------------------|------------------------|
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)**  | **3.63**              | **4.66**     | **2.76**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large (Scala)** | **4.06**               | **5.39**     | **3.2**   |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)**         | **0.68**               | **1.15**     | **1.0**   |
| 🐍 **ImageToText (Python)**                                   | **0.31**               | **1.21**     | **0.89**  |
| 🔴 **Presidio**    | 0.54 | None | None |

### Time Metrics (CPU) - Average Time/File

- Google Colab Notebook HIGH RAM [ 8 Cores ] - 0.18 Credits/hr
- Databricks Standalone Driver 64 GB [ 16 Cores ] m4.4xlarge - 3 dbu/h
- Databricks Cluster Driver 64 GB [ 16 Cores ] m4.4xlarge, with minimum & maximum 8 Executors 32GB [ 8 Cores ] m4.2xlarge - 15 dbu/h
  
| **Model**                                                   | **Google Colab** | **Databricks Standalone** | **Databricks Cluster** |
|------------------------------------------------------------|----------------|------------------------|------------------------|
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)**  | **11.87**              | **6.11**     | **2.94**  |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large (Scala)** | **22.85**               | **19.48**     | **3.59**   |
| 🚀 **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)**         | **2.73**               | **1.64**     | **1.83**   |
| 🐍 **ImageToText (Python)**                                   | **1.12**               | **0.3**     | **0.85**  |
| 🔴 **Presidio**    | 0.54 | None | None |

### Sample Results

![Dicom Redaction Sample 1](https://github.com/JohnSnowLabs/dicom-deid-dataset/blob/v1_changes/results/output_sample_1.png)

![Dicom Redaction Sample 2](https://github.com/JohnSnowLabs/dicom-deid-dataset/blob/v1_changes/results/output_sample_2.png)

![Dicom Redaction Sample 3](https://github.com/JohnSnowLabs/dicom-deid-dataset/blob/v1_changes/results/output_sample_3.png)

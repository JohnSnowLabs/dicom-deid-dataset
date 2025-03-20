import json 
import glob
import os 
import zipfile
import shutil

def build_annotation_gt(source_path, main_ann_result_path, ocr_ann_result_path):
    
    json_files = ['6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-101.dcm',
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
                 '6415974217_06-09-1988-ABDOMENPELVIS-29078_237_000000-PJN-15958_1-17.dcm']

    collect_result_main = {}
    collect_result_lib = {}
    
    for file in json_files:

        in_file_name = os.path.join(source_path, file.replace(".dcm", ".json"))
        
        with open(in_file_name, "r") as file_in:
            content = json.loads(file_in.read())
    
        filename = content["filename"]
    
        collect_value = []
        collect_label = []
        
        for ann in content["annotation"]:
            temp = {"label" : ann["value"]["text"].replace("^", " ").strip().lower(),
                    "left" : ann["value"]["bbox"][0],
                    "top" : ann["value"]["bbox"][1],
                    "width" : ann["value"]["bbox"][2],
                    "height" : ann["value"]["bbox"][3]
                   }
            
            collect_value.append(temp)
            collect_label.append( ann["value"]["text"].replace("^", " ").strip().lower())
    
        collect_result_lib[filename] = collect_label
        collect_result_main[filename] = collect_value
    
        with open(main_ann_result_path, "w") as file_out_main:
            json.dump(collect_result_main, file_out_main, indent=4)
    
        with open(ocr_ann_result_path, "w") as file_out_lib:
            json.dump(collect_result_lib, file_out_lib, indent=4)

if __name__ == "__main__":

    source_path = "./dicom_files/"
    main_ann_result_path = "./gt_main.json"
    ocr_ann_result_path = "./gt_ocr.json"

    with zipfile.ZipFile("./dicom_files.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    macosx_dir = "./__MACOSX"
    if os.path.exists(macosx_dir):
        shutil.rmtree(macosx_dir)

    build_annotation_gt(source_path, main_ann_result_path, ocr_ann_result_path)

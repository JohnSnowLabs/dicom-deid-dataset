import json 
import glob
import os 
import zipfile
import shutil

def build_annotation_gt(source_path, main_ann_result_path, ocr_ann_result_path, json_files):

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

def delete_unwanted_files(source_path, json_files):

    expected_filenames = {os.path.splitext(file)[0] for file in json_files}

    for filename in os.listdir(source_path):
        file_base, file_ext = os.path.splitext(filename)  

        if file_base not in expected_filenames:
            for ext in [".json", ".dcm", ".jpg"]:
                file_path = os.path.join(source_path, file_base + ext)
                if os.path.exists(file_path):
                    os.remove(file_path)


if __name__ == "__main__":

    source_path = "./dicom_files/"
    main_ann_result_path = "./gt_main.json"
    ocr_ann_result_path = "./gt_ocr.json"

    with zipfile.ZipFile("./dicom_files.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    macosx_dir = "./__MACOSX"
    if os.path.exists(macosx_dir):
        shutil.rmtree(macosx_dir)

    json_files = [
        "292821506_07-13-2013-XR_CHEST_AP_PORTABLE_for_Douglas_Davidson-46198_1001_000000-37718_1-1.dcm",
        "339833062_07-05-2001-19638_3001578_000000-60758_1-2.dcm",
        "339833062_07-05-2001-19638_3001578_000000-60758_1-5.dcm",
        "6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-106.dcm",
        "6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-105.dcm",
        "6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-070.dcm",
        "6670427471_05-26-2000-FORFILE_CT_ABD_ANDOR_PEL_-_CD-25398_5_000000-NEPHRO__4_0__B40f__M0_4-18678_1-015.dcm",
        "6415974217_06-09-1988-ABDOMENPELVIS-29078_237_000000-PJN-15958_1-10.dcm",
        "6415974217_06-09-1988-ABDOMENPELVIS-29078_237_000000-PJN-15958_1-03.dcm",
        "3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-146.dcm",
        "3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-144.dcm",
        "3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-137.dcm",
        "3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-125.dcm",
        "3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-121.dcm",
        "3209648408_09-23-1999-CT_UROGRAM-31798_3_000000-PARENCHYMAL_PHASE_Sep1999-95798_1-110.dcm"
    ]

    build_annotation_gt(source_path, main_ann_result_path, ocr_ann_result_path, json_files)
    delete_unwanted_files(source_path, json_files)

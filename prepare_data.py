import json 
import glob
import os 
import zipfile
import shutil

def build_annotation_gt(source_path, main_ann_result_path, ocr_ann_result_path):
    
    json_files = glob.glob(os.path.join(source_path, "*.json"))
    
    collect_result_main = {}
    collect_result_lib = {}
    
    for file in json_files:
    
        with open(file, "r") as file_in:
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
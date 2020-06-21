import xml.etree.ElementTree as ET
import os
import csv


# DATA_DIR= "C:/DEV/PillData/fdm_dm_spl_release_human_rx_part1/prescription/xml_only/small_test_set"
# DATA_DIR= "C:/DEV/PillData/fdm_dm_spl_release_human_rx_part1/prescription/xml_only/with_imprint"
DATA_DIR= "C:/DEV/PillData/homeo_imprint"
FORMS_TO_PROCESS = {"C25158", "C42895", "C42896", "C42917", "C42902",
    "C42904", "C42916", "C42928", "C42936", "C42954", "C25394", "C42998",
    "C42893", "C124794", "C42897", "C60997", "C42905", "C42997", "C42910", 
    "C42927", "C42931", "C42930", "C61004", "C61005", "C42964", "C42963",
     "C42999", "C61006", "C42985", "C42992", "C147579"}

def get_imprint(el_tree):
    elem = el_tree.find(".//*[@code='SPLIMPRINT']..{*}value")
    return(elem.text)

def get_shape(el_tree):
    elem = el_tree.find(".//*[@code='SPLSHAPE']..{*}value")
    return(elem.attrib["displayName"])

def get_color(el_tree):
    try:
        elem = el_tree.find(".//*[@code='SPLCOLOR']..{*}value")
        return(elem.attrib["displayName"])
    except:
        return("")

def get_size(el_tree):
    try:
        elem = el_tree.find(".//*[@code='SPLSIZE']..{*}value")
        return(elem.attrib["value"])
    except:
        return("")

def get_unit(el_tree):
    try:
        elem = el_tree.find(".//*[@code='SPLSIZE']..{*}value")
        return(elem.attrib["unit"])
    except:
        return("")

def get_name(el_tree):
    try:
        elem = el_tree.find("./{*}manufacturedProduct/{*}manufacturedProduct/{*}name")
        return(elem.text)
    except:
        elem = el_tree.find("./{*}manufacturedProduct/{*}manufacturedMedicine/{*}name")
        return(elem.text)

def get_code(el_tree):
    try:
        elem = el_tree.find("./{*}manufacturedProduct/{*}manufacturedProduct/{*}code")
        return(elem.attrib["code"])
    except:
        elem = el_tree.find("./{*}manufacturedProduct/{*}manufacturedMedicine/{*}code")
        return(elem.attrib["code"])

def get_form_code(el_tree):
    try:
        elem = el_tree.find("./{*}manufacturedProduct/{*}manufacturedProduct/{*}formCode")
        return(elem.attrib["code"])
    except:
        elem = el_tree.find("./{*}manufacturedProduct/{*}manufacturedMedicine/{*}formCode")
        return(elem.attrib["code"])


def process_file(path):
    tree = ET.parse(path)
    root = tree.getroot()
    subjects = root.findall(".//{*}subject")
    pill_list = []  # one file could contain info regarding many pills, hence the list
    for elem in subjects:
        form_code = get_form_code(elem)
        # print(f"form_code={form_code}")
        if form_code not in FORMS_TO_PROCESS:
            continue # not our type of form factor - skipping

        try:
            imprint = get_imprint(elem)
        except:
            # if there's no imprint - don't process this subject
            continue

        pill_info = {}
        pill_info["code"] = get_code(elem).strip()
        pill_info["name"] = get_name(elem).strip()
        pill_info["imprint"] = imprint.strip()
        pill_info["shape"] = get_shape(elem).strip().upper()
        pill_info["color"] = get_color(elem).strip().upper()
        pill_info["size"] = get_size(elem).strip()
        # pill_info["unit"] = get_unit(elem).strip().upper()
        pill_info["xml_file"] = os.path.basename(path)
        pill_info["class"] = 3 # 1-prescription, 2=otc, 3=homeopatic, 4=custom(LV)
        pill_list.append(pill_info)
        # print(f"imprint={imprint}")
        # print(f"shape={get_shape(elem)}")
        # print(f"color={get_color(elem)}")
        # print(f"size={get_size(elem)}")
        # print(f"unit={get_unit(elem)}")
        # print(f"name={get_name(elem)}")
        # print(f"code={get_code(elem)}")
    return(pill_list)

# START ################
dir_data_xml_files = next(os.walk(DATA_DIR))

counter = 0
with open("pills_homeo_from_xml3.csv", "w", newline="\n", encoding="utf-8") as csv_output_file:
# with open("pills_from_xml.csv", "w", newline="") as csv_output_file:
    # fieldnames = ["code", "name", "imprint", "shape", "color", "size", "unit", "xml_file", "class"]
    fieldnames = ["code", "name", "imprint", "shape", "color", "size", "xml_file", "class"]
    csv_writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    
    for file_name in dir_data_xml_files[2]:
        # print(file_name)
        full_path = os.path.join(dir_data_xml_files[0], file_name)
        # print(full_path)
        try:
            pill_list = process_file(full_path)
            # print(pill_list)
            # for pill_info in pill_list:
            csv_writer.writerows(pill_list)
        except Exception as e:
            print(f"Error while processing {file_name}")
            print(e)

        counter += 1
        if counter%100 == 0:
            print(counter) # display progress after next 100 files processed
        
print(f"finished. processed {counter} files.")
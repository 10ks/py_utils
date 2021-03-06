import xml.etree.ElementTree as ET

# Only Capsules, Pills, Tablets (from https://www.fda.gov/industry/structured-product-labeling-resources/dosage-forms)
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


tree = ET.parse("pill_info8.xml")
root = tree.getroot()

# result = root.findall(".*[@name='Singapore']/year")
# result = root.fin dall(".//neighbor[2]")
# result = root.findall(".//*[@code='SPLIMPRINT']/../{*}value")
# result = root.findall(".//*[@code='SPLIMPRINT']..{*}value")
# result = root.find(".//*[@code='SPLIMPRINT']..{*}value")
# result = root.findall(".//*[@code='SPLCOLOR']..{*}value")
subjects = root.findall(".//{*}subject")

# print(f"text={result.text}")
print(subjects)
for elem in subjects:
    print("-----")
    # print(elem)
    # print(f"tag={elem.tag}")
    # print(f"text={elem.text}")
    # print(f"attribs={elem.attrib}")
    # print(f"shape={elem.attrib['displayName']}")


    # TODO check if form code is in tablets list
    # https://www.fda.gov/industry/structured-product-labeling-resources/dosage-forms
    try:
        imprint = get_imprint(elem)
    except:
        # if there's no imprint - don't process this subject
        continue
    print(f"imprint={imprint}")

    form_code = get_form_code(elem)
    print(f"form_code={form_code}")
    if form_code not in FORMS_TO_PROCESS:
        # print("not our form - skipping")
        continue
    
    
    print(f"shape={get_shape(elem)}")
    print(f"color={get_color(elem)}")
    print(f"size={get_size(elem)}")
    print(f"unit={get_unit(elem)}")
    print(f"name={get_name(elem)}")
    print(f"code={get_code(elem)}")
    


    
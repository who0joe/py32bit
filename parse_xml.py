"""
python parse_xml.py path/to/your/xmlfile.xml
"""
import xml.etree.ElementTree as ET
import sys

def xml_to_dict(element):
    # 자식 요소가 없는 경우, 텍스트 값을 반환 (속성 포함)
    if len(element) == 0:
        return element.text if not element.attrib else {'_text': element.text, '_attributes': element.attrib}

    # 자식 요소가 있는 경우, 자식 요소들을 딕셔너리로 변환
    result = {'_attributes': element.attrib} if element.attrib else {}
    for child in element:
        child_result = xml_to_dict(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_result)
            else:
                result[child.tag] = [result[child.tag], child_result]
        else:
            result[child.tag] = child_result

    return result

def parse_xml_file(file_path):
    # XML 파일 파싱
    tree = ET.parse(file_path)
    root = tree.getroot()

    # XML을 딕셔너리로 변환
    return xml_to_dict(root)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_xml.py <path_to_xml_file>")
        sys.exit(1)

    xml_file_path = sys.argv[1]
    try:
        result = parse_xml_file(xml_file_path)
        print(result)
    except Exception as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)

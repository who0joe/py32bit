import xml.etree.ElementTree as ET

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

# XML 문자열
xml_data = '''<root>
                <child>
                    <subchild>data1</subchild>
                    <subchild>data2</subchild>
                </child>
                <child2 attr="value">text</child2>
              </root>'''

# XML 문자열 파싱
root = ET.fromstring(xml_data)

# XML을 딕셔너리로 변환
xml_dict = xml_to_dict(root)
print(xml_dict)

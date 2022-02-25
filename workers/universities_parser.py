import xml.etree.ElementTree as ET


def analyze_university(university: ET) -> None:
    if university.tag != "Certificate":
        return
    for parameter in university:
        if parameter.tag == "RegionName" and parameter.text != "г. Москва":
            continue
        if parameter.tag == "TypeCode" and parameter.text != "Permanent":
            continue
        name = ""
        ogrn = ""
        name = ""


def main() -> None:
    tree = ET.parse('../data/universities.xml')
    root = tree.getroot()

    """
    <OpenData><Certificates><Certificate>
    Root is OpenData, but universities are stored in <Certificate> tag
    """

    for child in root:
        if child.tag == "Certificates":
            universities = child
            for university in universities:
                analyze_university(university)


if __name__ == "__main__":
    main()

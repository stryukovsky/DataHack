import os
import xml.etree.ElementTree as ET

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'


def analyze_university(university_model, university: ET) -> None:
    if university.tag != "Certificate":
        return
    name = ""
    ogrn = ""
    inn = ""
    kpp = ""
    address = ""
    for parameter in university:
        if parameter.tag == "RegionName" and parameter.text != "г. Москва":
            continue
        if parameter.tag == "TypeCode" and parameter.text != "Permanent":
            continue
        if parameter.tag == "EduOrgShortName":
            name = parameter.text
        if parameter.tag == "EduOrgINN":
            inn = parameter.text
        if parameter.tag == "EduOrgKPP":
            kpp = parameter.text
        if parameter.tag == "EduOrgOGRN":
            ogrn = parameter.text
        if parameter.tag == "PostAddress":
            address = parameter.text
    university_model.objects.create(short_name=name, ogrn=ogrn, inn=inn, kpp=kpp, post_address=address)


def main() -> None:
    django.setup()
    tree = ET.parse('../data/universities.xml')
    root = tree.getroot()
    from main.models import University
    """
    <OpenData><Certificates><Certificate>
    Root is OpenData, but universities are stored in <Certificate> tag
    """

    for child in root:
        if child.tag == "Certificates":
            universities = child
            for university in universities:
                analyze_university(University, university)


if __name__ == "__main__":
    main()

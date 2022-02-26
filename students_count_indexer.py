import os

import django
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'


def main():
    django.setup()
    from main.models import University
    driver = webdriver.Safari()
    url = "https://vuzoteka.ru/%D0%B2%D1%83%D0%B7%D1%8B/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0"
    for i in range(1, 10):
        if i == 1:
            page = ""
        else:
            page = "?page=" + str(i)

        driver.get(url + page)
        students = driver.find_elements(by=By.CLASS_NAME, value="institute-search-value")
        vuz = driver.find_elements(by=By.CLASS_NAME, value="institute-search-title")
        for j in range(0, len(vuz)):
            try:
                university = vuz[j].text
                students_count = students[j * 4].text
                attempt = list(university.split(" – "))[0]
                universities = University.objects.filter(name__icontains=university).all()
                print(attempt)
            except Exception as e:
                print(e)
                break
        print(f"page {i} is done")

    driver.close()


if __name__ == "__main__":
    main()

import json
import os
import django
import requests
from dateutil.parser import parse

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

API_SPENDINGS_BY_INN = "https://api.spending.gov.ru/v1/contracts/search/"


def build_url(inn: str, status: str) -> str:
    return f"{API_SPENDINGS_BY_INN}?customerinn={inn}&sort=-signDate"


def get_sum_for_university_by_inn(university, inn: str):
    url = build_url(inn, "EC")
    print(f"Attempt to get: {url}")
    response = requests.get(url)
    if response.status_code == 404:
        university.status = university.StatusChoices.NO_DATA
        university.save()
        return
    if response.status_code == 200:
        result = json.loads(response.content.decode("utf-8"))
        total_sum = 0
        print(f"Searching for {university.name}")
        for purchase in result['contracts']['data']:
            price = purchase['price']
            print(f"Found a purchase {price} rubles")
            execution: dict = purchase['execution']
            if (start_date_str := execution.get('startDate')) is not None:
                if (end_date_str := execution.get('endDate')) is not None:
                    start_date = parse(start_date_str)
                    print(f"Started at {start_date}")
                    end_date = parse(end_date_str)
                    if start_date.year == 2022:
                        print("Added")
                        total_sum += price
                        university.sum = total_sum
                        university.status = university.StatusChoices.INDEXED
        university.save()


def main():
    django.setup()
    from main.models import University

    for university in University.objects.all():
        if university.inn is not None and university.status == university.StatusChoices.UNEXPLORED:
            get_sum_for_university_by_inn(university, university.inn)


if __name__ == "__main__":
    main()

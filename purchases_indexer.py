import json
import os
import django
import requests
from dateutil.parser import parse
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

API_SPENDINGS_BY_INN = "https://api.spending.gov.ru/v1/contracts/search/"


def build_url(inn: str, status: str) -> str:
    return f"{API_SPENDINGS_BY_INN}?customerinn={inn}&sort=-signDate"


def search_purchases_by_inn(university, Purchase):
    url = build_url(university.inn, "EC")
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
            if start_date_str := purchase['signDate']:
                start_date = parse(start_date_str)
                print(f"Started at {start_date}")
                purchase_type = purchase['purchaseInfo']['name']
                purchase_type = "".join(list(purchase_type.split("\\")))
                if start_date.year == 2021:
                    Purchase.objects.create(
                        purchase_type=purchase_type,
                        university=university,
                        amount=price,
                        date=start_date
                    )
                    print("Added")
                    total_sum += price
                    university.sum = total_sum
                    university.status = university.StatusChoices.INDEXED
        university.save()


def main():
    django.setup()
    from main.models import University, Purchase

    unexplored_universities = University.objects.filter(status=University.StatusChoices.UNEXPLORED)
    print(unexplored_universities.count())
    for university in unexplored_universities:
        search_purchases_by_inn(university, Purchase)


if __name__ == "__main__":
    main()

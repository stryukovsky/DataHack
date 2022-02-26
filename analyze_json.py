import json
import os
import django
import requests
from dateutil.parser import parse

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'


def fill_purchases(University, Purchase, inn, filename):
    university = University.objects.filter(inn=inn).first()
    data = json.load(open(filename, "r"))
    print(f"Populating {university.name}")
    for purchase in data:
        amount = purchase['Начальная (максимальная) цена контракта']
        identifier = purchase['Реестровый номер закупки']
        if not Purchase.objects.filter(identifier=identifier):
            Purchase.objects.create(
                purchase_type=purchase['Наименование закупки'],
                university=university,
                amount=amount,
                identifier=identifier,
                date=parse(purchase['Дата размещения'])
            )
            university.sum += amount
            university.save()


def main():
    django.setup()
    from main.models import University, Purchase
    fill_purchases(University, Purchase, 7729134728, 'data/MGIMO.json')


if __name__ == "__main__":
    main()

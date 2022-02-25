import json
import os

import django
import requests

from app.settings import API_KEY

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

API = f"https://geocode-maps.yandex.ru/1.x/?format=json&apikey={API_KEY}&lang=ru-RU&geocode="


def build_url(address: str) -> str:
    return f"{API}{address}"


def decode_coordinates(university):
    if (address := university.post_address) is not None:
        url = build_url(address)
    else:
        return
    print(f"Attempt to get: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        response_object = json.loads(response.content.decode("utf-8"))
        coordinates_str = response_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
            'pos']
        longitude, latitude = coordinates_str.split(" ")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        university.longitude = longitude
        university.latitude = latitude
        university.save()
    print()


def main():
    django.setup()
    from main.models import University

    for university in University.objects.all():
        decode_coordinates(university)


if __name__ == "__main__":
    main()

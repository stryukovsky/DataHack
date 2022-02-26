import json
import os
import django
import requests
from dateutil.parser import parse

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'


def main():
    django.setup()
    from main.models import University

    University.objects.all().update(status=University.StatusChoices.UNEXPLORED, sum=0)


if __name__ == "__main__":
    main()

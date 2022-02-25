from django.db import models


class University(models.Model):
    short_name = models.CharField(max_length=255)
    ogrn = models.CharField(max_length=13)
    inn = models.CharField(max_length=12)
    kpp = models.CharField(max_length=9)
    post_address = models.CharField(max_length=255)


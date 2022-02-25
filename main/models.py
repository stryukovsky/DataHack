from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255, null=False)
    short_name = models.CharField(max_length=255, null=True)
    ogrn = models.CharField(max_length=13, null=True)
    inn = models.CharField(max_length=12, null=True)
    kpp = models.CharField(max_length=9, null=True)
    post_address = models.CharField(max_length=255, null=True)


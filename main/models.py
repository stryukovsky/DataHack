from django.db import models


class University(models.Model):
    class StatusChoices(models.IntegerChoices):
        UNEXPLORED = 0
        NO_DATA = 1
        INDEXED = 2

    name = models.CharField(max_length=255, null=False)
    short_name = models.CharField(max_length=255, null=True)
    ogrn = models.CharField(max_length=13, null=True)
    inn = models.CharField(max_length=12, null=True)
    kpp = models.CharField(max_length=9, null=True)
    post_address = models.CharField(max_length=255, null=True)
    sum = models.IntegerField(default=0)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.UNEXPLORED)
    longitude = models.CharField(max_length=255, default="")
    latitude = models.CharField(max_length=255, default="")


class Purchase(models.Model):
    purchase_type = models.CharField(max_length=1024, null=False, unique=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='purchases')
    amount = models.CharField(max_length=1024, null=False)
    date = models.DateField()

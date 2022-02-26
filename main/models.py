from django.db import models


class University(models.Model):
    class StatusChoices(models.IntegerChoices):
        UNEXPLORED = 0
        NO_DATA = 1
        INDEXED = 2

    name = models.CharField(max_length=255, null=False, unique=True)
    short_name = models.CharField(max_length=255, null=True)
    abbreviation = models.CharField(max_length=255, default="", null=False)
    ogrn = models.CharField(max_length=13, null=True)
    inn = models.CharField(max_length=12, null=True)
    kpp = models.CharField(max_length=9, null=True)
    post_address = models.CharField(max_length=255, null=True)
    sum = models.IntegerField(default=0)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.UNEXPLORED)
    longitude = models.CharField(max_length=255, default="")
    latitude = models.CharField(max_length=255, default="")
    students_count = models.PositiveBigIntegerField(default=0)
    rating_position = models.IntegerField(default=0)

    def __str__(self):
        return str(self.inn)


class Purchase(models.Model):
    identifier = models.CharField(max_length=1024, null=False, default="")
    purchase_type = models.CharField(max_length=1024, null=False, unique=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='purchases')
    amount = models.CharField(max_length=1024, null=False)
    date = models.DateField()

import math

from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import University
from main.serializers import UniversitySerializer, PieChartUnivesitySerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Index.html")


def pie_chart(request: HttpRequest) -> HttpResponse:
    return render(request, "PieChart.html", context={
        "total": University.objects.filter(rating_position__gt=0).aggregate(Sum('sum'))['sum__sum']
    })


def studs_bar(request: HttpRequest) -> HttpResponse:
    return render(request, "StudentsBar.html", context={
        "total": University.objects.filter(rating_position__gt=0).aggregate(Sum('sum'))['sum__sum']
    })


def universities_list(request: HttpRequest) -> HttpResponse:
    page = int(request.GET.get('page', 1))
    if page <= 0:
        page = 1

    objs = University.objects.filter()

    if (page - 1) * 7 > len(objs):
        page = math.ceil(len(objs) / 7)

    start = (page - 1) * 7
    end = page * 7 if page * 7 < len(objs) else len(objs)
    universities = objs.order_by("rating_position")[start:end]
    return render(request, "UniversitiesList.html", {"universities": universities, "current_page": page})


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True).filter(rating_position__lt=99).order_by(
        'rating_position')
    serializer_class = UniversitySerializer


class PieChartUniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True).order_by('-sum')
    serializer_class = PieChartUnivesitySerializer

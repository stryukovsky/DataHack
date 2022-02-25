from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import University
from main.serializers import UniversitySerializer, PieChartUnivesitySerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Index.html")


def pie_chart(request: HttpRequest) -> HttpResponse:
    return render(request, "PieChart.html")


def universities_list(request: HttpRequest) -> HttpResponse:
    page = int(request.GET.get('page', 1))
    if page <= 0:
        page = 1
    objs = University.objects.filter()
    start = (page-1)*7
    end = page*7 if page*7 < len(objs) else len(objs)
    universities = objs.order_by("name")[start:end]
    return render(request, "UniversitiesList.html", {"universities": universities})


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True).exclude(sum__lte=1).order_by('-sum')
    serializer_class = UniversitySerializer


class PieChartUniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True).exclude(sum__lte=1).order_by('-sum')
    serializer_class = PieChartUnivesitySerializer

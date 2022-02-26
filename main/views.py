from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import University
from main.serializers import UniversitySerializer, PieChartUnivesitySerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Index.html")


def pie_chart(request: HttpRequest) -> HttpResponse:
    return render(request, "PieChart.html")


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True).order_by('-sum')
    serializer_class = UniversitySerializer


class PieChartUniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True).order_by('-sum')
    serializer_class = PieChartUnivesitySerializer

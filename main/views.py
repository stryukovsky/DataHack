from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import University
from main.serializers import UniversitySerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Index.html")


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.exclude(longitude__isnull=True)
    serializer_class = UniversitySerializer

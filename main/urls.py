from django.urls import path
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register("universities", views.UniversityViewSet)

urlpatterns = [
    path("", views.index),
]

urlpatterns += router.urls

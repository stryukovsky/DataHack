from django.urls import path
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register("universities", views.UniversityViewSet)
router.register("pie_chart_universities", views.PieChartUniversityViewSet)

urlpatterns = [
    path("", views.index),
    path("pie_chart", views.pie_chart),
    path("u_list", views.universities_list)
]

urlpatterns += router.urls

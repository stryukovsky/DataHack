from rest_framework.serializers import ModelSerializer
from main.models import University


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'latitude', 'longitude', 'name', 'sum', 'inn', 'post_address']


class PieChartUnivesitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['short_name', 'sum']

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from main.models import University


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'latitude', 'longitude', 'name', 'short_name', 'sum', 'inn', 'post_address', 'students_count', 'abbreviation']


class PieChartUnivesitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['short_name', 'sum']

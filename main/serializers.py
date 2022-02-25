from rest_framework.serializers import ModelSerializer
from main.models import University


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['latitude', 'longitude', 'name']

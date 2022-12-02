from rest_framework.serializers import ModelSerializer

from mainapp.models import DataCoordinates, DataTransport


class DataCoordinatesSerializer(ModelSerializer):
    class Meta:
        model = DataCoordinates
        fields = ('__all__')
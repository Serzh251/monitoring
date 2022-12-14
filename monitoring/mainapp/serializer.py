from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from mainapp.models import DataCoordinates, DataTransport, Trip, Transport


class DataCoordinatesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DataCoordinates
        geo_field = "geom"
        fields = ('geom', 'velocity', 'transport')

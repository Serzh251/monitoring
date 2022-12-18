from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from mainapp.models import DataCoordinates, DataTransport, Trip, Transport


class DataCoordinatesSerializer(GeoFeatureModelSerializer):
    """Get geodata with transport name"""
    class Meta:
        model = DataCoordinates
        geo_field = "geom"
        fields = ('geom', 'velocity', 'transport', 'add_datetime')

    def get_properties(self, instance, fields):
        return {
            'transport_id': instance.transport.id,
            'transport': instance.transport.name,
            'velocity': instance.velocity,
            'add_datetime': instance.add_datetime,
        }


class TransportListSerializer(ModelSerializer):
    """get data transport list"""
    class Meta:
        model = Transport
        fields = ('id', 'name', 'description', 'type')

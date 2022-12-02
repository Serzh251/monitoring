from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from mainapp.models import Transport, Trip, DataCoordinates, DataTransport

admin.site.register(Transport)
admin.site.register(Trip, LeafletGeoAdmin)
admin.site.register(DataCoordinates, LeafletGeoAdmin)
admin.site.register(DataTransport)

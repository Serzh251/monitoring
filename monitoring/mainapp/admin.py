from django.contrib import admin

from mainapp.models import Transport, Trip, DataCoordinates, DataTransport

admin.site.register(Transport)
admin.site.register(Trip)
# admin.site.register(DataCoordinates)
admin.site.register(DataTransport)
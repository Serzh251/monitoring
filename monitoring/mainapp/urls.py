from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from mainapp.views import MainView, GetdataView, MapLayer, data_raw
from mainapp.models import DataCoordinates

app_name = 'mainapp'
router = DefaultRouter()
router.register('data_geo', GetdataView)



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('api/', include(router.urls)),
    path('data_raw/', data_raw, name='data_raw'),
    re_path(r'^data.geojson$',
            MapLayer.as_view(model=DataCoordinates,properties=('transport_name',
                                                               'transport_velocity', 'add_datetime')),name='data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
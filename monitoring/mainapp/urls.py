from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from mainapp.views import MainView, GetLastLocationView, MapLayer, data_raw, GetTransportListView
from mainapp.models import DataCoordinates

app_name = 'mainapp'
router = DefaultRouter()
router.register('last_location', GetLastLocationView)
router.register('transport_list', GetTransportListView)

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('api/', include(router.urls)),
    path('data_raw/', data_raw, name='data_raw'),
    re_path(r'^data.geojson$',
            MapLayer.as_view(model=DataCoordinates,properties=('transport_name',
                                                               'transport_velocity', 'add_datetime')),name='data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
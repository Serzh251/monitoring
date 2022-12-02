from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.base import View
from djgeojson.views import GeoJSONLayerView
from rest_framework.viewsets import ModelViewSet

from mainapp.models import DataCoordinates, DataTransport
from mainapp.serializer import DataCoordinatesSerializer
from mainapp.services.parse_save_data import parse_wialon_data_to_dict, save_data_to_model


class MainView(TemplateView):
    template_name = 'mainappp/index.html'
    extra_context = {'title': 'Main'}


class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization


class GetdataView(ModelViewSet):
    serializer_class = DataCoordinatesSerializer
    queryset = DataCoordinates.objects.all()


@csrf_exempt
def data_raw(request):
    parse_data = parse_wialon_data_to_dict(request.body.decode('UTF-8'))
    if parse_data['valid_data']:
        save_data_to_model(parse_data)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

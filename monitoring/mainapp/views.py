from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from rest_framework.viewsets import ModelViewSet

from mainapp.models import DataCoordinates, DataTransport
from mainapp.serializer import DataCoordinatesSerializer
from mainapp.services.parse_save_data import parse_wialon_data_to_dict, save_data_to_model, check_auth


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
    parse_data = check_auth(request.headers)
    if not parse_data.get('auth'):
        return HttpResponse(content=parse_data['status_code'], status=403)

    parse_data.update(parse_wialon_data_to_dict(request.body.decode('UTF-8')))
    if parse_data['valid_data']:
        save_data_to_model(parse_data)
        return HttpResponse(content=parse_data['status_code'], status=200)
    else:
        return HttpResponse(content=parse_data['status_code'], status=400)

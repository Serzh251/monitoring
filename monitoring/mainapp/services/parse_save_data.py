

from mainapp.models import DataCoordinates, DataTransport
from mainapp.services.wialon import parse_short_msg, parse_long_msg


def parse_wialon_data_to_dict(data: str) -> dict:
    """parse wialon data to dict accordingly type"""

    if 'SD' in data:
        return parse_short_msg(data)
    elif 'D' in data:
        return parse_long_msg(data)
    return {'valid_data': False}


def save_data_to_model(data: dict):
    params_item = None
    if data.get('params'):
        params_item = DataTransport.objects.create(**data['params'])
    coordinates = data.get('coordinates')
    velocity = data.get('velocity')
    course = data.get('course')

    DataCoordinates.objects.create(
        geom=coordinates,
        velocity=velocity,
        course=course,
        data_for_points=params_item
    )

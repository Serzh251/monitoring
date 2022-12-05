from mainapp.models import DataCoordinates, DataTransport, Transport
from mainapp.services.wialon import parse_short_msg, parse_long_msg


def parse_wialon_data_to_dict(data: str) -> dict:
    """parse wialon data to dict accordingly type"""

    if 'SD' in data:
        return parse_short_msg(data)
    elif 'D' in data:
        return parse_long_msg(data)
    return {'valid_data': False}


def check_auth(headers: dict):
    """
    check the transport in the database and authorize if any
    """
    imei = headers.get('imei')
    password = headers.get('password')
    transport = Transport.objects.filter(identifier=imei).first()
    if transport and transport.password == password:
        return {'status_code': '#AL#1\r\n', 'auth': True, 'transport': transport}
    else:
        return {'status_code': '#AL#01\r\n',  'auth': False}


def save_data_to_model(data: dict):
    params_item = None
    transport = data['transport']
    if data.get('params'):
        params_item = DataTransport.objects.create(**data['params'])
    coordinates = data.get('coordinates')
    velocity = data.get('velocity')
    course = data.get('course')

    DataCoordinates.objects.create(
        geom=coordinates,
        velocity=velocity,
        course=course,
        data_for_points=params_item,
        transport=transport
    )

import crc16
from django.contrib.gis.geos import Point
from mainapp.models import DataCoordinates


def parse_wialon_data_to_dict(data: str) -> dict:
    """
    parse wialon data to dict
    example data - '#SD#NA;NA;48.07038;N;11.31;E;41.4848;084.4;NA;NA;CRC16'
    """
    data_dict = {}

    if 'SD' in data:
        payload = data.replace('#SD#', '').replace('\r\n', '').split(';')
        get_crc = payload.pop()
        payload_str = ','.join(payload).replace(',', ';') + ';'
        calc_crc = hex(crc16.crc16xmodem(payload_str.encode(encoding='utf-8')))
        if get_crc == calc_crc:
            data_dict['valid_data'] = True
        else:
            data_dict['valid_data'] = False
            return data_dict
        try:
            y = float(payload[2])
            x = float(payload[4])
            data_dict['valid_data'] = True
        except ValueError:
            data_dict['valid_data'] = False
            return data_dict
        if payload[3] == 'S': y = -y
        if payload[5] == 'W': x = -x
        data_dict['coordinates'] = Point(x, y)
        if payload[6] != 'NA':
            try:
                data_dict['velocity'] = round(float(payload[6]), 2)
            except ValueError:
                pass
        if payload[7] != 'NA':
            try:
                data_dict['course'] = round(float(payload[7]), 2)
            except ValueError:
                pass
        # print(data_dict)
        return data_dict

    data_dict['valid_data'] = False
    return data_dict


def save_data_to_model(data: dict):
    coordinates = data.get('coordinates')
    velocity = data.get('velocity')
    course = data.get('course')
    DataCoordinates.objects.create(
        geom=coordinates,
        velocity=velocity,
        course=course
    )


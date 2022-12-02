from django.contrib.gis.geos import Point
from mainapp.models import DataCoordinates


def parse_wialon_data_to_dict(data: str) -> dict:
    """
    parse wialon data to dict
    example data - '#SD#NA;NA;48.07038;N;11.31;E;41.4848;084.4;NA;NA;CRC16'
    """
    data_dict = {}
    data_lst = data.split(';')
    if 'SD' in data_lst[0]:
        try:
            y = float(data_lst[2])
            x = float(data_lst[4])
            data_dict['valid_data'] = True
        except ValueError:
            data_dict['valid_data'] = False
            return data_dict
        if data_lst[3] == 'S': y = -y
        if data_lst[5] == 'W': x = -x
        data_dict['coordinates'] = Point(x, y)
        if data_lst[6] != 'NA':
            try:
                data_dict['velocity'] = round(float(data_lst[6]), 2)
            except ValueError:
                pass
        if data_lst[7] != 'NA':
            try:
                data_dict['course'] = round(float(data_lst[7]), 2)
            except ValueError:
                pass
            print(data_dict)
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


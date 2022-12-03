import crc16
from django.contrib.gis.geos import Point


def parse_payload_gps(payload: list) -> dict:
    """
    function parse gps in list data into, transform in numbers and safe in data dict
    :param payload:
    :return data dict:
    """
    data_dict = {}
    try:
        y = float(payload[2])
        x = float(payload[4])
        if payload[3] == 'S': y = -y
        if payload[5] == 'W': x = -x
        data_dict['coordinates'] = Point(x, y)
        data_dict['valid_data'] = True

        if payload[6] != 'NA': data_dict['velocity'] = round(float(payload[6]), 2)
        if payload[7] != 'NA': data_dict['course'] = round(float(payload[7]), 2)
    except ValueError:
        data_dict['valid_data'] = False
        return data_dict
    return data_dict


def parse_short_msg(data: str) -> dict:
    """"
        get string in format wialon short message, return dict with payload data, or dict with errors
        example message:
            - #SD#NA;NA;48.07038;N;11.31;E;41.4848;084.4;NA;NA;CRC16
    """
    payload = data.replace('#SD#', '').replace('\r\n', '').split(';')
    data_dict = parse_payload_gps(payload)
    get_crc = payload.pop()
    payload_str = ','.join(payload).replace(',', ';') + ';'
    calc_crc = hex(crc16.crc16xmodem(payload_str.encode(encoding='utf-8')))
    if get_crc == calc_crc:
        data_dict['status_code'] = '#ASD#1\r\n'  # The package has been successfully registered.
    else:
        data_dict['status_code'] = '#ASD#13\r\n'  # error checksum
        return data_dict
    return data_dict


def parse_params(params: str) -> dict:
    """
    :param: params string in wialon format
    :return: dict with parse params in payload data
    """
    params_lst = params.split(',')
    data_dict = {}
    for el_lst in params_lst:
        el = el_lst.split(':')
        if el[1] == '1':
            data_dict[f'{el[0]}'] = int(el[2])
        elif el[1] == '2':
            data_dict[f'{el[0]}'] = float(el[2])
        else:
            data_dict[f'{el[0]}'] = str(el[2])
    return data_dict


def parse_long_msg(data: str) -> dict:
    """"
        get string in format wialon long message, return dict with payload data, or dict with errors
        example message:
            - #D#NA;NA;LatDeg;LatSign;LonDeg;LonSign;Speed;Course;NA;NA;NA;Inputs;Outputs;ADC;Ibutton;Params;CRC16\r\n
    """
    data_dict = {}
    payload = data.replace('#D#', '').replace('\r\n', '').split(';')
    get_crc = payload.pop()  # get crc element
    payload_str = ';'.join(payload) + ';'
    calc_crc = hex(crc16.crc16xmodem(payload_str.encode(encoding='utf-8')))

    if get_crc == calc_crc:
        params = ''
        for el in payload:
            if '-' in el:
                params = el
        data_dict = parse_payload_gps(payload)
        data_dict['params'] = parse_params(params)
        data_dict['valid_data'] = True
        data_dict['status_code'] = '#ASD#1\r\n'  # The package has been successfully registered.
    else:
        data_dict['valid_data'] = False
        data_dict['status_code'] = '#ASD#13\r\n'  # error checksum
        return data_dict
    return data_dict

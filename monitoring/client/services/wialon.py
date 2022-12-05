import crc16
from monitoring.client.services.params import get_params
from monitoring.client.services.parse_nmea import parse_mnea_string

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)  # set for python warning


def payload_gps(data: dict) -> str:
    """create string payload data with gps data"""
    return f'NA;NA;{data.get("LatDeg", "NA")};{data.get("LatSign", "NA")};' \
           f'{data.get("LonDeg", "NA")};{data.get("LonSign", "NA")};{data.get("Speed", "NA")};' \
           f'{data.get("Course", "NA")};NA;NA;'


def create_wialon_short_package(input_data: str) -> str:
    """Create short package with wialon protocol accordingly with description
       #SD#NA;NA;LatDeg;LatSign;LonDeg;LonSign;Speed;Course;NA;NA;CRC16\r\n
       #SD# - type package
       ; - delimiter
       NA - if no data
    """
    data_dict = parse_mnea_string(input_data)
    payload = payload_gps(data_dict)

    crc = hex(crc16.crc16xmodem(payload.encode(encoding='utf-8')))
    return f'#SD#{payload}{crc}\r\n'


def create_wialon_long_package(input_data: str) -> str:
    """Create long package with with params wialon protocol accordingly with description
       #D#NA;NA;LatDeg;LatSign;LonDeg;LonSign;Speed;Course;NA;NA;NA;Inputs;Outputs;ADC;Ibutton;Params;CRC16\r\n
       #D# - type package
       ; - delimiter
       NA - if no data
    """
    inputs, outputs, ads = ('NA',) * 3
    params = get_params()
    data_dict = parse_mnea_string(input_data)
    payload_coordinates = payload_gps(data_dict)
    payload = f'{payload_coordinates};NA;{inputs};{outputs};{ads};NA;{params};'

    crc = hex(crc16.crc16xmodem(payload.encode(encoding='utf-8')))
    return f'#D#{payload}{crc}\r\n'


# def login_to_server(host: str, imei: str, password: str) -> str:
#     """function for login on wilaon server, return token
#        example request:
#         - #L#Protocol_version;IMEI;Password;CRC16\r\n
#     """
#     import requests
#     payload = f''
#     r = requests.post(host, data=payload)
#     answer = r.content.decode()
#     if answer == '#ASD#1\r\n':  # success package transaction
#         pass
#     elif answer == '#ASD#13\r\n' or answer == 'AD#16\r\n':  # error checksum
#         pass
#     elif answer == '#AD#15\r\n':  # bad additional params
#         pass
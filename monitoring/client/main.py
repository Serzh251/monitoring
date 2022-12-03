import time

import crc16
import warnings
import random
warnings.filterwarnings("ignore", category=DeprecationWarning) # set for python warning


# data = 'GPGGA,123519,4807.038,S,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
# data = '$GPGLL,4916.45,N,12311.12,W,225444,A,*31'



def create_wialon_short_package(input_data: str) -> str:
    """Create short package with wialon protocol accordingly with desriprion
       #SD#NA;NA;LatDeg;LatSign;LonDeg;LonSign;Speed;Course;NA;NA;CRC16\r\n
       #SD# - type package
       ; - delimiter
       NA - if no data
    """
    data_str = input_data.split(',')
    data_dict = {}
    if 'GGA' in data_str[0]:
        data_dict['LatDeg'] = round(float(data_str[2]) / 100, 7)
        data_dict['LatSign'] = data_str[3]
        data_dict['LonDeg'] = round(float(data_str[4]) / 100, 7)
        data_dict['LonSign'] = data_str[5]

    elif 'GLL' in data_str[0]:
        data_dict['LatDeg'] = round(float(data_str[1]) / 100, 7)
        data_dict['LatSign'] = data_str[2]
        data_dict['LonDeg'] = round(float(data_str[3]) / 100, 7)
        data_dict['LonSign'] = data_str[4]

    elif 'RMC' in data_str[0]:
        data_dict['LatDeg'] = round(float(data_str[3]) / 100, 7)
        data_dict['LatSign'] = data_str[4]
        data_dict['LonDeg'] = round(float(data_str[5]) / 100, 7)
        data_dict['LonSign'] = data_str[6]
        data_dict['Speed'] = float(data_str[7]) * 1.852
        data_dict['Course'] = data_str[8]

    payload = f'NA;NA;{data_dict.get("LatDeg", "NA")};{data_dict.get("LatSign", "NA")};' \
              f'{data_dict.get("LonDeg", "NA")};{data_dict.get("LonSign", "NA")};{data_dict.get("Speed", "NA")};' \
              f'{data_dict.get("Course", "NA")};NA;NA;'

    crc = hex(crc16.crc16xmodem(payload.encode(encoding='utf-8')))
    return f'#SD#{payload}{crc}\r\n'


def send_package_to_server(host: str, payload: dict):
    """send input data to server"""
    import requests
    r = requests.post(host, data=payload)
    answer = r.content.decode()
    if answer == '#ASD#1\r\n':
        return True
    elif answer == '#ASD#13\r\n':
        return False


lat = 4807.038
lon = 1131.000

while True:
    lat += 0.001
    lon += 0.001
    velocity = random.randint(0, 100)

    data = f'$GPRMC,123519,A,{lat},N,{lon},E,{velocity},084.4,230394,003.1,W*6A'
    wialon_package_for_send = create_wialon_short_package(data)
    send_package_to_server(host='http://127.0.0.1:8066/data_raw/', payload=wialon_package_for_send)
    time.sleep(0.5)

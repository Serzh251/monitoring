import time
import random
from monitoring.client.services.wialon import create_wialon_short_package, create_wialon_long_package


# data = 'GPGGA,123519,4807.038,S,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
# data = '$GPGLL,4916.45,N,12311.12,W,225444,A,*31'
# data = '$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A'


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
    # wialon_package_for_send = create_wialon_short_package(data)
    wialon_package_for_send = create_wialon_long_package(data)
    send_package_to_server(host='http://127.0.0.1:8066/data_raw/', payload=wialon_package_for_send)
    time.sleep(2)

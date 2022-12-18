import time
import random
from monitoring.client.services.wialon import create_wialon_short_package, create_wialon_long_package
host='http://127.0.0.1:8066/data_raw/'
# host_token='http://127.0.0.1:8066/api-token-auth/'
# imei = '990012003416986'
# imei = '356926099216182'
imei = '356926993445645'
# imei = '354809100949797'
password = 'qwerty'
# data = 'GPGGA,123519,4807.038,S,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
# data = '$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A'
lat = 6407.038
lon = 4031.000
lat += 0.001
lon += 0.001
velocity = random.randint(0, 100)
data = f'$GPRMC,123519,A,{lat},N,{lon},E,{velocity},084.4,230394,003.1,W*6A'

# token = login_to_server(host=host_token, imei=imei, password=password)


def send_package_to_server(host: str, payload: dict, imei: str, password: str):
    """send data to server"""
    import requests
    headers = {'imei': imei, 'password': password}
    r = requests.post(host, data=payload, headers=headers)
    answer = r.content.decode()
    if answer == '#ASD#1\r\n':  # success package transaction
        pass
    elif answer == '#ASD#13\r\n' or answer == 'AD#16\r\n':  # error checksum
        pass
    elif answer == '#AD#15\r\n':  # bad additional params
        pass
    elif answer == '#AL#01\r\n':  # forbidden, not authorize
        pass


while True:
    # wialon_package_for_send = create_wialon_short_package(data)
    wialon_package_for_send = create_wialon_long_package(data)
    send_package_to_server(host=host, payload=wialon_package_for_send, imei=imei, password=password)
    time.sleep(2)

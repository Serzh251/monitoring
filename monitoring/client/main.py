
# data = 'GPGGA,123519,4807.038,S,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
# data = '$GPGLL,4916.45,N,12311.12,W,225444,A,*31'
data = '$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A'


def create_wialon_short_package(input_data: str) -> str:
    """Create short package with wialon protocol accordingly with desriprion
       #SD#NA;NA;LatDeg;LatSign;LonDeg;LonSign;Speed;Course;NA;NA;CRC16\r\n
       #SD# - type package
       ; - delimeter
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

    return f'#SD#NA;NA;' \
           f'{data_dict.get("LatDeg", "NA")};' \
           f'{data_dict.get("LatSign", "NA")};' \
           f'{data_dict.get("LonDeg", "NA")};' \
           f'{data_dict.get("LonSign", "NA")};' \
           f'{data_dict.get("Speed", "NA")};' \
           f'{data_dict.get("Course", "NA")};' \
           f'NA;NA;CRC16\r\n'


def send_package_to_server(host: str, payload: dict):
    """send input data to server"""
    import requests
    r = requests.post(host, data=payload)
    print(r.status_code)


wialon_package_for_send = create_wialon_short_package(data)
send_package_to_server(host='http://127.0.0.1:8066/data_raw/', payload=wialon_package_for_send)


def parse_mnea_string(data: str) -> dict:
    data_lst = data.split(',')
    data_dict = {}
    
    if 'GGA' in data_lst[0]:
        data_dict['LatDeg'] = round(float(data_lst[2]) / 100, 7)
        data_dict['LatSign'] = data_lst[3]
        data_dict['LonDeg'] = round(float(data_lst[4]) / 100, 7)
        data_dict['LonSign'] = data_lst[5]

    elif 'GLL' in data_lst[0]:
        data_dict['LatDeg'] = round(float(data_lst[1]) / 100, 7)
        data_dict['LatSign'] = data_lst[2]
        data_dict['LonDeg'] = round(float(data_lst[3]) / 100, 7)
        data_dict['LonSign'] = data_lst[4]

    elif 'RMC' in data_lst[0]:
        data_dict['LatDeg'] = round(float(data_lst[3]) / 100, 7)
        data_dict['LatSign'] = data_lst[4]
        data_dict['LonDeg'] = round(float(data_lst[5]) / 100, 7)
        data_dict['LonSign'] = data_lst[6]
        data_dict['Speed'] = float(data_lst[7]) * 1.852
        data_dict['Course'] = data_lst[8]
    return data_dict

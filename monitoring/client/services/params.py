dut1 = 20
dut2 = 30
dut3 = 40
dut4 = 90
engine_left = 'FuelFlow-2-1000|OilPG-2-5.6|OilTG-1-70|OilPD-2-3.4|OilTG-1-80|WaterT-1-90|VDC-2-28.8|EngineH-2-1205|RPM-2-1230'
engine_right = 'FuelFlow-2-2000|OilPG-2-5.6|OilTG-1-70|OilPD-2-3.4|OilTG-1-80|WaterT-1-90|VDC-2-28.8|EngineH-2-1100|RPM-2-1100'
engine_aux1 = 'FuelFlow-2-3000|OilPG-2-5.6|OilTG-1-70|OilPD-2-3.4|OilTG-1-80|WaterT-1-80|VDC-2-14.4|EngineH-2-1500|RPM-2-1500'
engine_aux2 = 'FuelFlow-2-4000|OilPG-2-5.6|OilTG-1-70|OilPD-2-3.4|OilTG-1-80|WaterT-1-30|VDC-2-12.8|EngineH-2-520|RPM-2-0'
energy_params = 'VAC-2-380|IAC-1-13.4|PAC-2-8844'


def get_params() -> str:
    """
        get raw data and forming params accordingly wialon
           Params - Name:Type:Value
                Name:  param name
                Type:  1 — Integer / Long, 2 — Double, 3 — String
                Value: Parameter value. Depends on the parameter type.
                example - fuel:2:45.8
        :return string in format params_item,params_item
    """
    return f'dut1:1:{dut1},dut2:1:{dut2},dut3:1:{dut3},dut4:1:{dut4},' \
           f'engine_left:3:{engine_left},engine_right:3:{engine_right},' \
           f'engine_aux1:3:{engine_aux1},engine_aux2:3:{engine_aux2},' \
           f'energy_params:3:{energy_params}'

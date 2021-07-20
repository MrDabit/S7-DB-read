# --------------------------------------------------------------------------------------
# | Py module: readDB.py                                                               |
# | Author: David García Rincón                                                        |
# | Date: 20210719                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | This module is conecting to the PLC with the IP address defined in #1              |
# | Read the CPU name and CPU status in #2                                             |
# | Then will point the DB defined in #3 and returns values of system and DB           |
# | Mandatory to install snap7 module                                                  |
# --------------------------------------------------------------------------------------

import snap7



def readDB():  # function readDB

    # 1. PLC connection definition
    IP = '192.168.1.10'
    RACK = 0
    SLOT = 2

    DB_NUMBER = 3
    START_ADDRESS = 0
    SIZE = 259

    # 1.1 PLC connection via snap7 client module
    plc = snap7.client.Client()
    plc.connect(IP, RACK, SLOT)

    # 2. Read PLC data
    plc_info = plc.get_cpu_info()
    plc_Type = plc_info.ModuleTypeName.decode('UTF-8').strip('\x00')
    #print(f'Module Type: {plc_info.ModuleTypeName}')
    plc_state = plc.get_cpu_state()
    # print(f'State:{plc_state}')

    # 3. Point DB and read data
    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    product_name = db[2:256].decode('UTF-8').strip('\x00')
    ## print(f'PRODUCT NAME: {product_name}')
    product_value = int.from_bytes(db[256:258], byteorder='big')
    ## print(f'PRODUCT VALUE: {product_value}')
    product_status = bool(db[258])
    # print(product_status)

    return (plc_Type, plc_state, product_name, product_value, product_status)


if __name__ == '__main__':
    datos = readDB()
    print(datos)

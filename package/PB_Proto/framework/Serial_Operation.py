import serial
import serial.tools.list_ports

Transepic_VID = 3368
Stm32_COM_VID = 1155
CH340_VID = 6790
Link_COMM = serial.Serial()  # 定义串口对象
Stm32_COM = serial.Serial()
CH340_COM = serial.Serial()
COM_LIST = ['']
Stm32_com = 'Stm32_COM'
CH340_com = 'CH340_COM'
Link_com = 'Link_COMM'

def get_com_list():
    global port_list
    # a = serial.tools.list_ports.comports()
    # print(a)
    # port_list = list(serial.tools.list_ports.comports())
    port_list = serial.tools.list_ports.comports()
    return port_list


# 打开串口
def serial_open(com_sel):
    global Link_COMM
    global Stm32_COM
    global CH340_COM
    if com_sel in COM_LIST:
        print(com_sel + "is already open")
        return
    get_com_list()
    if com_sel == Link_com:
        for port in port_list:
            if port.vid == Transepic_VID:
                try:
                    serial_port = port.device
                    Link_COMM = serial.Serial(serial_port, 115200, timeout=0.01)
                    if Link_COMM.isOpen():
                        COM_LIST.append('Link_COMM')
                        print(serial_port, "Link_COMM open success")
                except:
                    print("Link_COMM open failed")
    elif com_sel == Stm32_com:
        for port in port_list:
            if port.vid == Stm32_COM_VID:
                try:
                    serial_port = port.device
                    Stm32_COM = serial.Serial(serial_port, 115200, timeout=0.01)
                    if Stm32_COM.isOpen():
                        COM_LIST.append('Stm32_COM')
                        print(serial_port, "Stm32_COM open success")
                except:
                    print("Stm32_COM open failed")
    elif com_sel == CH340_com:
        for port in port_list:
            if port.vid == CH340_VID:
                try:
                    serial_port = port.device
                    CH340_COM = serial.Serial(serial_port, 115200, timeout=0.01)
                    if CH340_COM.isOpen():
                        COM_LIST.append('CH340_COM')
                        print(serial_port, "CH340_COM open success")
                except:
                    print("CH340_COM open failed")
    else:
        pass


# 关闭串口
def serial_close(com_sel):
    global Link_COMM
    global Stm32_COM
    global CH340_COM

    if com_sel == Link_com:
        if Link_COMM.isOpen():
            Link_COMM.close()
            while com_sel in COM_LIST:
                COM_LIST.remove('Link_COMM')
    elif com_sel == Stm32_com:
        if Stm32_COM.isOpen():
            Stm32_COM.close()
            while com_sel in COM_LIST:
                COM_LIST.remove('Stm32_COM')
    elif com_sel == CH340_com:
        if CH340_COM.isOpen():
            CH340_COM.close()
            while com_sel in COM_LIST:
                COM_LIST.remove('CH340_COM')
    else:
        pass




def check_comlist():
    return COM_LIST


def com_flush(com_sel):
    if com_sel == 'Link_COMM':
        Link_COMM.flushInput()
    elif com_sel == 'Stm32_COM':
        Stm32_COM.flushInput()
    elif com_sel == 'CH340_COM':
        CH340_COM.flushInput()
    else:
        pass

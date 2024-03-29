import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'protopy'))
import SPI_Proto_pb2


def setspimesg(**kwargs):
    mesg = SPI_Proto_pb2.SPI_Proto()

    if 'bus_num' in kwargs:
        mesg.bus_num = kwargs.get('bus_num')
    else:
        mesg.bus_num = 0x1

    if 'cfg' in kwargs:
        mesg.cfg = kwargs.get('cfg')

        if 'fstb' in kwargs:
            mesg.fstb = kwargs.get('fstb')
        else:
            mesg.fstb = 1  #MSB
        
        if 'cpol' in kwargs:
            mesg.cpol = kwargs.get('cpol')
        else:
            mesg.cpol = 1

        if 'cpha' in kwargs:
            mesg.cpha = kwargs.get('cpha')
        else:
            mesg.cpha = 1

        if 'size' in kwargs:
            mesg.size = kwargs.get('size')
        else:
            mesg.size = 1  #16bit

        if 'cspol' in kwargs:
            mesg.cspol = kwargs.get('cspol')
        else:
            mesg.cspol = 0

        if 'freq' in kwargs:
            mesg.freq = kwargs.get('freq')
        else:
            mesg.freq = 7  #SPI_187P5Khz

    # data buf is a necessary parameter
    for data in kwargs.get('data_buf'):
        mesg.data_buf.append(data)
    mesg.tx_size = len(mesg.data_buf)

    if 'rx_size' in kwargs:
        mesg.rx_size = kwargs.get('rx_size')
    else:
        mesg.rx_size = 0

    return mesg


def SPI_Proto_unpack_core(buf):
    pb_info = SPI_Proto_pb2.SPI_Proto()
    pb_info.ParseFromString(buf)
    return pb_info.data_buf


def SPI_Proto_pack_core(**kwargs):
    return setspimesg(**kwargs).SerializeToString()


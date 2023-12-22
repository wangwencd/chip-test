import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'protopy'))
import I2C_Proto_pb2


def seti2cmesg(**kwargs):
    mesg = I2C_Proto_pb2.I2C_Proto()

    if 'bus_num' in kwargs:
        mesg.i2c_bus_num = kwargs.get('bus_num')
    else:
        mesg.i2c_bus_num = 0x1

    if 'i2c_address' in kwargs:
        mesg.i2c_address = kwargs.get('i2c_address')
    else:
        mesg.i2c_address = 0x55

    # data buf is a necessary parameter
    for data in kwargs.get('data_buf'):
        mesg.data_buf.append(data)
    mesg.tx_size = len(mesg.data_buf)

    if 'rx_size' in kwargs:
        mesg.rx_size = kwargs.get('rx_size')
    else:
        mesg.rx_size = 0
    if 'restart' in kwargs:
        mesg.restart = kwargs.get('rx_size')
    else:
        mesg.restart = 0
    if 'frequency' in kwargs:
        mesg.frequency = kwargs.get('frequency')
    else:
        mesg.frequency = 2

    return mesg


def I2C_Proto_unpack_core(buf):
    pb_info = I2C_Proto_pb2.I2C_Proto()
    pb_info.ParseFromString(buf)
    return pb_info


def I2C_Proto_pack_core(**kwargs):
    return seti2cmesg(**kwargs).SerializeToString()

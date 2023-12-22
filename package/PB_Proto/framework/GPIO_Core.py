import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'protopy'))
import GPIO_Proto_pb2

def setgpiomesg(**kwargs):
    mesg = GPIO_Proto_pb2.GPIO_Proto()
    if 'gpio_num' in kwargs:
        mesg.gpio_num = kwargs.get('gpio_num')
    else:
        mesg.gpio_num = 0
    if 'config' in kwargs:
        mesg.config = kwargs.get('config')
    if 'get_value' in kwargs:
        mesg.get_value = kwargs.get('get_value')
    if 'set_value' in kwargs:
        mesg.set_value = kwargs.get('set_value')
    return mesg


def GPIO_Proto_unpack_core(buf):
    pb_info = GPIO_Proto_pb2.GPIO_Proto()
    pb_info.ParseFromString(buf)
    return pb_info


def GPIO_Proto_pack_core(**kwargs):
    gpio_message = setgpiomesg(**kwargs)
    return gpio_message.SerializeToString()
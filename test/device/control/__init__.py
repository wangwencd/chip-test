# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/20 16:59
File: __init__.py
"""
from test.device.serial.serial_common import Serial_Common
from test.device.visa.visa_common import Visa_Common
from test.device.rtu.rtu_common import RTU_Common
from test.device.tcp.tcp_common import TCP_Common

Communication_dict = {
    'Class name': 'Class',
    'serial': Serial_Common,
    'visa': Visa_Common,
    'rtu': RTU_Common,
    'tcp': TCP_Common,
}

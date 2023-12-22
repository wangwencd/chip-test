# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/5 9:40
File: __init__.py
"""
import logging
import serial.tools.list_ports as list_port

from test.device.flow.flow_KEITHLEY2400 import Flow_KEITHLEY2400
from test.device.flow.flow_IT8811 import Flow_IT8811
from test.device.flow.flow_DL11B import Flow_DL11B
from test.device.flow.flow_DHT260 import Flow_DHT260
from test.device.flow.flow_MAX32760 import Flow_MAX32670
from test.device.flow.flow_F413ZH import Flow_F413ZH
from test.device.flow.flow_F413CH import Flow_F413CH

L = logging.getLogger('Main')

# Instrument_Dict = {
#     'Device name': 'Device manufacturer',
#     '2400': 'Prolific',
#     'IT8811': 'Prolific',
#     'DL11B': 'wch.cn',
#     'DHT260': 'Prolific',
#     'MAX32670': 'wch.cn'
# }

Instrument_Dict = {
    'Device name': 'Device pid',
    '2400':   9123,
    'IT8811': 9123,
    'DL11B': 29987,
    'DHT260': 24577,
    'MAX32670': 29987,
    'F413ZH': 516,
    'F413CH': 517,
}

Instrument_Class = {
    'Device name': 'Device class',
    '2400': Flow_KEITHLEY2400,
    'IT8811': Flow_IT8811,
    'DL11B': Flow_DL11B,
    'DHT260': Flow_DHT260,
    'MAX32670': Flow_MAX32670,
    'F413ZH': Flow_F413ZH,
    'F413CH': Flow_F413CH,
}

# def find_port(instrument_name: str):
#     """
#     Find port number of instrument
#
#     Args:
#         instrument_name: Name of instrument
#
#     Returns:
#         port.device: Port number of instrument
#     """
#     port_list = list_port.comports() # Get list of port
#     for port in port_list:
#
#         if port.manufacturer == Instrument_Dict[instrument_name]:
#             return port.device, Instrument_Class[instrument_name] # Return the corresponding port number and class
#
#     # L.warning('Warning: could not the corresponding port com!')
#     return

def find_port(instrument_name: str):
    """
    Find port number of instrument

    Args:
        instrument_name: Name of instrument

    Returns:
        port.device: Port number of instrument
    """
    port_list = list_port.comports() # Get list of port
    for port in port_list:

        if port.pid == Instrument_Dict[instrument_name]:
            return port.device, Instrument_Class[instrument_name] # Return the corresponding port number and class

    # L.warning('Warning: could not the corresponding port com!')
    return


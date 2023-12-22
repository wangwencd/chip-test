# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/11/24 10:04
File: __init__.py.py
"""
from test.device.flow.flow_DHT260 import Flow_DHT260

Instrument_Addr = {
    'Device name': 'Device addr',
    'DHT260': '192.168.2.3',
}

Instrument_Port = {
    'Device name': 'Device class',
    'DHT260': 8000,
}

Instrument_Class = {
    'Device name': 'Device class',
    'DHT260': Flow_DHT260,
}

def determine_instrument(instrument_name: str):
    """
    Determine instrument ID

    Args:
        instrument_name: Device name

    Returns:
        instrument_Addr: Address of instrument
        instrument_Port: Port of instrument
    """

    def find_Addr(instrument_name, Instrument_Addr):
        """
        Find instrument Address from dict

        Args:
            instrument_name: Device name
            Instrument_Addr: Dict of instrument name and address

        Returns:
            value: ID of instrument
        """
        for key, value in Instrument_Addr.items():
            if instrument_name == key:
                return value

    def find_port(instrument_name, Instrument_Port):
        """
        Find instrument port number from dict

        Args:
            instrument_name: Device name
            Instrument_Port: Dict of instrument name and port number

        Returns:
            value: Class of instrument
        """
        for key, value in Instrument_Port.items():
            if instrument_name == key:
                return value

    def find_class(instrument_name, Instrument_Class):
        """
        Find instrument class from dict

        Args:
            instrument_name: Device name
            Instrument_Class: Dict of instrument name and class

        Returns:
            value: Class of instrument
        """
        for key, value in Instrument_Class.items():
            if instrument_name == key:
                return value

    instrument_addr = find_Addr(instrument_name, Instrument_Addr)
    instrument_port = find_port(instrument_name, Instrument_Port)
    instrument_class = find_class(instrument_name, Instrument_Class)

    return (instrument_addr, instrument_port, instrument_class)
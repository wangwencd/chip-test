# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/3/26 13:58
File: __init__.py.py
"""
from test.device.flow.flow_CH341A import Flow_CH341A
from test.device.flow.flow_CH347 import Flow_CH347

Instrument_Dll = {
    'Device name': 'Device dll name',
    'CH341A': 'CH341DLLA64.DLL',
    'CH347': 'CH347DLLA64.DLL',
}

Instrument_Function = {
    'Device name': 'Device function name',
    'CH341A': ['CH341OpenDevice', 'CH341CloseDevice'],
    'CH347': ['CH347OpenDevice', 'CH347CloseDevice'],
}


Instrument_Class = {
    'Device name': 'Device class',
    'CH341A': Flow_CH341A,
    'CH347': Flow_CH347,
}

def determine_instrument(instrument_name: str):
    """
    Determine instrument ID

    Args:
        instrument_name: Device name

    Returns:
        instrument_Dll: Dll name of instrument
        instrument_Class: Class of instrument
    """
    def find_dll(instrument_name, Instrument_Dll):
        """
        Find instrument dll from dict

        Args:
            instrument_name: Device name
            Instrument_Dll: Dict of instrument name and dll name

        Returns:
            value: Dll name of instrument
        """
        for key, value in Instrument_Dll.items():
            if instrument_name == key:
                return value

    def find_function(instrument_name, Instrument_Function):
        """
        Find instrument function name from dict

        Args:
            instrument_name: Device name
            Instrument_Function: Dict of instrument name and function name

        Returns:
            value: Function name of instrument
        """
        for key, value in Instrument_Function.items():
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

    instrument_dll = find_dll(instrument_name, Instrument_Dll)
    instrument_function = find_function(instrument_name, Instrument_Function)
    instrument_class = find_class(instrument_name, Instrument_Class)

    return (instrument_dll, instrument_function, instrument_class)

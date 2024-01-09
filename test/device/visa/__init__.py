# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/15 15:20
File: __init__.py
"""

from test.device.flow.flow_IT8811 import Flow_IT8811
from test.device.flow.flow_E36312A import Flow_E36312A
from test.device.flow.flow_KEITHLEY2400 import Flow_KEITHLEY2400
from test.device.flow.flow_DG1062Z import Flow_DG1062Z
from test.device.flow.flow_KEITHLEY2450 import Flow_KEITHLEY2450
from test.device.flow.flow_DMM7510 import Flow_DMM7510
from test.device.flow.flow_B2910BL import Flow_B2910BL
from test.device.flow.flow_B2912A import Flow_B2912A
from test.device.flow.flow_DP832 import Flow_DP832
from test.device.flow.flow_DP932 import Flow_DP932

Instrument_Dict = {
    'Device name': 'Device ID',
    'E36312A': 'USB0::0x2A8D::0x1102::MY59004756::INSTR',
    'IT8811': 'USB0::0x2EC7::0x8800::800831011777270002::INSTR',
    '2400': 'GPIB0::24::INSTR',
    'DG1062Z': 'USB0::0x1AB1::0x0642::DG1ZA242001973::INSTR',
    '2450': 'USB0::0x05E6::0x2450::04576931::INSTR',
    'DMM7510': 'USB0::0x05E6::0x7510::04558718::INSTR',
    'B2910BL': 'USB0::0x2A8D::0x9301::MY60440182::INSTR',
    'B2912A': 'USB0::0x2A8D::0xB401::MY61390597::INSTR',
    'DP832': 'USB0::0x1AB1::0x0E11::DP8C242002746::INSTR',
    'DP932': 'USB0::0x1AB1::0xA4A8::DP9A250700055::INSTR',
}

Instrument_Class = {
    'Device name': 'Device class',
    'E36312A': Flow_E36312A,
    'IT8811': Flow_IT8811,
    '2400': Flow_KEITHLEY2400,
    'DG1062Z': Flow_DG1062Z,
    '2450': Flow_KEITHLEY2450,
    'DMM7510': Flow_DMM7510,
    'B2910BL': Flow_B2910BL,
    'B2912A': Flow_B2912A,
    'DP832': Flow_DP832,
    'DP932': Flow_DP932,
}

def determine_instrument(instrument_name: str):
    """
    Determine instrument ID

    Args:
        instrument_name: Device name

    Returns:
        instrument_ID: ID of instrument
        instrument_class: Class of instrument
    """

    def find_ID(instrument_name, Instrument_Dict):
        """
        Find instrument ID from dict

        Args:
            instrument_name: Device name
            Instrument_Dict: Dict of instrument name and ID

        Returns:
            value: ID of instrument
        """
        for key, value in Instrument_Dict.items():
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

    instrument_ID = find_ID(instrument_name, Instrument_Dict)
    instrument_class = find_class(instrument_name, Instrument_Class)

    return (instrument_ID, instrument_class)
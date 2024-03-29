# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/3/26 13:58
File: ch_common.py
"""
import logging
from ctypes import *
from test.device.ch import determine_instrument
from parse.file.project_path import pro_path
L = logging.getLogger('Main')

class CH_Common(object):
    """
    CH common control
    """
    def open_instrument(self, condition):
        """
        Open power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        def check_instrument(instrument_dll: str):
            """
            Check if there is the instrument dll

            Args:
                instrument_dll: Dll name of instrument
            """
            if instrument_dll == None:
                L.error('Error: Instrument is not found in the device!')
                raise EnvironmentError
        instrument_name = str(condition.test_info['Instrument'])  # Get instrument name from test condition
        if 'Device_ID' in condition.test_info:
            self.dev = condition.test_info['Device_ID']
        else:
            self.dev = 0
        instrument_dll, instrument_function, instrument_class = determine_instrument(instrument_name)
        check_instrument(instrument_dll)
        dll_path = pro_path + '/package/CH_dll/' + instrument_dll
        self.instrument_function = instrument_function
        self.instrument = windll.LoadLibrary(dll_path)  # Open instrument
        self.open()
        condition.Class[instrument_name] = instrument_class

        return condition

    def open(self):
        """
        Open device
        """
        if eval('self.instrument.' + self.instrument_function[0] + '(' + str(self.dev) + ')') != -1:
            L.info('Device open success!')
        else:
            L.error('Error: Device open failed!')

    def close(self):
        """
        Close device
        """
        eval('self.instrument.' + self.instrument_function[1] + '(' + str(self.dev) + ')')


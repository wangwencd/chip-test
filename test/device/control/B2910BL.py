# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/6 14:58
File: B2910BL.py
"""
import logging

from test.device.control.KEITHLEY2450 import KEITHLEY2450
from parse.exception.exception_visa.lists.list_B2910BL import List_B2910BL

L = logging.getLogger('Main')

class B2910BL(KEITHLEY2450):
    """
    B2910BL control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'B2910BL'

    def check_error(self):
        """
        Read the most recent error.
        """
        command = ':SYSTem:ERRor?'
        result = self.control.query(command)
        code = result.split(',"')[0]

        if code != '+0':

            for key, value in List_B2910BL.items():

                if code == key:
                    L.info(self.name + ' Error result: ' + result)
                    raise value()

            L.info(self.name + ' Error result: ' + result)
            raise List_B2910BL['Other']()

    def set_CV_mode_max_current(self, value):
        """
        Set max current in CV mode

        Args:
            value: Max current value, string format, unit: A
        """
        command = ':SENS:CURR:PROT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max current: ' + str(value) + 'A' + ' in CV mode')
        self.check_error()

    def query_voltage(self):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:VOLT?'
        result = eval(self.control.query(command))[0]
        L.debug(self.name + ' voltage: ' + str(result) + 'V')
        self.check_error()

        return result

    def query_current(self):
        """
        Measure current value

        Returns:
            result: Current value, unit: A
        """
        command = ':MEASure:CURR?'
        result = eval(self.control.query(command))[0]
        L.debug(self.name + ' current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_all(self):
        """
        Measure voltage and current value

        Returns:
            result: Current value, unit: A
        """
        command = ':MEASure:VOLT?'
        voltage = eval(self.control.query(command))[0]

        command = ':MEASure:CURR?'
        current = eval(self.control.query(command))[0]
        L.debug(self.name + ' voltage: ' + str(voltage) + 'V, ' + ' current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current
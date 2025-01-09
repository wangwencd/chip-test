# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/7 10:07
File: IT6722A.py
"""
import logging
import re

from test.device.control.scpi import SCPI
from parse.exception.exception_visa.lists.list_IT6722A import List_IT6722A
L = logging.getLogger('Main')

class IT6722A(SCPI):
    """
    IT6722A control
    """
    def __init__(self, cls, name=None):
        super().__init__()
        self.control = cls
        self.name = name if name else 'IT6722A'

    def check_error(self):
        """
        Read the most recent error.
        """
        command = ':SYSTem:ERRor?'
        result = self.control.query(command)
        code = re.split(',', result)[0]

        if code != '0':

            for key, value in List_IT6722A.items():

                if code == key:
                    L.info(self.name + ' Error result: ' + result)
                    raise value()

            L.info(self.name + ' Error result: ' + result)
            raise List_IT6722A['Other']()

    def enable_remote(self):
        """
        Enable remote control mode
        """
        command = 'SYSTem:REMote'
        self.control.write(command)
        L.debug(self.name + ' enable remote control mode')
        self.check_error()

    def disable_remote(self):
        """
        Disable remote control mode
        """
        command = 'SYSTem:LOCal'
        self.control.write(command)
        L.debug(self.name + ' disable remote control mode')
        self.check_error()

    def channel_on(self):
        """
        Set channel output on
        """
        command = 'OUTPut ON'
        self.control.write(command)
        L.debug(self.name + ' channel ON')
        self.check_error()

    def channel_off(self):
        """
        Set channel output off
        """
        command = 'OUTPut OFF'
        self.control.write(command)
        L.debug(self.name + ' channel OFF')
        self.check_error()

    def set_channel_current(self, current):
        """
        Set current value

        Args:
            current: Current value, string format, unit: A
        """
        command = 'CURR ' + str(current)  # format example: CURR 1
        self.control.write(command)
        L.debug(self.name + ' set current: ' + str(current) + 'A')
        self.check_error()

    def set_channel_voltage(self, voltage):
        """
        Set voltage value

        Args:
            voltage: Voltage value, string format, unit: V
        """
        command = 'VOLT ' + str(voltage)  # format example: VOLT 1
        self.control.write(command)
        L.debug(self.name + ' set voltage: ' + str(voltage) + 'V')
        self.check_error()

    def set_channel_voltage_current(self, voltage, current):
        """
        Set voltage and current value

        Args:
            voltage: Voltage value, string format, unit: V
            current: Current value, string format, unit: A
        """
        command = 'APPL ' + str(voltage) + ', ' + str(current)  # format example: APPL 1, 1
        self.control.write(command)
        L.debug(self.name + ' set voltage: ' + str(voltage) + 'V,' + ' current: ' + str(current) + 'A')
        self.check_error()

    def query_voltage(self):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = 'MEASure:VOLT?'
        temp = self.control.query(command)
        result = eval(temp.split(',')[0])
        L.debug(self.name + ' voltage: ' + str(result) + 'V')
        self.check_error()

        return result

    def query_current(self):
        """
        Measure current value

        Returns:
            result: Current value, unit: A
        """
        command = 'MEASure:CURR?'
        result = self.control.query(command)
        L.debug(self.name + ' current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_power(self):
        """
        Measure power value

        Returns:
            result: Power value, unit: W
        """
        command = 'MEASure:POW?'
        result = self.control.query(command)
        L.debug(self.name + ' power: ' + str(result) + 'W')
        self.check_error()

        return result

    def query_all(self):
        """
        Measure voltage and current value

        Returns:
            result: Current value, unit: A
        """
        command = 'MEASure:VOLT?'
        voltage = self.control.query(command)

        command = 'MEASure:CURR?'
        current = self.control.query(command)
        L.debug(self.name + ' voltage: ' + str(voltage) + 'V, ' + 'current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current

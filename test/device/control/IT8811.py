# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/22 17:07
File: IT8811.py
"""
import logging

from test.device.control.scpi import SCPI
from parse.exception.exception_visa.lists.list_IT8811 import List_IT8811

L = logging.getLogger('Main')

class IT8811(SCPI):
    """
    IT8811 control
    """
    def __init__(self, cls, name=None):
        super().__init__()
        self.control = cls
        # self.name = 'IT8811'
        self.name = name if name else 'IT8811'

    def check_error(self):
        """
        Read the most recent error.
        """
        command = 'SYSTem:ERRor?'
        result = self.control.query(command)
        code = result.split(',"')[0]

        if code != '0' and '':

            for key, value in List_IT8811.items():

                if code == key:
                    L.info(self.name + ' Error result: ' + result)
                    raise value()

            L.info(self.name + ' Error result: ' + result)
            raise List_IT8811['Other']()

    def enable_remote(self):
        """
        Enter remote mode, commands are enabled
        """
        command = 'SYST:REM'
        self.control.write(command)
        L.debug(self.name + ' enable remote command')
        self.check_error()

    def channel_on(self):
        """
        Set all channels input on
        """
        command = 'INP 1'
        self.control.write(command)
        L.debug(self.name + ' channel ON')
        self.check_error()

    def channel_off(self):
        """
        Set all channels input off
        """
        command = 'INP 0'
        self.control.write(command)
        L.debug(self.name + ' channel OFF')
        self.check_error()

    def enter_CC_mode(self):
        """
        Enter CC mode
        """
        command = 'FUNC CURR'
        self.control.write(command)
        L.debug(self.name + ' enter CC mode')
        self.check_error()

    def enter_CV_mode(self):
        """
        Enter CV mode
        """
        command = 'FUNC VOLT'
        self.control.write(command)
        L.debug(self.name + ' enter CV mode')
        self.check_error()

    def enter_CR_mode(self):
        """
        Enter CR mode
        """
        command = 'FUNC RES'
        self.control.write(command)
        L.debug(self.name + ' enter CR mode')
        self.check_error()

    def enter_CW_mode(self):
        """
        Enter CW mode
        """
        command = 'FUNC POW'
        self.control.write(command)
        L.debug(self.name + ' enter CW mode')
        self.check_error()

    def set_CC_mode_current(self, value):
        """
        Set load current in CC mode

        Args:
            value: Load current, string format, unit： A
        """
        command = 'CURR ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set current: ' + str(value) + 'A' + ' in CC mode')
        self.check_error()

    def set_CC_mode_max_voltage(self, value):
        """
        Set max voltage in CC mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'CURR:HIGH ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CC mode')
        self.check_error()

    def set_CC_mode_min_voltage(self, value):
        """
        Set min voltage in CC mode

        Args:
            value: Min voltage value, string format, unit: V
        """
        command = 'CURR:LOW ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set min voltage: ' + str(value) + 'V' + ' in CC mode')
        self.check_error()

    def set_CV_mode_voltage(self, value):
        """
        Set load voltage in CV mode

        Args:
            value: Load voltage, string format, unit: V
        """
        command = 'VOLT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set voltage: ' + str(value) + 'V' + ' in CV mode')
        self.check_error()

    def set_CV_mode_max_current(self, value):
        """
        Set max current in CV mode

        Args:
            value: Max current value, string format, unit: A
        """
        command = 'VOLT:HIGH ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max current: ' + str(value) + 'A' + ' in CV mode')
        self.check_error()

    def set_CV_mode_min_current(self, value):
        """
        Set min current in CV mode

        Args:
            value: Min current value, string format, unit: A
        """
        command = 'VOLT:LOW ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set min current: ' + str(value) + 'A' + ' in CV mode')
        self.check_error()

    def set_CR_mode_resistance(self, value):
        """
        Set load resistance in CR mode

        Args:
            value: Load resistance, string format, unit: Ohm
        """
        command = 'RES ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set resistance: ' + str(value) + 'Ohm' + ' in CR mode')
        self.check_error()

    def set_CR_mode_max_voltage(self, value):
        """
        Set max voltage in CR mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'RES:HIGH ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CR mode')
        self.check_error()

    def set_CR_mode_min_voltage(self, value):
        """
        Set min voltage in CR mode

        Args:
            value: Min voltage value, string format, unit: V
        """
        command = 'RES:LOW ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set min voltage: ' + str(value) + 'V' + ' in CR mode')
        self.check_error()

    def set_CW_mode_power(self, value):
        """
        Set load power in CW mode

        Args:
            value: Load power, string format, unit: W
        """
        command = 'POW ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set power: ' + str(value) + 'W' + ' in CW mode')
        self.check_error()

    def set_CW_mode_max_voltage(self, value):
        """
        Set max voltage in CW mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'POW:HIGH ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CW mode')
        self.check_error()

    def set_CW_mode_min_voltage(self, value):
        """
        Set min voltage in CW mode

        Args:
            value: Min voltage value, string format, unit: V
        """
        command = 'POW:LOW ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set min voltage: ' + str(value) + 'V' + ' in CW mode')
        self.check_error()

    def query_voltage(self):
        """
        Measure load voltage

        Returns:
            result: Load voltage value, unit: V
        """
        command = 'MEAS:VOLT?'
        result = self.control.query(command)
        L.debug(self.name + ' voltage: ' + str(result) + 'V')
        self.check_error()

        return result

    def query_current(self):
        """
        Measure load current

        Returns:
            result: Load current value, unit: A
        """
        command = 'MEAS:CURR?'
        result = self.control.query(command)
        L.debug(self.name + ' current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_power(self):
        """
        Measure load power

        Returns:
            result: Load power value, unit: W
        """
        command = 'FETC:POW?'
        result = self.control.query(command)
        L.debug(self.name + ' power: ' + str(result) + 'W')
        self.check_error()

        return result

    def query_all(self):
        """
        Measure load voltage and current
        """
        command = 'MEAS:CURR?'
        current = self.control.query(command)

        command = 'MEAS:VOLT?'
        voltage = self.control.query(command)
        L.debug(self.name + ' voltage: ' + str(voltage) + 'V, ' + self.name + ' current: ' + str(current) + 'A')

        return voltage, current

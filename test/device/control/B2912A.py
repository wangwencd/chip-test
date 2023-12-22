# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/18 10:02
File: B2912A.py
"""
import logging

from test.device.control.B2910BL import B2910BL
from parse.exception.exception_visa.lists.list_B2910BL import List_B2910BL

L = logging.getLogger('Main')

class B2912A(B2910BL):
    """
    B2912A control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'B2912A'

    def query_voltage(self, channel=1):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:VOLT? (@' + str(channel) + ')'
        result = eval(self.control.query(command))
        L.debug(self.name + ' channel' + str(channel) + ' voltage: ' + str(result) + 'V')
        self.check_error()

        return result

    def query_current(self, channel=1):
        """
        Measure current value

        Returns:
            result: Current value, unit: A
        """
        command = ':MEASure:CURR? (@' + str(channel) + ')'
        result = eval(self.control.query(command))
        L.debug(self.name + ' channel' + str(channel) + ' current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_all(self, channel=1):
        """
        Measure voltage and current value

        Returns:
            result: Current value, unit: A
        """
        command = ':MEASure:VOLT? (@' + str(channel) + ')'
        voltage = eval(self.control.query(command))

        command = ':MEASure:CURR? (@' + str(channel) + ')'
        current = eval(self.control.query(command))
        L.debug(self.name + ' channel' + str(channel) + ' voltage: ' + str(voltage) + 'V, ' + ' current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current

    def set_CV_mode_max_current(self, value, channel=1):
        """
        Set max current in CV mode

        Args:
            value: Max current value, string format, unit: A
        """
        command = ':SENS' + str(channel) + ':CURR:PROT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' set max current: ' + str(value) + 'A' + ' in CV mode')
        self.check_error()

    def set_CC_mode_max_voltage(self, value, channel=1):
        """
        Set max voltage in CC mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = ':SENS' + str(channel) + ':VOLT:PROT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' set max voltage: ' + str(value) + 'V' + ' in CC mode')
        self.check_error()

    def set_CV_mode_voltage(self, value, channel=1):
        """
        Set power voltage in CV mode

        Args:
            value: Power voltage, string format, unit: V
        """
        command = ':SOURce' + str(channel) + ':VOLTage:LEVel:IMMediate:AMPLitude ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' set voltage: ' + str(value) + 'V' + ' in CV mode')
        self.check_error()

    def set_CC_mode_current(self, value, channel=1):
        """
        Set power current in CC mode

        Args:
            value: Power current, string format, unit： A
        """
        command = ':SOURce' + str(channel) + ':CURRent:LEVel:IMMediate:AMPLitude ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' set current: ' + str(value) + 'A' + ' in CC mode')
        self.check_error()

    def channel_on(self, channel=1):
        """
        Set channel output on
        """
        command = ':OUTPut' + str(channel) + ':STATe ON'
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' channel ON')
        self.check_error()

    def channel_off(self, channel=1):
        """
        Set channel output off
        """
        command = ':OUTPut' + str(channel) + ':STATe OFF'
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' channel OFF')
        self.check_error()

    def enter_CC_mode(self, channel=1):
        """
        Enter CC mode
        """
        command = ':SOUR' + str(channel) + ':FUNC:MODE CURR'
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' enter CC mode')
        self.check_error()

    def enter_CV_mode(self, channel=1):
        """
        Enter CV mode
        """
        command = ':SOUR' + str(channel) + ':FUNC:MODE VOLT'
        self.control.write(command)
        L.debug(self.name + ' channel' + str(channel) + ' enter CV mode')
        self.check_error()

    def set_CV_mode_voltage_range(self, channel=1, range='DEFault'):
        """
        Set CV mode voltage setting range

        Args:
            range: Voltage setting range value, unit: V
        """
        if range != 'DEFault':
            command = ':SOURce' + str(channel) + ':VOLTage:RANGe ' + str(range)
            L.debug(self.name + ' set voltage range: ' + str(range) + 'V')

        else:
            command = ':SOURce' + str(channel) + ':VOLTage:RANGe DEFault'
            L.debug(self.name + ' set voltage range: 20(default)V')
        self.control.write(command)
        self.check_error()


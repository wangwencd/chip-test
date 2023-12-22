# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/24 17:36
File: KEITHLEY2450.py
"""
import logging

from test.device.control.KEITHLEY2400 import KEITHLEY2400

L = logging.getLogger('Main')

class KEITHLEY2450(KEITHLEY2400):
    """
    KEITHLEY2450 control
    """
    def __init__(self, cls):
        super().__init__(cls)
        self.control = cls
        self.name = '2450'

    def set_CV_mode_max_current(self, value):
        """
        Set max current in CV mode

        Args:
            value: Max current value, string format, unit: A
        """
        command = 'SOURCe:VOLTage:ILIMit ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max current: ' + str(value) + 'A' + ' in CV mode')
        self.check_error()

    def set_CC_mode_max_voltage(self, value):
        """
        Set max voltage in CC mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'SOURCe:CURRent:VLIMit ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CC mode')
        self.check_error()

    def enter_memory_mode(self):
        """
        Rebuild 2450 memory mode, 2450 don't have this function
        """
        L.warning(self.name + " don't have memory mode func")

    def enable_all_measurement(self):
        """
        Enable all measurement functions, 2450 don't have this function
        """
        L.warning(self.name + " don't have enable all measurements func")

    def disable_all_measurement(self):
        """
        Disable all measurement functions, 2450 don't have this function
        """
        L.warning(self.name + " don't have disable all measurements func")

    def enable_concurrent_measurement(self):
        """
        Enable concurrent measurement, 2450 don't have this function
        """
        L.warning(self.name + " don't have enable concurrent measurement func")

    def disable_concurrent_measurement(self):
        """
        Disable concurrent measurement, 2450 don't have this function
        """
        L.warning(self.name + " don't have disable concurrent measurement func")

    def query_voltage(self):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:VOLT?'
        result = eval(self.control.query(command))
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
        result = eval(self.control.query(command))
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
        voltage = eval(self.control.query(command))

        command = ':MEASure:CURR?'
        current = eval(self.control.query(command))
        L.debug(self.name + ' voltage: ' + str(voltage) + 'V, ' + ' current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current

    def set_CV_mode_voltage(self, value):
        """
        Set power voltage in CV mode

        Args:
            value: Power voltage, string format, unit: V
        """
        command = ':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set voltage: ' + str(value) + 'V' + ' in CV mode')
        self.check_error()

    def set_CC_mode_current(self, value):
        """
        Set power current in CC mode

        Args:
            value: Power current, string format, unit： A
        """
        command = ':SOURce1:CURRent:LEVel:IMMediate:AMPLitude ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set current: ' + str(value) + 'A' + ' in CC mode')
        self.check_error()

    def enter_CV_mode_4_wire_mode(self):
        command = ':SENSe:VOLTage:RSENse ON'
        self.control.write(command)
        L.debug(self.name + ' enter 4-wire sense mode in CV mode!')
        self.check_error()

    def enter_CV_mode_2_wire_mode(self):
        command = ':SENSe:VOLTage:RSENse OFF'
        self.control.write(command)
        L.debug(self.name + ' enter 2-wire sense mode in CV mode!')
        self.check_error()

    def enter_CC_mode_4_wire_mode(self):
        command = ':SENSe:CURRent:RSENse ON'
        self.control.write(command)
        L.debug(self.name + ' enter 4-wire sense mode in CC mode!')
        self.check_error()

    def enter_CC_mode_2_wire_mode(self):
        command = ':SENSe:CURRent:RSENse OFF'
        self.control.write(command)
        L.debug(self.name + ' enter 2-wire sense mode in CC mode!')
        self.check_error()

    def enter_CR_mode_4_wire_mode(self):
        command = ':SENSe:RESistance:RSENse ON'
        self.control.write(command)
        L.debug(self.name + ' enter 4-wire sense mode in CR mode!')
        self.check_error()

    def enter_CR_mode_2_wire_mode(self):
        command = ':SENSe:RESistance:RSENse OFF'
        self.control.write(command)
        L.debug(self.name + ' enter 2-wire sense mode in CR mode!')
        self.check_error()



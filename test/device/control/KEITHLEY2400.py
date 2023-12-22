# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/9 9:58
File: KEITHLEY2400.py
"""
import logging

from test.device.control.scpi import SCPI
from parse.exception.exception_visa.lists.list_2400 import List_2400

L = logging.getLogger('Main')

class KEITHLEY2400(SCPI):
    """
    KEITHLEY2400 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = '2400'
        super().__init__()

    def check_error(self):
        """
        Read the most recent error.
        """
        command = ':SYSTem:ERRor?'
        result = self.control.query(command)
        code = result.split(',"')[0]

        if code != '0':

            for key, value in List_2400.items():

                if code == key:
                    L.info(self.name + ' Error result: ' + result)
                    raise value()

            L.info(self.name + ' Error result: ' + result)
            raise List_2400['Other']()

    def channel_on(self):
        """
        Set channel output on
        """
        command = ':OUTPut:STATe ON'
        self.control.write(command)
        L.debug(self.name + ' channel ON')
        self.check_error()

    def channel_off(self):
        """
        Set channel output off
        """
        command = ':OUTPut:STATe OFF'
        self.control.write(command)
        L.debug(self.name + ' channel OFF')
        self.check_error()

    def enter_CC_mode(self):
        """
        Enter CC mode
        """
        command = ':SOUR1:FUNC:MODE CURR'
        self.control.write(command)
        L.debug(self.name + ' enter CC mode')
        self.check_error()

    def enter_CV_mode(self):
        """
        Enter CV mode
        """
        command = ':SOUR1:FUNC:MODE VOLT'
        self.control.write(command)
        L.debug(self.name + ' enter CV mode')
        self.check_error()

    def enter_memory_mode(self):
        """
        Enter memory mode
        """
        command = ':SOUR1:FUNC:MODE MEM'
        self.control.write(command)
        L.debug(self.name + ' enter memory mode')
        self.check_error()

    def enable_concurrent_measurement(self):
        """
        Enable concurrent measurement
        """
        command = ':SENS1:FUNC:CONC ON'
        self.control.write(command)
        L.debug(self.name + ' enable concurrent measurement')
        self.check_error()

    def disable_concurrent_measurement(self):
        """
        Disable concurrent measurement
        """
        command = ':SENS1:FUNC:CONC OFF'
        self.control.write(command)
        L.debug(self.name + ' disable concurrent measurement')
        self.check_error()

    def enable_all_measurement(self):
        """
        Enable all measurement functions
        """
        command = ':SENS1:FUNC:ON:ALL'
        self.control.write(command)
        L.debug(self.name + ' enable all measurement functions')
        self.check_error()

    def disable_all_measurement(self):
        """
        Disable all measurement functions
        """
        command = ':SENS1:FUNC:OFF:ALL'
        self.control.write(command)
        L.debug(self.name + ' disable all measurement functions')
        self.check_error()

    def enable_auto_range_for_voltage_measurement(self):
        """
        Enable auto range for voltage measurement
        """
        command = ':SENS1:VOLT:DC:RANGE:AUTO ON'
        self.control.write(command)
        L.debug(self.name + ' enable auto range for voltage measurement')
        self.check_error()

    def disable_auto_range_for_voltage_measurement(self):
        """
        Disable auto range for voltage measurement
        """
        command = ':SENS1:VOLT:DC:RANGE:AUTO OFF'
        self.control.write(command)
        L.debug(self.name + ' disable auto range for voltage measurement')
        self.check_error()

    def enable_auto_range_for_current_measurement(self):
        """
        Enable auto range for current measurement
        """
        command = ':SENS1:CURR:DC:RANGE:AUTO ON'
        self.control.write(command)
        L.debug(self.name + ' enable auto range for current measurement')
        self.check_error()

    def disable_auto_range_for_current_measurement(self):
        """
        Disable auto range for current measurement
        """
        command = ':SENS1:CURR:DC:RANGE:AUTO OFF'
        self.control.write(command)
        L.debug(self.name + ' disable auto range for current measurement')
        self.check_error()

    def set_measurement_speed(self, value=1):
        """
        Set the integration period (speed) for measurements.

        Args:
            value: Power-line cycles per integration, 1 is 16.67ms
        """
        command = ':SENS1:VOLT:DC:NPLC ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set measurement speed: ' + str(value) + ' PLC')
        self.check_error()

    def query_voltage(self):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:VOLT?'
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
        command = ':MEASure:CURR?'
        temp = self.control.query(command)
        result = eval(temp.split(',')[1])
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
        temp = self.control.query(command)
        voltage = eval(temp.split(',')[0])

        command = ':MEASure:CURR?'
        temp = self.control.query(command)
        current = eval(temp.split(',')[1])
        L.debug(self.name + ' voltage: ' + str(voltage) + 'V, ' + ' current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current

    def enable_auto_range_for_voltage_setting(self):
        """
        Enable auto range for voltage setting
        """
        command = ':SOURce1:VOLTage:RANGe:AUTO ON'
        self.control.write(command)
        L.debug(self.name + ' enable auto range for voltage setting')
        self.check_error()

    def disable_auto_range_for_voltage_setting(self):
        """
        Disable auto range for voltage setting
        """
        command = ':SOURce1:VOLTage:RANGe:AUTO OFF'
        self.control.write(command)
        L.debug(self.name + ' disable auto range for voltage setting')
        self.check_error()

    def enable_auto_range_for_current_setting(self):
        """
        Enable auto range for current setting
        """
        command = ':SOURce1:CURRent:RANGe:AUTO ON'
        self.control.write(command)
        L.debug(self.name + ' enable auto range for current setting')
        self.check_error()

    def disable_auto_range_for_current_setting(self):
        """
        Disable auto range for current setting
        """
        command = ':SOURce1:CURRent:RANGe:AUTO OFF'
        self.control.write(command)
        L.debug(self.name + ' disable auto range for current setting')
        self.check_error()

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

    def set_CC_mode_max_voltage(self, value):
        """
        Set max voltage in CC mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = ':SENS:VOLT:PROT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CC mode')
        self.check_error()

    def select_output_off_state_HIMP(self):
        """
        Select himpedance of output-of state, thus disconnecting input/output
        """
        command = ':OUTPut:SMODe HIMP'
        self.control.write(command)
        L.debug(self.name + ' select HIMP of output-of state')
        self.check_error()

    def set_CV_mode_voltage_and_max_current(self, voltage, current):
        """
        Set power voltage in CV mode

        Args:
            voltage: Power voltage, string format, unit: V
            current: Max current value, string format, unit: A
        """
        command = ':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude ' + str(voltage)
        self.control.write(command)

        command = ':SENS:CURR:PROT ' + str(current)
        self.control.write(command)
        L.debug(self.name + ' set voltage: ' + str(voltage) + 'V,'
                + ' set max current: ' + str(current) + 'A' + ' in CV mode')
        self.check_error()

    def set_CV_mode_voltage_range(self, range='DEFault'):
        """
        Set CV mode voltage setting range

        Args:
            range: Voltage setting range value, unit: V
        """
        if range != 'DEFault':
            command = ':SOURce1:VOLTage:RANGe ' + str(range)
            L.debug(self.name + ' set voltage range: ' + str(range) + 'V')

        else:
            command = ':SOURce1:VOLTage:RANGe DEFault'
            L.debug(self.name + ' set voltage range: 20(default)V')
        self.control.write(command)
        self.check_error()

    def query_CV_mode_voltage_range(self):
        """
        Get CV mode voltage setting range

        Returns:
            result Voltage setting range value, unit: V
        """
        command = ':SOURce1:VOLTage:RANGe?'
        result = self.control.query(command)
        L.debug(self.name + ' get voltage range: ' + str(result) + 'V')
        self.check_error()

        return float(result)

    def enable_remote_sensing(self):
        """
        Enter into remote sensing mode
        """
        command = ':SYST:RSEN ON'
        self.control.write(command)
        L.debug(self.name + ' enable remote sensing')
        self.check_error()

    def enable_local_sensing(self):
        """
        Enter into local sensing mode
        """
        command = ':SYST:RSEN OFF'
        self.control.write(command)
        L.debug(self.name + ' enable local sensing')
        self.check_error()

    def set_CV_mode_current_range(self, range='DEFault'):
        """
        Set CV mode current setting range

        Args:
            range: Current setting range value, unit: A
        """
        if range != 'DEFault':
            command = ':SENSe1:CURRent:RANGe ' + str(range)
            L.debug(self.name + ' set current range: ' + str(range) + 'A')

        else:
            command = ':SENSe1:CURRent:RANGe DEFault'
            L.debug(self.name + ' set current range: 0.000105(default)A')
        self.control.write(command)
        self.check_error()
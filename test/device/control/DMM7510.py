# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/5/9 10:31
File: DMM7510.py
"""
import logging

from test.device.control.scpi import SCPI

L = logging.getLogger('Main')

function_list = {
    'Item': ('Command', 'Unit', 'Class'),
    'Voltage': ('VOLT', 'V', 'Voltage'),
    'Resistance': ('RES', 'ohm', 'Resistance'),
    'Current': ('CURR', 'A', 'Current'),
    'Temperature': ('TEMP', 'C', 'Temperature'),
    'Voltage_Ratio': ('VOLT:RAT', 'V', 'Voltage'),
    'Voltage_AC': ('VOLT:AC', 'V', 'Voltage'),
    'Fresistance': ('FRES', 'ohm', 'Resistance'),
    'Continuity': ('CONT', '', 'Continuity'),
    'Diode': ('DIOD', 'V', 'Diode'),
    'Frequency': ('FREQ', 'Hz', 'Frequency'),
    'Current_AC': ('CURR:AC', 'A', 'Current'),
    'Capacitance': ('CAP', 'C', 'Capacitance'),
    'Period': ('PER', '%', 'Period'),
    'Voltage_DIG': ('DIG:VOLT', 'V', 'Voltage'),
    'Current_DIG': ('DIG:CURR', 'A', 'Voltage'),
}

class DMM7510(SCPI):
    """
    DMM7510 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DMM7510'
        super().__init__()

    def query_one_measurement(self, option='Voltage'):
        """
        Measure one parameter according to function option

        Args:
            option: Option of one function

        Returns:
            result: Measurement result, unit options: V /A /C /Hz /ohm /C ...
        """
        for key, value in function_list.items():

            if option == key:
                command = ':MEASure:' + value[0] + '?'
                result = eval(self.control.query(command))
                L.debug(self.name + ' ' + option + ': ' + str(result) + value[1])
                break
        self.check_error()

        return result

    def set_one_measurement_speed(self, option='Voltage', speed=1):
        """
        Set the integration period (speed) for one measurement.

        Args:
            option: Option of one function
            speed: Power-line cycles per integration, 1 is 16.67ms
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':NPLC ' + str(speed)
                self.control.write(command)
                L.debug(self.name + ' set ' + option + ' measurement speed: ' + str(speed) + ' PLC')
        self.check_error()

    def set_one_measurement_average_count(self, option='Voltage', num=1):
        """
        Set the averaging number for one measurement.

        Args:
            option: Option of one function
            num: Averaging number of measurement, range from 1 to 100
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':AVER:COUNT ' + str(num)
                self.control.write(command)
                L.debug(self.name + ' set ' + option + ' average count: ' + str(num))
        self.check_error()

    def set_one_measurement_autorange(self, option='Voltage', flag='ON'):
        """
        Set the averaging number for one measurement.

        Args:
            option: Option of one function
            flag: Flag of auto range, option: ON or 1 / OFF or 0
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':RANGe:AUTO ' + str(flag)
                self.control.write(command)
                L.debug(self.name + ' set ' + option + ' auto range ' + str(flag))
        self.check_error()

    def set_one_measurement_autozero(self, option='Voltage', flag='ON'):
        """
        Set the autozero on/ off for one measurement.

        Args:
            option: Option of one function
            flag: Flag of auto range, option: ON or 1 / OFF or 0
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':AZER ' + str(flag)
                self.control.write(command)
                L.debug(self.name + ' set ' + option + ' auto zero ' + str(flag))
        self.check_error()

    def set_one_measurement_average_control(self, option='Voltage', type='REP'):
        """
        Set the averaging type for one measurement.

        Args:
            option: Option of one function
            type: Averaging type of measurement, option: REP or MOV
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':AVER:TCON ' + str(type)
                self.control.write(command)
                L.debug(self.name + ' set ' + option + ' average control: ' + str(type))
        self.check_error()

    def set_one_measurement_average(self, option='Voltage', flag='ON'):
        """
        Set the average on/ off for one measurement.

        Args:
            option: Option of one function
            flag: Flag of auto range, option: ON or 1 / OFF or 0
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':AVER ' + str(flag)
                self.control.write(command)
                L.debug(self.name + ' set ' + option + ' average ' + str(flag))
        self.check_error()

    def set_one_input_impedance(self, option='Voltage', choice='AUTO'):
        """
        Set input impedance of one function.

        Args:
            option: Option of one function
            choice: Input impedance choice, option: AUTO or MOHM10
        """
        for key, value in function_list.items():

            if option == key:
                command = value[0] + ':INP ' + choice
                self.control.write(command)
                L.debug(self.name + ' Set ' + option + ' input impedance: ' + choice)
                break
        self.check_error()

    def query_voltage(self):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:VOLTage:DC?'
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
        command = ':MEASure:CURRent:DC?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_resistance(self):
        """
        Measure resistance value

        Returns:
            result: Resistance value, unit: ohm
        """
        command = ':MEASure:RESistance?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' resistance: ' + str(result) + 'ohm')
        self.check_error()

        return result

    def query_temperature(self):
        """
        Measure temperature value

        Returns:
            result: Temperature value, unit: C
        """
        command = ':MEASure:TEMPerature?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' temperature: ' + str(result) + 'C')
        self.check_error()

        return result

    def query_diode(self):
        """
        Measure diode value

        Returns:
            result: Diode value, unit: V
        """
        command = ':MEASure:DIODe?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' diode: ' + str(result) + 'V')
        self.check_error()

        return result

    def query_capacitance(self):
        """
        Measure capacitance value

        Returns:
            result: Capacitance value, unit: C
        """
        command = ':MEASure:CAPacitance?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' capacitance: ' + str(result) + 'C')
        self.check_error()

        return result

    def query_digitize_voltage(self):
        """
        Measure digitize voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:DIGitize:VOLTage?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' digitize voltage: ' + str(result) + 'V')
        self.check_error()

        return result

    def query_digitize_current(self):
        """
        Measure digitize current value

        Returns:
            result: Current value, unit: A
        """
        command = ':MEASure:DIGitize:CURRent?'
        result = eval(self.control.query(command))
        L.debug(self.name + ' digitize current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_voltage_current(self):
        """
        Measure voltage value

        Returns:
            result: Voltage value, unit: V
        """
        command = ':MEASure:VOLTage:DC?'
        voltage = eval(self.control.query(command))

        command = ':MEASure:CURRent:DC?'
        current = eval(self.control.query(command))
        L.debug(self.name + ' voltage: ' + str(voltage) + 'V,' + ' current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current

    def set_voltage_measurement_speed(self, value=1):
        """
        Set the integration period (speed) for voltage measurements.

        Args:
            value: Power-line cycles per integration, 1 is 16.67ms
        """
        command = 'VOLT:NPLC ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set voltage measurement speed: ' + str(value) + ' PLC')
        self.check_error()

    def set_current_measurement_speed(self, value=1):
        """
        Set the integration period (speed) for current measurements.

        Args:
            value: Power-line cycles per integration, 1 is 16.67ms
        """
        command = 'CURR:NPLC ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set current measurement speed: ' + str(value) + ' PLC')
        self.check_error()

    def set_resistance_measurement_speed(self, value=1):
        """
        Set the integration period (speed) for resistance measurements.

        Args:
            value: Power-line cycles per integration, 1 is 16.67ms
        """
        command = 'RES:NPLC ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set resistance measurement speed: ' + str(value) + ' PLC')
        self.check_error()

    def set_voltage_average_count(self, value=10):
        """
        Set the averaging number for voltage measurements.

        Args:
            value: Averaging number of measurement, range from 1 to 100
        """
        command = 'VOLT:AVER:COUNT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set voltage averaging count: ' + str(value))
        self.check_error()

    def set_current_average_count(self, value=10):
        """
        Set the averaging number for current measurements.

        Args:
            value: Averaging number of measurement, range from 1 to 100
        """
        command = 'CURR:AVER:COUNT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set current averaging count: ' + str(value))
        self.check_error()

    def set_resistance_average_count(self, value=10):
        """
        Set the averaging number for resistance measurements.

        Args:
            value: Averaging number of measurement, range from 1 to 100
        """
        command = 'RES:AVER:COUNT ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' Set resistance averaging count: ' + str(value))
        self.check_error()

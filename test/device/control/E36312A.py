# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/15 15:33
File: E36312A.py
"""
import logging
from test.device.control.scpi import SCPI
from parse.exception.exception_visa.lists.list_E36312A import List_E36312A

L = logging.getLogger('Main')

class E36312A(SCPI):
    """
    E36312A control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'E36312A'
        super().__init__()

    def check_error(self):
        """
        Read the most recent error.
        """
        command = 'SYSTem:ERRor?'
        result = self.control.query(command)
        code = result.split(',"')[0]

        if code != '+0':

            for key, value in List_E36312A.items():

                if code == key:
                    L.info(self.name + ' Error result: ' + result)
                    raise value()

            L.info(self.name + ' Error result: ' + result)
            raise List_E36312A['Other']()

    def set_channel_voltage_current(self, voltage, current, channel=2):
        """
        Select channel and set voltage and current value

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3
            voltage: Voltage value, string format, unit: V
            current: Current value, string format, unit: A
        """
        command = 'APPL ' + 'Ch' + str(channel) + ', ' + str(voltage) + ', ' + str(current) # format example: APPL Ch1, 5, 1
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ', voltage: ' + str(voltage) + 'V' + ', current: ' + str(current) + 'A')
        self.check_error()

    def set_channel_current(self, current, channel=2):
        """
        Select channel and set current value

        Args:
            channel: Channel number, string format, options: 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3
            current: Current value, string format, unit: A
        """
        command = 'CURR ' + str(current) + ', ' + '(@' + str(channel) + ')' # format example: CURR 1, (@1)
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ', current: ' + str(current) + 'A')
        self.check_error()

    def set_channel_voltage(self, voltage, channel=2):
        """
        Select channel and set voltage value

        Args:
            channel: Channel number, string format, options: 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3
            voltage: Voltage value, string format, unit: V
        """
        command = 'VOLT ' + str(voltage) + ', ' + '(@' + str(channel) + ')' # format example: VOLT 1, (@1)
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ', voltage: ' + str(voltage) + 'V')
        self.check_error()

    def select_channel(self, channel):
        """
        Select the output to be programmed

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3
        """
        command = 'INST ' + 'CH' + str(channel) # format example: INST CH1
        self.control.write(command)
        L.debug(self.name + ' select channel:' + str(channel))
        self.check_error()

    def channel_on(self, channel=2):
        """
        Set channel output on

        Args:
            channel: Channel number, string format, options: 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3
        """
        command = 'OUTP ON,(@' + str(channel) + ')' # format example: OUTP ON,(@1)/ OUTP ON,(@1,3)
        self.control.write(command)
        L.debug(self.name + ' channel: ' + str(channel) + ' ON')
        self.check_error()

    def channel_off(self, channel=2):
        """
        Set channel output off

        Args:
            channel: Channel number, string format, options: 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3
        """
        command = 'OUTP OFF,(@' + str(channel) + ')' # format example: OUTP ON,(@1)/ OUTP ON,(@1,3)
        self.control.write(command)
        L.debug(self.name + ' channel: ' + str(channel) + ' OFF')
        self.check_error()

    def query_channel_current(self, channel=2):
        """
        Return current of channel

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3

        Returns:
            result: Current value of specific channel, unit: A
        """
        command = 'MEAS:CURR? ' + 'CH' + str(channel)  # format example: MEAS:CURR? CH1
        result = eval(self.control.query(command))
        L.debug(self.name + ' channel: ' + str(channel) + ', current: ' + str(result) + 'A')
        self.check_error()

        return result

    def query_channel_voltage(self, channel=2):
        """
        Return voltage of channel

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3

        Returns:
            result: Voltage value of specific channel, unit: V
        """
        command = 'MEAS:VOLT? ' + 'CH' + str(channel)  # format example: MEAS:VOLT? CH1
        result = eval(self.control.query(command))
        L.debug(self.name + ' channel: ' + str(channel) + ', voltage: ' + str(result) + 'V')
        self.check_error()

        return result

    def enter_independent_mode(self):
        """
        Enter power supply's independent mode
        Positive: CH2+ and CH3+, Negative: CH2- and CH3-.
        """
        command = 'OUTP:PAIR OFF'
        self.control.write(command)
        L.debug(self.name + ' enter independent mode')
        self.check_error()

    def enter_series_mode(self):
        """
        Enter power supply's series mode, voltage could be up to 50V.
        Positive: CH2+, Negative: CH3-.
        """
        command = 'OUTP:PAIR SER'
        self.control.write(command)
        L.debug(self.name + ' enter series mode')
        self.check_error()

    def enter_parallel_mode(self):
        """
        Enter power supply's parallel mode, current could be up to 2A.
        Positive: CH2+, Negative: CH2-.
        """
        command = 'OUTP:PAIR PAR'
        self.control.write(command)
        L.debug(self.name + ' enter parallel mode')
        self.check_error()

    def enter_tracking_mode(self):
        """
        Enter power supply's tracking mode, voltage settings of CH2 and CH3 are tracked.
        Positive: CH2+ and CH3+, Negative: CH2- and CH3-.
        """
        command = 'OUTP:PAIR TRAC'
        self.control.write(command)
        L.debug(self.name + ' enter tracing mode')
        self.check_error()

    def query_channel_all(self, channel=2):
        """
        Return voltage and current of channel

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3

        Returns:
            result: Voltage value of specific channel, unit: V
        """
        command = 'MEAS:VOLT? ' + 'CH' + str(channel)  # format example: MEAS:VOLT? CH1
        voltage = eval(self.control.query(command))

        command = 'MEAS:CURR? ' + 'CH' + str(channel)  # format example: MEAS:CURR? CH1
        current = eval(self.control.query(command))
        L.debug(self.name + ' channel: ' + str(channel) + ', voltage: ' + str(voltage) + 'V' + ', current: ' + str(current) + 'A')
        self.check_error()

        return voltage, current

    def enable_remote(self):
        """
        Enter remote mode, commands are enabled
        """
        command = 'SYST:REM'
        self.control.write(command)
        L.debug(self.name + ' enable remote command')
        self.check_error()
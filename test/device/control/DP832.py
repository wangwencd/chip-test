# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/11/15 16:56
File: DP832.py
"""
import logging
from test.device.control.B2912A import B2912A

L = logging.getLogger('Main')

class DP832(B2912A):
    """
    DP832 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DP832'
        super(DP832).__init__()

    def check_error(self):
        """
        Read the most recent error.
        """
        command = 'SYSTem:ERRor?'
        result = self.control.query(command)
        L.info('Error result: ' + result)

    def set_channel_voltage_current(self, voltage, current, channel=2):
        """
        Select channel and set voltage and current value

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3
            voltage: Voltage value, string format, unit: V
            current: Current value, string format, unit: A
        """
        command = ':APPL ' + 'Ch' + str(channel) + ',' + str(voltage) + ',' + str(current) # format example: :APPL Ch1,5,1
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
        command = 'SOUR' + str(channel) + ':CURR ' + str(current)  # format example: SOUR1:CURR 1
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
        command = 'SOUR' + str(channel) + ':VOLT ' + str(voltage)  # format example: SOUR1:VOLT 1
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ', voltage: ' + str(voltage) + 'V')
        self.check_error()

    def select_channel(self, channel):
        """
        Select the output to be programmed

        Args:
            channel: Channel number, string format, 3 options: 1 / 2 / 3
        """
        command = ':INST ' + 'CH' + str(channel)  # format example: INST CH1
        self.control.write(command)
        L.debug(self.name + ' select channel:' + str(channel))
        self.check_error()

    def channel_on(self, channel=2):
        """
        Set channel output on

        Args:
            channel: Channel number, string format, options: 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3
        """
        command = ':OUTP CH' + str(channel) + ',ON'  # format example: OUTP ON,(@1)/ OUTP ON,(@1,3)
        self.control.write(command)
        L.debug(self.name + ' channel: ' + str(channel) + ' ON')
        self.check_error()

    def channel_off(self, channel=2):
        """
        Set channel output off

        Args:
            channel: Channel number, string format, options: 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3
        """
        command = ':OUTP CH' + str(channel) + ',OFF'  # format example: OUTP ON,(@1)/ OUTP ON,(@1,3)
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
        command = ':MEAS:CURR? ' + 'CH' + str(channel)  # format example: MEAS:CURR? CH1
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

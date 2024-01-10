# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/12 11:41
File: flow_E36312A.py
"""
import logging
from test.device.control.E36312A import E36312A
import re

L = logging.getLogger('Main')

class Flow_E36312A(E36312A):
    """
    Control flow of E36312A
    """
    def __init__(self, cls):
        self.control = cls
        super(Flow_E36312A, self).__init__(cls)

    def prepare(self, condition):
        """
        Prepare instrument for test

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.CLS()
        self.enable_remote()

        return condition

    def set(self, condition):
        """
        Set voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = str(condition.test_info['Channel'])
        voltage = condition.test_info['Voltage']
        current = condition.test_info['Current']

        if channel == '1' or channel == '2' or channel == '3':
            self.enter_independent_mode()
            self.set_channel_voltage_current(voltage, current, channel=channel)

        elif re.search('2\+3', channel) is not None:
            self.enter_series_mode()
            self.set_channel_voltage_current(voltage, current)

        elif re.search('2\|3', channel) is not None:
            self.enter_parallel_mode()
            self.set_channel_voltage_current(voltage, current)

        return condition

    def measure(self, condition):
        """
        Measure voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = str(condition.measurement_info['Channel'])

        if channel == '1' or channel == '2' or channel == '3':
            voltage, current = self.query_channel_all(channel)

        elif re.search('(2\+3)|(2\|3)', channel) is not None:
            voltage, current = self.query_channel_all()

        condition.measurement_info['Voltage'] = voltage
        condition.measurement_info['Current'] = current

        return condition

    def on(self, condition):
        """
        Set channel on

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = str(condition.test_info['Channel'])

        if channel == '1' or channel == '2' or channel == '3':
            self.channel_on(channel=channel)

        elif re.search('(2\+3)|(2\|3)', channel) is not None:
            self.channel_on()

        return condition

    def off(self, condition):
        """
        Set channel off

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = str(condition.test_info['Channel'])

        if channel == '1' or channel == '2' or channel == '3':
            self.channel_off(channel=channel)

        elif re.search('(2\+3)|(2\|3)', channel) is not None:
            self.channel_off()

        return condition

    def close(self, condition):
        """
        Communication close

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.close_all()

        return condition

    def set_voltage(self, condition):
        """
        Set voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = str(condition.test_info['Channel'])
        voltage = condition.test_info['Voltage']

        if channel == '1' or channel == '2' or channel == '3':
            self.enter_independent_mode()
            self.set_channel_voltage(voltage, channel=channel)

        elif re.search('2\+3', channel) is not None:
            self.enter_series_mode()
            self.set_channel_voltage(voltage)

        elif re.search('2\|3', channel) is not None:
            self.enter_parallel_mode()
            self.set_channel_voltage(voltage)

        return condition

    def set_current(self, condition):
        """
        Set current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = str(condition.test_info['Channel'])
        current = condition.test_info['Current']

        if channel == '1' or channel == '2' or channel == '3':
            self.enter_independent_mode()
            self.set_channel_current(current, channel=channel)

        elif re.search('2\+3', channel) is not None:
            self.enter_series_mode()
            self.set_channel_current(current)

        elif re.search('2\|3', channel) is not None:
            self.enter_parallel_mode()
            self.set_channel_current(current)

        return condition


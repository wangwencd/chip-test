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
        self.set_channel_voltage_current(voltage, current, channel=channel)

        return condition

    def measure(self, condition):
        """
        Measure voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        try:
            channel = str(condition.measurement_info['Channel'])
        except:
            channel = str(condition.test_info['Channel'])
        voltage, current = self.query_channel_all(channel)

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
        self.channel_on(channel=channel)

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
        self.channel_off(channel=channel)

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
        self.set_channel_voltage(voltage, channel=channel)

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

        self.set_channel_current(current, channel=channel)

        return condition

    def enter_independent(self, condition):
        """
        Enter independent mode

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.enter_independent_mode()

        return condition

    def enter_series(self, condition):
        """
        Enter series mode , channel 2+3

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.enter_series_mode()

        return condition

    def enter_parallel(self, condition):
        """
        Enter parallel mode , channel 2|3

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.enter_parallel_mode()

        return condition

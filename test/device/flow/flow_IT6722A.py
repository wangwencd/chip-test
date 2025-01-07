# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/7 11:15
File: flow_IT6722A.py
"""
import logging
from test.device.control.IT6722A import IT6722A

L = logging.getLogger('Main')

class Flow_IT6722A(IT6722A):
    """
    Control flow of IT6722A
    """
    def __init__(self, cls, name=None):
        self.name = name if name else 'IT6722A'
        self.control = cls
        super(Flow_IT6722A, self).__init__(cls, self.name)

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
        voltage = condition.test_info['Voltage']
        current = condition.test_info['Current']
        self.set_channel_voltage_current(voltage=voltage, current=current)

        return condition

    def measure(self, condition):
        """
        Measure voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage, current = self.query_all()

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
        voltage = condition.test_info['Voltage']
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
        current = condition.test_info['Current']
        self.set_channel_current(current)

        return condition

    def measure_voltage(self, condition):
        """
        Measure voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage = self.query_voltage()
        condition.measurement_info['Voltage'] = voltage

        return condition

    def measure_current(self, condition):
        """
        Measure current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        current = self.query_current()
        condition.measurement_info['Current'] = current

        return condition

    def measure_power(self, condition):
        """
        Measure power

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        power = self.query_power()
        condition.measurement_info['Power'] = power

        return condition

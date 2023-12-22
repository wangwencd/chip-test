# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/12 11:31
File: flow_IT8811.py
"""
import logging
from test.device.control.IT8811 import IT8811

L = logging.getLogger('Main')

class Flow_IT8811(IT8811):
    """
    Control flow of IT8811
    """
    def __init__(self, cls):
        self.control = cls
        super(Flow_IT8811, self).__init__(cls)

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
        self.enter_CV_mode()

        voltage = condition.test_info['Voltage']
        self.set_CV_mode_voltage(voltage)

        current = condition.test_info['Current']
        self.set_CV_mode_max_current(current)

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
        self.set_CV_mode_voltage(voltage)

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
        self.set_CV_mode_max_current(current)

        return condition
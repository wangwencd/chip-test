# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/30 16:37
File: flow_DL11B.py
"""
import logging
from test.device.control.DL11B import DL11B

L = logging.getLogger('Main')

class Flow_DL11B(DL11B):
    """
    Control flow of DL11B
    """
    def __init__(self, cls):
        self.control = cls
        super(Flow_DL11B, self).__init__(cls)

    def prepare(self, condition):
        """
        Prepare instrument for test

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.change_resolution(0.1)
        if 'Temperature_Measurement_Compensation' in condition.test_info.keys():
            self.write_temperature_compensation(condition.test_info['Temperature_Measurement_Compensation'])
        temperature_compensation = self.query_temperature_compensation()

        return condition

    def set(self, condition):
        """
        Set voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        return condition

    def measure(self, condition):
        """
        Measure voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.measurement_info['Temperature'] = self.query_temperature()

        return condition

    def on(self, condition):
        """
        Set channel on

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        return condition

    def off(self, condition):
        """
        Set channel off

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

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
# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/11/16 10:30
File: flow_DP832.py
"""
import logging
from test.device.control.DP832 import DP832
from test.device.flow.flow_E36312A import Flow_E36312A

L = logging.getLogger('Main')

class Flow_DP832(DP832, Flow_E36312A):
    """
    Control flow of DP832
    """
    def __init__(self, cls):
        super(Flow_DP832, self).__init__(cls)

    def set(self, condition):
        """
        Set voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = condition.test_info['Channel']
        voltage = condition.test_info['Voltage']
        current = condition.test_info['Current']
        self.set_channel_voltage_current(voltage, current, channel=channel)

        return condition

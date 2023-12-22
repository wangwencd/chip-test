# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/10/17 13:48
File: flow_DG1062Z.py
"""
import logging
from test.device.control.DG1062Z import DG1062Z

L = logging.getLogger('Main')

class Flow_DG1062Z(DG1062Z):
    """
    Control flow of DG1062Z
    """
    def __init__(self, cls):
        self.control = cls
        super().__init__(cls)

    def prepare(self, condition):
        """
        Prepare instrument for test

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.CLS()

        return condition

    def set_channel_sin(self, condition):
        """
        Set channel to be SIN waveform

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        frequency = condition.test_info['Frequency']
        amplitude = condition.test_info['Amplitude']
        offset = condition.test_info['Offset']
        self.set_channel_sin_parameter(frequency=frequency, amplitude=amplitude, offset=offset)

        return condition

    def set_channel_squ(self, condition):
        """
        Set channel to be squal waveform

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        frequency = condition.test_info['Frequency']
        amplitude = condition.test_info['Amplitude']
        offset = condition.test_info['Offset']
        self.set_channel_squ_parameter(frequency=frequency, amplitude=amplitude, offset=offset)

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
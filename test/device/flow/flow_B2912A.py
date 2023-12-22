# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/18 10:04
File: flow_B2912A.py
"""
import logging

from test.device.control.B2912A import B2912A

L = logging.getLogger('Main')

class Flow_B2912A(B2912A):
    """
    Control flow of B2912A
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
        self.enable_auto_range_for_voltage_measurement()
        self.enable_auto_range_for_current_measurement()
        # self.select_output_off_state_HIMP()
        self.enter_CV_mode()
        self.enable_auto_range_for_voltage_setting()
        self.enable_auto_range_for_current_setting()

        return condition

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
        self.set_CV_mode_voltage(voltage, channel=channel)

        current = condition.test_info['Current']
        self.set_CV_mode_max_current(current, channel=channel)

        return condition

    def measure(self, condition):
        """
        Measure voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = condition.test_info['Channel']
        voltage, current = self.query_all(channel=channel)

        condition.measurement_info['Voltage'] = voltage
        condition.measurement_info['Current'] = current

        return condition

    def measure_voltage(self, condition):
        """
        Measure voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = condition.test_info['Channel']
        voltage = self.query_voltage(channel=channel)
        condition.measurement_info['Voltage'] = voltage

        return condition

    def on(self, condition):
        """
        Set channel on

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = condition.test_info['Channel']
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
        channel = condition.test_info['Channel']
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
        channel = condition.test_info['Channel']
        voltage = condition.test_info['Voltage']
        self.set_CV_mode_voltage(voltage, channel=channel)

        return condition

    def set_current(self, condition):
        """
        Set current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        channel = condition.test_info['Channel']
        current = condition.test_info['Current']
        self.set_CV_mode_max_current(current, channel=channel)

        return condition

    def enter_cc(self, condition):
        channel = condition.test_info['Channel']
        self.enter_CC_mode(channel=channel)

        return condition

    def set_cc_parameter(self, condition):
        channel = condition.test_info['Channel']
        current = condition.test_info['Current']
        voltage = condition.test_info['Voltage']
        self.set_CC_mode_current(current, channel=channel)
        self.set_CC_mode_max_voltage(voltage, channel=channel)

        return condition

    def set_cc_current(self, condition):
        channel = condition.test_info['Channel']
        current = condition.test_info['Current']
        self.set_CC_mode_current(current, channel=channel)

        return condition

    def set_speed(self, condition):
        speed = condition.test_info['Speed']
        self.set_measurement_speed(speed)

        return condition

    def set_cv_voltage_range(self, condition):
        channel = condition.test_info['Channel']
        range = condition.test_info['Range']
        self.set_CV_mode_voltage_range(channel=channel, range=range)

        return condition

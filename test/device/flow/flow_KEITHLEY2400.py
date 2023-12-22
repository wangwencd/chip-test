# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/11 9:42
File: flow_KEITHLEY2400.py
"""
import logging
from test.device.control.KEITHLEY2400 import KEITHLEY2400
L = logging.getLogger('Main')

class Flow_KEITHLEY2400(KEITHLEY2400):
    """
    Control flow of 2400
    """
    def __init__(self, cls):
        self.control = cls
        super(Flow_KEITHLEY2400, self).__init__(cls)

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
        self.select_output_off_state_HIMP()
        self.enter_CV_mode()
        self.enable_auto_range_for_voltage_setting()
        self.enable_auto_range_for_current_setting()
        self.enable_remote_sensing()

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
        self.set_CV_mode_voltage(voltage)

        current = condition.test_info['Current']
        self.set_CV_mode_max_current(current)

        try:
            measured_range = self.query_CV_mode_voltage_range()
            setting_range = condition.test_info['Charge_Voltage_Range']

            if measured_range < setting_range:
                self.set_CV_mode_voltage_range(setting_range)

        except:
            pass

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

        try:
            measured_range = self.query_CV_mode_voltage_range()
            setting_range = condition.test_info['Charge_Voltage_Range']

            if measured_range < setting_range:
                self.set_CV_mode_voltage_range(setting_range)

        except:
            pass

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
        self.set_CV_mode_current_range(current)
        self.set_CV_mode_max_current(current)

        try:
            measured_range = self.query_CV_mode_voltage_range()
            setting_range = condition.test_info['Charge_Voltage_Range']

            if measured_range < setting_range:
                self.set_CV_mode_voltage_range(setting_range)

        except:
            pass

        return condition

    def enable_remote_sensing_flow(self, condition):
        """
        Enter into remote sensing mode

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.enable_remote_sensing()

        return condition
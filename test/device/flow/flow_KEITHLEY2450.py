# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/25 14:24
File: flow_KEITHLEY2450.py
"""
import logging

from test.device.control.KEITHLEY2450 import KEITHLEY2450

L = logging.getLogger('Main')

class Flow_KEITHLEY2450(KEITHLEY2450):
    """
    Control flow of 2450
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
        voltage = condition.test_info['Voltage']
        self.set_CV_mode_voltage(voltage)

        try:
            measured_range = self.query_CV_mode_voltage_range()
            setting_range = float(condition.test_info['Charge_Voltage_Range'])

            if measured_range < setting_range:
                self.set_CV_mode_voltage_range(setting_range)

        except:
            pass

        current = condition.test_info['Current']
        # self.set_CV_mode_current_range(current)
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

        try:
            setting_range = condition.test_info['Charge_Voltage_Range']
            measured_range = self.query_CV_mode_voltage_range()

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
        self.set_CV_mode_current_range(current * 2)
        self.set_CV_mode_max_current(current)

        # try:
        #     measured_range = self.query_CV_mode_voltage_range()
        #     setting_range = condition.test_info['Charge_Voltage_Range']
        #
        #     if measured_range < setting_range:
        #         self.set_CV_mode_voltage_range(setting_range)
        #
        # except:
        #     pass

        return condition

    def enter_cc(self, condition):
        self.enter_CC_mode()

        return condition

    def enter_cv(self, condition):
        self.enter_CV_mode()

        return condition

    def set_cc_parameter(self, condition):
        current = condition.test_info['Current']
        voltage = condition.test_info['Voltage']
        self.set_CC_mode_current(current)
        self.set_CC_mode_max_voltage(voltage)

        return condition

    def set_cc_current(self, condition):
        current = condition.test_info['Current']
        self.set_CC_mode_current(current)

        return condition

    def enter_cv_4_wire(self, condition):
        self.enter_CV_mode_4_wire_mode()

        return condition

    def enter_cv_2_wire(self, condition):
        self.enter_CV_mode_2_wire_mode()

        return condition

    def enter_cc_4_wire(self, condition):
        self.enter_CC_mode_4_wire_mode()

        return condition

    def enter_cc_2_wire(self, condition):
        self.enter_CC_mode_2_wire_mode()

        return condition

    def enter_cr_4_wire(self, condition):
        self.enter_CR_mode_4_wire_mode()

        return condition

    def enter_cr_2_wire(self, condition):
        self.enter_CR_mode_2_wire_mode()

        return condition

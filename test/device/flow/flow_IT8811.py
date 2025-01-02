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
    def __init__(self, cls, name=None):
        self.name = name if name else 'IT8811'
        self.control = cls
        super(Flow_IT8811, self).__init__(cls, self.name)

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

    def enter_cc(self, condition):
        self.enter_CC_mode()

        return condition

    def enter_cv(self, condition):
        self.enter_CV_mode()

        return condition

    def enter_cr(self, condition):
        self.enter_CR_mode()

        return condition

    def enter_cw(self, condition):
        self.enter_CW_mode()

        return condition

    def set_cv_voltage(self, condition):
        """
        Set CV mode voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage = condition.test_info['Voltage']
        self.set_CV_mode_voltage(voltage)

        return condition

    def set_cv_current(self, condition):
        """
        Set CV mode current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        current = condition.test_info['Current']
        self.set_CV_mode_max_current(current)

        return condition

    def set_cc_voltage(self, condition):
        """
        Set CC mode voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage = condition.test_info['Voltage']
        self.set_CC_mode_max_voltage(voltage)

        return condition

    def set_cc_current(self, condition):
        """
        Set CC mode current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        current = condition.test_info['Current']
        self.set_CC_mode_current(current)

        return condition

    def set_cr_voltage(self, condition):
        """
        Set CR mode voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage = condition.test_info['Voltage']
        self.set_CR_mode_max_voltage(voltage)

        return condition

    def set_cr_resistance(self, condition):
        """
        Set CR mode resistance

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        resistance = condition.test_info['Resistance']
        self.set_CR_mode_resistance(resistance)

        return condition

    def set_cw_voltage(self, condition):
        """
        Set CW mode voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage = condition.test_info['Voltage']
        self.set_CW_mode_max_voltage(voltage)

        return condition

    def set_cw_power(self, condition):
        """
        Set CW mode power

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        power = condition.test_info['Power']
        self.set_CW_mode_power(power)

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

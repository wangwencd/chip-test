# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/5/9 11:34
File: flow_DMM7510.py
"""
import logging
from test.device.control.DMM7510 import DMM7510, function_list

L = logging.getLogger('Main')

class Flow_DMM7510(DMM7510):
    """
    Control flow of DMM7510
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

    def measure(self, condition):
        """
        Measure voltage and current

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        voltage, current = self.query_voltage_current()

        condition.measurement_info['Voltage'] = voltage
        condition.measurement_info['Current'] = current

        return condition

    def measure_one(self, condition):
        """
        Measure one parameter from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.measurement_info['Option']

        for key, value in function_list.items():

            if option == key:
                result = self.query_one_measurement(option=option)
                condition.measurement_info[value[2]] = result
                break

        return condition

    def set_one_speed(self, condition):
        """
        Set one measurement speed from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        speed = condition.test_info['Speed']

        for key, value in function_list.items():

            if option == key:
                self.set_one_measurement_speed(option=option, speed=speed)
                break

        return condition

    def set_one_average_count(self, condition):
        """
        Set one average count from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        num = condition.test_info['Count']

        for key, value in function_list.items():

            if option == key:
                self.set_one_measurement_average_count(option=option, num=num)
                break

        return condition

    def set_one_average_control(self, condition):
        """
        Set one average control type from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        type = condition.test_info['Type']

        for key, value in function_list.items():

            if option == key:
                self.set_one_measurement_average_control(option=option, type=type)
                break

        return condition

    def set_one_average(self, condition):
        """
        Set one function average on/off from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        flag = condition.test_info['Flag']

        for key, value in function_list.items():

            if option == key:
                self.set_one_measurement_average(option=option, flag=flag)
                break

        return condition

    def set_one_autorange(self, condition):
        """
        Set one function auto range on/off from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        flag = condition.test_info['Flag']

        for key, value in function_list.items():

            if option == key:
                self.set_one_measurement_autorange(option=option, flag=flag)
                break

        return condition

    def set_one_autozero(self, condition):
        """
        Set one function auto zero on/off from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        flag = condition.test_info['Flag']

        for key, value in function_list.items():

            if option == key:
                self.set_one_measurement_autozero(option=option, flag=flag)
                break

        return condition

    def set_one_impedance(self, condition):
        """
        Set one function auto zero on/off from instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        option = condition.test_info['Option']
        choice = condition.test_info['Choice']

        for key, value in function_list.items():

            if option == key:
                self.set_one_input_impedance(option=option, choice=choice)
                break

        return condition

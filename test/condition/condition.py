# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/26 11:47
File: condition.py
"""
import re
import numpy as np
from copy import deepcopy

class Condition(object):
    """
    Test condition information class
    """
    def __init__(self):
        """
        Init function, initialize parameters
        """
        """Function"""
        self.func = None # Function of process

        """Path"""
        self.config_path = None # Path aimed at configuration file
        self.saving_path = None # Path aimed at saving results

        """File"""
        self.file = None # File which is stored whole configuration

        """Instrument summary"""
        self.Class = {} # Instrument class summary

        """Test information summary"""
        self.test_info = {} # Test information of each command

        """Measurement information summary"""
        self.measurement_info = {} # Result of each measuring

        """Output information summary"""
        self.output_info = {
            'TTime': np.array([]),
            'Temperature': np.array([]),
            'VITime': np.array([]),
            'Voltage': np.array([]),
            'Current': np.array([]),
        }

        """Flag"""
        self.test_flag = False
        self.test_VI_flag = False
        self.test_T_flag = False
        self.measurement_flag = False
        self.output_flag = True
        self.sleep_flag = False

    def reset_test_info(self):
        """
        Reset test info dict to empty
        """
        self.test_info = {}

    def reset_measurement_info(self):
        """
        Reset measurement info dict to empty
        """
        self.measurement_info = {}

    def reset_output_info(self):
        """
        Reset output info dict to empty
        """
        self.output_info = {
            'TTime': np.array([]),
            'Temperature': np.array([]),
            'VITime': np.array([]),
            'Voltage': np.array([]),
            'Current': np.array([]),
        }

    def update_temerature(self, temperature: float):
        """
        Update temperature from measurement into output

        Args:
            temperature: Temperature value, unit: ℃
        """
        self.output_info['Temperature'] = np.append(self.output_info['Temperature'], temperature)

    def update_voltage(self, voltage: float):
        """
        Update voltage from measurement into output

        Args:
            voltage: Voltage value, unit: V
        """
        self.output_info['Voltage'] = np.append(self.output_info['Voltage'], voltage)

    def update_current(self, current: float):
        """
        Update current from measurement into output

        Args:
            current: Current value, unit: A
        """
        self.output_info['Current'] = np.append(self.output_info['Current'], current)

    def update_voltage_and_current(self, voltage: float, current: float):
        """
        Update voltage and current from measurement into output

        Args:
            voltage: Voltage value, unit: V
            current: Current value, unit: A
        """
        self.output_info['Voltage'] = np.append(self.output_info['Voltage'], voltage)
        self.output_info['Current'] = np.append(self.output_info['Current'], current)

    def update_T_time(self, time: float):
        """
        Update temperature measurement time into output

        Args:
            time: Temperature measurement time, unit: s
        """
        self.output_info['TTime'] = np.append(self.output_info['TTime'], time)

    def update_VI_time(self, time: float):
        """
        Update voltage and current measurement time into output

        Args:
            time: Voltage and current measurement time, unit: s
        """
        self.output_info['VITime'] = np.append(self.output_info['VITime'], time)

    def return_config_path(self):
        """
        Return config path

        Returns:
            config_path: Config path
        """
        return deepcopy(self.config_path)

    def return_saving_path(self):
        """
        Return saving path

        Returns:
            saving_path: Saving file path
        """
        return deepcopy(self.saving_path)

    def return_test_info(self):
        """
        Return test information

        Returns:
            test_info: Test information summary
        """
        return deepcopy(self.test_info)

    def return_measurement_info(self):
        """
        Return measurement information

        Returns:
            measurement_info: Measurement information summary
        """
        return deepcopy(self.measurement_info)

    def return_output_info(self):
        """
        Return output information

        Returns:
            output_info: Output information summary
        """
        return deepcopy(self.output_info)

    # def parse(self):
    #     """
    #     Parse configuration file
    #     """
    #     for key, value in self.test_info.items():
    #
    #         for i in re.split(',|;|{|}', str(value)): # Split values according to specific symbol
    #
    #             if re.search('.+:.+', i) != None: # Find real command in values
    #                 self.test_info[str(i.split(':')[0])] = str(i.split(':')[1])
    #
    #         if re.search('.+:.+', str(value)) != None: # Check if there is real command in this value, delete it if existing
    #             del self.test_info[key]
    #
    #     self.test_info = self.test_info.to_dict()






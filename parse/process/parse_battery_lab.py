# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/5 13:49
File: parse_battery_lab.py
"""
import numpy as np
from parse.file.file_operation import File_Operation

class Parse_battery_Lab:

    @staticmethod
    def parse(condition):
        """
        Get condition file from path, and convert into dict

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        file = File_Operation.find_file(condition.config_path, 'ini') # Find all .ini file from config path
        condition.file = File_Operation.get_dataframe_from_first(file) # Get .ini content from first file list
        condition.test_info = condition.file.iloc[0].to_dict()
        condition = Parse_battery_Lab.convert_unit(condition)

        condition.output_info['Flag'] = np.array([])
        condition.current_flag = 1
        condition.test_VI_flag = True
        condition.test_T_flag = True
        condition.measurement_flag = True

        return condition

    @staticmethod
    def convert_unit(condition):
        """
        Convert the unit from mV to V, mA to A in .ini file content

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Charge_Voltage'] = float(condition.test_info['Charge_Voltage']) / 1000
        condition.test_info['Charge_Voltage_Range'] = float(condition.test_info['Charge_Voltage_Range']) / 1000
        condition.test_info['Charge_Current'] = float(condition.test_info['Charge_Current']) / 1000
        condition.test_info['Relax_Current'] = float(condition.test_info['Relax_Current']) / 1000
        condition.test_info['Discharge_Voltage'] = float(condition.test_info['Discharge_Voltage']) / 1000
        condition.test_info['Discharge_Current_1'] = float(condition.test_info['Discharge_Current_1']) / 1000
        condition.test_info['Discharge_Current_2'] = float(condition.test_info['Discharge_Current_2']) / 1000
        condition.test_info['Discharge_Current_3'] = float(condition.test_info['Discharge_Current_3']) / 1000

        return condition
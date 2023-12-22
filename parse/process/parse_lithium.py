# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/12/22 15:52
File: parse_lithium.py
"""
import re
import numpy as np
from parse.file.file_operation import File_Operation

class Parse_Lithium:

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

        condition.output_info = {
            'Time': np.array([]),
            'Temperature': np.array([]),
            'Voltage': np.array([]),
            'Current': np.array([]),
            'Data': np.array([]),
        }
        condition.test_T_flag = True
        condition.test_VI_flag = True

        name = condition.func_name

        if re.search('accuracy|deviation', name, re.I) is not None:
            condition = Parse_Lithium.parse_accuracy(condition)

        else:
            condition = Parse_Lithium.parse_dnl(condition)

        return condition

    @staticmethod
    def parse_accuracy(condition):
        """
        Accuracy test parse preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Power_Voltage'] = float(condition.test_info['Power_Voltage']) / 1000
        condition.test_info['Power_Current'] = float(condition.test_info['Power_Current']) / 1000
        condition.test_info['Start_Voltage'] = float(condition.test_info['Start_Voltage']) / 1000
        condition.test_info['Step_Voltage'] = float(condition.test_info['Step_Voltage']) / 1000
        condition.test_info['End_Voltage'] = float(condition.test_info['End_Voltage']) / 1000
        condition.test_info['Start_Current'] = float(condition.test_info['Start_Current']) / 1000

        return condition

    @staticmethod
    def parse_dnl(condition):
        """
        DNL test parse preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Power_Voltage'] = float(condition.test_info['Power_Voltage']) / 1000
        condition.test_info['Power_Current'] = float(condition.test_info['Power_Current']) / 1000

        return condition
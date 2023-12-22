# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/6/27 19:38
File: parse_jupiter.py
"""
import re
import numpy as np
from parse.file.file_operation import File_Operation

class Parse_Jupiter:

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

        condition.test_T_flag = True
        condition.test_VI_flag = True

        name = condition.func_name

        if re.search('ramp_multi', name, re.I) is not None:
            condition = Parse_Jupiter.parse_ramp_multi(condition)

        elif re.search('ramp', name, re.I) is not None:
            condition = Parse_Jupiter.parse_ramp(condition)

        elif re.search('noise', name, re.I) is not None:
            condition = Parse_Jupiter.parse_ramp_multi(condition)

        return condition

    @staticmethod
    def parse_ramp(condition):
        """
        DNL test parse preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.output_info = {
            'Time': np.array([]),
            'Temperature': np.array([]),
            'Voltage': np.array([]),
            'Current': np.array([]),
            'Data': np.array([]),
        }

        return condition

    @staticmethod
    def parse_ramp_multi(condition):
        """
        DNL test parse preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.output_info = {
            'Time': np.array([]),
            'Temperature': np.array([]),
            'Voltage': np.array([]),
            'Current': np.array([]),
            'Data0': np.array([]),
            'Data1': np.array([]),
            'Data2': np.array([]),
            'Data3': np.array([]),
        }

        return condition
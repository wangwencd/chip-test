# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/10/8 17:42
File: parse_natrium.py
"""
import re
import numpy as np
from parse.file.file_operation import File_Operation

class Parse_Natrium:

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

        if re.search('ramp', name, re.I) is not None:
            condition = Parse_Natrium.parse_ramp(condition)

        elif re.search('noise', name, re.I) is not None:
            condition = Parse_Natrium.parse_ramp(condition)

        elif re.search('temperature', name, re.I) is not None:
            condition = Parse_Natrium.parse_ramp(condition)

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
            'Set_Voltage': np.array([]),
            'Data': np.array([]),
        }
        if 'Temperature_Setting_Flag' in condition.test_info.keys():
            condition.test_info['Temperature_Setting_Flag'] = bool(int(condition.test_info['Temperature_Setting_Flag']))
        else:
            condition.test_info['Temperature_Setting_Flag'] = True

        if 'Power_Setting_Flag' in condition.test_info.keys():
            condition.test_info['Power_Setting_Flag'] = bool(int(condition.test_info['Power_Setting_Flag']))
        else:
            condition.test_info['Power_Setting_Flag'] = True

        if 'ADC_Setting_Flag' in condition.test_info.keys():
            condition.test_info['ADC_Setting_Flag'] = bool(int(condition.test_info['ADC_Setting_Flag']))
        else:
            condition.test_info['ADC_Setting_Flag'] = True

        if 'ADC_Measurement_Flag' in condition.test_info.keys():
            condition.test_info['ADC_Measurement_Flag'] = bool(int(condition.test_info['ADC_Measurement_Flag']))
        else:
            condition.test_info['ADC_Measurement_Flag'] = True

        if 'Control_Setting_Flag' in condition.test_info.keys():
            condition.test_info['Control_Setting_Flag'] = bool(int(condition.test_info['Control_Setting_Flag']))
        else:
            condition.test_info['Control_Setting_Flag'] = True

        if 'Data_Average_Flag' in condition.test_info.keys():
            condition.test_info['Data_Average_Flag'] = bool(int(condition.test_info['Data_Average_Flag']))
        else:
            condition.test_info['Data_Average_Flag'] = True

        return condition

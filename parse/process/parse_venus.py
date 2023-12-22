# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/5/5 11:12
File: parse_venus.py
"""
from parse.file.file_operation import File_Operation

class Parse_Venus:

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

        return condition


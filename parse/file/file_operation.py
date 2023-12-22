# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/19 16:28
File: file_operation.py
"""
import os
import re
import logging
from configparser import ConfigParser
from pandas import read_csv, read_excel, DataFrame

L = logging.getLogger('Main')

class File_Operation(object):
    """
    File operations class
    """

    @staticmethod
    def create_file(path):
        """
        Judge if there is the file, create file when not existing.

        Args:
            path: File path
        """
        try:
            path = path.replace('\\', '/')

            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)

        except:
            L.error('Path is not right!')
            raise IsADirectoryError

    @staticmethod
    def find_file(path, ext) -> list:
        """
        Find all files with specific type

        Args:
            path: Top-level path
            ext: File extension

        Returns:
            file_list: List of file path
        """
        file_list = []
        try:
            for file in os.listdir(path): # Find all file and dir in the path
                file_path = os.path.join(path, file) # Make up full path of every member

                if os.path.isfile(file_path): # If it is the file

                    if re.search(ext + '$', file) != None: # Judge if it is the specific type
                        file_list.append(file_path)

                elif os.path.isdir(file_path): # If it is the dir
                    subfile_list = File_Operation.find_file(file_path, ext) # Enter next judgment
                    file_list = file_list + subfile_list

        except:
            L.error('Path is not right!')
            raise IsADirectoryError

        return file_list

    @staticmethod
    def get_dataframe_from_first(file_list) -> DataFrame:
        """
        Open first path from file list and turn it into dataframe.

        Args:
            file_list: File list, list format

        Returns:
            file: File content
        """
        if re.search('\.csv', file_list[0]) != None: # .csv file
            file = read_csv(file_list[0])

        elif re.search('\.xls(x|m|)', file_list[0]) != None: # .xlsx file
            file = read_excel(file_list[0])

        elif re.search('\.ini', file_list[0]) != None: # .ini file
            config = ConfigParser()
            config.optionxform = lambda option: option
            config.read(file_list[0], encoding='utf-8')
            temp = {}
            for index in range(len(config.items(config.sections()[0]))):
                temp[config.items(config.sections()[0])[index][0]] = config.items(config.sections()[0])[index][1]
            file = DataFrame(temp, index=[0])

        return file

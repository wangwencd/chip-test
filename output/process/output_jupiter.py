# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/7 15:25
File: output_jupiter.py
"""
import numpy as np
from output.result.result_output import Result_Output
from output.process.output_battery_lab import Output_Battery_Lab

class Output_Jupiter(Output_Battery_Lab):
    """Jupiter project output class """

    @staticmethod
    def output(condition):
        """
        Get output information from condition and output into a csv file

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        max_length = 0 # Max length of output info values
        header = '' # Header info

        """Get max length"""
        for value in condition.output_info.values():
            max_length = len(value) if len(value) > max_length else max_length
        data = np.empty(shape=(0, max_length)) # Generate an empty array, array size is the max length of output info

        """Get completed data and header info"""
        for key, value in condition.output_info.items():
            header = header + ', ' if header != '' else header
            data = np.vstack(
                (data, np.append(value, np.full([1, max_length - len(value)], np.nan)))
            ) # Complete data with NAN
            header = header + key # Complete header info
        data = np.transpose(data) # Transpose data array

        if max_length == 0: # If there is no data, don't generate result file
            return condition

        if condition.saving_path != None and condition.saving_path != '':
            Result_Output.to_csv(data, condition.saving_path, header=header,  length='8') # Save output info into a csv file

        else:
            Result_Output.to_csv(data, condition.config_path, header=header,  length='8') # Save output info into a csv file

        return condition
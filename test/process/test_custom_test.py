# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/22 9:53
File: test_custom_test.py
"""
import re
import numpy as np
import time
import logging
from test.device.flow.control_flow import Control_Flow
from parse.process.parse_custom_test import Parse_Custom_Test
from parse.multiprocess.queue import Q

L = logging.getLogger('Main')

class Test_Custom_Test(Control_Flow):
    """
    Custom test class
    """
    def __init__(self):
        super().__init__()

    def exec_func(self, condition):
        """
        Determine specific operation of instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        function_key = list(condition.test_info['Function'].keys())[0]  # Get key string from Function dict
        function_value = list(condition.test_info['Function'].values())[0]  # Get value string from Function dict
        condition.test_info.update(condition.test_info['Parameter'])  # Get test parameter from Parameter

        if function_key == 'nan':  # Function is empty
            return condition

        elif re.search('save', function_key, re.I) is not None:  # Function is saving data
            condition = self.exec_save(condition)

        elif function_value is None:  # Function has no function name
            condition = eval('self.' + function_key)(condition)  # run single function without function name

        else:  # Function has function name
            condition = eval('self.' + function_key)\
                (condition, function_value)  # run single function with function name
        return condition

    def test(self, condition):
        """
        Whole SOP of custom test, including all steps

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        step = int(condition.file.iloc[0]['Step'])
        max_step = int(condition.file.iloc[-1]['Step'])  # Get max step number from test file

        while condition.test_flag:
            condition.start_time = time.time()
            condition.condition_flag = True

            while condition.condition_flag:
                Q.put(round((step/max_step) * 100, 0))  # calculate progress and send to queue
                condition.test_info = (
                    condition.file.loc[condition.file['Step'] == step].iloc[-1]
                ).to_dict()  # Get test info according to target step, then convert into a dict

                if condition.test_info['Time'] == condition.test_info['Time']:  # Time sleep according to Time
                    time.sleep(float(condition.test_info['Time']))
                condition = self.exec_func(condition)
                condition = Parse_Custom_Test.parse_condition(condition)

                if condition.condition_flag:  # Judgements not satisfied
                    condition.reset_test_info()
                    continue

                if condition.test_info['Next'] != condition.test_info['Next']:  # Next is nan
                    step = int(condition.test_info['Step']) + 1

                else:  # Next has a target step.
                    step = int(condition.test_info['Next'])
                condition.test_info_temp.update(condition.test_info)
                condition.reset_test_info()

            if step > max_step:  # Last step
                break

        condition.test_flag = True
        return condition
    def exec_save(self, condition):
        """
        Save test_info or measurement_info data to output_info

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        number = str(condition.test_info.get('Number', ''))
        name = str(condition.test_info.get('Instrument', '')) + \
               str(condition.test_info.get('Info', '')) +\
               str(condition.test_info.get('Key', '')) + \
               number
        if name not in condition.output_info:  # Key not in output_info
            condition.output_info[name] = np.array([])  # Create empty array for Key

        if re.search('time', condition.test_info['Info'], re.I) is not None:
            condition.output_info[name] = np.append(
            condition.output_info[name],
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        )

        elif condition.test_info['Key'] is dict:  # Key is a dict
            if re.search('Measure', condition.test_info['Info'], re.I) is not None:
                condition.output_info[name] = np.append(
                    condition.output_info[name],
                    str(eval('condition.measurement_info')[condition.test_info['Key']][condition.test_info['Item']])
                )
            elif re.search('Test', condition.test_info['Info'], re.I) is not None:
                condition.output_info[name] = np.append(
                    condition.output_info[name],
                    str(eval('condition.test_info_temp')[condition.test_info['Key']][condition.test_info['Item']])
                )
        else:  # Key is not a dict
            if re.search('Measure', condition.test_info['Info'], re.I) is not None:
                condition.output_info[name] = np.append(
                    condition.output_info[name],
                    str(eval('condition.measurement_info')[condition.test_info['Key']])
                )
            elif re.search('Test', condition.test_info['Info'], re.I) is not None:
                condition.output_info[name] = np.append(
                    condition.output_info[name],
                    str(eval('condition.test_info_temp')[condition.test_info['Key']])
                )
        return condition

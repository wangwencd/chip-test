# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/22 9:53
File: test_custom_test.py
"""
import time
import logging
from test.device.flow.control_flow import Control_Flow
from parse.process.parse_custom_test import Parse_Custom_Test

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

        while True:
            condition.start_time = time.time()
            condition.condition_flag = True

            while condition.condition_flag:
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
                condition.reset_test_info()

            if step > max_step:  # Last step
                break

        condition.test_flag = False
        return condition

    def measure_VI_thread(self, condition):
        """
        Thread func of measuring vol and cur, could measure vol and cur cyclically, which is needed one thread to run.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        test_info = condition.return_test_info()  # Get measurement info from test info

        while condition.test_VI_flag:
            if condition.sleep_flag:
                time.sleep(3)
            condition.measurement_info = test_info
            condition = self.measure(condition)  # Measurement function
            condition.measurement_flag = True  # measuring voltage data updated
            condition.update_voltage_and_current(condition.measurement_info['Voltage'],
                                                 condition.measurement_info['Current'])  # Update vol and cur to output
            condition.update_VI_time(time.perf_counter())  # Update time of measuring vol and cur
            time.sleep(1)

        return condition

    def measure_T_thread(self, condition):
        """
        Thread func of measuring tem, could measure tem cyclically, which is needed one thread to run.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        test_info = condition.return_test_info()

        while condition.test_T_flag:
            condition.measurement_info = test_info
            condition = self.measure(condition)  # Measurement function
            condition.update_temerature(condition.measurement_info['Temperature'])  # Update tem to output
            condition.update_T_time(time.perf_counter())  # Update time of measuring tem
            time.sleep(1)

        return condition

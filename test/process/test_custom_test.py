# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/22 9:53
File: test_custom_test.py
"""
import re
import time
import logging

from parse.multiprocess.pool_thread import pool
from test.device.flow.control_flow import Control_Flow
from parse.process.parse_custom_test import Parse_Custom_Test

L = logging.getLogger('Main')

class Test_Custom_Test(Control_Flow):
    """
    Custom test class
    """
    def __init__(self):
        super().__init__()

    def determine_func(self, condition):
        """
        Determine specific operation of instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        function = condition.test_info['Function']  # Get function name from test info
        if re.match('pass', function, re.I) is not None:  # Pass this step
            return condition

        if re.match('open', function, re.I) is not None:  # Open instrument
            condition = self.open(condition)
            return condition

        elif re.match('prepare', function, re.I) is not None:  # Prepare instrument, such as enable remote, CLS
            condition = self.prepare(condition)
            return condition

        elif re.match('measure', function, re.I) is not None:  # Measure value of instrument

            if condition.test_info['Instrument'] != 'DL11B':
                future1 = pool.submit(self.measure_VI_thread, condition)

            if condition.test_info['Instrument'] == 'DL11B':
                future2 = pool.submit(self.measure_T_thread, condition)

            return condition

        elif re.match('set', function, re.I) is not None:  # Set instrument parameter
            condition = self.set(condition)
            return condition

        elif re.match('on', function, re.I) is not None:  # Put channel of instrument on
            condition = self.on(condition)
            return condition

        elif re.match('off', function, re.I) is not None:  # Put channel of instrument off
            condition = self.off(condition)
            return condition

        elif re.match('close', function, re.I) is not None:  # Close instrument
            condition.test_flag = False
            condition = self.close(condition)
            return condition

    def test(self, condition):
        """
        Whole SOP of custom test, including all steps

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        step = 0
        max_step = int(condition.file.iloc[-1]['Step'])

        while True:
            condition.test_info = condition.file.iloc[step]

            if condition.test_info['Time'] == condition.test_info['Time']:  # Time sleep according to Time
                time.sleep(float(condition.test_info['Time']))

            condition = self.determine_func(condition)
            condition = Parse_Custom_Test.get_condition(condition)

            if condition.test_info['Next'] == condition.test_info['Next']:
                step = int(condition.test_info['Next'])

            else:
                step = int(condition.test_info['Step']) + 1

            if step > max_step:
                break
            condition.reset_test_info()
            time.sleep(1)

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

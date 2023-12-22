# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/5/5 11:15
File: test_venus.py
"""
import copy
import re
import logging
import time
import traceback

from test.device.flow.control_flow import Control_Flow
from parse.file.reg_operation import Reg_Operation
from parse.multiprocess.pool_thread import pool

L = logging.getLogger('Main')

class Test_Venus(Control_Flow):
    """
    Venus project test class
    """
    def test(self, condition):
        """
        Venus test work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        name = condition.func_name

        if re.search('trim', name, re.I) is not None:
            condition = self.test_trim(condition)

        return condition

    def init_power_setting(self, condition):
        """
        Init power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
        condition.test_info['Communication'] = condition.test_info['Power_Communication']
        condition = self.open(condition)
        condition = self.prepare(condition)

        return condition

    def init_clock_setting(self, condition):
        """
        Init clock generating instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['Clock_Instrument']
        condition.test_info['Communication'] = condition.test_info['Clock_Communication']
        condition = self.open(condition)
        condition = self.prepare(condition)

        return condition

    def init_temperature_setting(self, condition):
        """
        Init temperature setting instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] \
            = condition.test_info['Temperature_Setting_Instrument']  # Temperature instrument name
        condition.test_info['Communication'] \
            = condition.test_info['Temperature_Setting_Communication']  # Temperature instrument communication method
        condition.test_info['Temperature'] = condition.test_info['Set_Temperature']
        condition = self.open(condition)  # Open instrument
        time.sleep(1)
        condition = self.prepare(condition)  # Prepare instrument
        time.sleep(1)
        condition = self.set(condition)
        time.sleep(1)
        condition = self.on(condition)  # Set instrument on
        time.sleep(1)
        condition = self.close(condition)
        L.info('Init temperature setting finished')

        return condition

    def stop_temperature_setting(self, condition):
        """
        Keep temperature normal value, then stop

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        normal_temperature = 25
        condition.test_info['Instrument'] \
            = condition.test_info['Temperature_Setting_Instrument']  # Temperature instrument name
        condition.test_info['Communication'] = condition.test_info['Temperature_Setting_Communication']
        condition.test_info['Temperature'] = normal_temperature
        condition = self.open(condition)  # Open instrument
        time.sleep(1)
        condition = self.prepare(condition)  # Prepare instrument
        time.sleep(1)
        condition = self.set(condition)
        time.sleep(1)
        condition = self.on(condition)  # Set instrument on
        time.sleep(1)
        condition = self.close(condition)
        condition.test_info['Set_Temperature'] = normal_temperature

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
        measurement_instrument = copy.deepcopy(test_info['Instrument'])
        measurement_period = float(copy.deepcopy(test_info['Measurement_Period']))
        if measurement_period < 2:
            measurement_period = 2

        while condition.test_T_flag:
            condition.measurement_info['Instrument'] = measurement_instrument
            condition = self.measure(condition)  # Measurement function
            time.sleep(measurement_period / 2)

        return condition

    def measure_VI_thread(self, condition):
        """
        Thread func of measuring vol & cur, could measure vol & cur cyclically, which is needed one thread to run.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        test_info = condition.return_test_info()
        measurement_instrument = copy.deepcopy(test_info['Instrument'])
        measurement_period = float(copy.deepcopy(test_info['Measurement_Period']))
        measurement_channel = int(copy.deepcopy(test_info['Measurement_Channel']))

        while condition.test_VI_flag:
            condition.measurement_info['Instrument'] = measurement_instrument
            condition.measurement_info['Channel'] = measurement_channel
            condition = self.measure(condition)  # Measurement function
            time.sleep(measurement_period / 2)

        return condition

    def temperature_judgement(self, condition):
        """
        Judge whether temperature is stable

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        flag = True

        while flag:
            t1 = time.time()
            t2 = time.time()

            while t2 <= t1 + float(condition.test_info['Temperature_Time_Threshold']):  # Calculate time

                if float(condition.measurement_info['Temperature']) >=\
                        float(condition.test_info['Set_Temperature']) - 2 and\
                        float(condition.measurement_info['Temperature']) <=\
                        float(condition.test_info['Set_Temperature']) + 2:
                    # Judge whether temperature is stable
                    flag = False
                    t2 = time.time()

                else:
                    flag = True
                    break
        L.info('Temperature judgement finished')
        time.sleep(1)

        return condition

    def begin_T_measurement(self, condition):
        """
        Begin temperature and power instrument measurement

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        """Begin tem instrument measurement with one thread"""
        condition.test_info['Instrument'] = condition.test_info['Temperature_Setting_Instrument']
        future1 = pool.submit(self.measure_T_thread, condition)
        L.info('Begin temperature measurement finished')

        return condition

    def begin_VI_measurement(self, condition):
        """
        Begin ADC instrument measurement

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        """Begin tem instrument measurement with one thread"""
        condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
        future2 = pool.submit(self.measure_VI_thread, condition)
        L.info('Begin ADC measurement finished')

        return condition

    def test_trim(self, condition):
        """
        Test Venus trimming function
        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Init instrument"""
        try:
            measurement_period = float(condition.test_info['Measurement_Period'])
            condition = self.init_power_setting(condition)
            condition = self.init_clock_setting(condition)
            for i in range(2):
                condition.test_T_flag = True
                condition.test_VI_flag = True
                """Init temperature instrument and start temperature measurement"""
                condition.test_info['Set_Temperature'] = condition.test_info['Temperature' + '_' + str(i + 1)]
                # condition = self.init_temperature_setting(condition)
                # condition = self.begin_T_measurement(condition)
                # condition = self.temperature_judgement(condition)
                time.sleep(measurement_period)
                """Set 1st VDD"""
                condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
                condition.test_info['Channel'] = condition.test_info['Vdd_Channel']
                condition.test_info['Voltage'] = condition.test_info['Vdd_Voltage_1']
                condition.test_info['Current'] = condition.test_info['Vdd_Current_1']
                condition = self.set(condition)
                condition = self.on(condition)
                time.sleep(measurement_period)
                """Set VIN"""
                condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
                condition.test_info['Channel'] = condition.test_info['Vin_Channel']
                condition.test_info['Voltage'] = condition.test_info['Vin_Voltage']
                condition.test_info['Current'] = condition.test_info['Vin_Current']
                condition = self.set(condition)
                condition = self.on(condition)
                time.sleep(measurement_period)
                """Start voltage and current measurement"""
                condition = self.begin_VI_measurement(condition)
                time.sleep(measurement_period)
                condition.measurement_info['Current_1'] = condition.measurement_info['Current']
                """Set 1st clock"""
                condition.test_info['Instrument'] = condition.test_info['Clock_Instrument']
                condition.test_info['Amplitude'] = condition.test_info['Clock_Amplitude_1']
                condition.test_info['Offset'] = condition.test_info['Clock_Offset_1']
                condition.test_info['Frequency'] = condition.test_info['Clock_Frequency_1']
                condition = self.operate(condition, 'set_channel_squ')
                condition = self.on(condition)
                time.sleep(measurement_period)
                """Judge if supply current increasing by 1mA"""
                condition.measurement_info['Current_2'] = condition.measurement_info['Current']
                # while float(condition.measurement_info['Current_2']) - float(condition.measurement_info['Current_1']) < 0.0005:
                #     condition.measurement_info['Current_2'] = condition.measurement_info['Current']
                time.sleep(measurement_period)
                """Close clock"""
                condition.test_info['Instrument'] = condition.test_info['Clock_Instrument']
                condition = self.off(condition)
                time.sleep(measurement_period)
                """Set 2nd VDD"""
                condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
                condition.test_info['Channel'] = condition.test_info['Vdd_Channel']
                condition.test_info['Voltage'] = condition.test_info['Vdd_Voltage_2']
                condition.test_info['Current'] = condition.test_info['Vdd_Current_2']
                condition = self.set(condition)
                condition = self.on(condition)
                time.sleep(measurement_period)
                """Set 2nd clock"""
                condition.test_info['Instrument'] = condition.test_info['Clock_Instrument']
                condition.test_info['Amplitude'] = condition.test_info['Clock_Amplitude_2']
                condition.test_info['Offset'] = condition.test_info['Clock_Offset_2']
                condition.test_info['Frequency'] = condition.test_info['Clock_Frequency_2']
                condition = self.operate(condition, 'set_channel_squ')
                condition = self.on(condition)
                time.sleep(measurement_period)
                """Close clock"""
                condition.test_info['Instrument'] = condition.test_info['Clock_Instrument']
                condition = self.off(condition)
                time.sleep(measurement_period)
                """Close VDD and VIN"""
                condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
                condition.test_info['Channel'] = condition.test_info['Vdd_Channel']
                condition = self.off(condition)
                condition.test_info['Channel'] = condition.test_info['Vin_Channel']
                condition = self.off(condition)
                time.sleep(measurement_period)
                """End measurement"""
                condition.test_T_flag = False
                condition.test_VI_flag = False
                time.sleep(measurement_period)

            # condition = self.stop_temperature_setting(condition)
            # condition.test_info['Set_Temperature'] = 25
            # condition = self.temperature_judgement(condition)

        except:
            L.error(traceback.format_exc())
            """Close Power instrument"""
            condition.test_VI_flag = False  # Stop measurement
            time.sleep(1)
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition.test_info['Communication'] = condition.test_info['Power_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition.test_info['Communication'] = condition.test_info['Power_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Clock_Instrument']
            condition.test_info['Communication'] = condition.test_info['Clock_Communication']
            condition = self.open(condition)
            condition = self.close(condition)

            condition = self.stop_temperature_setting(condition)
            condition.test_info['Set_Temperature'] = 25
            condition = self.temperature_judgement(condition)
            L.info('Finish except flow')

        return condition

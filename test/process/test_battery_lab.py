# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/16 11:48
File: test_battery_lab.py
"""

import time
import logging
import threading
import numpy as np
from test.device.flow.control_flow import Control_Flow
from parse.multiprocess.pool_thread import pool

L = logging.getLogger('Main')

class Test_Battery_Lab(Control_Flow):
    """
    Battery Lab SOP control class
    """
    def __init__(self):
        super().__init__()

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
            condition.output_info['Flag'] = np.append(condition.output_info['Flag'], condition.current_flag)
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

    def init_temperature_measurement(self, condition):
        """
        Init temperature measurement instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] \
            = condition.test_info['Temperature_Measurement_Instrument']  # Temperature instrument name
        condition.test_info['Communication'] \
            = condition.test_info['Temperature_Measurement_Communication']
        # Temperature instrument communication method
        condition = self.open(condition)  # Open instrument
        condition = self.prepare(condition)  # Prepare instrument
        condition = self.on(condition)  # Set instrument on
        L.info('Init temperature measurement finished')

        return condition

    def init_charge(self, condition):
        """
        Init battery charge power supply

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary

        """
        condition.test_info['Instrument'] = condition.test_info['Charge_Instrument']
        condition.test_info['Communication'] = condition.test_info['Charge_Communication']
        condition.test_info['Voltage'] = condition.test_info['Charge_Voltage']
        condition.test_info['Current'] = condition.test_info['Charge_Current']
        condition = self.open(condition)
        # condition = self.prepare(condition)
        condition = self.set(condition)
        condition = self.on(condition)
        L.info('Init charge finished')

        return condition

    def init_discharge(self, condition):
        """
        Init battery charge load supply

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary

        """
        condition.test_info['Instrument'] = condition.test_info['Discharge_Instrument']
        condition.test_info['Communication'] = condition.test_info['Discharge_Communication']
        condition = self.open(condition)
        condition = self.prepare(condition)
        L.info('Init charge finished')

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
        condition.test_info['Instrument'] = condition.test_info['Temperature_Measurement_Instrument']
        future1 = pool.submit(self.measure_T_thread, condition)
        # t1 = threading.Thread(target=self.measure_T_thread, args=(condition, ), daemon=True)
        # t1.start()
        L.info('Begin temperature measurement finished')

        return condition

    def begin_VI_measurement(self, condition):
        """
        Begin temperature and power instrument measurement

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Begin vol and cur instrument measurement with one thread"""
        condition.test_info['Instrument'] = condition.test_info['Charge_Instrument']
        future2 = pool.submit(self.measure_VI_thread, condition)
        # t2 = threading.Thread(target=self.measure_VI_thread, args=(condition,), daemon=True)
        # t2.start()
        L.info('Begin voltage and current measurement finished')

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

    def charge_judgement(self, condition):
        """
        Judge whether battery charge enough

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        flag = True

        while flag:
            t1 = time.time()
            t2 = time.time()

            while t2 <= t1 + float(condition.test_info['Charge_Time_Threshold']):  # Calculate time

                if condition.measurement_flag is True:  # measuring voltage data updated

                    if float(condition.measurement_info['Voltage']) * 1000 \
                            >= float(condition.test_info['Charge_Voltage_Threshold']) and \
                            float(condition.measurement_info['Current']) * 1000 \
                            <= float(condition.test_info['Charge_Current_Threshold']):
                        # Judge whether battery is fully enough
                        flag = False
                        condition.measurement_flag = False
                        t2 = time.time()

                    else:
                        flag = True
                        condition.measurement_flag = False
                        break
        L.info('Charge judgement finished')
        time.sleep(1)

        return condition

    def begin_discharge(self, condition):
        """
        Begin battery discharge

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['Charge_Instrument']
        condition.test_info['Voltage'] = condition.test_info['Discharge_Voltage']
        condition.test_info['Current'] = condition.test_info['Discharge_Current']
        condition.sleep_flag = True
        time.sleep(1)
        condition.current_flag = 3
        condition = self.off(condition)
        condition = self.operate(condition, 'set_voltage')
        condition = self.operate(condition, 'set_current')
        condition = self.on(condition)
        condition.sleep_flag = False
        L.info('Begin discharge finished')

        return condition

    def stop_discharge(self, condition):
        """
        Stop battery discharge

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['Charge_Instrument']
        condition = self.off(condition)
        L.info('Stop discharge finished')
        time.sleep(1)

        return condition

    def discharge_judgement(self, condition):
        """
        Judge whether battery discharge enough

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        t1 = time.time()
        t2 = time.time()
        num = 10

        while t2 - t1 < float(condition.test_info['Discharge_Time_Threshold']):  # Calculate time
            voltage_sum = []

            while len(voltage_sum) < num:  # Collect data

                while condition.measurement_flag is True:  # measuring voltage data updated
                    voltage_sum.append(float(condition.measurement_info['Voltage']))
                    condition.measurement_flag = False
            voltage = 1000 * sum(voltage_sum) / len(voltage_sum)

            """If voltage is less than threshold, enter next step, otherwise keep judging"""
            if voltage < float(condition.test_info['Discharge_Voltage_Threshold']):
                L.info('Battery has finished discharging')

                return condition
            t2 = time.time()
        L.warning('Time is over ' + str(condition.test_info['Discharge_Time_Threshold']) + 's')

        return condition

    def cal_voltage(self, condition):
        """
        Calculate average value of voltage

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        flag = True
        voltage_sum = []
        num = 10

        while flag:

                while condition.measurement_flag is True:  # measuring voltage data updated
                    voltage_sum.append(float(condition.measurement_info['Voltage']))
                    condition.measurement_flag = False

                    if len(voltage_sum) == num:  # Collect enough data
                        flag = False
                        break
        condition.measurement_info['Ave_Voltage'] =\
            1000 * sum(voltage_sum) / len(voltage_sum)  # Calculate average of voltage
        L.info('Calculate voltage finished')

        return condition

    def stop_charge(self, condition):
        """
        End charge or discharge

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Voltage'] = condition.test_info['Charge_Voltage']
        condition.test_info['Current'] = condition.test_info['Relax_Current']
        condition.sleep_flag = True
        time.sleep(1)
        condition = self.off(condition)
        condition = self.set(condition)
        # condition = self.set_current(condition)
        condition = self.on(condition)
        condition.sleep_flag = False
        L.info('End charge')

        return condition

    def relax_judgement(self, condition):
        """
        Judge whether battery relax enough

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Current'] = condition.test_info['Relax_Current']
        condition.sleep_flag = True
        time.sleep(1)
        condition.current_flag = 2
        condition = self.off(condition)
        condition = self.set_current(condition)
        condition = self.on(condition)
        condition.sleep_flag = False

        """If deviation < 1mV, enter next step, otherwise keep calculating deviation until timeout"""
        t1 = time.time()
        t2 = time.time()
        num = 100

        while t2 - t1 < float(condition.test_info['Reset_Time_Threshold']):  # Calculate time
            voltage_sum1 = []
            voltage_sum2 = []

            while len(voltage_sum1) < num:  # Collect first data summary

                while condition.measurement_flag is True:  # measuring voltage data updated
                    voltage_sum1.append(float(condition.measurement_info['Voltage']))
                    condition.measurement_flag = False

            while len(voltage_sum2) < num:  # Collect second data summary

                while condition.measurement_flag is True:  # measuring voltage data updated
                    voltage_sum2.append(float(condition.measurement_info['Voltage']))
                    condition.measurement_flag = False

            if len(voltage_sum1) > len(voltage_sum2):  # Make sure length of list is same
                voltage_sum1 = voltage_sum1[0: len(voltage_sum2)]

            elif len(voltage_sum1) < len(voltage_sum2):
                voltage_sum2 = voltage_sum2[0: len(voltage_sum1)]

            deviation = 1000 * abs(
                (sum(voltage_sum1) - sum(voltage_sum2)) / len(voltage_sum1)
            )  # Calculate deviation of voltage

            """If deviation < 1mV, enter next step, otherwise keep judging"""
            if deviation <= 1:
                L.info('Battery voltage is stable')

                return condition
            t2 = time.time()
        L.warning('Time is over ' + str(condition.test_info['Reset_Time_Threshold']) + 's')

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
        flag = True

        while flag:
            t1 = time.time()
            t2 = time.time()

            while t2 <= t1 + float(condition.test_info['Temperature_Time_Threshold']):  # Calculate time

                if float(condition.measurement_info['Temperature']) >= float(normal_temperature) - 2 and \
                        float(condition.measurement_info['Temperature']) <= float(normal_temperature) + 2:
                    # Judge whether temperature is stable
                    flag = False
                    t2 = time.time()

                else:
                    flag = True
                    break
        condition = self.open(condition)  # Open instrument
        time.sleep(1)
        condition = self.off(condition)
        time.sleep(1)
        condition = self.close(condition)
        L.info('Stop temperature finished')
        time.sleep(1)

        return condition

    def test(self, condition):
        """
        Whole SOP of battery test, including all steps

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        try:
            """Init temperature setting instrument"""
            if condition.test_info['Temperature_Setting_Flag'] is True:
                condition = self.init_temperature_setting(condition)

            """Init temperature measurement instrument"""
            if condition.test_info['Temperature_Measurement_Flag'] is True:
                condition = self.init_temperature_measurement(condition)

                """Begin temperature measurement"""
                condition = self.begin_T_measurement(condition)
                time.sleep(1)

            """Judge whether temperature is stable"""
            if condition.test_info['Temperature_Measurement_Flag'] is True:
                condition = self.temperature_judgement(condition)

            if condition.test_info['Charge_Setting_Flag'] is True:
                """Init battery charge instrument"""
                condition = self.init_charge(condition)
                condition.current_flag = 1
                time.sleep(1)

                """Begin voltage measurement"""
                condition = self.begin_VI_measurement(condition)

                """Judge whether charge is enough"""
                condition = self.charge_judgement(condition)

                """Stop charge"""
                condition = self.stop_charge(condition)
                condition.current_flag = 2

            if condition.test_info['Temperature_Measurement_Flag'] is True:
                """Judge whether temperature is stable"""
                condition = self.temperature_judgement(condition)

            if condition.test_info['Charge_Setting_Flag'] is True:
                """Judge whether relaxing is enough"""
                condition = self.relax_judgement(condition)
                flag = 1

                while True:

                    if flag == 1:
                        L.info('Enter branch 1')
                        """Begin discharge"""
                        condition.test_info['Discharge_Current'] = condition.test_info['Discharge_Current_1']
                        condition = self.begin_discharge(condition)
                        """Judge whether discharge is enough"""
                        condition.test_info['Discharge_Voltage_Threshold'] \
                            = condition.test_info['Discharge_Voltage_Threshold_1']
                        condition = self.discharge_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 2 if condition.measurement_info['Ave_Voltage'] \
                                    < float(condition.test_info['Voltage_Judgement_1']) else 3

                    if flag == 2:
                        L.info('Enter branch 2')
                        """Judge whether relaxing is enough"""
                        condition = self.relax_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 1 if condition.measurement_info['Ave_Voltage'] \
                                    >= float(condition.test_info['Voltage_Judgement_2']) else 4

                    if flag == 3:
                        L.info('Enter branch 3')
                        """Judge whether relaxing is enough"""
                        condition = self.relax_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 4 if condition.measurement_info['Ave_Voltage'] \
                                    < float(condition.test_info['Voltage_Judgement_3']) else 1

                    if flag == 4:
                        L.info('Enter branch 4')
                        """Begin discharge"""
                        condition.test_info['Discharge_Current'] = condition.test_info['Discharge_Current_2']
                        condition = self.begin_discharge(condition)
                        """Judge whether discharge is enough"""
                        condition.test_info['Discharge_Voltage_Threshold'] = \
                            condition.test_info['Discharge_Voltage_Threshold_2']
                        condition = self.discharge_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 5 if condition.measurement_info['Ave_Voltage'] \
                                    < float(condition.test_info['Voltage_Judgement_4']) else 6

                    if flag == 5:
                        L.info('Enter branch 5')
                        """Judge whether relaxing is enough"""
                        condition = self.relax_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 7 if condition.measurement_info['Ave_Voltage'] \
                                    < float(condition.test_info['Voltage_Judgement_5']) else 4

                    if flag == 6:
                        L.info('Enter branch 6')
                        """Judge whether relaxing is enough"""
                        condition = self.relax_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 7 if condition.measurement_info['Ave_Voltage'] \
                                    < float(condition.test_info['Voltage_Judgement_6']) else 4

                    if flag == 7:
                        L.info('Enter branch 7')
                        """Begin discharge"""
                        condition.test_info['Discharge_Current'] = condition.test_info['Discharge_Current_3']
                        condition = self.begin_discharge(condition)
                        """Judge whether discharge is enough"""
                        condition.test_info['Discharge_Voltage_Threshold'] = \
                            condition.test_info['Discharge_Voltage_Threshold_3']
                        condition = self.discharge_judgement(condition)
                        """Judge whether relaxing is enough"""
                        condition = self.relax_judgement(condition)
                        """Calculate average of voltage"""
                        condition = self.cal_voltage(condition)

                        """Judge next step"""
                        flag = 8 if condition.measurement_info['Ave_Voltage'] \
                                    < float(condition.test_info['Voltage_Judgement_7']) else 7

                    if flag == 8:
                        L.info('Enter branch 8')
                        """Finally step"""
                        break

                condition.test_VI_flag = False  # Stop charge measurement
                time.sleep(1)
            if condition.test_info['Charge_Setting_Flag'] is True:
                """Close charge instrument"""
                condition.test_info['Instrument'] = condition.test_info['Charge_Instrument']
                condition = self.off(condition)
            if condition.test_info['Temperature_Setting_Flag'] is True:
                """Close temperature setting instrument"""
                condition = self.stop_temperature_setting(condition)
                """Close temperature measurement instrument"""
                condition.test_T_flag = False  # Stop charge measurement
                time.sleep(1)
            if condition.test_info['Temperature_Measurement_Flag'] is True:
                condition.test_info['Instrument'] = condition.test_info['Temperature_Measurement_Instrument']
                condition = self.off(condition)
            L.debug('Finish normal flow')

        except:

            condition.test_VI_flag = False  # Stop measurement
            time.sleep(1)

            if condition.test_info['Charge_Setting_Flag'] is True:
                """Close charge instrument"""
                condition.test_info['Instrument'] = condition.test_info['Charge_Instrument']
                condition.test_info['Communication'] = condition.test_info['Charge_Communication']
                try:
                    condition = self.open(condition)
                except:
                    pass
                condition = self.off(condition)
            if condition.test_info['Temperature_Setting_Flag'] is True:
                """Close temperature setting instrument"""
                condition.test_info['Instrument'] \
                    = condition.test_info['Temperature_Setting_Instrument']  # Temperature instrument name

                try:
                    condition = self.open(condition)
                except:
                    pass
                condition = self.stop_temperature_setting(condition)
            if condition.test_info['Temperature_Measurement_Flag'] is True:
                """Close temperature measurement instrument"""
                condition.test_T_flag = False  # Stop charge measurement
                time.sleep(1)
                condition.test_info['Instrument'] = condition.test_info['Temperature_Measurement_Instrument']
                condition.test_info['Communication'] = condition.test_info['Temperature_Measurement_Communication']

                try:
                    condition = self.open(condition)
                except:
                    pass
                condition = self.off(condition)
            L.debug('Finish except flow')

        finally:
            condition.test_VI_flag = False  # Stop measurement
            condition.test_T_flag = False  # Stop measurement
            L.debug('Finish final flow')

            return condition



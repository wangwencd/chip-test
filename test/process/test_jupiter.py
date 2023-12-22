# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/6/27 19:41
File: test_jupiter.py
"""
import re
import copy
import logging
import time
import traceback
import numpy as np

from test.device.flow.control_flow import Control_Flow
from parse.file.reg_operation import Reg_Operation
from parse.multiprocess.pool_thread import pool

L = logging.getLogger('Main')

class Test_Jupiter(Control_Flow):
    """
    Jupiter project test class
    """
    def test(self, condition):
        """
        Jupiter test work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        name = condition.func_name

        if re.search('ramp_multi', name, re.I) is not None:
            condition = self.test_ramp_multi(condition)

        elif re.search('noise', name, re.I) is not None:
            condition = self.test_noise(condition)

        elif re.search('ramp', name, re.I) is not None:
            condition = self.test_ramp(condition)

        return condition

    @staticmethod
    def refresh_I2C(data_buf=[], rx_size=0, i2c_address=0x48, restart=0, frequency=1, bus_num=3):
        """
        Refresh I2C command, which will be sent to mcu.

        Args:
            data_buf: List of register address and data, format: list, e.g. [0x00, 0x01].
            rx_size: Length of register data user wants to get, format: int.
            i2c_address: I2C slave address, format: int.
            restart: Determine whether I2C would restart after this command, 0=off/ 1=on, format: int.
            frequency: Determine I2C transmission rate, 1=100K/ 2= 400K/ 3=1M/ 4=4M/ 5=10K, format: int.
            bus_num: Determine I2C pin at MAX32670 KIT, 1=(12: SCL, 13: SDA), format: int.

        Returns:
            msg: Group of I2C command which will be sent to mcu, format: dict.
        """
        """Need to set data_buf, rx_size"""
        msg = {
            'bus_num': bus_num,
            'i2c_address': i2c_address,
            'data_buf': data_buf,
            'rx_size': rx_size,
            'restart': restart,
            "frequency": frequency,
        }

        return msg

    @staticmethod
    def refresh_GPIO(gpio_num=1, gpio_func=0, gpio_vssel=0, gpio_pad=0, set_value=0, get_value=0):
        """
        Refresh GPIO command, which will be sent to mcu.

        Args:
            gpio_num: Determine GPIO PIN at MAX32670 KIT, 1=(1: GPIO)/ 2=(2: GPIO), format: int.
            gpio_func: Determine GPIO is output/input function, 0=IN/ 1=OUT, format: int.
            gpio_vssel: Determine which voltage would be set to GPIO, 0=VDDIO/ 1=VDDIOH, format: int.
            gpio_pad: Determine state of GPIO pin, 0=None/ 1=Pull up/ 2= Pull down, format: int.
            set_value: GPIO state user want to send, 0=LOW/ 1=HIGH, format: int.
            get_value: GPIO state user get, 0=LOW/ 1=HIGH, format: int.

        Returns:
            msg: Group of GPIO command which will be sent to mcu, format: dict.
        """
        msg = {}
        if gpio_func == 1:  # Output GPIO function
            """Need to set gpio_num, gpio_func, set_value"""
            msg = {
                'gpio_num': gpio_num,
                'set_value': set_value,
                'gpio_func': gpio_func,
                'gpio_vssel': gpio_vssel,
                'gpio_pad': gpio_pad,
            }

        elif gpio_func == 0:  # Input GPIO function
            """Need to set gpio_num, gpio_func"""
            msg = {
                'gpio_num': gpio_num,
                'get_value': get_value,
                'gpio_func': gpio_func,
                'gpio_vssel': gpio_vssel,
                'gpio_pad': gpio_pad,
            }

        return msg

    @staticmethod
    def refresh_reset():
        """
        Refresh RESET command, which will be sent to mcu.

        Returns:
            msg: Group of RESET command which will be sent to mcu, format: dict.
        """
        msg = {}

        return msg

    def init_control_setting(self, condition):
        """
        Init controller instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
        condition.test_info['Communication'] = condition.test_info['Control_Communication']
        condition = self.open(condition)

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

    def init_adc_setting(self, condition):
        """
        Init ADC power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
        condition.test_info['Communication'] = condition.test_info['ADC_Setting_Communication']
        condition = self.open(condition)
        condition = self.prepare(condition)

        return condition

    def init_adc_measurement(self, condition):
        """
        Init ADC power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.test_info['Instrument'] = condition.test_info['ADC_Measurement_Instrument']
        condition.test_info['Communication'] = condition.test_info['ADC_Measurement_Communication']
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

    def set_power(self, condition):
        """
        Power chip according to config

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        condition.test_info['Instrument'] = condition.test_info['Power_Instrument']  # Power
        condition.test_info['Voltage'] = condition.test_info['Power_Voltage_1']
        condition.test_info['Current'] = condition.test_info['Power_Current_1']
        condition.test_info['Channel'] = condition.test_info['Power_Channel_1']
        condition = self.set(condition)
        condition = self.on(condition)
        condition.test_info['Voltage'] = condition.test_info['Power_Voltage_2']
        condition.test_info['Current'] = condition.test_info['Power_Current_2']
        condition.test_info['Channel'] = condition.test_info['Power_Channel_2']
        condition = self.set(condition)
        condition = self.on(condition)

        return condition

    def set_preparation(self, condition):
        """
        Chip preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
        bus_num = int(condition.test_info['Reg_Bus_Number'])
        """Step 1"""
        test_info = copy.deepcopy(condition.test_info)
        for key, value in test_info.items():

            if re.search('Reg_Function_', key, re.I) is not None:  # I2C write/read
                order = key.split('Reg_Function_')[1]

                if re.match('w', value, re.I) is not None:  # I2C write
                    reg_value = Reg_Operation.hex_to_dec(test_info['Reg_Value_' + order])
                    reg_slave = Reg_Operation.hex_to_dec(test_info['Reg_Slave_' + order])[0]
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=reg_slave,
                        data_buf=reg_value,
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_write')

                elif re.match('r', value, re.I) is not None:  # I2C read
                    reg_num = int(test_info['Reg_Num_' + order])
                    reg_slave = Reg_Operation.hex_to_dec(test_info['Reg_Slave_' + order])[0]
                    reg_value = Reg_Operation.hex_to_dec(test_info['Reg_Value_' + order])
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=reg_slave,
                        data_buf=reg_value,
                        rx_size=reg_num,
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_read')
                time.sleep(0.1)

            elif re.search('GPIO_Function_', key, re.I) is not None:  # GPIO write/read
                order = key.split('GPIO_Function_')[1]

                if re.match('w', value, re.I) is not None:  # GPIO write
                    gpio_num = int(test_info['GPIO_Num_' + order])
                    gpio_value = int(test_info['GPIO_Value_' + order])
                    condition.test_info['Msg'] = (self.refresh_GPIO(
                        gpio_num=gpio_num,
                        gpio_func=1,
                        set_value=gpio_value,

                    )).copy()
                    condition = self.operate(condition, 'GPIO_write')

                elif re.match('r', value, re.I) is not None:  # GPIO read
                    gpio_num = int(test_info['GPIO_Num_' + order])
                    condition.test_info['Msg'] = (self.refresh_GPIO(  # POR pin set to 1
                        gpio_num=gpio_num,
                        gpio_func=0,
                    )).copy()
                    condition = self.operate(condition, 'GPIO_read')
                time.sleep(0.1)

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
        # condition.test_info['Instrument'] = condition.test_info['Temperature_Measurement_Instrument']
        future1 = pool.submit(self.measure_T_thread, condition)
        L.info('Begin temperature measurement finished')

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

    def begin_VI_measurement(self, condition):
        """
        Begin ADC instrument measurement

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        """Begin tem instrument measurement with one thread"""
        condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
        future2 = pool.submit(self.measure_VI_thread, condition)
        L.info('Begin ADC measurement finished')

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

    def measure_all(self, condition):
        """
        Measure voltage, current from instrument and reg data from mcu, then update those into output.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        retest_time = int(condition.test_info['Retest_Time'])
        voltage = []
        data = []
        bus_num = int(condition.test_info['Reg_Bus_Number'])
        measurement_period = float(condition.test_info['Measurement_Period'])

        for i in range(retest_time):
            """Measure register"""
            time.sleep(measurement_period)
            while True:
                condition.test_info['Instrument'] = condition.test_info['ADC_Measurement_Instrument']
                condition.measurement_info['Option'] = 'Voltage'
                condition = self.operate(condition, 'measure_one')
                # condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
                # condition.measurement_info['Option'] = 'Voltage'
                # condition.test_info['Channel'] = '1'
                # condition = self.operate(condition, 'measure_voltage')
                time.sleep(0.005)
                condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                condition.test_info['Msg'] = (self.refresh_I2C(
                    i2c_address=int(condition.test_info['Reg_Slave'], 16),
                    data_buf=[int(condition.test_info['Reg_Address'], 16)],
                    rx_size=2,
                    bus_num=bus_num
                )).copy()
                condition = self.operate(condition, 'I2C_read')
                if condition.measurement_info['Msg'] is None:
                    pass

                elif len(condition.measurement_info['Msg'].data_buf) >= 1:
                    result = Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf)
                    if result >= 32768:
                        result = result - 65536
                    data.append(result)
                    break
            """Measure voltage and current"""
            # condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            # condition.measurement_info['Option'] = 'Voltage'
            # condition.test_info['Channel'] = '1'
            # condition = self.operate(condition, 'measure_voltage')
            # voltage1 = condition.measurement_info['Voltage']
            # condition.test_info['Channel'] = '2'
            # condition = self.operate(condition, 'measure_voltage')
            # voltage2 = condition.measurement_info['Voltage']
            # voltage.append(abs(voltage1) - abs(voltage2))
            voltage.append(condition.measurement_info['Voltage'])
        condition.output_info['Time'] = np.append(
            condition.output_info['Time'],
            time.perf_counter()
        )  # Update time to output
        try:
            condition.output_info['Temperature'] = np.append(
                condition.output_info['Temperature'],
                condition.measurement_info['Temperature']
            )  # Update temperature to output
        except:
            pass
        condition.output_info['Voltage'] = np.append(
            condition.output_info['Voltage'],
            np.median(voltage)
        )  # Update voltage to output
        condition.output_info['Data'] = np.append(
            condition.output_info['Data'],
            round(np.median(data))
        )  # Update data to output

        return condition

    def measure_multi(self, condition):
        """
        Measure voltage, current from instrument and reg data from mcu, then update those into output.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        retest_time = int(condition.test_info['Retest_Time'])
        voltage = []
        data = [[], [], [], []]
        bus_num = int(condition.test_info['Reg_Bus_Number'])
        i2c_slave = eval(condition.test_info['Reg_Slave'])
        measurement_period = float(condition.test_info['Measurement_Period'])

        for i in range(retest_time):
            time.sleep(measurement_period)
            condition.test_info['Instrument'] = condition.test_info['ADC_Measurement_Instrument']
            condition.measurement_info['Option'] = 'Voltage'
            condition = self.operate(condition, 'measure_one')
            """Measure register"""
            for j in range(len(i2c_slave)):
                time.sleep(0.005)
                while True:
                    condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=i2c_slave[j],
                        data_buf=[int(condition.test_info['Reg_Address'], 16)],
                        rx_size=2,
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_read')

                    if condition.measurement_info['Msg'] is None:
                        pass

                    elif len(condition.measurement_info['Msg'].data_buf) >= 1:
                        result = Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf)
                        if result >= 32768:
                            result = result - 65536
                        data[j].append(result)
                        break

            """Measure voltage and current"""
            # condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            # condition.measurement_info['Option'] = 'Voltage'
            # condition = self.operate(condition, 'measure_voltage')
            # voltage.append(condition.measurement_info['Voltage'])
            voltage.append(condition.measurement_info['Voltage'])
        condition.output_info['Time'] = np.append(
            condition.output_info['Time'],
            time.perf_counter()
        )  # Update time to output
        try:
            condition.output_info['Temperature'] = np.append(
                condition.output_info['Temperature'],
                condition.measurement_info['Temperature']
            )  # Update temperature to output
        except:
            pass
        condition.output_info['Voltage'] = np.append(
            condition.output_info['Voltage'],
            np.median(voltage)
        )  # Update voltage to output

        for j in range(len(i2c_slave)):
            condition.output_info['Data' + str(j)] = np.append(
                condition.output_info['Data' + str(j)],
                round(np.median(data[j]))
            )  # Update data to output

        return condition

    def test_ramp(self, condition):
        """
        Test Jupiter DNL of ADC

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = bool(int(condition.test_info['Temperature_Setting']))

        try:
            """Temperature setting"""
            if temperature_setting is True:  # Setting temperature
                condition = self.init_temperature_setting(condition)
                condition = self.begin_T_measurement(condition)
                time.sleep(1)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:  # Not setting
                pass

            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.set_power(condition)  # Power setting
            time.sleep(1)
            condition = self.init_control_setting(condition)
            condition = self.init_adc_setting(condition)
            condition = self.init_adc_measurement(condition)

            """Preparation"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']  # ADC setting
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']  # ADC setting
            condition.test_info['Voltage'] = condition.test_info['Start_Voltage']
            condition.test_info['Current'] = condition.test_info['Start_Current']
            condition.test_info['Channel'] = '1'
            condition = self.set(condition)
            condition = self.on(condition)

            condition.test_info['Voltage'] = condition.test_info['End_Voltage']
            condition.test_info['Current'] = condition.test_info['Start_Current']
            condition.test_info['Channel'] = '2'
            condition = self.set(condition)
            condition = self.on(condition)

            condition.test_info['Instrument'] = condition.test_info['ADC_Measurement_Instrument']  # ADC measurement
            condition.test_info['Option'] = 'Voltage'
            condition.test_info['Flag'] = 'ON'
            condition.test_info['Type'] = 'REP'
            condition.test_info['Count'] = '1'
            condition.test_info['Choice'] = 'AUTO'
            condition = self.operate(condition, 'set_one_autorange')
            condition = self.operate(condition, 'set_one_autozero')
            condition = self.operate(condition, 'set_one_average_control')
            condition = self.operate(condition, 'set_one_average_count')
            condition = self.operate(condition, 'set_one_average')
            condition = self.operate(condition, 'set_one_impedance')
            #
            condition = self.set_preparation(condition)  # MCU
            # time.sleep(1)
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']  # Power
            condition.test_info['Voltage'] = condition.test_info['Power_Voltage_3']
            condition.test_info['Current'] = condition.test_info['Power_Current_3']
            condition.test_info['Channel'] = condition.test_info['Power_Channel_3']
            condition = self.set(condition)
            condition = self.on(condition)
            time.sleep(1)

            """Set"""
            start_voltage = float(condition.test_info['Start_Voltage'])
            end_voltage = float(condition.test_info['End_Voltage'])
            step_voltage = float(condition.test_info['Step_Voltage'])
            measurement_period = float(condition.test_info['Measurement_Period'])
            set_voltage_1 = start_voltage
            set_voltage_2 = end_voltage

            while start_voltage < end_voltage:
                condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
                condition.test_info['Voltage'] = set_voltage_1
                condition.test_info['Channel'] = '1'
                condition = self.operate(condition, 'set_voltage')
                condition.test_info['Voltage'] = set_voltage_2
                condition.test_info['Channel'] = '2'
                condition = self.operate(condition, 'set_voltage')
                condition.output_info['Current'] = np.append(
                    condition.output_info['Current'],
                    set_voltage_1
                )  # Update time to output
                condition = self.measure_all(condition)
                set_voltage_1 = round(set_voltage_1 + step_voltage, 6)
                set_voltage_2 = round(set_voltage_2 - step_voltage, 6)
                start_voltage = round(start_voltage + step_voltage, 6)

            """Close ADC instrument"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            condition.test_info['Channel'] = '1'
            condition = self.off(condition)
            condition.test_info['Channel'] = '2'
            condition = self.off(condition)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition.test_info['Channel'] = condition.test_info['Power_Channel_1']
            condition = self.off(condition)
            condition.test_info['Channel'] = condition.test_info['Power_Channel_2']
            condition = self.off(condition)
            condition.test_info['Channel'] = condition.test_info['Power_Channel_3']
            condition = self.off(condition)
            """Close temperature setting instrument"""
            if temperature_setting is True:
                condition = self.stop_temperature_setting(condition)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            condition = self.close(condition)
            L.info('Finish normal flow')
        except:
            L.error(traceback.format_exc())

        finally:
            condition.test_VI_flag = False  # Stop measurement
            condition.test_T_flag = False  # Stop measurement
            L.info('Finish final flow')

            return condition

    def test_ramp_multi(self, condition):
        """
        Test Jupiter DNL of 4 ADC

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = bool(int(condition.test_info['Temperature_Setting']))

        try:
            """Temperature setting"""
            if temperature_setting is True:  # Setting temperature
                condition = self.init_temperature_setting(condition)
                condition = self.begin_T_measurement(condition)
                time.sleep(1)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:  # Not setting
                pass

            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.set_power(condition)  # Power setting
            time.sleep(1)
            condition = self.init_control_setting(condition)
            condition = self.init_adc_setting(condition)
            condition = self.init_adc_measurement(condition)

            """Preparation"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']  # ADC setting
            condition.test_info['Voltage'] = condition.test_info['Start_Voltage']
            condition.test_info['Current'] = condition.test_info['Start_Current']
            condition.test_info['Channel'] = '1'
            condition = self.set(condition)
            condition = self.on(condition)

            condition.test_info['Voltage'] = condition.test_info['End_Voltage']
            condition.test_info['Current'] = condition.test_info['Start_Current']
            condition.test_info['Channel'] = '2'
            condition = self.set(condition)
            condition = self.on(condition)

            condition.test_info['Instrument'] = condition.test_info['ADC_Measurement_Instrument']  # ADC measurement
            condition.test_info['Option'] = 'Voltage'
            condition.test_info['Flag'] = 'ON'
            condition.test_info['Type'] = 'REP'
            condition.test_info['Count'] = '2'
            condition.test_info['Choice'] = 'AUTO'
            condition = self.operate(condition, 'set_one_autorange')
            condition = self.operate(condition, 'set_one_autozero')
            condition = self.operate(condition, 'set_one_average_control')
            condition = self.operate(condition, 'set_one_average_count')
            condition = self.operate(condition, 'set_one_average')
            condition = self.operate(condition, 'set_one_impedance')


            condition = self.set_preparation(condition)  # MCU

            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']  # Power
            condition.test_info['Voltage'] = condition.test_info['Power_Voltage_3']
            condition.test_info['Current'] = condition.test_info['Power_Current_3']
            condition.test_info['Channel'] = condition.test_info['Power_Channel_3']
            condition = self.set(condition)
            condition = self.on(condition)
            time.sleep(1)

            time.sleep(1)

            """Set"""
            start_voltage = float(condition.test_info['Start_Voltage'])
            end_voltage = float(condition.test_info['End_Voltage'])
            step_voltage = float(condition.test_info['Step_Voltage'])
            measurement_period = float(condition.test_info['Measurement_Period'])
            set_voltage_1 = start_voltage
            set_voltage_2 = end_voltage

            while start_voltage <= end_voltage:
                condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
                condition.test_info['Voltage'] = set_voltage_1
                condition.test_info['Channel'] = '1'
                condition = self.operate(condition, 'set_voltage')
                condition.test_info['Voltage'] = set_voltage_2
                condition.test_info['Channel'] = '2'
                condition = self.operate(condition, 'set_voltage')
                condition.output_info['Current'] = np.append(
                    condition.output_info['Current'],
                    set_voltage_1
                )  # Update time to output
                condition = self.measure_multi(condition)
                set_voltage_1 = round(set_voltage_1 + step_voltage, 6)
                set_voltage_2 = round(set_voltage_2 - step_voltage, 6)
                start_voltage = round(start_voltage + step_voltage, 6)

            """Close ADC instrument"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            condition.test_info['Channel'] = '1'
            condition = self.off(condition)
            condition.test_info['Channel'] = '2'
            condition = self.off(condition)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition.test_info['Channel'] = condition.test_info['Power_Channel_1']
            condition = self.off(condition)
            condition.test_info['Channel'] = condition.test_info['Power_Channel_2']
            condition = self.off(condition)
            condition.test_info['Channel'] = condition.test_info['Power_Channel_3']
            condition = self.off(condition)
            """Close temperature setting instrument"""
            if temperature_setting is True:
                condition = self.stop_temperature_setting(condition)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            condition = self.close(condition)
            L.info('Finish normal flow')
        except:
            L.error(traceback.format_exc())

        finally:
            condition.test_VI_flag = False  # Stop measurement
            condition.test_T_flag = False  # Stop measurement
            L.info('Finish final flow')

            return condition

    def test_sine(self, condition):
        """
        Test lithium DNL of ADC according sine wave

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = bool(int(condition.test_info['Temperature_Setting']))

        try:
            """Temperature setting"""
            if temperature_setting is True:  # Setting temperature
                condition = self.init_temperature_setting(condition)
                condition = self.begin_T_measurement(condition)
                time.sleep(1)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:  # Not setting
                pass

            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.init_adc_setting(condition)
            condition = self.init_control_setting(condition)

            """Preparation"""
            condition = self.set_power(condition)
            condition = self.set_preparation(condition)

            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            condition = self.operate(condition, 'set_channel_sin')
            condition = self.on(condition)
            time.sleep(1)

            retest_time = int(condition.test_info['Retest_Time'])  # Get retest time

            if isinstance(condition.test_info['Measurement_Period'], str):  # Get measurement interval
                condition.test_info['Period'] = eval(condition.test_info['Measurement_Period']) * 1000

            else:
                condition.test_info['Period'] = float(condition.test_info['Measurement_Period']) * 1000

            """Measure register"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            bus_num = int(condition.test_info['Reg_Bus_Number'])
            condition.test_info['Msg'] = (
                condition.test_info['Period'],
                (self.refresh_I2C(
                    i2c_address=int(condition.test_info['Reg_Slave'], 16),
                    data_buf=[int(condition.test_info['Reg_Address'], 16)],
                    rx_size=2,
                    bus_num=bus_num
            )).copy())
            condition = self.operate(condition, 'GO_write')  # Send cyclic sampling command

            for i in range(retest_time):

                condition = self.operate(condition, 'I2C_read_standby')  # Read I2C once

                if condition.measurement_info['Msg'] is None:  # If master do not receive data
                    condition = self.close(condition)
                    condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                    condition.test_info['Communication'] = condition.test_info['Control_Communication']
                    condition = self.open(condition)
                    condition = self.operate(condition, 'Reset')
                    L.error("Could not receive data")
                    break

                elif len(condition.measurement_info['Msg'].data_buf) >= 1:  # If master receive right datas
                    result = Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf)

                else:  # If master receive wrong data
                    L.error("Could not receive data")
                    break

                condition.output_info['Time'] = np.append(
                    condition.output_info['Time'],
                    time.perf_counter()
                )  # Update time to output
                condition.output_info['Data'] = np.append(
                    condition.output_info['Data'],
                    result
                )  # Update data to output

            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            for i in range(5):  # Reset MCU
                condition = self.operate(condition, 'Reset')
                time.sleep(1)

            condition.test_VI_flag = False  # Stop charge measurement
            time.sleep(1)
            """Close ADC instrument"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            condition = self.off(condition)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition = self.off(condition)
            """Close temperature setting instrument"""
            if temperature_setting is True:
                condition = self.stop_temperature_setting(condition)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass
            """Close temperature measurement instrument"""
            condition.test_T_flag = False  # Stop charge measurement
            time.sleep(1)
            if temperature_setting is True:
                condition.test_info['Instrument'] = condition.test_info['Temperature_Setting_Instrument']
                condition.test_info['Communication'] = condition.test_info['Temperature_Setting_Communication']
                condition = self.open(condition)
                condition = self.off(condition)
                condition = self.close(condition)
                time.sleep(1)
            elif temperature_setting is False:
                pass
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            condition = self.close(condition)
            L.info('Finish normal flow')

        except:
            L.error(traceback.format_exc())
            """Close ADC instrument"""
            condition.test_VI_flag = False  # Stop measurement
            time.sleep(1)
            condition.test_info['Instrument'] = condition.test_info['ADC_Setting_Instrument']
            condition.test_info['Communication'] = condition.test_info['ADC_Setting_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition.test_info['Communication'] = condition.test_info['Power_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            """Close temperature setting instrument"""
            if temperature_setting is True:
                condition = self.stop_temperature_setting(condition)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass
            """Close temperature measurement instrument"""
            condition.test_T_flag = False  # Stop charge measurement
            time.sleep(1)
            if temperature_setting is True:
                condition.test_info['Instrument'] = condition.test_info['Temperature_Setting_Instrument']
                condition.test_info['Communication'] = condition.test_info['Temperature_Setting_Communication']
                condition = self.open(condition)
                condition = self.off(condition)
                condition = self.close(condition)
                time.sleep(1)
            elif temperature_setting is False:
                pass
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            condition.test_info['Communication'] = condition.test_info['Control_Communication']
            condition = self.open(condition)
            condition = self.close(condition)
            L.info('Finish except flow')

        finally:
            condition.test_VI_flag = False  # Stop measurement
            condition.test_T_flag = False  # Stop measurement
            L.info('Finish final flow')

            return condition

    def test_noise(self, condition):
        """
        Test Jupiter DNL of 4 ADC

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = bool(int(condition.test_info['Temperature_Setting']))

        try:
            """Temperature setting"""
            if temperature_setting is True:  # Setting temperature
                condition = self.init_temperature_setting(condition)
                condition = self.begin_T_measurement(condition)
                time.sleep(1)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:  # Not setting
                pass

            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.set_power(condition)  # Power setting
            time.sleep(1)
            condition = self.init_control_setting(condition)

            """Preparation"""
            condition = self.set_preparation(condition)  # MCU
            time.sleep(1)

            """Set"""
            retest_time = int(condition.test_info['Retest_Time'])
            voltage = []
            data = [[], [], [], []]
            bus_num = int(condition.test_info['Reg_Bus_Number'])
            i2c_slave = eval(condition.test_info['Reg_Slave'])
            measurement_period = float(condition.test_info['Measurement_Period'])

            for i in range(retest_time):
                data = [[], [], [], []]
                time.sleep(measurement_period)
                """Measure register"""
                for j in range(len(i2c_slave)):
                    time.sleep(0.005)
                    while True:
                        condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                        condition.test_info['Msg'] = (self.refresh_I2C(
                            i2c_address=i2c_slave[j],
                            data_buf=[int(condition.test_info['Reg_Address'], 16)],
                            rx_size=2,
                            bus_num=bus_num
                        )).copy()
                        condition = self.operate(condition, 'I2C_read')

                        if condition.measurement_info['Msg'] is None:
                            pass

                        elif len(condition.measurement_info['Msg'].data_buf) >= 1:
                            result = Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf)
                            data[j].append(result)
                            break

                    """Measure voltage and current"""
                condition.output_info['Time'] = np.append(
                    condition.output_info['Time'],
                    time.perf_counter()
                )  # Update time to output
                try:
                    condition.output_info['Temperature'] = np.append(
                        condition.output_info['Temperature'],
                        condition.measurement_info['Temperature']
                    )  # Update temperature to output
                except:
                    pass
                for j in range(len(i2c_slave)):
                    condition.output_info['Data' + str(j)] = np.append(
                        condition.output_info['Data' + str(j)],
                        data[j]
                    )  # Update data to output
            # """Close power instrument"""
            # condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            # condition.test_info['Channel'] = condition.test_info['Power_Channel_1']
            # condition = self.off(condition)
            # condition.test_info['Channel'] = condition.test_info['Power_Channel_2']
            # condition = self.off(condition)
            """Close temperature setting instrument"""
            if temperature_setting is True:
                condition = self.stop_temperature_setting(condition)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            condition = self.close(condition)
            L.info('Finish normal flow')
        except:
            L.error(traceback.format_exc())

        finally:
            condition.test_VI_flag = False  # Stop measurement
            condition.test_T_flag = False  # Stop measurement
            L.info('Finish final flow')

            return condition
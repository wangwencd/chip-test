# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/12/20 15:42
File: test_lithium.py
"""
import setup
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

class Test_Lithium(Control_Flow):
    """
    Lithium project test class
    """
    def test(self, condition):
        """
        Lithium test work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        name = condition.func_name

        if re.search('accuracy', name, re.I) is not None:
            condition = self.test_accuracy(condition)

        elif re.search('deviation', name, re.I) is not None:
            condition = self.test_deviation(condition)

        elif re.search('dnl', name, re.I) is not None:
            condition = self.test_dnl(condition)

        elif re.search('bgr', name, re.I) is not None:
            condition = self.test_otp_bgr(condition)

        return condition

    @staticmethod
    def refresh_I2C(data_buf=[], rx_size=0, i2c_address=0x51, restart=0, frequency=5, bus_num=1):
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
        condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
        condition.test_info['Communication'] = condition.test_info['ADC_Communication']
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
        i2c_slave = int(condition.test_info['Reg_Slave'], 16)
        bus_num = int(condition.test_info['Reg_Bus_Number'])
        """Step 1"""
        test_info = copy.deepcopy(condition.test_info)
        for key, value in test_info.items():

            if re.search('Reg_Function_', key, re.I) is not None:  # I2C write/read
                order = key.split('Reg_Function_')[1]

                if re.match('w', value, re.I) is not None:  # I2C write
                    reg_value = Reg_Operation.hex_to_dec(test_info['Reg_Value_' + order])
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=i2c_slave,
                        data_buf=reg_value,
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_write')

                elif re.match('r', value, re.I) is not None:  # I2C read
                    reg_num = int(test_info['Reg_Num_' + order])
                    reg_value = Reg_Operation.hex_to_dec(test_info['Reg_Value_' + order])
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=i2c_slave,
                        data_buf=reg_value,
                        rx_size=reg_num,
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_read')
                time.sleep(1)

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
                time.sleep(2)

        return condition

    def set_power(self, condition):
        """
        Power chip according to config

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """

        condition.test_info['Instrument'] = condition.test_info['Power_Instrument']

        condition.test_info['Channel'] = '2+3'
        condition.test_info['Voltage'] = condition.test_info['Power_Voltage']
        condition.test_info['Current'] = condition.test_info['Power_Current']
        condition = self.set(condition)
        condition = self.on(condition)

        return condition

    def set_adc(self, condition):
        """Set"""
        condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
        condition.test_info['Voltage'] = condition.test_info['Start_Voltage']
        condition.test_info['Current'] = condition.test_info['Start_Current']
        condition = self.set(condition)
        condition = self.on(condition)
        time.sleep(2)

        return condition

    def set_signal(self, condition):
        """Set"""
        condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
        condition = self.operate(condition, 'set_channel_sin')
        condition = self.on(condition)
        time.sleep(2)

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

        while condition.test_VI_flag:
            condition.measurement_info['Instrument'] = measurement_instrument
            condition = self.measure(condition)  # Measurement function
            time.sleep(measurement_period / 2)

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
        temperature = []
        voltage = []
        current = []
        data = []
        measurement_period = float(condition.test_info['Measurement_Period'])
        bus_num = int(condition.test_info['Reg_Bus_Number'])
        for i in range(retest_time):
            time.sleep(measurement_period / 2)
            """Measure register"""
            while True:
                condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                condition.test_info['Msg'] = (self.refresh_I2C(
                    i2c_address=int(condition.test_info['Reg_Slave'], 16),
                    data_buf=[int(condition.test_info['Reg_Address'], 16)],
                    rx_size=2,
                    bus_num=bus_num
                )).copy()
                condition = self.operate(condition, 'I2C_read')

                if condition.measurement_info['Msg'] is None:
                    condition = self.close(condition)
                    condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                    condition.test_info['Communication'] = condition.test_info['Control_Communication']
                    condition = self.open(condition)
                    condition = self.operate(condition, 'Reset')
                    time.sleep(measurement_period)

                elif len(condition.measurement_info['Msg'].data_buf) >= 1:
                    result = Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf)
                    if result > 65000:
                        result = result - 65536
                    data.append(result)
                    break
            condition.measurement_info['Instrument'] = condition.test_info['ADC_Instrument']
            condition = self.measure(condition)
            """Measure voltage and current"""
            voltage.append(condition.measurement_info['Voltage'])
            current.append(condition.measurement_info['Current'])
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
        condition.output_info['Current'] = np.append(
            condition.output_info['Current'],
            np.median(current)
        )  # Update current to output
        condition.output_info['Data'] = np.append(
            condition.output_info['Data'],
            round(np.median(data))
        )  # Update data to output
        time.sleep(measurement_period / 2)

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

    def test_dnl(self, condition):
        """
        Test lithium DNL of ADC
        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = False  # Temperature setting flag. If ture, Setting temperature, otherwise not setting

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
            condition = self.set_signal(condition)
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
            condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
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
            condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
            condition.test_info['Communication'] = condition.test_info['ADC_Communication']
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

    def test_accuracy(self, condition):
        """
        Test lithium linearity error of GPADC
        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = True  # Temperature setting flag. If ture, Setting temperature, otherwise not setting

        try:
            """Temperature setting"""
            if temperature_setting is True:
                condition = self.init_temperature_setting(condition)
                condition = self.begin_T_measurement(condition)
                time.sleep(1)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass

            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.init_adc_setting(condition)
            condition = self.init_control_setting(condition)

            """Preparation"""
            condition = self.set_power(condition)
            condition = self.set_preparation(condition)
            condition = self.set_adc(condition)
            time.sleep(1)
            """Set"""
            start_voltage = condition.test_info['Start_Voltage']
            end_voltage = condition.test_info['End_Voltage']
            step_voltage = condition.test_info['Step_Voltage']
            measurement_period = float(condition.test_info['Measurement_Period'])

            """Measure register"""
            while start_voltage < end_voltage:

                while True:

                    try:
                        condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
                        condition.test_info['Voltage'] = start_voltage
                        condition = self.set_voltage(condition)
                        time.sleep(measurement_period * 2)
                        break

                    except:
                        L.error(traceback.format_exc())
                        time.sleep(1)
                condition = self.measure_all(condition)
                start_voltage = start_voltage + step_voltage
                time.sleep(measurement_period / 2)
            condition.test_VI_flag = False  # Stop charge measurement
            time.sleep(1)
            """Close ADC instrument"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
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
            condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
            condition.test_info['Communication'] = condition.test_info['ADC_Communication']
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

    def test_deviation(self, condition):
        """
        Test lithium deviation of ADC
        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        temperature_setting = False    # Temperature setting flag. If ture, Setting temperature, otherwise not setting

        try:
            """Temperature setting"""
            if temperature_setting is True:
                """Init temperature device and set temperature"""
                condition = self.init_temperature_setting(condition)
                condition = self.begin_T_measurement(condition)
                time.sleep(1)
                condition = self.temperature_judgement(condition)
            elif temperature_setting is False:
                pass

            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.init_adc_setting(condition)
            condition = self.init_control_setting(condition)
            """Preparation"""
            condition = self.set_power(condition)
            condition = self.set_preparation(condition)
            condition = self.set_adc(condition)
            time.sleep(1)
            """Set"""
            measurement_period = float(condition.test_info['Measurement_Period'])
            time.sleep(measurement_period / 2)
            """Measure register"""
            retest_time = int(condition.test_info['Retest_Time'])
            measurement_period = float(condition.test_info['Measurement_Period'])
            bus_num = int(condition.test_info['Reg_Bus_Number'])
            for i in range(retest_time):
                time.sleep(measurement_period / 2)
                """Measure register"""
                while True:
                    condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=int(condition.test_info['Reg_Slave'], 16),
                        data_buf=[int(condition.test_info['Reg_Address'], 16)],
                        rx_size=2,
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_read')

                    if condition.measurement_info['Msg'] is None:
                        condition = self.close(condition)
                        time.sleep(measurement_period)
                        condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                        condition.test_info['Communication'] = condition.test_info['Control_Communication']
                        condition = self.open(condition)

                    elif len(condition.measurement_info['Msg'].data_buf) >= 1:
                        result = Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf)
                        if result > 65000:
                            result = result - 65536
                        break
                condition.measurement_info['Instrument'] = condition.test_info['ADC_Instrument']
                condition = self.measure(condition)
                condition.output_info['Data'] = np.append(
                    condition.output_info['Data'],
                    result
                )  # Update data to output
                condition.output_info['Time'] = np.append(
                    condition.output_info['Time'],
                    time.perf_counter()
                )  # Update time to output
                try:
                    """Measure temperature"""
                    condition.output_info['Temperature'] = np.append(
                        condition.output_info['Temperature'],
                        condition.measurement_info['Temperature']
                    )  # Update temperature to output
                except:
                    pass
                """Measure voltage and current"""
                condition.output_info['Voltage'] = np.append(
                    condition.output_info['Voltage'],
                    condition.measurement_info['Voltage']
                )  # Update voltage to output
                condition.output_info['Current'] = np.append(
                    condition.output_info['Current'],
                    condition.measurement_info['Current']
                )  # Update current to output
                time.sleep(measurement_period / 2)

            time.sleep(measurement_period / 2)
            condition.test_VI_flag = False  # Stop charge measurement
            time.sleep(1)
            """Close ADC instrument"""
            condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
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
            condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
            condition.test_info['Communication'] = condition.test_info['ADC_Communication']
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

    def test_external_clk(self, condition):
        """
        Test lithium external_clk function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Measure register"""
        bus_num = 2
        condition = self.init_control_setting(condition)

        condition.test_info['Msg'] = (self.refresh_GPIO(
            gpio_num=2,
            gpio_func=1,
            set_value=1,
        )).copy()
        condition = self.operate(condition, 'GPIO_write')
        time.sleep(2)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x06', 16), int('0x11', 16), int('0x10', 16), int('0x7C', 16),  int('0x30', 16)],
            i2c_address=0x08,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)

        condition.test_info['Msg'] = (self.refresh_GPIO(
            gpio_num=3,
            gpio_func=1,
            set_value=1,
        )).copy()
        condition = self.operate(condition, 'GPIO_write')
        time.sleep(2)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('020', 16)],
            rx_size=2,
            i2c_address=0x08,
            bus_num=bus_num
        )).copy()
        for i in range(100):
            condition = self.operate(condition, 'I2C_read')
        print('done')
        time.sleep(0.5)

        return condition

    def test_otp(self, condition):
        """
        Test lithium otp function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Measure register"""
        bus_num = 2
        condition = self.init_control_setting(condition)

        condition.test_info['Msg'] = (self.refresh_GPIO(
            gpio_num=3,
            gpio_func=1,
            set_value=1,
        )).copy()
        condition = self.operate(condition, 'GPIO_write')
        time.sleep(2)

        condition.test_info['Msg'] = (self.refresh_GPIO(
            gpio_num=2,
            gpio_func=1,
            set_value=1,
        )).copy()
        condition = self.operate(condition, 'GPIO_write')
        time.sleep(2)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x08', 16), int('0x80', 16)],
            i2c_address=0x08,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x08', 16)],
            rx_size=1,
            i2c_address=0x08,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)

        condition.test_info['Msg'] = (self.refresh_GPIO(
            gpio_num=3,
            gpio_func=1,
            set_value=0,
        )).copy()
        condition = self.operate(condition, 'GPIO_write')
        time.sleep(2)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[
                int('0x50', 16),  # 50
                int('0x2C', 16),  # 50
                int('0x71', 16),  # 51
                int('0x40', 16),  # 52
                int('0x90', 16),  # 53
                int('0x4A', 16),  # 54
                int('0x4A', 16),  # 55
                int('0xF0', 16),  # 56
                int('0x04', 16),  # 57
                int('0x10', 16),  # 58
                int('0x04', 16),  # 59
                int('0x10', 16),  # 5A
                int('0x51', 16)   # 5B
            ],
            i2c_address=0x08,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(3)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x50', 16)],
            rx_size=12,
            i2c_address=0x51,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)

        # condition.test_info['Msg'] = (self.refresh_I2C(
        #     data_buf=[int('0x51', 16), int('0x30', 16),],
        #     i2c_address=0x51,
        # )).copy()
        # condition = self.operate(condition, 'I2C_write')
        # time.sleep(1)
        #
        # condition.test_info['Msg'] = (self.refresh_I2C(
        #     data_buf=[int('0x51', 16)],
        #     rx_size=1,
        #     i2c_address=0x51,
        # )).copy()
        # condition = self.operate(condition, 'I2C_read')
        # time.sleep(1)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x5F', 16), int('0x50', 16)],
            i2c_address=0x51,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x5F', 16)],
            rx_size=1,
            i2c_address=0x51,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x0A', 16), int('0xAB', 16)],
            i2c_address=0x51,
            bus_num=bus_num
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        print('done')
        time.sleep(0.5)

        return condition

    def test_gpadc_m_sel(self, condition):
        """
        Test lithium gpadc_m_sel function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        import numpy as np

        num = 10
        """Measure register"""
        condition = self.init_control_setting(condition)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x06', 16), int('0x11', 16), int('0x10', 16), int('0x78', 16), int('0x30', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x06', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)

        """M = 256"""
        L.info('This is M=256')
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16), int('0x00', 16), int('0x15', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('020', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        data = []
        for i in range(num):
            condition = self.operate(condition, 'I2C_read')
            data.append(Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf))
            time.sleep(1)
        var = np.var(data)
        L.info('Var is ' + str(var))
        time.sleep(1)

        """M = 128"""
        L.info('This is M=128')
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16), int('0x01', 16), int('0x15', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('020', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        data = []
        for i in range(num):
            condition = self.operate(condition, 'I2C_read')
            data.append(Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf))
            time.sleep(1)
        var = np.var(data)
        L.info('Var is ' + str(var))
        time.sleep(1)

        """M = 64"""
        L.info('This is M=64')
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16), int('0x02', 16), int('0x15', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('020', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        data = []
        for i in range(num):
            condition = self.operate(condition, 'I2C_read')
            data.append(Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf))
            time.sleep(1)
        var = np.var(data)
        L.info('Var is ' + str(var))
        time.sleep(1)

        """M = 32"""
        L.info('This is M=32')
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16), int('0x03', 16), int('0x15', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x05', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('020', 16)],
            rx_size=2,
            i2c_address=0x08,
        )).copy()
        data = []
        for i in range(num):
            condition = self.operate(condition, 'I2C_read')
            data.append(Reg_Operation.dec_to_one(condition.measurement_info['Msg'].data_buf))
            time.sleep(1)
        var = np.var(data)
        L.info('Var is ' + str(var))
        time.sleep(1)

        print('done')

        return condition

    def test_uv_delay(self, condition):
        """
        Test lithium uv_delay function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Measure register"""
        condition = self.init_control_setting(condition)

        delay_option = 0  # Option: 0, 1, 2, 3

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x06', 16), int('0x11', 16), int('0x10', 16), int('0x78', 16), int('0x30', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)

        if delay_option == 0:
            L.info('uv delay = 0.6s')
        elif delay_option == 1:
            L.info('uv delay = 2.4s')
        elif delay_option == 2:
            L.info('uv delay = 4.8s')
        elif delay_option == 3:
            L.info('uv delay = 9.6s')
        # Step 1
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x12', 16), int('0x00', 16), int('0x01', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x14', 16), int('0x03', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16), int('0x0b', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        # Step 2
        if delay_option == 0:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x00', 16)],
                i2c_address=0x08,
            )).copy()
        elif delay_option == 1:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x40', 16)],
                i2c_address=0x08,
            )).copy()
        elif delay_option == 2:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x80', 16)],
                i2c_address=0x08,
            )).copy()
        elif delay_option == 3:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0xC0', 16)],
                i2c_address=0x08,
            )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x0D', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        # Step 3
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x12', 16), int('0x40', 16), int('0x01', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x14', 16), int('0x00', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        # Step 4
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        time.sleep(0.1)
        while True:
            condition = self.operate(condition, 'I2C_read')
            temp = Reg_Operation.dec_to_hex(condition.measurement_info['Msg'].data_buf)
            result = Reg_Operation.hex_to_one(temp)
            if result == '0x0b':
                break
        L.info('uv delay is finished')
        time.sleep(1)
        print('done')

        return condition

    def test_ov_delay(self, condition):
        """
        Test lithium ov_delay function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Measure register"""
        condition = self.init_control_setting(condition)

        delay_option = 3  # Option: 0, 1, 2, 3

        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x06', 16), int('0x11', 16), int('0x10', 16), int('0x78', 16), int('0x30', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)

        if delay_option == 0:
            L.info('ov delay = 0.6s')
        elif delay_option == 1:
            L.info('ov delay = 1.2s')
        elif delay_option == 2:
            L.info('ov delay = 2.4s')
        elif delay_option == 3:
            L.info('ov delay = 4.8s')
        # Step 1
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x10', 16), int('0x60', 16), int('0x6E', 16), int('0x00', 16), int('0x01', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x14', 16), int('0x03', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16), int('0x0F', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        # Step 2
        if delay_option == 0:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x00', 16)],
                i2c_address=0x08,
            )).copy()
        elif delay_option == 1:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x10', 16)],
                i2c_address=0x08,
            )).copy()
        elif delay_option == 2:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x20', 16)],
                i2c_address=0x08,
            )).copy()
        elif delay_option == 3:
            condition.test_info['Msg'] = (self.refresh_I2C(
                data_buf=[int('0x0D', 16), int('0x30', 16)],
                i2c_address=0x08,
            )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x0D', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_read')
        time.sleep(1)
        # Step 3
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x10', 16), int('0x00', 16), int('0x02', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        time.sleep(1)
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x14', 16), int('0x00', 16)],
            i2c_address=0x08,
        )).copy()
        condition = self.operate(condition, 'I2C_write')
        # Step 4
        condition.test_info['Msg'] = (self.refresh_I2C(
            data_buf=[int('0x00', 16)],
            rx_size=1,
            i2c_address=0x08,
        )).copy()
        time.sleep(0.1)
        while True:
            condition = self.operate(condition, 'I2C_read')
            temp = Reg_Operation.dec_to_hex(condition.measurement_info['Msg'].data_buf)
            result = Reg_Operation.hex_to_one(temp)
            if result == '0x07':
                break
        L.info('ov delay is finished')
        time.sleep(1)
        print('done')

        return condition

    def test_otp_bgr(self, condition):
        """
        Test lithium BGR trim function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        try:
            """Init instruments"""
            condition = self.init_power_setting(condition)
            condition = self.init_adc_setting(condition)
            condition = self.init_control_setting(condition)
            condition = self.init_temperature_measurement(condition)
            """Preparation"""
            condition = self.set_power(condition)
            time.sleep(1)
            condition = self.set_preparation(condition)
            time.sleep(1)
            condition.test_info['Instrument'] = condition.test_info['Temperature_Measurement_Instrument']
            future1 = pool.submit(self.measure_T_thread, condition)
            L.info('Begin temperature measurement finished')
            time.sleep(1)
            """Measure parameter"""
            retest_time = int(condition.test_info['Retest_Time'])
            measurement_period = float(condition.test_info['Measurement_Period'])
            bus_num = int(condition.test_info['Reg_Bus_Number'])
            temperature = eval(condition.test_info['Set_Temperature_range'])

            for i in range(len(temperature)):
                condition.test_info['Set_Temperature'] = temperature[i]
                condition = self.init_temperature_setting(condition)
                condition = self.temperature_judgement(condition)
                start_value = int(condition.test_info['Start_Value'])
                step_value = int(condition.test_info['Step_Value'])
                end_value = int(condition.test_info['End_Value'])
                time.sleep(2)

                while start_value < end_value:
                    time.sleep(measurement_period / 2)
                    condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=int('0x08', 16),
                        data_buf=[int('0x08', 16)],
                        rx_size=2,
                        bus_num=2
                    )).copy()
                    condition = self.operate(condition, 'I2C_read')
                    time.sleep(measurement_period)
                    condition.test_info['Msg'] = (self.refresh_I2C(
                        i2c_address=int(condition.test_info['Reg_Slave'], 16),
                        data_buf=[int(condition.test_info['Reg_Address'], 16), start_value],
                        bus_num=bus_num
                    )).copy()
                    condition = self.operate(condition, 'I2C_write')
                    time.sleep(measurement_period)
                    condition.test_info['Instrument'] = condition.test_info['ADC_Instrument']
                    condition.measurement_info['Instrument'] = condition.test_info['ADC_Instrument']
                    condition.measurement_info['Option'] = 'Voltage'
                    voltage = []
                    for i in range(retest_time):
                        condition = self.operate(condition, 'measure_one')
                        voltage.append(condition.measurement_info['Voltage'])
                    condition.output_info['Data'] = np.append(
                        condition.output_info['Data'],
                        start_value
                    )  # Update data to output
                    condition.output_info['Time'] = np.append(
                        condition.output_info['Time'],
                        time.perf_counter()
                    )  # Update time to output
                    """Measure temperature"""
                    condition.output_info['Temperature'] = np.append(
                        condition.output_info['Temperature'],
                        condition.measurement_info['Temperature']
                    )  # Update temperature to output
                    """Measure voltage and current"""
                    condition.output_info['Voltage'] = np.append(
                        condition.output_info['Voltage'],
                        np.median(voltage)
                    )  # Update voltage to output
                    # condition.output_info['Current'] = np.append(
                    #     condition.output_info['Current'],
                    #     condition.measurement_info['Current']
                    # )  # Update current to output
                    start_value = start_value + step_value
                    time.sleep(measurement_period / 2)
            time.sleep(measurement_period / 2)
            condition.test_VI_flag = False  # Stop charge measurement
            time.sleep(1)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition = self.off(condition)
            """Close temperature setting instrument"""
            condition = self.stop_temperature_setting(condition)
            condition = self.temperature_judgement(condition)
            """Close temperature measurement instrument"""
            condition.test_T_flag = False  # Stop charge measurement
            time.sleep(1)
            condition.test_info['Instrument'] = condition.test_info['Temperature_Setting_Instrument']
            condition.test_info['Communication'] = condition.test_info['Temperature_Setting_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            condition = self.close(condition)
            time.sleep(1)
            """Close controlling instrument"""
            condition.test_info['Instrument'] = condition.test_info['Control_Instrument']
            condition = self.close(condition)
            L.info('Finish normal flow')

        except:
            L.error(traceback.format_exc())
            """Close ADC instrument"""
            condition.test_VI_flag = False  # Stop measurement
            time.sleep(1)
            """Close power instrument"""
            condition.test_info['Instrument'] = condition.test_info['Power_Instrument']
            condition.test_info['Communication'] = condition.test_info['Power_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            """Close temperature setting instrument"""
            # condition = self.stop_temperature_setting(condition)
            # condition = self.temperature_judgement(condition)
            """Close temperature measurement instrument"""
            condition.test_T_flag = False  # Stop charge measurement
            time.sleep(1)
            condition.test_info['Instrument'] = condition.test_info['Temperature_Setting_Instrument']
            condition.test_info['Communication'] = condition.test_info['Temperature_Setting_Communication']
            condition = self.open(condition)
            condition = self.off(condition)
            condition = self.close(condition)
            time.sleep(1)
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

if __name__ == '__main__':
    from test.condition.condition import Condition
    from parse.self_logging.logger import Logger

    Logger()
    c = Condition()
    c.test_info['Control_Instrument'] = 'F413ZH'
    c.test_info['Control_Communication'] = 'serial'
    self = Test_Lithium()
    # self.test_external_clk(c)
    # self.test_otp(c)
    self.test_otp(c)

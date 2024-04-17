# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/2/17 14:35
File: tool_plot.py
"""
import copy
import os
import math
import logging
import re
import time

import numpy as np
import pandas as pd
import traceback
import matplotlib.pyplot as plt

from output.result.result_output import Result_Output

L = logging.getLogger('Main')

class ToolPlot(object):

    @staticmethod
    def plot_main(condition):
        """
        Determine plot function, is the ToolPlot main function.

        Args:
            condition: Condition information summary
        """
        if os.path.isdir(condition.config_path) is True:  # Config path is related to folder

            for root, dirs, files in os.walk(condition.config_path):  # Search folder

                for file in files:  # Execute each file in folder

                    if re.search('\.csv|\.xls|\.xlsx', file) is None:
                        continue
                    path = os.path.join(root, file)

                    try:
                        eval('ToolPlot.' + condition.tool_func)(path, condition.saving_path)  # Execute file

                    except:
                        L.error(traceback.format_exc())

        else:  # Config path is related to file
            eval('ToolPlot.plot_' + condition.tool_func)(condition.config_path, condition.saving_path)  # Execute file

    @staticmethod
    def plot_linearity(config_path, saving_path=None):
        """
        Calculate linearity error and plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        """Get original data"""
        file = pd.read_csv(config_path)
        x = np.array(file.iloc[:, 2])
        y = np.array(file.iloc[:, 4])
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        bit = 16  # Bit number
        bit_depth = int(math.pow(2, bit))  # Bit depth

        for i in range(len(y)):

            if msb is not None and y[i] >= msb:
                y[i] = y[i] - bit_depth

            elif lsb is not None and y[i] < lsb:
                y[i] = y[i] + bit_depth
        """Calculate fitting parameter"""
        fitting_a, fitting_b = np.polyfit(x, y, 1)  # Calculate fitting paramter
        new_y = fitting_a * x + fitting_b  # Get fitting data
        INL = y - new_y  # Calculate linearity error
        """Plot figure"""
        fig, ax = plt.subplots(1, 2)
        ax[0].scatter(
            x,
            y,
            s=5,
            c='g',
            marker='o',
            label='Data'
        )  # Plot data figure
        ax[0].scatter(
            x,
            new_y,
            s=5,
            c='r',
            marker='+',
            label='y = ' + str(round(fitting_a, 3)) + '*x + ' + str(round(fitting_b, 3))
        )  # Plot fitting data figure

        ax[0].set_title('data VS fitting data')  # Add title
        ax[0].set_xlabel('Voltage(V)')  # Add x label
        ax[0].set_ylabel('Data(LSB)')  # Add y label
        ax[0].legend(loc="best")  # Add legend
        ax[0].grid(True)  # Show grid

        ax[1].scatter(x, INL, s=5, c='r', marker='o', label='Data')  # Plot INL figure
        ax[1].plot(x, INL)  # Plot INL figure
        ax[1].set_title('Error')  # Add title
        ax[1].set_xlabel('Voltage(V)')  # Add x label
        ax[1].set_ylabel('Error(LSB)')  # Add y label
        ax[1].grid(True)  # Show grid
        """Save figure"""
        if saving_path is not None:
            Result_Output.to_png(
                plt,
                saving_path
            )

        else:
            Result_Output.to_png(
                plt,
                os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0]
            )
        """Show figure"""
        # plt.show()

    @staticmethod
    def plot_dnl(config_path, saving_path=None):
        """
        Calculate DNL, INL and plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        @nb.jit(nopython=True)
        def count_actual_times(data, result):
            result_code = np.array([i for i in range(min(data), max(data))], dtype=np.int32)
            for i in range(len(data)):  # Count actual times
                result[int(data[i]) - min(data)] = result[int(data[i]) - min(data)] + 1
            return result, result_code

        @nb.jit(nopython=True)
        def count_new_data(data, data_temp, min_data, max_data, number):

            for i in range(len(data_temp)):

                if data_temp[i] < min_data:
                    data = np.append(data, np.int32(1))

                elif data_temp[i] > max_data:
                    data = np.append(data, max_data - min_data + np.int32(1))

                elif min_data <= data_temp[i] <= max_data:
                    data = np.append(data, data_temp[i] - min_data + np.int32(1))

                if len(data) == number:
                    break

            return data

        @nb.jit(nopython=True)
        def calculate_inl(inl, dnl):

            for i in range(len(dnl)):

                if i == 0:
                    inl[i] = dnl[i]
                else:
                    inl[i] = inl[i - 1] + dnl[i]

            return inl
        """Set parameter"""
        t1 = time.time()
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        method = 1
        confidence_level = 1.96  # Confidence level
        inl_fitting_flag = True  # Flag of INL fitting
        """Get original data"""
        file = pd.read_csv(config_path)
        data_temp = np.array(file.iloc[:, 4], dtype=np.int32)
        for i in range(len(data_temp)):
            if msb is not None and data_temp[i] > msb:
                data_temp[i] = data_temp[i] - 65536

            elif lsb is not None and data_temp[i] < lsb:
                data_temp[i] = data_temp[i] + 65536

        if method == 1:
            length = max(data_temp) - min(data_temp) + 1
            data_result_num = np.zeros(length, dtype=np.int32)  # Generate actual density array
            data_result_num, data_result_code = count_actual_times(data_temp, data_result_num)
            start_position = np.where(data_result_num == max(data_result_num[0: int(len(data_result_num) / 2)]))[0][0]
            stop_position = np.where(data_result_num == max(data_result_num[int(len(data_result_num) / 2): -1]))[0][0]
            min_data = data_result_code[start_position]
            max_data = data_result_code[stop_position]
            data_result = data_result_num[start_position: stop_position + 1]
            length = max_data - min_data + 1
            """Calculate DNL"""
            error_precision = math.ceil(
                100 * math.sqrt(math.pi * length * np.square(confidence_level) / len(file))
            ) / 100  # Calculate error precision
            print('Confidence level: ' + str(confidence_level))
            print('Error precision: ' + str(error_precision) + 'LSB')
            data = data_temp
            # number = round(
            #     math.pi * length * np.square(confidence_level) / np.square(error_precision)
            # )  # Calculate total sample number
            # data = data_temp[0: number]
            # data_result = np.zeros(length, dtype=np.int32)
            # data_result, data_result_code = count_actual_times(data, data_result)
            # data = np.array([], dtype=np.int32)
            # for i in range(len(data_temp)):
            #
            #     if min_data <= data_temp[i] <= max_data:
            #         data = np.append(data, data_temp[i] - min_data + np.int32(1))
            #
            #     if len(data) == number:
            #         break

            # data_result = np.zeros(length, dtype=np.int32)
            # data_result, data_result_code = count_actual_times(data, data_result)

        elif method == 2:
            data = data_temp
            length = max(data) - min(data) + 1
            error_precision = math.ceil(
                100 * math.sqrt(math.pi * length * np.square(confidence_level) / len(file))
            ) / 100  # Calculate error precision
            print('Confidence level: ' + str(confidence_level))
            print('Error precision: ' + str(error_precision) + 'LSB')
            number = round(
                math.pi * length * np.square(confidence_level) / np.square(error_precision)
            )  # Calculate total sample number
            data = data[0: number]
            data_result = np.zeros(length, dtype=np.int32)
            data_result, data_result_code = count_actual_times(data, data_result)

        data_num = np.array([i + 1 for i in range(length)], dtype=np.int32)  # Generate sample number
        data_ideal = np.zeros(length, dtype=np.float64)  # Generate ideal density array
        for i in range(length):    # Calculate ideal density probability
            data_ideal[i] = 1 / np.pi * (
                    np.arcsin((2 * (i + 1 - length / 2)) / length)
                    -
                    np.arcsin((2 * (i - length / 2)) / length)
            )
        data_result = np.array(data_result, dtype=np.float64)
        data_result = data_result / len(data)

        result_dnl = data_result / data_ideal - 1  # Calculate DNL

        """Calculate INL"""
        result_inl = np.zeros(len(result_dnl))
        result_inl = calculate_inl(result_inl, result_dnl)

        if inl_fitting_flag is True:
            fitting_inl_x, fitting_inl_y = np.polyfit(data_num, result_inl, 1)

            new_result_inl = fitting_inl_x * data_num + fitting_inl_y  # Get fitting data
            result_inl = result_inl - new_result_inl
        """Plot figure"""
        fig, ax = plt.subplots(1, 2)
        ax[0].plot(
            data_num,
            result_dnl
        )  # Plot data figure
        ax[0].set_title('DNL')  # Add title
        ax[0].set_xlabel('Code')  # Add x label
        ax[0].set_ylabel('DNL(LSB)')  # Add y label
        ax[0].grid(True)  # Show grid

        ax[1].plot(
            data_num,
            result_inl
        )  # Plot data figure
        ax[1].set_title('INL')  # Add title
        ax[1].set_xlabel('Code')  # Add x label
        ax[1].set_ylabel('INL(LSB)')  # Add y label
        ax[1].grid(True)  # Show grid

        """Save figure"""
        output = np.array([data_num, result_dnl, result_inl])

        if saving_path is not None:
            Result_Output.to_png(
                plt,
                saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL'
            )

        else:
            Result_Output.to_png(
                plt,
                os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result'
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL'
            )
        """Show figure"""
        # plt.show()
        t2 = time.time()
        print(t2 - t1)

    @staticmethod
    def plot_dnl_sine(config_path, saving_path=None):
        """
        Calculate DNL, INL and plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        @nb.jit(nopython=True)
        def count_actual_times(data, result):
            result_code = np.array([i for i in range(min(data), max(data))], dtype=np.int32)
            for i in range(len(data)):  # Count actual times
                result[int(data[i]) - min(data)] = result[int(data[i]) - min(data)] + 1
            return result, result_code

        @nb.jit(nopython=True)
        def count_new_data(data, data_temp, min_data, max_data, number):

            for i in range(len(data_temp)):

                if data_temp[i] < min_data:
                    data = np.append(data, np.int32(1))

                elif data_temp[i] > max_data:
                    data = np.append(data, max_data - min_data + np.int32(1))

                elif min_data <= data_temp[i] <= max_data:
                    data = np.append(data, data_temp[i] - min_data + np.int32(1))

                if len(data) == number:
                    break

            return data

        @nb.jit(nopython=True)
        def calculate_inl(inl, dnl):

            for i in range(len(dnl)):

                if i == 0:
                    inl[i] = dnl[i]
                else:
                    inl[i] = inl[i - 1] + dnl[i]

            return inl
        """Set parameter"""
        t1 = time.time()
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        confidence_level = 1.96  # Confidence level
        inl_fitting_flag = True  # Flag of INL fitting
        """Get original data"""
        file = pd.read_csv(config_path)
        file_temp = file.drop(file.index[(file.iloc[:, 1] == 0)])
        data_result_num = np.array(file_temp.iloc[:, 1], dtype=np.int32)
        data_result_code = np.array(file_temp.iloc[:, 0], dtype=np.int32)

        start_position = np.where(data_result_num == max(data_result_num[0: int(len(data_result_num) / 2)]))[0][0]
        stop_position = np.where(data_result_num == max(data_result_num[int(len(data_result_num) / 2): -1]))[0][0]
        min_data = data_result_code[start_position]
        max_data = data_result_code[stop_position]
        data_result = data_result_num[start_position: stop_position + 1]
        length = max_data - min_data + 1

        """Calculate DNL"""
        error_precision = math.ceil(
            100 * math.sqrt(math.pi * length * np.square(confidence_level) / sum(data_result))
        ) / 100  # Calculate error precision
        print('Confidence level: ' + str(confidence_level))
        print('Error precision: ' + str(error_precision) + 'LSB')


        data_num = np.array([i + 1 for i in range(length)], dtype=np.int32)  # Generate sample number
        data_ideal = np.zeros(length, dtype=np.float64)  # Generate ideal density array
        for i in range(length):    # Calculate ideal density probability
            data_ideal[i] = 1 / np.pi * (
                    np.arcsin((2 * (i + 1 - length / 2)) / length)
                    -
                    np.arcsin((2 * (i - length / 2)) / length)
            )
        data_result = np.array(data_result, dtype=np.float64)
        data_result = data_result / sum(data_result)

        result_dnl = data_result / data_ideal - 1  # Calculate DNL

        """Calculate INL"""
        result_inl = np.zeros(len(result_dnl))
        result_inl = calculate_inl(result_inl, result_dnl)

        if inl_fitting_flag is True:
            fitting_inl_x, fitting_inl_y = np.polyfit(data_num, result_inl, 1)

            new_result_inl = fitting_inl_x * data_num + fitting_inl_y  # Get fitting data
            result_inl = result_inl - new_result_inl
        """Plot figure"""
        fig, ax = plt.subplots(1, 2)
        ax[0].plot(
            data_num,
            result_dnl
        )  # Plot data figure
        ax[0].set_title('DNL')  # Add title
        ax[0].set_xlabel('Code')  # Add x label
        ax[0].set_ylabel('DNL(LSB)')  # Add y label
        ax[0].grid(True)  # Show grid

        ax[1].plot(
            data_num,
            result_inl
        )  # Plot data figure
        ax[1].set_title('INL')  # Add title
        ax[1].set_xlabel('Code')  # Add x label
        ax[1].set_ylabel('INL(LSB)')  # Add y label
        ax[1].grid(True)  # Show grid

        """Save figure"""
        output = np.array([data_num, result_dnl, result_inl])

        if saving_path is not None:
            Result_Output.to_png(
                plt,
                saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL'
            )

        else:
            Result_Output.to_png(
                plt,
                os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result'
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL'
            )
        """Show figure"""
        # plt.show()
        t2 = time.time()
        print(t2 - t1)

    @staticmethod
    def plot_dnl_ramp(config_path, saving_path=None):
        """
        Calculate DNL, INL and plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        """Set parameter"""
        t1 = time.time()
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        LSB = 0.0000625  # ADC LSB, unit: uV
        inl_fitting_flag = True  # Flag of INL fitting
        file = pd.read_csv(config_path)
        original_code = np.array(file.iloc[:, 4], dtype=np.int32)
        original_voltage = np.array(file.iloc[:, 2], dtype=np.float64)

        for i in range(len(original_code)):

            if msb is not None and original_code[i] >= msb:
                original_code[i] = original_code[i] - 65536

            elif lsb is not None and original_code[i] < lsb:
                original_code[i] = original_code[i] + 65536
        """Get original data"""
        min_code = min(original_code)
        max_code = max(original_code)
        result_dnl = np.zeros([max_code - min_code + 1], dtype=np.float64)
        data_num = np.array(range(0, len(result_dnl)), dtype=np.int32)
        code_time = []
        code = min_code

        for i in range(len(result_dnl)):
            voltage = original_voltage[np.where(original_code == code)]

            if len(voltage) == 0:  # Missing code
                result_dnl[i] = -1

            elif len(voltage) == 1:
                result_dnl[i] = (min(abs(original_voltage - voltage[0])) - LSB) / LSB

            else:
                result_dnl[i] = ((max(voltage) - min(voltage)) - LSB) / LSB

            code_time.append(len(voltage))

            code = code + 1

        """Calculate INL"""
        result_inl = np.zeros(len(result_dnl))
        for i in range(len(result_dnl)):

            if i == 0:
                result_inl[i] = result_dnl[i]
            else:
                result_inl[i] = result_inl[i - 1] + result_dnl[i]

        if inl_fitting_flag is True:
            fitting_inl_x, fitting_inl_y = np.polyfit(data_num, result_inl, 1)

            new_result_inl = fitting_inl_x * data_num + fitting_inl_y  # Get fitting data
            result_inl = result_inl - new_result_inl
        """Plot figure"""
        fig, ax = plt.subplots(1, 2)
        ax[0].plot(
            data_num,
            result_dnl
        )  # Plot data figure
        ax[0].set_title('DNL')  # Add title
        ax[0].set_xlabel('Code')  # Add x label
        ax[0].set_ylabel('DNL(LSB)')  # Add y label
        ax[0].grid(True)  # Show grid

        ax[1].plot(
            data_num,
            result_inl
        )  # Plot data figure
        ax[1].set_title('INL')  # Add title
        ax[1].set_xlabel('Code')  # Add x label
        ax[1].set_ylabel('INL(LSB)')  # Add y label
        ax[1].grid(True)  # Show grid

        """Save figure"""
        output = np.array([data_num, result_dnl, result_inl, code_time])

        if saving_path is not None:
            Result_Output.to_png(
                plt,
                saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL, Times'
            )

        else:
            Result_Output.to_png(
                plt,
                os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result'
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL, Times'
            )
        """Show figure"""
        # plt.show()
        t2 = time.time()
        print(t2 - t1)

    @staticmethod
    def plot_best_fit(config_path, saving_path=None):
        """
        Calculate DNL, INL and plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        """Set parameter"""
        t1 = time.time()
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        bit = 16  # Bit number
        bit_depth = int(math.pow(2, bit))  # Bit depth
        file = pd.read_csv(config_path)
        original_code = np.array(file.iloc[:, 4], dtype=np.int32)
        original_measurement_voltage = np.array(file.iloc[:, 2], dtype=np.float64)
        original_setting_voltage = np.array(file.iloc[:, 3], dtype=np.float64)

        for i in range(len(original_code)):

            if msb is not None and original_code[i] >= msb:
                original_code[i] = original_code[i] - bit_depth

            elif lsb is not None and original_code[i] < lsb:
                original_code[i] = original_code[i] + bit_depth
        """Get original data"""
        min_code = min(original_code)
        max_code = max(original_code)
        data_num = np.array(range(0, max_code - min_code + 1), dtype=np.int32)
        code = min_code
        fitting_voltage = np.zeros([max_code - min_code + 1], dtype=np.float64)
        code_time = np.zeros([max_code - min_code + 1], dtype=np.int32)
        # for i in range(len(fitting_voltage)):
        #     voltage = original_voltage[np.where(original_code == code)]
        #     code_time[i] = len(voltage)
        #
        #     if len(voltage) == 0:  # Missing code
        #         voltage = original_voltage[np.where(original_code == (code - 1))]
        #         fitting_voltage[i] = max(voltage)
        #         print(str(code) + ' is missing code!')
        #
        #     elif len(voltage) == 1:
        #         fitting_voltage[i] = voltage[0]
        #         print(str(code) + ' is occurred only one time!')
        #
        #     else:
        #         fitting_voltage[i] = np.median(voltage)
        #
        #     code = code + 1
        measurement_voltage = []
        setting_voltage = []
        code_time = []
        data = []
        for j in range(len(data_num)):

            if len(np.where(original_code == code)[0]) <= 0 or \
                    len(np.where(original_code == code)[0]) >= 12:
                pass

            else:
                measurement_voltage.append(
                    np.median(original_measurement_voltage[np.where(original_code == code)]))
                setting_voltage.append(np.median(original_setting_voltage[np.where(original_code == code)]))
                code_time.append(len(original_measurement_voltage[np.where(original_code == code)]))
                data.append(code)
            code = code + 1
        data_num = data

        poly = np.polyfit(data_num, measurement_voltage, 1)
        new_fitting_voltage = np.polyval(poly, data_num)
        result_voltage = measurement_voltage - new_fitting_voltage

        """Calculate INL"""
        result_inl = result_voltage / poly[0]
        result_dnl = np.zeros(len(data_num))

        for i in range(len(result_inl)):

            if i == 0:
                result_dnl[i] = result_inl[i]
            else:
                result_dnl[i] = result_inl[i] - result_inl[i - 1]
        """Plot figure"""
        fig, ax = plt.subplots(1, 2)
        ax[0].plot(
            data_num,
            result_dnl
        )  # Plot data figure
        ax[0].set_title('DNL')  # Add title
        ax[0].set_xlabel('Code')  # Add x label
        ax[0].set_ylabel('DNL(LSB)')  # Add y label
        ax[0].grid(True)  # Show grid

        ax[1].plot(
            data_num,
            result_inl
        )  # Plot data figure
        ax[1].set_title('INL')  # Add title
        ax[1].set_xlabel('Code')  # Add x label
        ax[1].set_ylabel('INL(LSB)')  # Add y label
        ax[1].grid(True)  # Show grid

        """Save figure"""
        output = np.array([data_num, result_dnl, result_inl, measurement_voltage, new_fitting_voltage, code_time])

        if saving_path is not None:
            Result_Output.to_png(
                plt,
                saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL, Vol, F-Vol, Times',
                length='8'
            )

        else:
            Result_Output.to_png(
                plt,
                os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result'
            )
            Result_Output.to_csv(
                np.transpose(output),
                path=os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
                header='Data, DNL, INL, Vol, F-Vol, Times',
                length='8'
            )
        """Show figure"""
        # plt.show()
        t2 = time.time()
        print(t2 - t1)

    @staticmethod
    def plot_4_best_fit(config_path, saving_path=None):
        """
        Calculate DNL, INL and plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        """Set parameter"""
        t1 = time.time()
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        FSR = 4.096
        LSB = 0.00007629  # ADC LSB, unit: uV
        method = 1  # Flag of INL fitting
        file = pd.read_csv(config_path)
        original_code = []

        for i in range(4):

            if file.iloc[0, 4 + i] == file.iloc[0, 4 + i]:
                original_code_temp = np.array(file.iloc[:, 4 + i], dtype=np.int32)
                original_code.append(original_code_temp)
        original_measurement_voltage = np.array(file.iloc[:, 2], dtype=np.float64)
        original_setting_voltage = np.array(file.iloc[:, 3], dtype=np.float64)

        for i in range(len(original_code)):
            original_code_temp = original_code[i]

            for j in range(len(original_code_temp)):

                if msb is not None and original_code_temp[j] >= msb:
                    original_code_temp[j] = original_code_temp[j] - 65536

                elif lsb is not None and original_code_temp[j] < lsb:
                    original_code_temp[j] = original_code_temp[j] + 65536

            if method == 1:
                """Get original data"""
                min_code = min(original_code_temp)
                max_code = max(original_code_temp)
                code = min_code
                data_num = np.array(range(0, max_code - min_code + 1), dtype=np.int32)
                # measurement_voltage = np.zeros([max_code - min_code + 1], dtype=np.float64)
                # setting_voltage = np.zeros([max_code - min_code + 1], dtype=np.float64)
                # code_time = np.zeros([max_code - min_code + 1], dtype=np.int32)
                #
                # for j in range(len(measurement_voltage)):
                #     measurement = original_measurement_voltage[np.where(original_code_temp == code)]
                #     setting = original_setting_voltage[np.where(original_code_temp == code)]
                #     code_time[j] = len(measurement)
                #
                #     if len(measurement) == 0:  # Missing code
                #         measurement = original_measurement_voltage[np.where(original_code_temp == (code - 1))]
                #         setting = original_setting_voltage[np.where(original_code_temp == (code - 1))]
                #         measurement_voltage[j] = max(measurement)
                #         setting_voltage[j] = max(setting)
                #         print(str(code) + ' is missing code!')
                #
                #     elif len(measurement) == 1:
                #         measurement_voltage[j] = measurement[0]
                #         setting_voltage[j] = setting[0]
                #         print(str(code) + ' is occurred only one time!')
                #
                #     else:
                #         measurement_voltage[j] = np.median(measurement)
                #         setting_voltage[j] = np.median(setting)
                #     code = code + 1

                measurement_voltage = []
                setting_voltage = []
                code_time = []
                data = []
                for j in range(len(data_num)):

                    if len(np.where(original_code_temp == code)[0]) <= 1 or \
                            len(np.where(original_code_temp == code)[0]) >= 11:
                        pass

                    else:
                        measurement_voltage.append(np.median(original_measurement_voltage[np.where(original_code_temp == code)]))
                        setting_voltage.append(np.median(original_setting_voltage[np.where(original_code_temp == code)]))
                        code_time.append(len(original_measurement_voltage[np.where(original_code_temp == code)]))
                        data.append(code)
                    code = code + 1
                data_num = data

                poly = np.polyfit(data_num, measurement_voltage, 1)  # measurement, code
                new_measurement_data = np.polyval(poly, data_num)
                result_measurement_data = measurement_voltage - new_measurement_data

                poly = np.polyfit(data_num, setting_voltage, 1)  # measurement, code
                new_setting_data = np.polyval(poly, data_num)
                result_setting_data = setting_voltage - new_setting_data

                poly = np.polyfit(setting_voltage, measurement_voltage, 1)  # measurement, code
                new_setting_measurement = np.polyval(poly, setting_voltage)
                result_setting_measurement = measurement_voltage - new_setting_measurement

                result_inl = (result_measurement_data) / LSB
                result_dnl = np.zeros(len(data_num))

                for j in range(len(result_inl)):

                    if j == 0:
                        result_dnl[j] = result_inl[j]
                    else:
                        result_dnl[j] = result_inl[j] - result_inl[j - 1]
                """Plot figure"""
                fig, ax = plt.subplots(1, 2)
                ax[0].plot(
                    data_num,
                    result_dnl
                )  # Plot data figure
                ax[0].set_title('DNL')  # Add title
                ax[0].set_xlabel('Code')  # Add x label
                ax[0].set_ylabel('DNL(LSB)')  # Add y label
                ax[0].grid(True)  # Show grid

                ax[1].plot(
                    data_num,
                    result_inl
                )  # Plot data figure
                ax[1].set_title('INL')  # Add title
                ax[1].set_xlabel('Code')  # Add x label
                ax[1].set_ylabel('INL(LSB)')  # Add y label
                ax[1].grid(True)  # Show grid

                """Save figure"""
                output = np.array([data_num, result_dnl, result_inl, measurement_voltage, new_measurement_data, code_time])

                if saving_path is not None:
                    Result_Output.to_png(
                        plt,
                        saving_path,
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i)
                    )
                    Result_Output.to_csv(
                        np.transpose(output),
                        path=saving_path,
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i),
                        header='Data, DNL, INL, Vol, F-Data, Times',
                        length='8'
                    )

                else:
                    Result_Output.to_png(
                        plt,
                        os.path.dirname(config_path),
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i)
                    )
                    Result_Output.to_csv(
                        np.transpose(output),
                        path=os.path.dirname(config_path),
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i),
                        header='Data, DNL, INL, Vol, F-Data, Times',
                        length='8'
                    )
                """Show figure"""
                # plt.show()
                t2 = time.time()
                print(t2 - t1)

            if method == 2:
                """Get original data"""
                min_code = min(original_code_temp)
                max_code = max(original_code_temp)
                fitting_voltage = np.zeros([max_code - min_code + 1], dtype=np.float64)
                data_num = np.array(range(min_code, max_code + 1), dtype=np.int32)
                code = min_code
                code_time = np.zeros([max_code - min_code + 1], dtype=np.int32)

                for j in range(len(fitting_voltage)):
                    voltage = original_measurement_voltage[np.where(original_code_temp == code)]
                    code_time[j] = len(voltage)

                    if len(voltage) == 0:  # Missing code
                        voltage = original_measurement_voltage[np.where(original_code_temp == (code - 1))]
                        fitting_voltage[j] = max(voltage)
                        print(str(code) + ' is missing code!')

                    elif len(voltage) == 1:
                        fitting_voltage[j] = voltage[0]
                        print(str(code) + ' is occurred only one time!')

                    else:
                        fitting_voltage[j] = np.median(voltage)

                    code = code + 1
                adc_reading = data_num * FSR / pow(2, 16)
                adc_gain_correction = adc_reading * (
                        fitting_voltage[-1] - fitting_voltage[0]
                ) / (
                        adc_reading[-1] - adc_reading[0]
                )
                adc_offset_correction = adc_gain_correction - (adc_gain_correction[0] - fitting_voltage[0])
                error = adc_offset_correction - fitting_voltage

                """Calculate INL"""
                result_inl = error / LSB
                result_dnl = np.zeros(len(data_num))

                for j in range(len(result_inl)):

                    if j == 0:
                        result_dnl[j] = result_inl[j]
                    else:
                        result_dnl[j] = result_inl[j] - result_inl[j - 1]
                """Plot figure"""
                fig, ax = plt.subplots(1, 2)
                ax[0].plot(
                    data_num,
                    result_dnl
                )  # Plot data figure
                ax[0].set_title('DNL')  # Add title
                ax[0].set_xlabel('Code')  # Add x label
                ax[0].set_ylabel('DNL(LSB)')  # Add y label
                ax[0].grid(True)  # Show grid

                ax[1].plot(
                    data_num,
                    result_inl
                )  # Plot data figure
                ax[1].set_title('INL')  # Add title
                ax[1].set_xlabel('Code')  # Add x label
                ax[1].set_ylabel('INL(LSB)')  # Add y label
                ax[1].grid(True)  # Show grid

                """Save figure"""
                output = np.array([data_num, result_dnl, result_inl, code_time])

                if saving_path is not None:
                    Result_Output.to_png(
                        plt,
                        saving_path,
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i)
                    )
                    Result_Output.to_csv(
                        np.transpose(output),
                        path=saving_path,
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i),
                        header='Data, DNL, INL, Times',
                        length='8'
                    )

                else:
                    Result_Output.to_png(
                        plt,
                        os.path.dirname(config_path),
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i)
                    )
                    Result_Output.to_csv(
                        np.transpose(output),
                        path=os.path.dirname(config_path),
                        name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result' + str(i),
                        header='Data, DNL, INL, Times',
                        length='8'
                    )
                """Show figure"""
                # plt.show()
                t2 = time.time()
                print(t2 - t1)

    @staticmethod
    def plot_noise(config_path, saving_path=None):
        """
        Calculate noise plot figure

        Args:
            config_path: Original data path, format: str.
            saving_path: Saving figure path, format: str
        """
        """Set parameter"""
        t1 = time.time()
        msb = 32768  # Data convert param, format: int or None
        lsb = None  # Data convert param, format: int or None
        bit = 16  # Bit number
        bit_depth = int(math.pow(2, bit))  # Bit depth
        file = pd.read_csv(config_path)
        original_code = np.array(file.iloc[:, 4], dtype=np.int32)

        for i in range(len(original_code)):

            if msb is not None and original_code[i] >= msb:
                original_code[i] = original_code[i] - bit_depth

            elif lsb is not None and original_code[i] < lsb:
                original_code[i] = original_code[i] + bit_depth

        """Calculate data"""
        mean_value = np.mean(original_code)  # Calculate median value of original_code
        median_value = np.median(original_code)  # Calculate median value of original_code
        std_deviation = np.std(original_code)  # Calculate std deviation of original_code
        min_value = min(original_code)
        max_value = max(original_code)
        dataframe = pd.DataFrame(original_code)
        """Plot figure"""
        # plt.hist(original_code, bins=30, alpha=0.8)
        dataframe.hist()
        plt.xlabel('Code')
        plt.ylabel('Number')
        plt.title('Histogram of Code')
        plt.figtext(0.95, 0.95, f'Standard Deviation: {std_deviation:.2f}', horizontalalignment='right', verticalalignment='top')
        plt.figtext(0.95, 0.90, f'Mean: {mean_value:.2f}', horizontalalignment='right', verticalalignment='top')
        plt.figtext(0.95, 0.85, f'Median: {median_value:.2f}', horizontalalignment='right', verticalalignment='top')
        plt.figtext(0.95, 0.80, f'Max: {max_value:.2f}', horizontalalignment='right', verticalalignment='top')
        plt.figtext(0.95, 0.75, f'Min: {min_value:.2f}', horizontalalignment='right', verticalalignment='top')
        """Save figure"""

        if saving_path is not None:
            Result_Output.to_png(
                plt,
                saving_path,
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result',
            )

        else:
            Result_Output.to_png(
                plt,
                os.path.dirname(config_path),
                name=(os.path.basename(config_path)).split(os.path.splitext(config_path)[-1])[0] + '-result'
            )

        """Show figure"""
        # plt.show()
        t2 = time.time()
        print(t2 - t1)

if __name__ == '__main__':
    from test.condition.condition import Condition
    condition = Condition()

    path = r'C:\Users\ww\Desktop\jupiter\Noise'

    condition.config_path = path
    condition.tool_func = 'plot_noise'
    condition = ToolPlot.plot_main(condition)
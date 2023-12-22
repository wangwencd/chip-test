# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/5 13:55
File: parse_custom_test.py
"""

import re
import time
import logging

from parse.file.file_operation import File_Operation

L = logging.getLogger('Main')

class Parse_Custom_Test:

    @classmethod
    def parse(cls, condition):
        """
        Get condition file from path, and convert into dict

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        file = File_Operation.find_file(condition.config_path, 'xlsx')
        condition.file = File_Operation.get_dataframe_from_first(file)
        condition.test_VI_flag = True
        condition.test_T_flag = True
        condition.measurement_flag = True

        return condition

    @classmethod
    def get_condition(cls, condition):
        """
        Get condition of judgement and run judgement according to content in Condition.
        Judgement items are included: Voltage, Current, Temperature, Time.
        Judgement methods are included: <, >, <=, >=, ==, !=.
        Condition methods between judgements are included： and, or.
        The maximum of judgement num is 3(thus num could be 0, 1, 2, 3).
        If num is 0:
            Judgement will be passed.
        If num is 1:
            Judgement will be like: if a > b.
        If num is 2:
            Judgement will be like: if a > b and c <= d.
        If num is 3:
            Judgement will be like: if (a > b and c <= d) or e == f.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        """Get Condition info of this step"""
        # condition.test_info = condition.test_info.to_dict()
        string = str(condition.test_info['Condition'])
        """Get judgement num"""
        element_num = len(re.findall('<|>|<=|>=|==|!=', string))
        L.info('Judgement num is ' + str(element_num))
        """Get condition methods between judgements"""
        for index, value in enumerate(re.findall(',|;', string)):
            condition.test_info['condition_method' + '_' + str(index)] = value
        """Get every judgement info, including judgement item, method, target value"""
        for index, value in enumerate(re.findall('\w+[ ]?(?:<|>|<=|>=|==|\!=)[ ]?\d+[\.]?\d*', string)):
            [
                condition.test_info['judgement_item' + '_' + str(index)], # Get judgement item
                condition.test_info['judgement_method' + '_' + str(index)], # Get judgement method
                condition.test_info['judgement_value' + '_' + str(index)] # Get judgement target value
            ] = re.split('(<|>|<=|>=|==|!=)', value)
        """Get priority of condition method"""
        if re.search('\(.+\)', string) is not None:
            condition.test_info['position'] = str(re.findall('<|>|<=|>=|==|!=|\(|\)', string).index('(') + 1) +\
                                              ',' +\
                                              str(re.findall('<|>|<=|>=|==|!=|\(|\)', string).index(')') - 1)
            # pos_left = []
            # pos_right = []
            # for index, value in enumerate(re.findall('<|>|<=|>=|==|!=|\(|\)', string)):
            #     pos_left.append(index) if value == '(' else pos_left
            #     pos_right.append(index) if value == '(' else pos_right

        if element_num == 0:  # Num is 0
            pass

        elif element_num == 1:  # Num is 1
            cls.t1 = time.time()

            while True:
                result = cls.judge_one(
                    condition,
                    condition.test_info['judgement_item_0'],
                    condition.test_info['judgement_method_0'],
                    condition.test_info['judgement_value_0']
                )  # Get result of 1st judgement

                if result:  # Judgements satisfied
                    break
                time.sleep(1)

        elif element_num == 2:  # Num is 2
            cls.t1 = time.time()

            while True:
                result0 = cls.judge_one(
                    condition,
                    condition.test_info['judgement_item_0'],
                    condition.test_info['judgement_method_0'],
                    condition.test_info['judgement_value_0']
                )  # Get result of 1st judgement
                result1 = cls.judge_one(
                    condition,
                    condition.test_info['judgement_item_1'],
                    condition.test_info['judgement_method_1'],
                    condition.test_info['judgement_value_1']
                )  # Get result of 2nd judgement

                if condition.test_info['condition_method_0'] == ',':  # Format is: If a and b

                    if result0 and result1:  # Judgements satisfied
                        break

                elif condition.test_info['condition_method_0'] == ';':  # Format is: If a or b

                    if result0 or result1:  # Judgements satisfied
                        break
                time.sleep(1)

        elif element_num == 3:  # Num is 3
            cls.t1 = time.time()

            while True:
                result0 = cls.judge_one(
                    condition,
                    condition.test_info['judgement_item_0'],
                    condition.test_info['judgement_method_0'],
                    condition.test_info['judgement_value_0']
                )  # Get result of 1st judgement
                result1 = cls.judge_one(
                    condition,
                    condition.test_info['judgement_item_1'],
                    condition.test_info['judgement_method_1'],
                    condition.test_info['judgement_value_1']
                )  # Get result of 2nd judgement
                result2 = cls.judge_one(
                    condition,
                    condition.test_info['judgement_item_2'],
                    condition.test_info['judgement_method_2'],
                    condition.test_info['judgement_value_2']
                )  # Get result of 3rd judgement

                if condition.test_info['condition_method_0'] == ',' \
                        and condition.test_info['condition_method_1'] == ',':  # Format is: If a and b and c

                    if result0 and result1 and result2:  # Judgements satisfied
                        break

                elif condition.test_info['condition_method_0'] == ';' \
                        and condition.test_info['condition_method_1'] == ';':  # Format is: If a or b or c

                    if result0 or result1 or result2:  # Judgements satisfied
                        break

                elif condition.test_info['condition_method_0'] == ',' \
                        and condition.test_info['condition_method_1'] == ';':  # Format is: If a and b or c

                    if condition.test_info['position'] == '1,2':  # Format is: If (a and b) or c

                        if (result0 and result1) or result2:  # Judgements satisfied
                            break

                    elif condition.test_info['position'] == '2,3':  # Format is: If a and (b or c)

                        if result0 and (result1 or result2):  # Judgements satisfied
                            break

                    else:
                        raise ValueError

                elif condition.test_info['condition_method_0'] == ';' \
                        and condition.test_info['condition_method_1'] == ',':  # Format is: If a or b and c

                    if condition.test_info['position'] == '1,2':  # Format is: If (a or b) and c

                        if (result0 or result1) and result2:  # Judgements satisfied
                            break

                    elif condition.test_info['position'] == '2,3':  # Format is: If a or (b and c)

                        if result0 or (result1 and result2):  # Judgements satisfied
                            break

                    else:
                        raise ValueError

        return condition

    @classmethod
    def judge_one(cls, condition, key, cond, value):
        """
        One function to judge <, >, <=, >=, ==, !=

        Args:
            condition: Condition information summary
            key: Name of judgement item, including voltage, current and time
            cond: Method of judgement item, including <, >, <=, >=, ==, !=
            value: Value of judgement item

        Returns:
            Result: Result of judgement, True or False
        """
        def judge(item, cond, value):
            """
            Judge size of something with target value

            Args:
                item: Value of judgement item that need judging
                cond: Method of judgement item
                value: Target value of judgement item

            Returns:
                Result: True or False
            """
            if re.search('<(?!=)', cond) is not None:  # If a < b

                if item < value:  # Judgements satisfied
                    return True

                else:  # Judgements not satisfied
                    return False

            elif re.search('>(?!=)', cond) is not None:  # If a > b

                if item > value:  # Judgements satisfied
                    return True

                else:  # Judgements not satisfied
                    return False

            elif re.search('<=', cond) is not None:  # If a <= b

                if item <= value:  # Judgements satisfied
                    return True

                else:  # Judgements not satisfied
                    return False

            elif re.search('>=', cond) is not None:  # If a >= b

                if item >= value:  # Judgements satisfied
                    return True

                else:  # Judgements not satisfied
                    return False

            elif re.search('==', cond) is not None:  # if a == b

                if item == value:  # Judgements satisfied
                    return True

                else:  # Judgements not satisfied
                    return False

            elif re.search('\!=', cond) is not None:  # if a != b

                if item != value:  # Judgements satisfied
                    return True

                else:  # Judgements not satisfied
                    return False

        value = float(value)

        if re.search('Voltage|Vol', key, re.I) is not None:  # If judgement item is voltage

            try:
                item = condition.measurement_info['Voltage']

            except:
                L.error('Could not measure voltage value!')
            result = judge(item, cond, value)

        elif re.search('Current|Cur', key, re.I) is not None:  # If judgement item is current

            try:
                item = condition.measurement_info['Current']

            except:
                L.error('Could not measure current value!')
            result = judge(item, cond, value)

        elif re.search('Temperature|Tem', key, re.I) is not None:  # If judgement item is temperature

            try:
                item = condition.measurement_info['Temperature']

            except:
                L.error('Could not measure temperature value!')
            result = judge(item, cond, value)

        elif re.search('Time', key, re.I) is not None:  # If judgement item is time
            cls.t2 = time.time()
            item = cls.t2 - cls.t1
            result = judge(item, cond, value)

        return result

    # @staticmethod
    # def cal_voltage(condition):
    #     """
    #     Calculate average value of voltage
    #
    #     Args:
    #         condition: Condition information summary
    #
    #     Returns:
    #         condition: Condition information summary
    #     """
    #     flag = True
    #     voltage_sum = []
    #     num = 10
    #
    #     while flag:
    #
    #             while condition.measurement_flag == True: # measuring voltage data updated
    #                 voltage_sum.append(float(condition.measurement_info['Voltage']))
    #                 condition.measurement_flag = False
    #
    #                 if len(voltage_sum) == num: # Collect enough data
    #                     flag = False
    #                     break
    #     condition.measurement_info['Ave_Voltage'] = 1000 * sum(voltage_sum) / num # Calculate average of voltage
    #
    #     return condition
    #
    # @staticmethod
    # def cal_current(condition):
    #     """
    #     Calculate average value of current
    #
    #     Args:
    #         condition: Condition information summary
    #
    #     Returns:
    #         condition: Condition information summary
    #     """
    #     flag = True
    #     current_sum = []
    #     num = 10
    #
    #     while flag:
    #
    #             while condition.measurement_flag == True: # measuring voltage data updated
    #                 current_sum.append(float(condition.measurement_info['Current']))
    #                 condition.measurement_flag = False
    #
    #                 if len(current_sum) == num: # Collect enough data
    #                     flag = False
    #                     break
    #     condition.measurement_info['Ave_Current'] = 1000 * sum(current_sum) / num # Calculate average of current
    #
    #     return condition
    #
    # @staticmethod
    # def cal_voltage_and_current(condition):
    #     """
    #     Calculate average value of voltage and current
    #
    #     Args:
    #         condition: Condition information summary
    #
    #     Returns:
    #         condition: Condition information summary
    #     """
    #     flag = True
    #     voltage_sum = []
    #     current_sum = []
    #     num = 10
    #
    #     while flag:
    #
    #             while condition.measurement_flag == True: # measuring voltage data updated
    #                 voltage_sum.append(float(condition.measurement_info['Voltage']))
    #                 current_sum.append(float(condition.measurement_info['Current']))
    #                 condition.measurement_flag = False
    #
    #                 if len(voltage_sum) == num and len(current_sum) == num: # Collect enough data
    #                     flag = False
    #                     break
    #     condition.measurement_info['Ave_Voltage'] = 1000 * sum(voltage_sum) / num  # Calculate average of voltage
    #     condition.measurement_info['Ave_Current'] = 1000 * sum(current_sum) / num # Calculate average of current
    #
    #     return condition


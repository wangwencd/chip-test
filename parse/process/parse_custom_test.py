# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/5 13:55
File: parse_custom_test.py
"""
import copy
import re
import time
import logging
import pandas as pd
import numpy as np

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
        condition = Parse_Custom_Test.parse_file(condition)
        condition.reset_output_info()
        condition.test_info_temp = {}
        condition.test_VI_flag = True
        condition.test_T_flag = True
        condition.measurement_flag = True

        return condition

    @staticmethod
    def parse_condition(condition):
        """
        Parse condition of judgement and run judgement according to content in Condition.
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
        # L.info('Judgement num is ' + str(element_num))
        """Get condition methods between judgements"""
        for index, value in enumerate(re.findall(',|;', string)):
            condition.test_info['condition_method' + '_' + str(index)] = value
        """Get every judgement info, including judgement item, method, target value"""
        for index, value in enumerate(re.findall('\w+[ ]?(?:<|>|<=|>=|==|\!=)[ ]?\d+[\.]?\d*', string)):
            [
                condition.test_info['judgement_item' + '_' + str(index)], # Get judgement item
                condition.test_info['judgement_method' + '_' + str(index)], # Get judgement method
                condition.test_info['judgement_value' + '_' + str(index)] # Get judgement target value
            ] = re.split('(<=|>=|<|>|==|!=)', value)
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
            condition.condition_flag = False

        elif element_num == 1:  # Num is 1
            result = Parse_Custom_Test.judge_one(
                condition,
                condition.test_info['judgement_item_0'],
                condition.test_info['judgement_method_0'],
                condition.test_info['judgement_value_0']
            )  # Get result of 1st judgement

            if result:  # Judgements satisfied
                condition.condition_flag = False
            else:  # Judgements not satisfied
                condition.condition_flag = True

        elif element_num == 2:  # Num is 2

            result0 = Parse_Custom_Test.judge_one(
                condition,
                condition.test_info['judgement_item_0'],
                condition.test_info['judgement_method_0'],
                condition.test_info['judgement_value_0']
            )  # Get result of 1st judgement
            result1 = Parse_Custom_Test.judge_one(
                condition,
                condition.test_info['judgement_item_1'],
                condition.test_info['judgement_method_1'],
                condition.test_info['judgement_value_1']
            )  # Get result of 2nd judgement

            if condition.test_info['condition_method_0'] == ',':  # Format is: If a and b

                if result0 and result1:  # Judgements satisfied
                    condition.condition_flag = False
                else:  # Judgements not satisfied
                    condition.condition_flag = True

            elif condition.test_info['condition_method_0'] == ';':  # Format is: If a or b

                if result0 or result1:  # Judgements satisfied
                    condition.condition_flag = False
                else:  # Judgements not satisfied
                    condition.condition_flag = True

        elif element_num == 3:  # Num is 3

            result0 = Parse_Custom_Test.judge_one(
                condition,
                condition.test_info['judgement_item_0'],
                condition.test_info['judgement_method_0'],
                condition.test_info['judgement_value_0']
            )  # Get result of 1st judgement
            result1 = Parse_Custom_Test.judge_one(
                condition,
                condition.test_info['judgement_item_1'],
                condition.test_info['judgement_method_1'],
                condition.test_info['judgement_value_1']
            )  # Get result of 2nd judgement
            result2 = Parse_Custom_Test.judge_one(
                condition,
                condition.test_info['judgement_item_2'],
                condition.test_info['judgement_method_2'],
                condition.test_info['judgement_value_2']
            )  # Get result of 3rd judgement

            if condition.test_info['condition_method_0'] == ',' \
                    and condition.test_info['condition_method_1'] == ',':  # Format is: If a and b and c

                if result0 and result1 and result2:  # Judgements satisfied
                    condition.condition_flag = False
                else:  # Judgements not satisfied
                    condition.condition_flag = True

            elif condition.test_info['condition_method_0'] == ';' \
                    and condition.test_info['condition_method_1'] == ';':  # Format is: If a or b or c

                if result0 or result1 or result2:  # Judgements satisfied
                    condition.condition_flag = False
                else:  # Judgements not satisfied
                    condition.condition_flag = True

            elif condition.test_info['condition_method_0'] == ',' \
                    and condition.test_info['condition_method_1'] == ';':  # Format is: If a and b or c

                if condition.test_info['position'] == '1,2':  # Format is: If (a and b) or c

                    if (result0 and result1) or result2:  # Judgements satisfied
                        condition.condition_flag = False
                    else:  # Judgements not satisfied
                        condition.condition_flag = True

                elif condition.test_info['position'] == '2,3':  # Format is: If a and (b or c)

                    if result0 and (result1 or result2):  # Judgements satisfied
                        condition.condition_flag = False
                    else:  # Judgements not satisfied
                        condition.condition_flag = True

                else:
                    raise ValueError

            elif condition.test_info['condition_method_0'] == ';' \
                    and condition.test_info['condition_method_1'] == ',':  # Format is: If a or b and c

                if condition.test_info['position'] == '1,2':  # Format is: If (a or b) and c

                    if (result0 or result1) and result2:  # Judgements satisfied
                        condition.condition_flag = False
                    else:  # Judgements not satisfied
                        condition.condition_flag = True

                elif condition.test_info['position'] == '2,3':  # Format is: If a or (b and c)

                    if result0 or (result1 and result2):  # Judgements satisfied
                        condition.condition_flag = False
                    else:  # Judgements not satisfied
                        condition.condition_flag = True

                else:
                    raise ValueError

        return condition

    @staticmethod
    def judge_one(condition, key, cond, value):
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
            item = float(item)
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
            condition.stop_time = time.time()
            item = condition.stop_time - condition.start_time
            result = judge(item, cond, value)

        return result

    @staticmethod
    def parse_param_string(parameter: str):
        """
        Parse one Function string in test file.

        Args:
            parameter: Function string needed to be parsed.

        Returns:
            result: Parsed result, format: dict
        """
        result = {}
        if parameter != parameter:  # parameter is nan
            result = {None: None}
            return result

        elif re.search('=', parameter) is None:  # parameter don't have function name
            result[parameter] = [None]
            return result

        elif re.search(';', parameter) is None:  # parameter has function name
            key = parameter.split('=')[0]  # str on the left of symbol
            value = parameter.split('=')[1]  # str on the right of symbol

            if re.search(':', parameter) is not None and\
                    re.search('(\{.+:.+\})', parameter) is None:  # parameter has more than 1 step

                if value.count(':') == 1:  # value has start, end
                    start_value = float(value.split(':')[0])
                    end_value = float(value.split(':')[1])
                    result[key] = [start_value, end_value]

                elif value.count(':') == 2:  # value has start, step, end
                    start_value = float(value.split(':')[0])
                    step_value = float(value.split(':')[1])
                    end_value = float(value.split(':')[2])
                    target_value = []

                    if start_value <= end_value:  # start is less than end in value
                        while start_value <= end_value:
                            target_value.append(start_value)
                            start_value = start_value + step_value
                        result[key] = target_value

                    elif start_value >= end_value:  # start is more than end in value
                        while start_value >= end_value:
                            target_value.append(start_value)
                            start_value = start_value + step_value
                        result[key] = target_value

            else:    # parameter has only 1 step
                result[key] = [value]
                return result

        elif re.search(';', parameter) is not None:  # parameter has more than 1 command
            command = parameter.split(';')

            for i in range(len(command)):
                temp = Parse_Custom_Test.parse_param_string(command[i])  # Repeat parsing
                result.update(temp)

        return result

    @staticmethod
    def parse_one_param(parameter: str):
        """
        Parse one Parameter string in test file.

        Args:
            parameter: Parameter string need to be parsed

        Returns:
            result: Parsed result, format: dict
        """

        result = Parse_Custom_Test.parse_param_string(parameter)
        step_length = 1

        for value in result.values():
            step_length = len(value) * step_length  # Calculate total length

        if step_length == 0:
            return result

        for key, value in result.items():
            new_value = []
            multiple = int(step_length / len(value))  # Calculate multiple of this parameter needed

            for i in range(multiple):
                new_value.extend(value)  # Complete parameter according to total step length
            result[key] = new_value  # Put parameter into dict

        return result

    @staticmethod
    def parse_one_next(parameter):
        """
        Parse one Next string in test file.

        Args:
            parameter: Next string need to be parsed

        Returns:
            result: Parsed result, format: list
        """
        result = []
        if parameter != parameter or parameter == 'nan':  # parameter is nan
            return np.nan

        elif re.match('\d+', parameter) is not None:  # parameter is a number
            result.extend(parameter)

        elif re.match('{|}', parameter) is not None:  # parameter is a small cycle
            result = \
                list(
                    map(
                        int, re.findall('\d+', parameter)
                    )
                )  # Get all cycle step and convert into a list

        return result

    @staticmethod
    def parse_file(condition):
        """
        Parse test file, and extend all test items.

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        def copy_deep(df):
            """Custom function for deep copying using Numba."""
            target = copy.deepcopy(df)
            for column_name in df.columns:
                target.at[target.index[0], column_name] = copy.deepcopy(df.at[df.index[0], column_name])
            return target
        file = condition.file
        """Extend Parameter function"""
        new_file_temp = []
        target_file_temp = []
        t1 = time.time()
        for i in range(len(file.index)):
            this_line = (file.loc[file.index == i]).copy(deep=True)
            function = Parse_Custom_Test.parse_param_string(str(this_line.at[i, 'Function']))  # Parse function string
            this_line.at[i, 'Function'] = function
            parameter = Parse_Custom_Test.parse_one_param(str(this_line.at[i, 'Parameter']))  # Parse parameter string
            this_line.at[i, 'Parameter'] = parameter
            next = Parse_Custom_Test.parse_one_next(str(this_line.at[i, 'Next']))  # Parse next string
            this_line.at[i, 'Next'] = next
            if len(list(parameter.values())[0]) <= 1:  # No step in Parameter
                new_file_temp.append(this_line)    # Append this test item of file to new file
            else:  # A step in Parameter
                for j in range(len(list(parameter.values())[0])):
                    temp = this_line.copy(deep=True)
                    temp.at[i, 'Parameter'] = {}
                    for key, value in parameter.items():
                        temp.loc[i, 'Parameter'].update({key: value[j]})
                    new_file_temp.append(temp)    # Append this test item of file to new file
        new_file = pd.concat(new_file_temp, axis=0)  # Convert a list into a dataframe
        new_file.reset_index(drop=True, inplace=True)  # Reset index of dataframe
        t2 = time.time()
        print(t2 - t1)
        """Extend Next function"""
        for i in range(len(new_file.index)):
            this_line = copy_deep(new_file.loc[new_file.index == i])
            # this_line = (new_file.loc[new_file.index == i]).copy(deep=True)
            next = this_line.at[i, 'Next']
            if next != next or len(next) <= 1:
                target_file_temp.append(this_line)  # Append this test item of file to new file
            elif len(next) > 1:  # A cycle in Next
                for j in range(len(next)):
                    if this_line.at[i, 'Step'] == next[j]:  # Current line is the line that needed to add
                        # temp = this_line.copy(deep=True)
                        temp = copy_deep(this_line)
                        temp.at[i, 'Next'] = np.nan
                        """Solve the problem of nested object sharing"""
                        # temp.at[i, 'Function'] = copy.deepcopy(this_line.at[i, 'Function'])
                        # temp.at[i, 'Parameter'] = copy.deepcopy(this_line.at[i, 'Parameter'])
                    else:  # Current line is not the line that needed to add
                        # temp = (new_file.loc[new_file['Step'] == next[j]]).copy(deep=True)
                        temp = copy_deep(new_file.loc[new_file['Step'] == next[j]])
                        temp.at[temp.index[0], 'Next'] = np.nan
                        """Solve the problem of nested object sharing"""
                        # temp.at[temp.index[0], 'Function'] = copy.deepcopy(temp.at[temp.index[0], 'Function'])
                        # temp.at[temp.index[0], 'Parameter'] = copy.deepcopy(temp.at[temp.index[0], 'Parameter'])
                    target_file_temp.append(temp)  # Append this test item of file to new file
            else:  # No cycle in Next
                target_file_temp.append(this_line)  # Append this test item of file to new file
        target_file = pd.concat(target_file_temp, axis=0)  # Convert a list into a dataframe
        target_file.reset_index(drop=True, inplace=True)  # Reset index of dataframe
        t3 = time.time()
        print(t3 - t2)
        """Update test file information"""
        for i in range(len(target_file.index)):
            target_file.at[i, 'Step'] = i
            target_file.at[i, 'Function'] = Parse_Custom_Test.update_function(target_file.at[i, 'Function'])
            target_file.at[i, 'Parameter'] = Parse_Custom_Test.update_parameter(target_file.at[i, 'Parameter'])
            target_file.at[i, 'Next'] = Parse_Custom_Test.update_next(target_file.at[i, 'Next'])
        condition.file = target_file
        t4 = time.time()
        print(t4 - t3)
        return condition

    @staticmethod
    def update_function(parameter: dict):
        """
        Update Function string in test file.

        Args:
            parameter: Function string before updating

        Returns:
            parameter: Function string after updating
        """
        for key, value in parameter.items():

            if value is None or value[0] is None:  # Format: {A: None} or {A: [None]}
                parameter[key] = None  # To format: {A: None}
            else:  # Format: {A: [B]}
                parameter[key] = value[0]  # To format: {A: B}
        return parameter

    @staticmethod
    def update_parameter(parameter: dict):
        """
        Update Parameter string in test file.

        Args:
            parameter: Parameter string before updating

        Returns:
            parameter: Parameter string after updating
        """
        for key, value in parameter.items():

            if isinstance(value, list):  # Format: {A:[B]}
                try:
                    value = eval(value[0])  # To format: {A: B(float)}
                except:
                    value = str(value[0])  # To format: {A: B(str)}
                parameter[key] = value

            elif isinstance(value, str):  # Format: {A:(str)}
                try:
                    parameter[key] = eval(value)  # To format: {A: B(float)} or {A: B(dict)} or {A: B(list)}
                except:
                    parameter[key] = str(value)  # To format: {A: B(str)}

        return parameter

    @staticmethod
    def update_next(parameter: list):
        """
        Update Next string in test file.

        Args:
            parameter: Next string before updating

        Returns:
            parameter: Next string after updating
        """
        if isinstance(parameter, list):  # Format: [A]

            if parameter is []:
                parameter = np.nan  # To format: np.nan

            else:
                parameter = int(parameter[0])  # To format: A(int)

        return parameter

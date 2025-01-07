# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/7 11:03
File: list_IT6722A.py
"""
from parse.exception.exception_visa.exceptions.exception_IT6722A import *

List_IT6722A = {
    'Other': Exception_Other_error,
    '110': Exception_No_input_command,
    '120': Exception_Parameter_overflowed,
    '130': Exception_Wrong_units_for_parameter,
    '140': Exception_Wrong_type_of_parameter,
    '150': Exception_Wrong_number_of_parameter,
    '160': Exception_Unmatched_quotation_mark,
    '165': Exception_Unmatched_bracket,
    '170': Exception_Invalid_command,
    '180': Exception_No_entry_in_list,
    '191': Exception_Too_many_char,
    '-200': Exception_Execution_error,
    '-310': Exception_System_error,
    '-350': Exception_Too_many_errors,
    '-410': Exception_Query_INTERRUPTED,
    '-430': Exception_Query_DEADLOCKED,
    '2': Exception_Mainframe_Initialization_Lost,
    '3': Exception_Module_Calibration_Lost,
    '4': Exception_Eeprom_failure,
    '6': Exception_Output_Locked,
    '40': Exception_Flash_write_failed,
    '41': Exception_Flash_erase_failed,
    '217': Exception_RS232_receiver_parity,
    '223': Exception_Front_panel_buffer_overrun,
    '224': Exception_Front_panel_timeout,
    '402': Exception_CAL_password_is_incorrect,
    '403': Exception_CAL_not_enabled,
    '404': Exception_readback_cal_are_incorrect,
    '405': Exception_programming_cal_are_incorrect,
}

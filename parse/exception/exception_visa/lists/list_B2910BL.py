# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/6 15:16
File: list_B2910BL.py
"""
from parse.exception.exception_visa.exceptions.exception_B2910BL import *

List_B2910BL = {
    'Other': Exception_Other_error,
    '-100': Exception_Command_error,
    '-101': Exception_Invalid_character,
    '-102': Exception_Syntax_error,
    '-103': Exception_Invalid_separator,
    '-104': Exception_Data_type_error,
    '-105': Exception_GET_not_allowed,
    '-108': Exception_Parameter_not_allowed,
    '-109': Exception_Missing_parameter,
    '-110': Exception_Command_header_error,
    '-111': Exception_Header_separator_error,
    '-112': Exception_Program_mnemonic_too_long,
    '-113': Exception_Undefined_header,
    '-114': Exception_Header_suffix_out_of_range,
    '-120': Exception_Numeric_data_error,
    '-121': Exception_Invalid_character_in_number,
    '-123': Exception_Exponent_too_large,
    '-124': Exception_Too_many_digits,
    '-128': Exception_Numeric_data_not_allowed,
    '-130': Exception_Suffix_error,
    '-131': Exception_Invalid_suffix,
    '-134': Exception_Suffix_too_long,
    '-138': Exception_Suffix_not_allowed,
    '-140': Exception_Character_data_error,
    '-141': Exception_Invalid_character_data,
    '-144': Exception_Character_data_too_long,
    '-148': Exception_Character_data_not_allowed,
    '-150': Exception_String_data_error,
    '-151': Exception_Invalid_string_data,
    '-158': Exception_String_data_not_allowed,
    '-160': Exception_Block_data_error,
    '-161': Exception_Invalid_block_data,
    '-168': Exception_Block_data_not_allowed,
    '-170': Exception_Expression_error,
    '-171': Exception_Invalid_expression,
    '-178': Exception_Expression_data_not_allowed,
    '-200': Exception_Execution_error,
    '-220': Exception_Parameter_error,
    '-221': Exception_Settings_conflict,
    '-222': Exception_Data_out_of_range,
    '-223': Exception_Too_much_data,
    '-224': Exception_Illegal_parameter_value,
    '-230': Exception_Data_corrupt_or_stale,
    '-231': Exception_Data_questionable,
    '-232': Exception_Invalid_format,
    '-233': Exception_Invalid_version,
    '-240': Exception_Hardware_error,
    '-241': Exception_Hardware_missing,
    '-300': Exception_Device_specific_error,
    '-310': Exception_System_error,
    '-311': Exception_Memory_error,
    '-313': Exception_Calibration_memory_lost,
    '-315': Exception_Configuration_memory_lost,
    '-321': Exception_Out_of_memory,
    '-350': Exception_Queue_overflow,
    '-400': Exception_Query_error,
    '-410': Exception_Query_INTERRUPTED,
    '-420': Exception_Query_UNTERMINATED,
    '-430': Exception_Query_DEADLOCKED,
    '-440': Exception_Query_UNTERMINATED_after_indefinite_response,
    '101': Exception_Wrong_password,
    '102': Exception_Enter_password_for_calibration,
    '103': Exception_Data_load_failed,
    '104': Exception_Data_save_failed,
    '111': Exception_Self_calibration_failed_Voltage_offset,
    '112': Exception_Self_calibration_failed_Current_offset,
    '113': Exception_Self_calibration_failed_Voltage_gain,
    '114': Exception_Self_calibration_failed_Current_gain,
    '115': Exception_Self_calibration_failed_CMR_DAC,
    '121': Exception_Self_test_failed_CPU_communication,
    '122': Exception_Self_test_failed_Fan_status,
    '131': Exception_Self_test_failed_SMU_communication,
    '132': Exception_Self_test_failed_CPLD_access,
    '133': Exception_Self_test_failed_Trigger_count,
    '134': Exception_Self_test_failed_DAC_ADC,
    '135': Exception_Self_test_failed_Loop_control,
    '136': Exception_Self_test_failed_I_sense,
    '137': Exception_Self_test_failed_V_sense,
    '138': Exception_Self_test_failed_F_COM_comparison,
    '139': Exception_Self_test_failed_V_switch,
    '140': Exception_Self_test_failed_Temperature_sensor,
    '141': Exception_Self_test_skipped,
    '201': Exception_Not_able_to_perform_requested_operation,
    '202': Exception_Instrument_locked_by_another_IO_session,
    '203': Exception_Not_able_to_execute_while_instrument_is_measuring,
    '210': Exception_Operation_is_not_completed,
    '211': Exception_Cannot_switch_low_sense_terminal_with_output_on,
    '212': Exception_Output_relay_must_be_on,
    '213': Exception_Output_relay_must_be_off,
    '214': Exception_Display_must_be_enabled,
    '215': Exception_Remote_sensing_must_be_on,
    '216': Exception_Auto_resistance_measurement_must_be_off,
    '290': Exception_Not_able_to_recall_state,
    '291': Exception_State_file_size_error,
    '292': Exception_State_file_corrupt,
    '301': Exception_Overvoltage_status_detected,
    '302': Exception_Overcurrent_status_245V_detected,
    '303': Exception_Overcurrent_status_35V_detected,
    '304': Exception_Over_range_current_status_detected,
    '305': Exception_High_temperature1_status_detected,
    '306': Exception_High_temperature2_status_detected,
    '307': Exception_High_temperature3_status_detected,
    '308': Exception_High_temperature4_status_detected,
    '311': Exception_Abuse_detected,
    '312': Exception_F_COM_minus_abuse_detected,
    '313': Exception_F_COM_plus_abuse_detected,
    '314': Exception_Low_sense_minus_abuse_detected,
    '315': Exception_Low_sense_plus_abuse_detected,
    '321': Exception_SMU_main_power_supply_failure_detected,
    '322': Exception_SMU_positive_power_supply_failure_detected,
    '323': Exception_SMU_negative_power_supply_failure_detected,
    '324': Exception_SMU_power_supply_was_turned_off,
    '331': Exception_Interlock_open_detected,
    '341': Exception_Fan_speed_is_too_slow,
    '342': Exception_Fan_speed_is_too_fast,
    '351': Exception_Internal_communication_failure_detected_by_SMU,
    '352': Exception_Watchdog_timer_expired,
    '353': Exception_F_COM_CPLD_reset_detected,
    '354': Exception_VADC_data_was_lost,
    '355': Exception_IADC_data_was_lost,
    '356': Exception_Sense_data_FIFO_overflow_detected,
    '361': Exception_Internal_communication_failure_detected_by_CPU,
    '362': Exception_Internal_command_queue_overflow_detected,

}
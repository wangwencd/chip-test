# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/20 11:31
File: list_E36312A.py
"""
from parse.exception.exception_visa.exceptions.exception_E36312A import *

List_E36312A = {
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
    '-123': Exception_Numeric_overflow,
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
    '-170': Exception_Generic_expression_error,
    '-171': Exception_Invalid_expression,
    '-178': Exception_Expression_data_not_allowed,
    '-200': Exception_Execution_error,
    '-220': Exception_Parameter_error,
    '-221': Exception_Settings_conflict,
    '-222': Exception_Data_out_of_range,
    '-223': Exception_Too_much_data,
    '-224': Exception_Illegal_parameter_value,
    '-225': Exception_Out_of_memory,
    '-230': Exception_Data_corrupt_or_stale,
    '-231': Exception_Data_questionable,
    '-240': Exception_Hardware_error,
    '-241': Exception_Hardware_missing,
    '-260': Exception_Expression_error,
    '-261': Exception_Math_error_in_expression,
    '-400': Exception_Query_Error,
    '-410': Exception_Query_INTERRUPTED,
    '-420': Exception_Query_UNTERMINATED,
    '-430': Exception_Query_DEADLOCKED,
    '-440': Exception_Query_UNTERMINATED_after_indefinite_response,
    '304': Exception_Volt_and_curr_in_incompatible_transient_modes,
    '307': Exception_List_lengths_are_not_equivalent,
    '308': Exception_This_command_is_not_allow_while_list_is_running,
    '513': Exception_LAN_invalid_IP_address,
    '514': Exception_LAN_duplicate_IP_address,
    '515': Exception_LAN_failed_to_renew_DHCP_lease,
    '516': Exception_LAN_failed_to_configure,
    '517': Exception_LAN_failed_to_initialize,
    '518': Exception_LAN_VXI_11_fault,
    '543': Exception_Configuration_mismatched,
    '550': Exception_3p3V_power_lost,
    '551': Exception_5p0V_power_lost,
    '552': Exception_12V_power_lost,
    '561': Exception_Analog_board_CH1_does_not_respond,
    '562': Exception_Analog_board_CH2_does_not_respond,
    '563': Exception_Analog_board_CH3_does_not_respond,
    '564': Exception_Analog_board_CH1_over_temperature,
    '565': Exception_Analog_board_CH2_over_temperature,
    '566': Exception_Analog_board_CH3_over_temperature,
    '567': Exception_Analog_board_CH1_command_timed_out,
    '568': Exception_Analog_board_CH2_command_timed_out,
    '569': Exception_Analog_board_CH3_command_timed_out,
    '600': Exception_Analog_board_CH1_failed_to_enter_boot_loader,
    '601': Exception_Analog_board_CH2_failed_to_enter_boot_loader,
    '602': Exception_Analog_board_CH3_failed_to_enter_boot_loader,
    '603': Exception_Analog_board_CH1_failed_to_comm_SEM_Fail,
    '604': Exception_Analog_board_CH2_failed_to_comm_SEM_Fail,
    '605': Exception_Analog_board_CH3_failed_to_comm_SEM_Fail,
    '606': Exception_Analog_board_CH1_failed_to_comm_UNSPECIFIED,
    '607': Exception_Analog_board_CH2_failed_to_comm_UNSPECIFIED,
    '608': Exception_Analog_board_CH3_failed_to_comm_UNSPECIFIED,
    '610': Exception_Fan_test_failed,
    '611': Exception_EEPROM_load_failed,
    '612': Exception_EEPROM_checksum_failed,
    '613': Exception_EEPROM_save_failed,
    '614': Exception_Invalid_serial_number,
    '615': Exception_Invalid_MAC_address,
    '616': Exception_Front_panel_does_not_respond,
    '720': Exception_CH3_is_not_allowed_when_serial_or_parallel_or_track_is_enabled,
    '721': Exception_Calibration_is_not_allowed_when_serial_or_parallel_or_track_is_enabled,
    '722': Exception_Multiple_channels_selection_is_not_allowed_during_calibration,
    '729': Exception_Not_allow_to_enable_output,
    '735': Exception_Cannot_change_while_trigger_is_initiated,
    '736': Exception_Trig_init_disallow_as_channel_is_coupled_with_another_channel_that_has_trig_initiated,
    '737': Exception_This_command_is_only_supported_in_E3631A_persona_mode,
    '738': Exception_This_command_is_only_supported_in_E3631XA_persona_mode,
    '739': Exception_Channel_list_is_ignored_by_this_command_in_E3631A_persona_mode,
    '742': Exception_Illegal_operation,
    '743': Exception_Operation_not_allowed_when_in_parallel_or_series_mode,
    '750': Exception_USB_not_connected,
    '751': Exception_USB_host_access_failed,
    '752': Exception_Insufficient_space_in_USB_drive,
    '753': Exception_Data_logger_is_running,
    '754': Exception_Data_logger_do_not_have_valid_data,
    '800': Exception_CH2_and_CH3_coupled_by_track_system,
    '801': Exception_CH2_and_CH3_coupled_by_trigger_subsystem,
    '900': Exception_Firmware_update_failed,
}
# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/15 17:08
File: exception_E36312A.py
"""

from parse.exception.exception_base import Exception_Base

class Exception_Other_error(Exception_Base):
    """Other error"""

class Exception_Command_error(Exception_Base):
    """Command error"""

class Exception_Invalid_character(Exception_Base):
    """Invalid character"""

class Exception_Syntax_error(Exception_Base):
    """Syntax error"""

class Exception_Invalid_separator(Exception_Base):
    """Invalid separator"""

class Exception_Data_type_error(Exception_Base):
    """Data type error"""

class Exception_GET_not_allowed(Exception_Base):
    """GET not allowed"""

class Exception_Parameter_not_allowed(Exception_Base):
    """Parameter not allowed"""

class Exception_Missing_parameter(Exception_Base):
    """Missing parameter"""

class Exception_Command_header_error(Exception_Base):
    """Command header error"""

class Exception_Header_separator_error(Exception_Base):
    """Header separator error"""

class Exception_Program_mnemonic_too_long(Exception_Base):
    """Program mnemonic too long"""

class Exception_Undefined_header(Exception_Base):
    """Undefined header"""

class Exception_Header_suffix_out_of_range(Exception_Base):
    """Header suffix out of range"""

class Exception_Numeric_data_error(Exception_Base):
    """Numeric data error"""

class Exception_Invalid_character_in_number(Exception_Base):
    """Invalid character in number"""

class Exception_Numeric_overflow(Exception_Base):
    """Numeric overflow"""

class Exception_Too_many_digits(Exception_Base):
    """Too many digits"""

class Exception_Numeric_data_not_allowed(Exception_Base):
    """Numeric data not allowed"""

class Exception_Suffix_error(Exception_Base):
    """Suffix error"""

class Exception_Invalid_suffix(Exception_Base):
    """Invalid suffix"""

class Exception_Suffix_too_long(Exception_Base):
    """Suffix too long"""

class Exception_Suffix_not_allowed(Exception_Base):
    """Suffix not allowed"""

class Exception_Character_data_error(Exception_Base):
    """Character data error"""

class Exception_Invalid_character_data(Exception_Base):
    """Invalid character data"""

class Exception_Character_data_too_long(Exception_Base):
    """Character data too long"""

class Exception_Character_data_not_allowed(Exception_Base):
    """Character data not allowed"""

class Exception_String_data_error(Exception_Base):
    """String data error"""

class Exception_Invalid_string_data(Exception_Base):
    """Invalid string data"""

class Exception_String_data_not_allowed(Exception_Base):
    """String data not allowed"""

class Exception_Block_data_error(Exception_Base):
    """Block data error"""

class Exception_Invalid_block_data(Exception_Base):
    """Invalid block data"""

class Exception_Block_data_not_allowed(Exception_Base):
    """Block data not allowed"""

class Exception_Generic_expression_error(Exception_Base):
    """Generic Expression error"""

class Exception_Invalid_expression(Exception_Base):
    """Invalid expression"""

class Exception_Expression_data_not_allowed(Exception_Base):
    """Expression data not allowed"""

class Exception_Execution_error(Exception_Base):
    """Execution error"""

class Exception_Parameter_error(Exception_Base):
    """Parameter error"""

class Exception_Settings_conflict(Exception_Base):
    """Settings conflict"""

class Exception_Data_out_of_range(Exception_Base):
    """Data out of range"""

class Exception_Too_much_data(Exception_Base):
    """Too much data"""

class Exception_Illegal_parameter_value(Exception_Base):
    """Illegal parameter value"""

class Exception_Out_of_memory(Exception_Base):
    """Exception_Out_of_memory"""

class Exception_Data_corrupt_or_stale(Exception_Base):
    """Data corrupt or stale"""

class Exception_Data_questionable(Exception_Base):
    """Data questionable"""

class Exception_Hardware_error(Exception_Base):
    """Hardware error"""

class Exception_Hardware_missing(Exception_Base):
    """Hardware missing"""

class Exception_Expression_error(Exception_Base):
    """Expression error"""

class Exception_Math_error_in_expression(Exception_Base):
    """Math error in expression"""

class Exception_Query_Error(Exception_Base):
    """Query Error"""

class Exception_Query_INTERRUPTED(Exception_Base):
    """Query INTERRUPTED"""

class Exception_Query_UNTERMINATED(Exception_Base):
    """Query UNTERMINATED"""

class Exception_Query_DEADLOCKED(Exception_Base):
    """Query DEADLOCKED"""

class Exception_Query_UNTERMINATED_after_indefinite_response(Exception_Base):
    """Query UNTERMINATED after indefinite response"""

class Exception_Volt_and_curr_in_incompatible_transient_modes(Exception_Base):
    """Volt and curr in incompatible transient modes"""

class Exception_List_lengths_are_not_equivalent(Exception_Base):
    """List lengths are not equivalent"""

class Exception_This_command_is_not_allow_while_list_is_running(Exception_Base):
    """This command is not allow while list is running"""

class Exception_LAN_invalid_IP_address(Exception_Base):
    """LAN invalid IP address"""

class Exception_LAN_duplicate_IP_address(Exception_Base):
    """LAN duplicate IP address"""

class Exception_LAN_failed_to_renew_DHCP_lease(Exception_Base):
    """LAN failed to renew DHCP lease"""

class Exception_LAN_failed_to_configure(Exception_Base):
    """LAN failed to configure"""

class Exception_LAN_failed_to_initialize(Exception_Base):
    """LAN failed to initialize"""

class Exception_LAN_VXI_11_fault(Exception_Base):
    """LAN VXI-11 fault"""

class Exception_Configuration_mismatched(Exception_Base):
    """Configuration mismatched"""

class Exception_3p3V_power_lost(Exception_Base):
    """3.3V power lost"""

class Exception_5p0V_power_lost(Exception_Base):
    """5.0V power lost"""

class Exception_12V_power_lost(Exception_Base):
    """12V power lost"""

class Exception_Analog_board_CH1_does_not_respond(Exception_Base):
    """Analog board (CH1) does not respond"""

class Exception_Analog_board_CH2_does_not_respond(Exception_Base):
    """Analog board (CH2) does not respond"""

class Exception_Analog_board_CH3_does_not_respond(Exception_Base):
    """Analog board (CH3) does not respond"""

class Exception_Analog_board_CH1_over_temperature(Exception_Base):
    """Analog board (CH1) over temperature"""

class Exception_Analog_board_CH2_over_temperature(Exception_Base):
    """Analog board (CH2) over temperature"""

class Exception_Analog_board_CH3_over_temperature(Exception_Base):
    """Analog board (CH3) over temperature"""

class Exception_Analog_board_CH1_command_timed_out(Exception_Base):
    """Analog board (CH1) command timed out"""

class Exception_Analog_board_CH2_command_timed_out(Exception_Base):
    """Analog board (CH2) command timed out"""

class Exception_Analog_board_CH3_command_timed_out(Exception_Base):
    """Analog board (CH3) command timed out"""

class Exception_Analog_board_CH1_failed_to_enter_boot_loader(Exception_Base):
    """Analog board (CH1) failed to enter boot loader"""

class Exception_Analog_board_CH2_failed_to_enter_boot_loader(Exception_Base):
    """Analog board (CH2) failed to enter boot loader"""

class Exception_Analog_board_CH3_failed_to_enter_boot_loader(Exception_Base):
    """Analog board (CH3) failed to enter boot loader"""

class Exception_Analog_board_CH1_failed_to_comm_SEM_Fail(Exception_Base):
    """Analog board (CH1) failed to comm (SEM Fail)"""

class Exception_Analog_board_CH2_failed_to_comm_SEM_Fail(Exception_Base):
    """Analog board (CH2) failed to comm (SEM Fail)"""

class Exception_Analog_board_CH3_failed_to_comm_SEM_Fail(Exception_Base):
    """Analog board (CH3) failed to comm (SEM Fail)"""

class Exception_Analog_board_CH1_failed_to_comm_UNSPECIFIED(Exception_Base):
    """Analog board (CH1) failed to comm (UNSPECIFIED)"""

class Exception_Analog_board_CH2_failed_to_comm_UNSPECIFIED(Exception_Base):
    """Analog board (CH2) failed to comm (UNSPECIFIED)"""

class Exception_Analog_board_CH3_failed_to_comm_UNSPECIFIED(Exception_Base):
    """Analog board (CH3) failed to comm (UNSPECIFIED)"""

class Exception_Fan_test_failed(Exception_Base):
    """Fan test failed"""

class Exception_EEPROM_load_failed(Exception_Base):
    """EEPROM load failed"""

class Exception_EEPROM_checksum_failed(Exception_Base):
    """EEPROM checksum failed"""

class Exception_EEPROM_save_failed(Exception_Base):
    """EEPROM save failed"""

class Exception_Invalid_serial_number(Exception_Base):
    """Invalid serial number"""

class Exception_Invalid_MAC_address(Exception_Base):
    """Invalid MAC address"""

class Exception_Front_panel_does_not_respond(Exception_Base):
    """Front panel does not respond"""

class Exception_CH3_is_not_allowed_when_serial_or_parallel_or_track_is_enabled(Exception_Base):
    """CH3 is not allowed when serial/parallel/track is enabled"""

class Exception_Calibration_is_not_allowed_when_serial_or_parallel_or_track_is_enabled(Exception_Base):
    """Calibration is not allowed when serial/parallel is enabled"""

class Exception_Multiple_channels_selection_is_not_allowed_during_calibration(Exception_Base):
    """Multiple channels selection is not allowed during calibration"""

class Exception_Not_allow_to_enable_output(Exception_Base):
    """Not allow to enable output"""

class Exception_Cannot_change_while_trigger_is_initiated(Exception_Base):
    """Cannot change while trigger is initiated"""

class Exception_Trig_init_disallow_as_channel_is_coupled_with_another_channel_that_has_trig_initiated(Exception_Base):
    """Trig init disallow as channel is coupled with another channel that has trig initiated"""

class Exception_This_command_is_only_supported_in_E3631A_persona_mode(Exception_Base):
    """This command is only supported in E3631A persona mode"""

class Exception_This_command_is_only_supported_in_E3631XA_persona_mode(Exception_Base):
    """This command is only supported in E3631XA persona mode"""

class Exception_Channel_list_is_ignored_by_this_command_in_E3631A_persona_mode(Exception_Base):
    """Channel list is ignored by this command in E3631A persona mode"""

class Exception_Illegal_operation(Exception_Base):
    """Illegal operation"""

class Exception_Operation_not_allowed_when_in_parallel_or_series_mode(Exception_Base):
    """Operation not allowed when in parallel/series mode"""

class Exception_USB_not_connected(Exception_Base):
    """USB not connected"""

class Exception_USB_host_access_failed(Exception_Base):
    """USB host access failed"""

class Exception_Insufficient_space_in_USB_drive(Exception_Base):
    """Insufficient space in USB drive"""

class Exception_Data_logger_is_running(Exception_Base):
    """Data logger is running"""

class Exception_Data_logger_do_not_have_valid_data(Exception_Base):
    """Data logger do not have valid data"""

class Exception_CH2_and_CH3_coupled_by_track_system(Exception_Base):
    """CH2 and CH3 coupled by track system"""

class Exception_CH2_and_CH3_coupled_by_trigger_subsystem(Exception_Base):
    """CH2 and CH3 coupled by trigger subsystem"""

class Exception_Firmware_update_failed(Exception_Base):
    """Firmware update failed"""


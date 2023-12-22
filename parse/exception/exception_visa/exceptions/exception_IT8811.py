# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/25 11:08
File: exception_IT8811.py
"""
from parse.exception.exception_base import Exception_Base

class Exception_Other_error(Exception_Base):
    """Other error"""

class Exception_DESIGN_ERROR(Exception_Base):
    """DESIGN ERROR"""

class Exception_No_Input_Command_to_parse(Exception_Base):
    """No Input Command to parse"""

class Exception_Numeric_suffix_is_invalid_value(Exception_Base):
    """Numeric suffix is invalid value"""

class Exception_Invalid_value_in_numeric_or_channel_list(Exception_Base):
    """Invalid value in numeric or channel list"""

class Exception_Invalid_number_of_dimensions_in_a_channel_list(Exception_Base):
    """Invalid number of dimensions in a channel list"""

class Exception_Parameter_of_type_Numeric_Value_overflowed_its_storage(Exception_Base):
    """Parameter of type Numeric Value overflowed its storage"""

class Exception_Wrong_units_for_parameter(Exception_Base):
    """Wrong units for parameter"""

class Exception_Wrong_type_of_parameters(Exception_Base):
    """Wrong type of parameter(s)"""

class Exception_Wrong_number_of_parameters(Exception_Base):
    """Wrong number of parameters"""

class Exception_Unmatched_quotation_mark_in_parameters(Exception_Base):
    """Unmatched quotation mark (single/double) in parameters"""

class Exception_Unmatched_bracket(Exception_Base):
    """Unmatched bracket"""

class Exception_Command_keywords_were_not_recognized(Exception_Base):
    """Command keywords were not recognized"""

class Exception_No_entry_in_list_to_retrieve(Exception_Base):
    """No entry in list to retrieve"""

class Exception_Too_many_dimensions_in_entry_to_be_returned_in_parameters(Exception_Base):
    """Too many dimensions in entry to be returned in parameters"""

class Exception_Too_many_char(Exception_Base):
    """Too many char"""

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

class Exception_Expression_error(Exception_Base):
    """Expression error"""

class Exception_Invalid_expression(Exception_Base):
    """Invalid expression"""

class Exception_Expression_data_not_allowed(Exception_Base):
    """Expression data not allowed"""

class Exception_Execution_error(Exception_Base):
    """Execution error"""

class Exception_Settings_conflict(Exception_Base):
    """Settings conflict"""

class Exception_Data_out_of_range(Exception_Base):
    """Data out of range"""

class Exception_Too_much_data(Exception_Base):
    """Too much data"""

class Exception_Illegal_parameter_value(Exception_Base):
    """Illegal parameter value"""

class Exception_Out_of_memory(Exception_Base):
    """Out of memory"""

class Exception_Data_Corrupt_or_Stale(Exception_Base):
    """Data Corrupt or Stale"""

class Exception_Macro_error(Exception_Base):
    """Macro error"""

class Exception_Macro_execution_error(Exception_Base):
    """Macro execution error"""

class Exception_Illegal_macro_label(Exception_Base):
    """Illegal macro label"""

class Exception_Macro_recursion_error(Exception_Base):
    """Macro recursion error"""

class Exception_Macro_redefinition_not_allowed(Exception_Base):
    """Macro redefinition not allowed"""

class Exception_System_error(Exception_Base):
    """System error"""

class Exception_Too_many_errors(Exception_Base):
    """Too many errors"""

class Exception_sets_Standard_Event_Status_Register_bit(Exception_Base):
    """sets Standard Event Status Register bit #2"""

class Exception_Query_error(Exception_Base):
    """Query error"""

class Exception_Query_INTERRUPTED(Exception_Base):
    """Query INTERRUPTED"""

class Exception_Query_UNTERMINATED_before_response_complete(Exception_Base):
    """Query UNTERMINATED before response complete"""

class Exception_Query_DEADLOCKED(Exception_Base):
    """Query DEADLOCKED"""

class Exception_Query_UNTERMINATED_after_response_complete(Exception_Base):
    """Query UNTERMINATED before response complete"""

class Exception_Module_Initialization_Lost(Exception_Base):
    """Module Initialization Lost"""

class Exception_Mainframe_Initialization_Lost(Exception_Base):
    """Mainframe Initialization Lost"""

class Exception_Module_Calibration_Lost(Exception_Base):
    """Module Calibration Lost"""

class Exception_Non_volatile_RAM_STATE_section_checksum_failed(Exception_Base):
    """Non-volatile RAM STATE section checksum failed"""

class Exception_Non_volatile_RAM_RST_section_checksum_failed(Exception_Base):
    """Non-volatile RAM RST section checksum failed"""

class Exception_RAM_selftest(Exception_Base):
    """RAM selftest"""

class Exception_CVDAC_selftest_1(Exception_Base):
    """CVDAC selftest 1"""

class Exception_CVDAC_selftest_2(Exception_Base):
    """CVDAC selftest 2"""

class Exception_CCDAC_selftest_1(Exception_Base):
    """CCDAC selftest 1"""

class Exception_CCDAC_selftest_2(Exception_Base):
    """CCDAC selftest 2"""

class Exception_CRDAC_selftest_1(Exception_Base):
    """CRDAC selftest 1"""

class Exception_CRDAC_selftest_2(Exception_Base):
    """CRDAC selftest 2"""

class Exception_Input_Down(Exception_Base):
    """Input Down"""

class Exception_Flash_write_failed(Exception_Base):
    """Flash write failed"""

class Exception_Flash_erase_failed(Exception_Base):
    """Flash erase failed"""

class Exception_Digital_I_or_O_selftest_error(Exception_Base):
    """Digital I/O selftest error"""

class Exception_RS_232_buffer_overrun_error(Exception_Base):
    """RS-232 buffer overrun error"""

class Exception_RS_232_receiver_framing_error(Exception_Base):
    """RS-232 receiver framing error"""

class Exception_RS_232_receiver_parity_error(Exception_Base):
    """RS-232 receiver parity error"""

class Exception_RS_232_receiver_overrun_error(Exception_Base):
    """RS-232 receiver overrun error"""

class Exception_Front_panel_uart_overrun(Exception_Base):
    """Front panel uart overrun"""

class Exception_Front_panel_uart_framing(Exception_Base):
    """Front panel uart framing"""

class Exception_Front_panel_uart_parity(Exception_Base):
    """Front panel uart parity"""

class Exception_Front_panel_buffer_overrun(Exception_Base):
    """Front panel buffer overrun"""

class Exception_Front_panel_timeout(Exception_Base):
    """Front panel timeout"""

class Exception_Front_Crc_Check_error(Exception_Base):
    """Front Crc Check error"""

class Exception_Front_Cmd_Error(Exception_Base):
    """Front Cmd Error"""

class Exception_CAL_switch_prevents_calibration(Exception_Base):
    """CAL switch prevents calibration"""

class Exception_CAL_password_is_incorrect(Exception_Base):
    """CAL password is incorrect"""

class Exception_CAL_not_enabled(Exception_Base):
    """CAL not enabled"""

class Exception_Computed_readback_cal_constants_are_incorrect(Exception_Base):
    """Computed readback cal constants are incorrect"""

class Exception_Computed_programming_cal_constants_are_incorrect(Exception_Base):
    """Computed programming cal constants are incorrect"""

class Exception_Incorrect_sequence_of_calibration_commands(Exception_Base):
    """Incorrect sequence of calibration commands"""

class Exception_CV_or_CC_status_is_incorrect_for_this_command(Exception_Base):
    """CV or CC status is incorrect for this command"""

class Exception_Output_mode_switch_must_be_in_NORMAL_position(Exception_Base):
    """Output mode switch must be in NORMAL position"""

class Exception_Lists_inconsistent(Exception_Base):
    """Lists inconsistent"""

class Exception_Too_many_sweep_points(Exception_Base):
    """Too many sweep points"""

class Exception_Command_only_applies_to_RS_232_interface(Exception_Base):
    """Command only applies to RS-232 interface"""

class Exception_FETCH_of_data_that_was_not_acquired(Exception_Base):
    """FETCH of data that was not acquired"""

class Exception_Measurement_overrange(Exception_Base):
    """Measurement overrange"""

class Exception_Command_not_allowed_while_list_initiated(Exception_Base):
    """Command not allowed while list initiated"""

class Exception_Corrupt_update_data(Exception_Base):
    """Corrupt update data"""

class Exception_Not_Updating(Exception_Base):
    """Not Updating"""


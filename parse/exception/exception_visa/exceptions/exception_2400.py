# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/10 12:07
File: exception_2400.py
"""
from parse.exception.exception_base import Exception_Base

class Exception_Other_error(Exception_Base):
    """Other error"""

class Exception_Query_UNTERMINATED_after_indefinite_response(Exception_Base):
    """Query UNTERMINATED after indefinite response"""

class Exception_Query_DEADLOCKED(Exception_Base):
    """Query DEADLOCKED"""

class Exception_Query_UNTERMINATED(Exception_Base):
    """Query UNTERMINATED"""

class Exception_Query_INTERRUPTED(Exception_Base):
    """Query INTERRUPTED"""

class Exception_Input_buffer_overrun(Exception_Base):
    """Input buffer overrun"""

class Exception_Framing_error_in_program_message(Exception_Base):
    """Framing error in program message"""

class Exception_Parity_error_in_program_message(Exception_Base):
    """Parity error in program message"""

class Exception_Communications_error(Exception_Base):
    """Communications error"""

class Exception_Queue_overflow(Exception_Base):
    """Queue overflow"""

class Exception_Self_test_failed(Exception_Base):
    """Self-test failed"""

class Exception_Save_or_recall_memory_lost(Exception_Base):
    """Save/recall memory lost"""

class Exception_Configuration_memory_lost(Exception_Base):
    """Configuration memory lost"""

class Exception_Program_syntax_error(Exception_Base):
    """Program syntax error"""

class Exception_Program_currently_running(Exception_Base):
    """Program currently running"""

class Exception_Illegal_program_name(Exception_Base):
    """Illegal program name"""

class Exception_Cannot_create_program(Exception_Base):
    """Cannot create program"""

class Exception_Expression_error(Exception_Base):
    """Expression error"""

class Exception_Hardware_missing(Exception_Base):
    """Hardware missing"""

class Exception_Data_corrupt_or_stale(Exception_Base):
    """Data corrupt or stale"""

class Exception_Out_of_memory(Exception_Base):
    """Out of memory"""

class Exception_Illegal_parameter_value(Exception_Base):
    """Illegal parameter value"""

class Exception_Too_much_data(Exception_Base):
    """Too much data"""

class Exception_Parameter_data_out_of_range(Exception_Base):
    """Parameter data out of range"""

class Exception_Settings_conflict(Exception_Base):
    """Settings conflict"""

class Exception_Parameter_error(Exception_Base):
    """Parameter error"""

class Exception_Arm_deadlock(Exception_Base):
    """Arm deadlock"""

class Exception_Trigger_deadlock(Exception_Base):
    """Trigger deadlock"""

class Exception_Init_ignored(Exception_Base):
    """Init ignored"""

class Exception_Arm_ignored(Exception_Base):
    """Arm ignored"""

class Exception_Trigger_ignored(Exception_Base):
    """Trigger ignored"""

class Exception_Trigger_error(Exception_Base):
    """Trigger error"""

class Exception_Settings_lost_due_to_rtl(Exception_Base):
    """Settings lost due to rtl"""

class Exception_Invalid_while_in_local(Exception_Base):
    """Invalid while in local"""

class Exception_Execution_error(Exception_Base):
    """Execution error"""

class Exception_Expression_data_not_allowed(Exception_Base):
    """Expression data not allowed"""

class Exception_Invalid_expression(Exception_Base):
    """Invalid expression"""

class Exception_Block_data_not_allowed(Exception_Base):
    """Block data not allowed"""

class Exception_Invalid_block_data(Exception_Base):
    """Invalid block data"""

class Exception_Block_data_error(Exception_Base):
    """Block data error"""

class Exception_String_data_not_allowed(Exception_Base):
    """String data not allowed"""

class Exception_String_too_long(Exception_Base):
    """String too long"""

class Exception_Invalid_string_data(Exception_Base):
    """Invalid string data"""

class Exception_String_data_error(Exception_Base):
    """String data error"""

class Exception_Character_data_not_allowed(Exception_Base):
    """Character data not allowed"""

class Exception_Character_data_too_long(Exception_Base):
    """Character data too long"""

class Exception_Invalid_character_data(Exception_Base):
    """Invalid character data"""

class Exception_Character_data_error(Exception_Base):
    """Character data error"""

class Exception_Numeric_data_not_allowed(Exception_Base):
    """Numeric data not allowed"""

class Exception_Too_many_digits(Exception_Base):
    """Too many digits"""

class Exception_Exponent_too_large(Exception_Base):
    """Exponent too large"""

class Exception_Invalid_character_in_number(Exception_Base):
    """Invalid character in number"""

class Exception_Numeric_data_error(Exception_Base):
    """Numeric data error"""

class Exception_Header_suffix_out_of_range(Exception_Base):
    """Header suffix out of range"""

class Exception_Undefined_header(Exception_Base):
    """Undefined header"""

class Exception_Program_mnemonic_too_long(Exception_Base):
    """Program mnemonic too long"""

class Exception_Header_separator_error(Exception_Base):
    """Header separator error"""

class Exception_Command_header_error(Exception_Base):
    """Command header error"""

class Exception_Missing_parameter(Exception_Base):
    """Missing parameter"""

class Exception_Parameter_not_allowed(Exception_Base):
    """Parameter not allowed"""

class Exception_GET_not_allowed(Exception_Base):
    """GET not allowed"""

class Exception_Data_type_error(Exception_Base):
    """Data type error"""

class Exception_Invalid_separator(Exception_Base):
    """Invalid separator"""

class Exception_Syntax_error(Exception_Base):
    """Syntax error"""

class Exception_Invalid_character(Exception_Base):
    """Invalid character"""

class Exception_Command_error(Exception_Base):
    """Command error"""

class Exception_Limit_1_failed(Exception_Base):
    """Limit 1 failed"""

class Exception_Low_limit_2_failed(Exception_Base):
    """Low limit 2 failed"""

class Exception_High_limit_2_failed(Exception_Base):
    """High limit 2 failed"""

class Exception_Low_limit_3_failed(Exception_Base):
    """Low limit 3 failed"""

class Exception_High_limit_3_failed(Exception_Base):
    """High limit 3 failed"""

class Exception_Active_limit_tests_passed(Exception_Base):
    """Active limit tests passed"""

class Exception_Reading_available(Exception_Base):
    """Reading available"""

class Exception_Reading_overflow(Exception_Base):
    """Reading overflow"""

class Exception_Buffer_available(Exception_Base):
    """Buffer available"""

class Exception_Buffer_full(Exception_Base):
    """Buffer full"""

class Exception_Limit_4_failed(Exception_Base):
    """Limit 4 failed"""

class Exception_OUTPUT_enable_asserted(Exception_Base):
    """OUTPUT enable asserted"""

class Exception_Temperature_limit_exceeded(Exception_Base):
    """Temperature limit exceeded"""

class Exception_Voltage_limit_exceeded(Exception_Base):
    """Voltage limit exceeded"""

class Exception_Source_in_compliance(Exception_Base):
    """Source in compliance"""

class Exception_Operation_complete(Exception_Base):
    """Operation complete"""

class Exception_Device_calibrating(Exception_Base):
    """Device calibrating"""

class Exception_Device_sweeping(Exception_Base):
    """Device sweeping"""

class Exception_Waiting_in_trigger_layer(Exception_Base):
    """Waiting in trigger layer"""

class Exception_Waiting_in_arm_layer(Exception_Base):
    """Waiting in arm layer"""

class Exception_Entering_idle_layer(Exception_Base):
    """Entering idle layer"""

class Exception_Questionable_Calibration(Exception_Base):
    """Questionable Calibration"""

class Exception_Command_Warning(Exception_Base):
    """Command Warning"""

class Exception_Date_of_calibration_not_set(Exception_Base):
    """Date of calibration not set"""

class Exception_Next_date_of_calibration_not_set(Exception_Base):
    """Next date of calibration not set"""

class Exception_Calibration_data_invalid(Exception_Base):
    """Calibration data invalid"""

class Exception_DAC_calibration_overflow(Exception_Base):
    """DAC calibration overflow"""

class Exception_DAC_calibration_underflow(Exception_Base):
    """DAC calibration underflow"""

class Exception_Source_offset_data_invalid(Exception_Base):
    """Source offset data invalid"""

class Exception_Source_gain_data_invalid(Exception_Base):
    """Source gain data invalid"""

class Exception_Measurement_offset_data_invalid(Exception_Base):
    """Measurement offset data invalid"""

class Exception_Measurement_gain_data_invalid(Exception_Base):
    """Measurement gain data invalid"""

class Exception_Not_permitted_with_cal_locked(Exception_Base):
    """Not permitted with cal locked"""

class Exception_Not_permitted_with_cal_un_locked(Exception_Base):
    """Not permitted with cal un-locked"""

class Exception_Reading_buffer_data_lost(Exception_Base):
    """Reading buffer data lost"""

class Exception_GPIB_address_lost(Exception_Base):
    """GPIB address lost"""

class Exception_Power_on_state_lost(Exception_Base):
    """Power-on state lost"""

class Exception_DC_calibration_data_lost(Exception_Base):
    """DC calibration data lost"""

class Exception_Calibration_dates_lost(Exception_Base):
    """Calibration dates lost"""

class Exception_GPIB_communication_language_lost(Exception_Base):
    """GPIB communication language lost"""

class Exception_Invalid_system_communication(Exception_Base):
    """Invalid system communication"""

class Exception_ASCII_only_with_RS_232(Exception_Base):
    """ASCII only with RS-232"""

class Exception_Insufficient_vector_data(Exception_Base):
    """Insufficient vector data"""

class Exception_OUTPUT_blocked_by_output_enable(Exception_Base):
    """OUTPUT blocked by output enable"""

class Exception_Not_permitted_with_OUTPUT_off(Exception_Base):
    """Not permitted with OUTPUT off"""

class Exception_Expression_list_full(Exception_Base):
    """Expression list full"""

class Exception_Undefined_expression_exists(Exception_Base):
    """Undefined expression exists"""

class Exception_Expression_not_found(Exception_Base):
    """Expression not found"""

class Exception_Definition_not_allowed(Exception_Base):
    """Definition not allowed"""

class Exception_Expression_cannot_be_deleted(Exception_Base):
    """Expression cannot be deleted"""

class Exception_Source_memory_location_revised(Exception_Base):
    """Source memory location revised"""

class Exception_OUTPUT_blocked_by_Over_Temp(Exception_Base):
    """OUTPUT blocked by Over Temp"""

class Exception_Not_an_operator_or_number(Exception_Base):
    """Not an operator or number"""

class Exception_Mismatched_parenthesis(Exception_Base):
    """Mismatched parenthesis"""

class Exception_Not_a_number_of_data_handle(Exception_Base):
    """Not a number of data handle"""

class Exception_Mismatched_brackets(Exception_Base):
    """Mismatched brackets"""

class Exception_Too_many_parenthesis(Exception_Base):
    """Too many parenthesis"""

class Exception_Entire_expression_not_parsed(Exception_Base):
    """Entire expression not parsed"""

class Exception_Unknown_token(Exception_Base):
    """Unknown token"""

class Exception_Error_parsing_mantissa(Exception_Base):
    """Error parsing mantissa"""

class Exception_Error_parsing_exponent(Exception_Base):
    """Error parsing exponent"""

class Exception_Error_parsing_value(Exception_Base):
    """Error parsing value"""

class Exception_Invalid_data_handle_index(Exception_Base):
    """Invalid data handle index"""

class Exception_Too_small_for_sense_range(Exception_Base):
    """Too small for sense range"""

class Exception_Invalid_with_source_read_back_on(Exception_Base):
    """Invalid with source read-back on"""

class Exception_Cannot_exceed_compliance_range(Exception_Base):
    """Cannot exceed compliance range"""

class Exception_Invalid_with_auto_ohms_on(Exception_Base):
    """Invalid with auto-ohms on"""

class Exception_Attempt_to_exceed_power_limit(Exception_Base):
    """Attempt to exceed power limit"""

class Exception_Invalid_with_ohms_guard_on(Exception_Base):
    """Invalid with ohms guard on"""

class Exception_Invalid_on_1_amp_range(Exception_Base):
    """Invalid on 1 amp range"""

class Exception_Invalid_on_1kV_range(Exception_Base):
    """Invalid on 1kV range"""

class Exception_Invalid_with_INF_ARM_COUNT(Exception_Base):
    """Invalid with INF ARM:COUNT"""

class Exception_Invalid_in_Pulse_Mode(Exception_Base):
    """Invalid in Pulse Mode"""

class Exception_Internal_System_Error(Exception_Base):
    """Internal System Error"""

# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/6 15:16
File: exception_B2910BL.py
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

class Exception_Exponent_too_large(Exception_Base):
    """Exponent too large"""

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

class Exception_Expression_error(Exception_Base):
    """Expression error"""

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

class Exception_Data_corrupt_or_stale(Exception_Base):
    """Data corrupt or stale"""

class Exception_Data_questionable(Exception_Base):
    """Data questionable"""

class Exception_Invalid_format(Exception_Base):
    """Invalid format"""

class Exception_Invalid_version(Exception_Base):
    """Invalid version"""

class Exception_Hardware_error(Exception_Base):
    """Hardware error"""

class Exception_Hardware_missing(Exception_Base):
    """Hardware missing"""

class Exception_Device_specific_error(Exception_Base):
    """Device-specific error"""

class Exception_System_error(Exception_Base):
    """System error"""

class Exception_Memory_error(Exception_Base):
    """Memory error"""

class Exception_Calibration_memory_lost(Exception_Base):
    """Calibration memory lost"""

class Exception_Configuration_memory_lost(Exception_Base):
    """Configuration memory lost"""

class Exception_Out_of_memory(Exception_Base):
    """Out of memory"""

class Exception_Queue_overflow(Exception_Base):
    """Queue overflow"""

class Exception_Query_error(Exception_Base):
    """Query error"""

class Exception_Query_INTERRUPTED(Exception_Base):
    """Query INTERRUPTED"""

class Exception_Query_UNTERMINATED(Exception_Base):
    """Query UNTERMINATED"""

class Exception_Query_DEADLOCKED(Exception_Base):
    """Query DEADLOCKED"""

class Exception_Query_UNTERMINATED_after_indefinite_response(Exception_Base):
    """Query UNTERMINATED after indefinite response"""

class Exception_Wrong_password(Exception_Base):
    """Wrong password"""

class Exception_Enter_password_for_calibration(Exception_Base):
    """Enter password for calibration"""

class Exception_Data_load_failed(Exception_Base):
    """Data load failed"""

class Exception_Data_save_failed(Exception_Base):
    """Data save failed"""

class Exception_Self_calibration_failed_Voltage_offset(Exception_Base):
    """Self-calibration failed; Voltage offset"""

class Exception_Self_calibration_failed_Current_offset(Exception_Base):
    """Self-calibration failed; Current offset"""

class Exception_Self_calibration_failed_Voltage_gain(Exception_Base):
    """Self-calibration failed; Voltage gain"""

class Exception_Self_calibration_failed_Current_gain(Exception_Base):
    """Self-calibration failed; Current gain"""

class Exception_Self_calibration_failed_CMR_DAC(Exception_Base):
    """Self-calibration failed; CMR DAC"""

class Exception_Self_test_failed_CPU_communication(Exception_Base):
    """Self-test failed; CPU communication"""

class Exception_Self_test_failed_Fan_status(Exception_Base):
    """Self-test failed; Fan status"""

class Exception_Self_test_failed_SMU_communication(Exception_Base):
    """Self-test failed; SMU communication"""

class Exception_Self_test_failed_CPLD_access(Exception_Base):
    """Self-test failed; CPLD access"""

class Exception_Self_test_failed_Trigger_count(Exception_Base):
    """Self-test failed; Trigger count"""

class Exception_Self_test_failed_DAC_ADC(Exception_Base):
    """Self-test failed; DAC/ADC"""

class Exception_Self_test_failed_Loop_control(Exception_Base):
    """Self-test failed; Loop control"""

class Exception_Self_test_failed_I_sense(Exception_Base):
    """Self-test failed; I sense"""

class Exception_Self_test_failed_V_sense(Exception_Base):
    """Self-test failed; V sense"""

class Exception_Self_test_failed_F_COM_comparison(Exception_Base):
    """Self-test failed; F-COM comparison"""

class Exception_Self_test_failed_V_switch(Exception_Base):
    """Self-test failed; V switch"""

class Exception_Self_test_failed_Temperature_sensor(Exception_Base):
    """Self-test failed; Temperature sensor"""

class Exception_Self_test_skipped(Exception_Base):
    """Self-test skipped"""

class Exception_Not_able_to_perform_requested_operation(Exception_Base):
    """Not able to perform requested operation"""

class Exception_Instrument_locked_by_another_IO_session(Exception_Base):
    """Instrument locked by another I/O session"""

class Exception_Not_able_to_execute_while_instrument_is_measuring(Exception_Base):
    """Not able to execute while instrument is measuring"""

class Exception_Operation_is_not_completed(Exception_Base):
    """Operation is not completed"""

class Exception_Cannot_switch_low_sense_terminal_with_output_on(Exception_Base):
    """Cannot switch low sense terminal with output on"""

class Exception_Output_relay_must_be_on(Exception_Base):
    """Output relay must be on"""

class Exception_Output_relay_must_be_off(Exception_Base):
    """Output relay must be off"""

class Exception_Display_must_be_enabled(Exception_Base):
    """Display must be enabled"""

class Exception_Remote_sensing_must_be_on(Exception_Base):
    """Remote sensing must be on"""

class Exception_Auto_resistance_measurement_must_be_off(Exception_Base):
    """Auto resistance measurement must be off"""

class Exception_Not_able_to_recall_state(Exception_Base):
    """Not able to recall state"""

class Exception_State_file_size_error(Exception_Base):
    """State file size error"""

class Exception_State_file_corrupt(Exception_Base):
    """State file corrupt"""

class Exception_Overvoltage_status_detected(Exception_Base):
    """Overvoltage status detected"""

class Exception_Overcurrent_status_245V_detected(Exception_Base):
    """Overcurrent status(245 V) detected;"""

class Exception_Overcurrent_status_35V_detected(Exception_Base):
    """Overcurrent status(35 V) detected"""

class Exception_Over_range_current_status_detected(Exception_Base):
    """Over range current status detected"""

class Exception_High_temperature1_status_detected(Exception_Base):
    """High temperature1 status detected"""

class Exception_High_temperature2_status_detected(Exception_Base):
    """High temperature2 status detected"""

class Exception_High_temperature3_status_detected(Exception_Base):
    """High temperature3 status detected"""

class Exception_High_temperature4_status_detected(Exception_Base):
    """High temperature3 status detected"""

class Exception_Abuse_detected(Exception_Base):
    """Abuse detected"""

class Exception_F_COM_minus_abuse_detected(Exception_Base):
    """F-COM(minus) abuse detected"""

class Exception_F_COM_plus_abuse_detected(Exception_Base):
    """F-COM(plus) abuse detected"""

class Exception_Low_sense_minus_abuse_detected(Exception_Base):
    """Low sense(minus) abuse detected"""

class Exception_Low_sense_plus_abuse_detected(Exception_Base):
    """Low sense(plus) abuse detected"""

class Exception_SMU_main_power_supply_failure_detected(Exception_Base):
    """SMU main power supply failure detected"""

class Exception_SMU_positive_power_supply_failure_detected(Exception_Base):
    """SMU positive power supply failure detected"""

class Exception_SMU_negative_power_supply_failure_detected(Exception_Base):
    """SMU negative power supply failure detected"""

class Exception_SMU_power_supply_was_turned_off(Exception_Base):
    """SMU power supply was turned off"""

class Exception_Interlock_open_detected(Exception_Base):
    """Interlock open detected"""

class Exception_Fan_speed_is_too_slow(Exception_Base):
    """Fan speed is too slow"""

class Exception_Fan_speed_is_too_fast(Exception_Base):
    """Fan speed is too fast"""

class Exception_Internal_communication_failure_detected_by_SMU(Exception_Base):
    """Internal communication failure detected by SMU"""

class Exception_Watchdog_timer_expired(Exception_Base):
    """Watchdog timer expired"""

class Exception_F_COM_CPLD_reset_detected(Exception_Base):
    """F-COM CPLD reset detected"""

class Exception_VADC_data_was_lost(Exception_Base):
    """VADC data was lost"""

class Exception_IADC_data_was_lost(Exception_Base):
    """IADC data was lost"""

class Exception_Sense_data_FIFO_overflow_detected(Exception_Base):
    """Sense data FIFO overflow detected"""

class Exception_Internal_communication_failure_detected_by_CPU(Exception_Base):
    """Internal communication failure detected by CPU"""

class Exception_Internal_command_queue_overflow_detected(Exception_Base):
    """Internal command queue overflow detected"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

class Exception_(Exception_Base):
    """"""

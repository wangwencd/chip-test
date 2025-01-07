# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/7 10:55
File: exception_IT6722A.py
"""
from parse.exception.exception_base import Exception_Base

class Exception_Other_error(Exception_Base):
    """Other error"""

class Exception_No_input_command(Exception_Base):
    """No input command"""

class Exception_Parameter_overflowed(Exception_Base):
    """Parameter overflowed"""

class Exception_Wrong_units_for_parameter(Exception_Base):
    """Wrong units for parameter"""

class Exception_Wrong_type_of_parameter(Exception_Base):
    """Wrong type of parameter"""

class Exception_Wrong_number_of_parameter(Exception_Base):
    """Wrong number of parameter"""

class Exception_Unmatched_quotation_mark(Exception_Base):
    """Unmatched quotation mark"""

class Exception_Unmatched_bracket(Exception_Base):
    """Unmatched bracket"""

class Exception_Invalid_command(Exception_Base):
    """Invalid command"""

class Exception_No_entry_in_list(Exception_Base):
    """No entry in list"""

class Exception_Too_many_char(Exception_Base):
    """Too many char"""

class Exception_Execution_error(Exception_Base):
    """Execution error"""

class Exception_System_error(Exception_Base):
    """System error"""

class Exception_Too_many_errors(Exception_Base):
    """Too many errors"""

class Exception_Query_INTERRUPTED(Exception_Base):
    """Query INTERRUPTED"""

class Exception_Query_DEADLOCKED(Exception_Base):
    """Query DEADLOCKED"""

class Exception_Mainframe_Initialization_Lost(Exception_Base):
    """Mainframe Initialization Lost"""

class Exception_Module_Calibration_Lost(Exception_Base):
    """Module Calibration Lost"""

class Exception_Eeprom_failure(Exception_Base):
    """Eeprom failure"""

class Exception_Output_Locked(Exception_Base):
    """Output Locked"""

class Exception_Flash_write_failed(Exception_Base):
    """Flash write failed"""

class Exception_Flash_erase_failed(Exception_Base):
    """Flash erase failed"""

class Exception_RS232_receiver_parity(Exception_Base):
    """RS-232 receiver parity"""

class Exception_Front_panel_buffer_overrun(Exception_Base):
    """Front panel buffer overrun"""

class Exception_Front_panel_timeout(Exception_Base):
    """Front panel timeout"""

class Exception_CAL_password_is_incorrect(Exception_Base):
    """CAL password is incorrect"""

class Exception_CAL_not_enabled(Exception_Base):
    """CAL not enabled"""

class Exception_readback_cal_are_incorrect(Exception_Base):
    """readback cal are incorrect"""

class Exception_programming_cal_are_incorrect(Exception_Base):
    """programming cal are incorrect"""



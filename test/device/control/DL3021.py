# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/12/31 13:42
File: DL3021.py
"""
import logging

from test.device.control.IT8811 import IT8811

L = logging.getLogger('Main')

class DL3021(IT8811):
    """
    DL3021 control
    """
    def __init__(self, cls, name=None):
        self.control = cls
        super().__init__(cls, self.name)
        self.name = name if name else 'DL3021'

    def set_CC_mode_max_voltage(self, value):
        """
        Set max voltage in CC mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'CURR:VLIM ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CC mode')
        self.check_error()

    def set_CV_mode_max_current(self, value):
        """
        Set max current in CV mode

        Args:
            value: Max current value, string format, unit: A
        """
        command = 'VOLT:ILIM ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max current: ' + str(value) + 'A' + ' in CV mode')
        self.check_error()

    def set_CR_mode_max_voltage(self, value):
        """
        Set max voltage in CR mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'RES:VLIM ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CR mode')
        self.check_error()

    def set_CW_mode_max_voltage(self, value):
        """
        Set max voltage in CW mode

        Args:
            value: Max voltage value, string format, unit: V
        """
        command = 'POW:VLIM ' + str(value)
        self.control.write(command)
        L.debug(self.name + ' set max voltage: ' + str(value) + 'V' + ' in CW mode')
        self.check_error()

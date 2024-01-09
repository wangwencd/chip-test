# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/12/26 18:28
File: mcuwindow_control.py
"""
import re
import logging
import traceback
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from .ui_mcuwindow import Ui_ui_mcuwindow
from test.device.flow.control_flow import Control_Flow
from test.condition.condition import Condition
from parse.file.reg_operation import Reg_Operation

L = logging.getLogger('Main')

class MCUwindow_Control(QWidget, Ui_ui_mcuwindow):
    """
    MCUwindow UI control class
    """
    def __init__(self):
        """
        Init MCUwindow UI, and define UI slot function
        """
        super().__init__()

        """Set Ui interface according to QT designer"""
        self.setupUi(self)

        """Set icon"""
        self.setWindowIcon(QIcon('./gear.ico'))

        """Instantiate some class"""
        self.cond = Condition()
        self.flow = Control_Flow()

        """Define slot function"""
        self.pushButton_open.clicked.connect(self.open_mcu)  # Open mcu push button plot function
        self.pushButton_close.clicked.connect(self.close_mcu)  # Close mcu push button plot function
        self.pushButton_write.clicked.connect(lambda: self.set_parameter(1))  # Set func push button plot function
        self.pushButton_read.clicked.connect(lambda: self.set_parameter(2))  # Set func push button plot function

    def find_mcu_name(self):
        """
        Return mcu name from tabWidget_instrument.currentWidget

        Returns:
            new_name: Instrument name
        """
        new_name = self.comboBox_device.currentText()  # Get tab name from tabWidget_instrument

        return new_name

    def open_mcu(self):
        """
        Open mcu plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_mcu_name()  # Get instrument string
            self.cond.test_info['Communication'] = 'serial'  # Get communication string
            self.cond = self.flow.open(self.cond)  # Open instrument function of class
            L.info('Open instrument: ' + self.cond.test_info['Instrument'] +
                   ', Communication: ' + self.cond.test_info['Communication'])

        except:
            L.error(traceback.format_exc())

    def close_mcu(self):
        """
        Close mcu plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_mcu_name()  # Get instrument string
            self.cond = self.flow.close(self.cond)  # Open instrument function of class
            L.info('Open instrument: ' + self.cond.test_info['Instrument'] +
                   ', Communication: ' + self.cond.test_info['Communication'])

        except:
            L.error(traceback.format_exc())

    def set_parameter(self, function):
        """
        Set func plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_mcu_name()  # Get instrument string
            flow = self.flow.confirm_flow_class(self.cond, self.cond.test_info['Instrument'])  # Confirm class of flow
            if function == 1:
                self.write_mcu(flow)  # Go into function of specific class
            elif function == 2:
                self.read_mcu(flow)  # Go into function of specific class

        except:
            L.error(traceback.format_exc())

    def write_mcu(self, flow):
        """
        Operate mcu, according to mcu window ui

        Args:
            flow: Class of control flow
        """
        name = self.tabWidget_function.currentWidget().objectName()  # Return specific function of mcu

        if re.search('I2C', name, re.I) is not None:  # I2C

            reg_data = self.reg_inversion(Reg_Operation.hex_to_dec(self.lineEdit_I2C_reg_value.text()))
            reg_address = Reg_Operation.hex_to_dec(self.lineEdit_I2C_reg_address.text())
            data_buf = reg_address + reg_data

            self.cond.test_info['Msg'] = {
                'bus_num': int(self.lineEdit_I2C_bus_num.text()),
                'i2c_address': int(self.lineEdit_I2C_slave.text(), 16),
                'data_buf': data_buf,
                'rx_size': 0,
                'restart': int(self.lineEdit_I2C_restart.text()),
                "frequency": int(self.lineEdit_I2C_frequency.text()),
            }
            self.cond = flow.I2C_write(self.cond)

        elif re.search('GPIO', name, re.I) is not None:  # GPIO
            self.cond.test_info['Msg'] = {
                'gpio_num': int(self.lineEdit_GPIO_number.text()),
                'set_value': int(self.lineEdit_GPIO_value.text()),
                'gpio_func': 1,
                'gpio_vssel': int(self.lineEdit_GPIO_vssel.text()),
                'gpio_pad': int(self.lineEdit_GPIO_pad.text()),
            }
            self.cond = flow.GPIO_write(self.cond)

        elif re.search('RST', name, re.I) is not None:  # RST
            self.cond.test_info['Msg'] = {
            }
            self.cond = flow.Reset(self.cond)

        elif re.search('SPI', name, re.I) is not None:  # SPI

            reg_data = self.reg_inversion(Reg_Operation.hex_to_dec(self.lineEdit_SPI_reg_value.text()))
            reg_address = Reg_Operation.hex_to_dec(self.lineEdit_SPI_reg_address.text())
            data_buf = reg_address + reg_data

            self.cond.test_info['Msg'] = {
                'cfg': int(self.lineEdit_SPI_config.text()),
                'fstb': int(self.lineEdit_SPI_first_bit.text()),
                'cpol': int(self.lineEdit_SPI_CPOL.text()),
                'cpha': int(self.lineEdit_SPI_CHPA.text()),
                'size': int(self.lineEdit_SPI_data_size.text()),
                'cspol': int(self.lineEdit_SPI_CSPOL.text()),
                'freq': int(self.lineEdit_SPI_frequency.text()),
                'data_buf': data_buf,
                'rx_size': 0,
                'bus_num': int(self.lineEdit_SPI_bus_num.text()),
            }
            self.cond = flow.SPI_write(self.cond)

    def read_mcu(self, flow):
        """
        Operate mcu, according to mcu window ui

        Args:
            flow: Class of control flow
        """
        name = self.tabWidget_function.currentWidget().objectName()  # Return specific function of mcu

        if re.search('I2C', name, re.I) is not None:  # I2C
            data_buf = Reg_Operation.hex_to_dec(
                self.lineEdit_I2C_reg_address.text()
            )
            self.cond.test_info['Msg'] = {
                'bus_num': int(self.lineEdit_I2C_bus_num.text()),
                'i2c_address': int(self.lineEdit_I2C_slave.text(), 16),
                'data_buf': data_buf,
                'rx_size': int(self.lineEdit_I2C_rx_size.text()),
                'restart': int(self.lineEdit_I2C_restart.text()),
                "frequency": int(self.lineEdit_I2C_frequency.text()),
            }
            self.cond = flow.I2C_read(self.cond)
            data_buf_string = ''
            try:
                reg_data = self.reg_inversion(self.cond.measurement_info['Msg'].data_buf)
            except:
                self.lineEdit_I2C_reg_value.setText(data_buf_string)
                return
            data_buf = Reg_Operation.dec_to_hex(reg_data)
            for data in data_buf:
                data_buf_string = data_buf_string + data + ','
            self.lineEdit_I2C_reg_value.setText(data_buf_string)

        elif re.search('GPIO', name, re.I) is not None:  # GPIO
            self.cond.test_info['Msg'] = {
                'gpio_num': int(self.lineEdit_GPIO_number.text()),
                'get_value': int(self.lineEdit_GPIO_value.text()),
                'gpio_func': 0,
                'gpio_vssel': int(self.lineEdit_GPIO_vssel.text()),
                'gpio_pad': int(self.lineEdit_GPIO_pad.text()),
            }
            self.cond = flow.GPIO_read(self.cond)
            self.lineEdit_GPIO_value.setText(str(self.cond.measurement_info['Msg'].get_value))

        elif re.search('RST', name, re.I) is not None:  # RST
            self.cond.test_info['Msg'] = {
            }
            self.cond = flow.Reset(self.cond)

        elif re.search('SPI', name, re.I) is not None:  # SPI
            data_buf = Reg_Operation.hex_to_dec(
                self.lineEdit_SPI_reg_address.text()
            )
            self.cond.test_info['Msg'] = {
                'cfg': int(self.lineEdit_SPI_config.text()),
                'fstb': int(self.lineEdit_SPI_first_bit.text()),
                'cpol': int(self.lineEdit_SPI_CPOL.text()),
                'cpha': int(self.lineEdit_SPI_CHPA.text()),
                'size': int(self.lineEdit_SPI_data_size.text()),
                'cspol': int(self.lineEdit_SPI_CSPOL.text()),
                'freq': int(self.lineEdit_SPI_frequency.text()),
                'data_buf': data_buf,
                'rx_size': int(self.lineEdit_SPI_reg_number.text()),
                'bus_num': int(self.lineEdit_SPI_bus_num.text()),
            }
            self.cond = flow.SPI_read(self.cond)
            data_buf_string = ''
            try:
                reg_data = self.reg_inversion(self.cond.measurement_info['Msg'].data_buf)
            except:
                self.lineEdit_SPI_reg_value.setText(data_buf_string)
                return
            data_buf = Reg_Operation.dec_to_hex(reg_data)
            for data in data_buf:
                data_buf_string = data_buf_string + data + ','
            self.lineEdit_SPI_reg_value.setText(data_buf_string)

    def reg_inversion(self, reg_list: list):

        if self.radioButton_reg_inversion.isChecked():
            reg_list.reverse()

        return reg_list
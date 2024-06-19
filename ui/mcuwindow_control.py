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

    def find_device_name(self):
        """
        Return device name from tabWidget_instrument.currentWidget

        Returns:
            new_name: Device name
        """
        new_name = self.comboBox_device.currentText()  # Get tab name from tabWidget_instrument

        return new_name

    def find_device_communication(self):
        """
        Return device name from tabWidget_instrument.currentWidget

        Returns:
            new_name: Device communication
        """
        protocol = self.comboBox_protocol.currentText()  # Get tab name from tabWidget_instrument

        return protocol

    def open_mcu(self):
        """
        Open mcu plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_device_name()  # Get instrument string
            self.cond.test_info['Communication'] = self.find_device_communication()  # Get communication string
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
            self.cond.test_info['Instrument'] = self.find_device_name()  # Get instrument string
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
            self.cond.test_info['Instrument'] = self.find_device_name()  # Get instrument string
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
            data_buf = self.reg_inversion(Reg_Operation.hex_to_dec(
                self.lineEdit_SPI_DO.text()
            ))
            self.cond.test_info['Msg'] = (refresh_SPI(
                bus_num=self.lineEdit_SPI_bus_num.text(),
                cfg=self.lineEdit_SPI_config.text(),
                cpol=self.lineEdit_SPI_CPOL.text(),
                cpha=self.lineEdit_SPI_CHPA.text(),
                fstb=self.lineEdit_SPI_first_bit.text(),
                size=self.lineEdit_SPI_data_size.text(),
                frequency=self.lineEdit_SPI_frequency.text(),
                data_buf=data_buf,
                rx_size=len(data_buf),
            )).copy()

            for key, value in self.cond.test_info['Msg'].items():
                try:
                    self.cond.test_info['Msg'][key] = int(value)
                except:
                    pass
            self.cond = flow.SPI_write(self.cond)
            data_buf_string = ''
            try:
                reg_data = self.reg_inversion(self.cond.measurement_info['Msg'])
            except:
                self.lineEdit_SPI_DI.setText(data_buf_string)
                return
            data_buf = Reg_Operation.dec_to_hex(reg_data)
            for data in data_buf:
                data_buf_string = data_buf_string + data + ','
            self.lineEdit_SPI_DI.setText(data_buf_string)

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
                reg_data = self.reg_inversion(self.cond.measurement_info['Msg'])
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
            self.lineEdit_GPIO_value.setText(str(self.cond.measurement_info['Msg']))

        elif re.search('RST', name, re.I) is not None:  # RST
            self.cond.test_info['Msg'] = {
            }
            self.cond = flow.Reset(self.cond)

        elif re.search('SPI', name, re.I) is not None:  # SPI
            data_buf = self.reg_inversion(Reg_Operation.hex_to_dec(
                self.lineEdit_SPI_DO.text()
            ))
            self.cond.test_info['Msg'] = (refresh_SPI(
                bus_num=self.lineEdit_SPI_bus_num.text(),
                cfg=self.lineEdit_SPI_config.text(),
                cpol=self.lineEdit_SPI_CPOL.text(),
                cpha=self.lineEdit_SPI_CHPA.text(),
                fstb=self.lineEdit_SPI_first_bit.text(),
                size=self.lineEdit_SPI_data_size.text(),
                frequency=self.lineEdit_SPI_frequency.text(),
                data_buf=data_buf,
                rx_size=len(data_buf),
            )).copy()

            for key, value in self.cond.test_info['Msg'].items():
                try:
                    self.cond.test_info['Msg'][key] = int(value)
                except:
                    pass
            self.cond = flow.SPI_read(self.cond)
            data_buf_string = ''
            try:
                reg_data = self.reg_inversion(self.cond.measurement_info['Msg'])
            except:
                self.lineEdit_SPI_DI.setText(data_buf_string)
                return
            data_buf = Reg_Operation.dec_to_hex(reg_data)
            for data in data_buf:
                data_buf_string = data_buf_string + data + ','
            self.lineEdit_SPI_DI.setText(data_buf_string)

    def reg_inversion(self, reg_list: list):

        if self.radioButton_reg_inversion.isChecked():
            reg_list.reverse()

        return reg_list

def refresh_SPI(data_buf=[], cfg=0, cpol=0, cpha=0, fstb=1, size=1, cspol=0, rx_size=0, frequency=5, bus_num=1):
    """
    Refresh SPI command, which will be sent to mcu.

    Args:
        data_buf: List of register address and data, format: list, e.g. [0x00, 0x01].
        rx_size: Length of register data user wants to get, format: int.
        cfg: SPI setting configuration, 0=not set/ 1=set, format: int.
        cpol: SPI polarity configuration, 0=low/ 1=high, format: int.
        cpha: SPI phase configuration, 0=first edge/ 1=second edge, format: int.
        fstb: SPI data transforming configuration, 0=LSB/ 1=MSB, format: int.
        size: SPI data size configuration, 0=8bit/ 1=16bit, format:int.
        cspol: SPI effective CS configuration, 0=low level is effective/ 1=high level is effective, format: int.
        frequency: SPI transmission rate, 0=24M/ 1=12/ 2=6M/ 3=3M/ 4=1.5M/ 5=750K/ 6=375K/ 7=187.5K, format: int.
        bus_num: SPI pin at mcu, default is 1, format: int.

    Returns:
        msg: Group of SPI command which will be sent to mcu, format: dict.
    """
    """Need to set data_buf, rx_size"""
    msg = {
        'data_buf': data_buf,
        'bus_num': bus_num,
        'cfg': cfg,
        'cpol': cpol,
        'cpha': cpha,
        'fstb': fstb,
        'size': size,
        'cspol': cspol,
        'rx_size': rx_size,
        "freq": frequency,
    }

    return msg
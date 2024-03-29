# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/3/26 13:52
File: CH341A.py
"""
import logging
from ctypes import *
from parse.file.reg_operation import Reg_Operation

L = logging.getLogger('Main')

class CH341A(object):
    """
    CH341A control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'CH341A'

    def I2C_stream(self, **kwargs):
        """
        I2C streaming operation

        Args:
            **kwargs: Message dict

        Returns:
            in_buf: I2C return message
        """
        i2c_address = kwargs.get('i2c_address')
        data_buf = kwargs.get('data_buf')
        iIndex = 0
        iReadLength = 0
        if 'bus_num' in kwargs:
            iIndex = kwargs.get('bus_num')
        if 'rx_size' in kwargs:
            iReadLength = kwargs.get('rx_size')
        iWriteLength = len([i2c_address] + data_buf)
        iWriteBuffer = (c_byte * iWriteLength)()
        oReadBuffer = (c_byte * iReadLength)()
        iWriteBuffer[0] = (i2c_address << 1)
        for i in range(iWriteLength - 1):
            iWriteBuffer[i + 1] = data_buf[i]
        self.control.instrument.CH341StreamI2C(iIndex, iWriteLength, iWriteBuffer, iReadLength, oReadBuffer)
        result_list = [value & 0xff for value in list(oReadBuffer)]
        return result_list

    def I2C_speed(self, **kwargs):
        """
        Set I2C speed

        Args:
            **kwargs: Message dict
        """
        bus_num = int(kwargs['bus_num'])
        imode = 1

        if 'frequency' in kwargs:
            for key, value in I2C_frequency.items():
                if kwargs.get('frequency') == key:
                    imode = value
        self.control.instrument.CH341SetStream(bus_num, imode)

    def write_I2C(self, msg):
        """
        Output i2c message

        Args:
            msg: Message dict

        Returns:
            in_buf: Return i2c data
        """
        data_buf = msg['data_buf']
        self.I2C_speed(**msg)
        result_list = self.I2C_stream(**msg)
        self.parse_result(data_buf, 1)

        return result_list

    def read_I2C(self, msg):
        """
        Get i2c message

        Args:
            msg: Message dict

        Returns:
            in_buf: Return i2c data
        """
        self.I2C_speed(**msg)
        result_list = self.I2C_stream(**msg)
        self.parse_result(result_list, 2)

        return result_list

    def reset(self, **kwargs):
        """
        Reset device

        Args:
            kwargs: Message dict
        """
        iIndex = 0
        if 'bus_num' in kwargs:
            iIndex = kwargs.get('bus_num')
        self.control.instrument.CH341ResetDevice(iIndex)

        self.parse_result(kwargs, 5)

    def SPI_stream(self, **kwargs):
        """
        SPI streaming operation

        Args:
            **kwargs: Message dict

        Returns:
            in_buf: SPI return message
        """
        data_buf = kwargs.get('data_buf')
        iIndex = 0
        in_length = 0
        iChipSelect = 128
        if 'bus_num' in kwargs:
            iIndex = kwargs.get('bus_num')
        if 'rx_size' in kwargs:
            in_length = kwargs.get('rx_size')
        if 'cpol' in kwargs:
            for key, value in SPI_CS.items():
                if kwargs.get('cpol') == key:
                    iChipSelect = value
        out_length = len(data_buf)
        iLength = max(in_length, out_length)
        ioBuffer = (c_byte * iLength)()
        for i in range(out_length):
            ioBuffer[i] = data_buf[i]
        self.control.instrument.CH341StreamSPI4(iIndex, iChipSelect, iLength, ioBuffer)
        result_list = [value & 0xff for value in list(ioBuffer)]
        return result_list

    def write_SPI(self, msg):
        """
        Output SPI message

        Args:
            msg: Message dict

        Returns:
            in_buf: Return SPI data
        """
        data_buf = msg['data_buf']
        result_list = self.SPI_stream(**msg)
        self.parse_result(data_buf, 6)

        return result_list

    def read_SPI(self, msg):
        """
        Get SPI message

        Args:
            msg: Message dict

        Returns:
            in_buf: Return SPI data
        """
        result_list = self.SPI_stream(**msg)
        self.parse_result(result_list, 7)

        return result_list

    def parse_result(self, msg, func_flag):
        """
        Parse result and output the information

        Args:
            msg: Result structure
            func_flag: Function flag, func_flag = 1/2/3/4
        """
        if msg is not None:

            if func_flag == 1:  # I2C write function
                parse_result = Reg_Operation.dec_to_hex(msg)
                L.info(self.name + ' write address: [' + str(parse_result[0]) + '], value: ' + str(parse_result[1:]))

            elif func_flag == 2:  # I2C read function
                parse_result = Reg_Operation.dec_to_hex(msg)
                L.info(self.name + ' read value: ' + str(parse_result))

            elif func_flag == 3:  # GPIO write function
                L.info(self.name + ' write PIN: [' + str(msg['gpio_num']) + '], value: [' + str(msg['set_value']) + ']')

            elif func_flag == 4:  # GPIO write function
                L.info(self.name + ' read PIN: [' + str(msg) + '], value: [' + str(msg.get_value) + ']')

            elif func_flag == 5:  # Reset function
                L.info(self.name + ' reset')

            elif func_flag == 6:  # SPI write function
                parse_result = Reg_Operation.dec_to_hex(msg['data_buf'])
                L.info(
                    self.name + ' write address: [' + str(parse_result[0]) + '], value: ' + str(parse_result[1:])
                )

            elif func_flag == 7:  # SPI read function
                parse_result = Reg_Operation.dec_to_hex(msg)
                L.info(self.name + ' read value: ' + str(parse_result))


I2C_frequency = {
    'frequency': 'imode',
    1: 1,
    2: 2,
    3: 3,
    4: 3,
    5: 0,
}

SPI_CS = {
    'CS ID': 'iChipSelect',
    0: 128,
    1: 129,
    2: 130,
}
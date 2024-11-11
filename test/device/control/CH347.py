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

class mSpiCfgS(Structure):
    """
    _SPI_CONFIG
    """

    _fields_ = [
        ('iMode', c_char),  # 0-3:SPI Mode0/1/2/3
        ('iClock', c_char),  # 0=60MHz, 1=30MHz, 2=15MHz, 3=7.5MHz, 4=3.75MHz, 5=1.875MHz, 6=937.5KHz，7=468.75KHz
        ('iByteOrder', c_char),  # 0=LSB, 1=MSB
        ('iSpiWriteReadInterval', c_short),  # Write/ Read interval time, unit: us
        ('iSpiOutDefaultData', c_char),  # SPI default data when reading
        ('iChipSelect', c_long),  # Chip selection, 0:No CS, 128:CS1, 129:CS2
        ('CS1Polarity', c_char),  # CS1 polarity, 0:active low, 1:active high
        ('CS2Polarity', c_char),  # CS2 polarity, 0:active low, 1:active high
        ('iIsAutoDeativeCS', c_short),  # Whether to automatically deactivate CS, 0:no, 1:yes
        ('iActiveDelay', c_short),  # Delay time after writing/ read while CS is active, unit: us
        ('iDelayDeactive', c_long),  # Delay time after writing/ read while CS is deactivated, unit: us
    ]

class CH347(object):
    """
    CH347 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'CH347'
        self.spi_config = mSpiCfgS()
        self.last_kwargs = {}

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
        iIndex = kwargs.get('bus_num', 0)
        iReadLength = kwargs.get('rx_size', 0)
        iWriteLength = len([i2c_address] + data_buf)
        iWriteBuffer = (c_byte * iWriteLength)()
        oReadBuffer = (c_byte * iReadLength)()
        iWriteBuffer[0] = (i2c_address << 1)
        iWriteBuffer[1:iWriteLength] = data_buf[:iWriteLength - 1]
        self.control.instrument.CH347StreamI2C(iIndex, iWriteLength, iWriteBuffer, iReadLength, oReadBuffer)
        result_list = [value & 0xff for value in list(oReadBuffer)]
        return result_list

    def I2C_speed(self, **kwargs):
        """
        Set I2C speed

        Args:
            **kwargs: Message dict
        """
        bus_num = kwargs.get('bus_num', 0)
        frequency = kwargs.get('frequency', 1)
        imode = I2C_frequency[frequency]
        self.control.instrument.CH347I2C_Set(bus_num, imode)

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

    def SPI_init(self, **kwargs):
        """
        Init SPI config

        Args:
            kwargs: Message dict
        """
        def get_iMode(**kwargs):
            cpol = kwargs.get('cpol', 1)
            cpha = kwargs.get('cpha', 1)
            if cpol == 0 and cpha == 0:
                return c_char(0)

            elif cpol == 0 and cpha == 1:
                return c_char(1)

            elif cpol == 1 and cpha == 0:
                return c_char(2)

            elif cpol == 1 and cpha == 1:
                return c_char(3)
        if self.last_kwargs == kwargs:
            return
        iIndex = kwargs.get('bus_num', 0)
        iMode = get_iMode(**kwargs)
        iClock = kwargs.get('freq', 0)
        iByteOrder = kwargs.get('fstb', 0)
        iChipSelect = SPI_CS[kwargs.get('cspol', 0)]
        self.spi_config = mSpiCfgS(
            iMode=iMode,
            iClock=iClock,
            iByteOrder=iByteOrder,
            iChipSelect=iChipSelect
        )
        self.control.instrument.CH347SPI_Init(iIndex, byref(self.spi_config))
        self.last_kwargs = kwargs

    def SPI_stream(self, **kwargs):
        """
        SPI streaming operation

        Args:
            **kwargs: Message dict

        Returns:
            in_buf: SPI return message
        """
        data_buf = kwargs.get('data_buf')
        iIndex = kwargs.get('bus_num', 0)
        cspol = kwargs.get('cspol', 0)
        iChipSelect = SPI_CS[cspol]
        iLength = len(data_buf)
        ioBuffer = (c_byte * iLength)(*data_buf)
        self.control.instrument.CH347StreamSPI4(iIndex, iChipSelect, iLength, ioBuffer)
        result_list = [value & 0xff for value in list(ioBuffer)]
        return result_list

    def SPI_speed(self, **kwargs):
        """
        Set SPI speed

        Args:
            **kwargs: Message dict
        """
        bus_num = kwargs.get('bus_num', 0)
        frequency = kwargs.get('frequency', 1)
        imode = SPI_frequency[frequency]
        self.control.instrument.CH347I2C_Set(bus_num, imode)

    def write_SPI(self, msg):
        """
        Output SPI message

        Args:
            msg: Message dict

        Returns:
            in_buf: Return SPI data
        """
        data_buf = msg['data_buf']
        self.SPI_init(**msg)
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
        self.SPI_init(**msg)
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
    1: 1,  # 100kHz
    2: 2,  # 400kHz
    3: 3,  # 750kHz
    4: 3,  # 750kHz
    5: 0,  # 20kHz
}

SPI_frequency = {
    'frequency': 'imode',
    0: 0,  # 60MHz
    1: 1,  # 30MHz
    2: 2,  # 15MHz
    3: 3,  # 7.5MHz
    4: 4,  # 3.75MHz
    5: 5,  # 1.875MHz
    6: 6,  # 937.5kHz
    7: 7,  # 468.75kHz
}

SPI_CS = {
    'CS ID': 'iChipSelect',
    0: 128,  # CS0 selected
    1: 129,  # CS1 selected
}



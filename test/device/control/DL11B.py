# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/30 16:35
File: DL11B.py
"""
import logging
import modbus_tk.defines as cst

L = logging.getLogger('Main')

class DL11B(object):
    """
    DL11B control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DL11B'
        self.compensation = 0.0

    def change_resolution(self, resolution=0.1):
        """
        Change temperature resolution on display

        Args:
            resolution: Resolution of temperature, float format, options: 0.1 / 1
        """
        if resolution == 0.1:  # Resolution is 0.1℃
            self.control.write(1, cst.WRITE_SINGLE_REGISTER, 258, 1, 0)
            L.debug(self.name + ' resolution is 0.1!')

        elif resolution == 1 or resolution == 1.0:  # Resolution is 1℃
            self.control.write(1, cst.WRITE_SINGLE_REGISTER, 258, 1, 1)
            L.debug(self.name + ' resolution is 1!')

        else:
            L.error(self.name + ' resolution is not right format!')
            raise ValueError

    def write_temperature_compensation(self, value, channel=1):
        """
        Write temperature compensation of one channel

        Args:
            value: Temperature compensation value of one channel, float format, unit: ℃
            channel: Channel number, int format, options: 1 / 2 / 3 / 4 / 5 / 6
        """
        temp = int(10 * float(value))
        self.control.write(1,
                           cst.WRITE_SINGLE_REGISTER,
                           511 + int(channel),
                           1,
                           temp
                           )
        L.debug(self.name + ' channel: ' + str(channel) + ', set temperature compensation: ' + str(value) + 'C')

    def query_temperature_compensation(self, channel=1):
        """
        Query temperature compensation from reg

        Args:
            channel: Channel number, int format, options: 1 / 2 / 3 / 4 / 5 / 6

        Returns:
            compensation: Result of temperature compensation of one channel
        """
        compensation = self.control.query(1,
                                    cst.READ_HOLDING_REGISTERS,
                                    511 + int(channel),
                                    1
                                    )[0] / 10

        if compensation > 6000: # Value is negative
            self.compensation = compensation - 6553.6

        else: # Value is positive
            self.compensation = compensation
        L.debug(self.name + ' channel: ' + str(channel) + ', get temperature compensation: ' + str(self.compensation) + 'C')

        return self.compensation

    def query_temperature(self, channel=1):
        """
        Query temperature

        Args:
            channel: Channel number, int format, options: 1 / 2 / 3 / 4 / 5 / 6

        Returns:
            result: Result of temperature of one channel
        """
        result = self.control.query(1,
                                    cst.READ_INPUT_REGISTERS,
                                    1023 + int(channel),
                                    1
                                    )[0]

        if result > 32678:
            result = (result - 65535) / 10
        else:
            result = result / 10
        result = result + self.compensation
        L.debug(self.name + ' channel: ' + str(channel) + ', temperature: ' + str(result))

        return result

    def close_all(self):
        """
        Close modbus RTU com
        """
        self.control.close()

    def RST(self):
        """
        Reset serial com
        """
        self.control.reset()
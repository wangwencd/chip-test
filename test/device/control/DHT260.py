# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/10/24 14:17
File: DHT260.py
"""
import re
import logging
import modbus_tk.defines as cst

L = logging.getLogger('Main')

class DHT260(object):
    """
    DHT260 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DHT260'

    def check_error(self):
        """
        Read the most recent error.
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            result = self.control.query(1,
                                        cst.READ_HOLDING_REGISTERS,
                                        2142,
                                        16
                                        )[0] / 10

        elif 'tcp' in self.control.__str__():  # TCP communication
            result = self.control.query(1,
                                        cst.READ_HOLDING_REGISTERS,
                                        2142,
                                        16
                                        )[0] / 10

    def channel_on(self):
        """
        Channel on
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               32971,
                               0,
                               65280
                               )

        elif 'tcp' in self.control.__str__():  # TCP communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               33055,
                               0,
                               65280
                               )
        L.debug(self.name + ' channel on')

    def channel_off(self):
        """
        Channel off
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               32971,
                               0,
                               0
                               )

        elif 'tcp' in self.control.__str__():  # TCP communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               33057,
                               0,
                               65280
                               )
        L.debug(self.name + ' channel off')

    def set_temperature(self, temperature):
        """
        Write temperature parameter

        Args:
            temperature: Temperature value, float format, unit: ℃
        """
        temp = int(10 * float(temperature))

        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_REGISTER,
                               2000,
                               0,
                               temp
                               )
            self.save_change()

        elif 'tcp' in self.control.__str__():  # TCP communication
            self.control.write(1,
                               cst.WRITE_SINGLE_REGISTER,
                               1999,
                               0,
                               temp
                               )
        L.debug(self.name + ', set temperature: ' + str(temperature) + 'C')

    def set_humidity(self, humidity):
        """
        Write humidity parameter

        Args:
            humidity: Humidity value, float format, unit: %
        """
        temp = int(10 * float(humidity))

        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_REGISTER,
                               2001,
                               0,
                               temp
                               )
            self.save_change()

        elif 'tcp' in self.control.__str__():  # TCP communication
            self.control.write(1,
                               cst.WRITE_SINGLE_REGISTER,
                               2000,
                               0,
                               temp
                               )
        L.debug(self.name + ', set temperature: ' + str(humidity) + '%')

    def save_change(self):
        """
        Write this bit after set temperature/ humidity
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               32159,
                               0,
                               65280
                               )

        elif 'tcp' in self.control.__str__():  # TCP communication
            pass
        L.debug(self.name + ' save the change')

    def query_temperature(self):
        """
        Query temperature parameter

        Returns:
            result: Temperature value
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            result = self.control.query(1,
                               cst.READ_HOLDING_REGISTERS,
                               2100,
                               1
                               )[0]

        elif 'tcp' in self.control.__str__():  # TCP communication
            result = self.control.query(1,
                               cst.READ_INPUT_REGISTERS,
                               2099,
                               1
                               )[0]

        if result > 60000:
            result = (result - 65535) / 10
        else:
            result = result / 10
        L.debug(self.name + ' get temperature: ' + str(result) + 'C')

        return result

    def query_humidity(self):
        """
        Query humidity parameter

        Returns:
            result: Humidity value
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            result = self.control.query(1,
                               cst.READ_HOLDING_REGISTERS,
                               2102,
                               1
                               )[0] /10

        elif 'tcp' in self.control.__str__():  # TCP communication
            result = self.control.query(1,
                               cst.READ_INPUT_REGISTERS,
                               2101,
                               1
                               )[0] /10

        L.debug(self.name + ' get humidity: ' + str(result) + '%')

        return result

    def enable_temperature(self):
        """
        Enable the temperature setting
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               32144,
                               0,
                               65280
                               )

        elif 'tcp' in self.control.__str__():  # TCP communication
            pass
        L.debug(self.name + ' enable setting temperature')

    def enable_humidity(self):
        """
        Enable the humidity setting
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.write(1,
                               cst.WRITE_SINGLE_COIL,
                               32145,
                               0,
                               65280
                               )

        elif 'tcp' in self.control.__str__():  # TCP communication
            pass
        L.debug(self.name + ' enable setting humidity')

    def RST(self):
        """
        Reset serial com
        """
        if 'rtu' in self.control.__str__():  # RTU communication
            self.control.reset()

        elif 'tcp' in self.control.__str__():  # TCP communication
            pass


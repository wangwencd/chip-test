# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/5 10:07
File: serial_common.py
"""
import logging
import serial

from test.device.serial import find_port
L = logging.getLogger('Main')

class Serial_Common(object):
    """
    Serial Common control
    """

    def open_instrument(self, condition):
        """
        Open power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        def check_instrument(instrument_port: str):
            """
            Check if there is the instrument port number

            Args:
                instrument_port: Port number of instrument
            """
            if instrument_port == None:
                L.error('Error: Instrument is not found in the serial!')
                raise EnvironmentError

        instrument_name = str(condition.test_info['Instrument']) # Get instrument name from test condition
        instrument_port, instrument_class = find_port(instrument_name)
        check_instrument(instrument_port)
        if instrument_name == 'MAX32670':
            self.instrument = serial.Serial(port=instrument_port,baudrate=115200, timeout=0.1)  # Open instrument
        else:
            self.instrument = serial.Serial(port=instrument_port, timeout=1, write_timeout=1) # Open instrument
            self.instrument.timeout = 1
        condition.Class[instrument_name] = instrument_class

        return condition

    def query(self, command: str):
        """
        Write order to instrument and read result from instrument

        Args:
            command: Command by SCPI

        Returns:
            result: Result of command
        """
        self.instrument.write((str(command) + '\n').encode())
        msg = self.instrument.read(size=128)
        #
        # while msg.decode() == '':
        #     msg = self.instrument.read(size=128)

        if '\n' in msg.decode():
            return msg.decode().split('\n')[0]
        else:
            return msg.decode()

    def write(self, command: str):
        """
        Write order to instrument

        Args:
            command: Command by SCPI
        """
        self.instrument.write((str(command) + '\n').encode())

    def read(self):
        """
        Read result from instrument

        Returns:
            result: Result of command
        """
        msg = self.instrument.read(size=128)
        #
        # while msg.decode() == '':
        #     msg = self.instrument.read(size=128)

        if '\n' in msg.decode():
            return msg.decode().split('\n')[0]
        else:
            return msg.decode()

    def open(self):
        """
        Open serial com
        """
        self.instrument.open()

    def close(self):
        """
        Close serial com
        """
        self.instrument.close()

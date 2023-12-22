# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/11/24 10:05
File: tcp_common.py
"""
import logging

from modbus_tk import modbus_tcp
from test.device.tcp import determine_instrument
L = logging.getLogger('Main')

class TCP_Common(object):
    """
    Modbus TCP common control
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

        instrument_name = str(condition.test_info['Instrument'])  # Get instrument name from test condition
        instrument_addr, instrument_port, instrument_class = determine_instrument(instrument_name)
        check_instrument(instrument_port)
        self.instrument = modbus_tcp.TcpMaster(host=instrument_addr, port=instrument_port)  # Open instrument
        self.instrument.set_timeout(1.0)
        self.instrument.set_verbose(True)
        condition.Class[instrument_name] = instrument_class

        return condition

    def query(self, *args: tuple):
        """
        Write order to instrument and read result from instrument

        Args:
            *args: Command by Modbus TCP

        Returns:
            result: Result of command
        """
        if len(args) < 3:
            L.error('Parameters are not enough!')
            raise ValueError

        elif len(args) == 3:
            return self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2]
            )

        elif len(args) == 4:
            return self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3]
            )

        elif len(args) == 5:
            return self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4]
            )

        elif len(args) == 6:
            return self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4],
                data_format=args[5]
            )

        elif len(args) == 7:
            return self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4],
                data_format=args[5],
                expected_length=args[6]
            )

        elif len(args) == 8:
            return self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4],
                data_format=args[5],
                expected_length=args[6],
                write_starting_address_FC23=args[7]
            )

    def write(self, *args):
        """
        Write order to instrument

        Args:
            *args: Command by Modbus RTU
        """
        if len(args) < 3:
            L.error('Parameters are not enough!')
            raise ValueError

        elif len(args) == 3:
            self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2]
            )

        elif len(args) == 4:
            self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3]
            )

        elif len(args) == 5:
            self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4]
            )

        elif len(args) == 6:
            self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4],
                data_format=args[5]
            )

        elif len(args) == 7:
            self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4],
                data_format=args[5],
                expected_length=args[6]
            )

        elif len(args) == 8:
            self.instrument.execute(
                slave=args[0],
                function_code=args[1],
                starting_address=args[2],
                quantity_of_x=args[3],
                output_value=args[4],
                data_format=args[5],
                expected_length=args[6],
                write_starting_address_FC23=args[7]
            )

    def read(self, *args: tuple):
        """
        Read result from instrument

        Args:
            *args: Command by Modbus TCP

        Returns:
            result: Result of command
        """
        return self.query(args)

    def open(self):
        """
        Open modbus RTU com
        """
        self.instrument.open()

    def close(self):
        """
        Close modbus RTU com
        """
        self.instrument.close()

    def reset(self):
        """
        Clear serial com
        """
        self.instrument._serial.flushOutput()
        self.instrument._serial.flushInput()

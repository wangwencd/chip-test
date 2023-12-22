# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/15 14:42
File: visa_common.py
"""
import logging
from pyvisa import ResourceManager
from test.device.visa import determine_instrument

L = logging.getLogger('Main')

class Visa_Common(object):
    """
    Visa common control
    """
    RM = ResourceManager()

    def get_resourcelist(self):
        """
        Get list name of resource
        """
        self.list_ID = self.RM.list_resources()

    def open_instrument(self, condition):
        """
        Open power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        def check_instrument(instrument_ID: str, list_ID: tuple):
            """
            Check if there is the specific instrument

            Args:
                instrument_ID: ID of instrument
                list_ID: ID list of current instrument
            """
            for ID in list_ID:
                if ID == instrument_ID:
                    return
            L.error('Error: Instrument is not found in the VISA!')
            raise EnvironmentError

        instrument_name = str(condition.test_info['Instrument'])  # Get instrument name from test condition
        instrument_ID, instrument_class = determine_instrument(instrument_name)  # Determine ID and class from name
        self.get_resourcelist()
        check_instrument(instrument_ID, self.list_ID)
        self.instrument = self.RM.open_resource(instrument_ID)  # Open instrument
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
        return self.instrument.query(str(command)).replace('\n','')

    def write(self, command: str):
        """
        Write order to instrument

        Args:
            command: Command by SCPI
        """
        self.instrument.write(str(command))

    def read(self, command: str):
        """
        Read result from instrument

        Args:
            command: Command by SCPI

        Returns:
            result: Result of command
        """
        return self.instrument.read(str(command)).replace('\n','')

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

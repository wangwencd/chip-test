# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/3/26 14:03
File: flow_CH341A.py
"""
import logging
from test.device.control.CH341A import CH341A

L = logging.getLogger('Main')

class Flow_CH341A(CH341A):
    """
    Control flow of CH341A
    """
    def __init__(self, cls):
        self.control = cls
        super().__init__(cls)

    def prepare(self, condition):
        """
        CH341A preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.reset(bus_num=self.control.dev)

        return condition

    def I2C_write(self, condition):
        """
        Write message from I2C

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        in_buf = self.write_I2C(msg)

        return condition

    def I2C_read(self, condition):
        """
        Read message from I2C

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        in_buf = self.read_I2C(msg)
        condition.measurement_info['Msg'] = in_buf

        return condition

    def SPI_write(self, condition):
        """
        Write message from SPI

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        in_buf = self.write_SPI(msg)

        return condition

    def SPI_read(self, condition):
        """
        Read message from SPI

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        in_buf = self.read_SPI(msg)
        condition.measurement_info['Msg'] = in_buf

        return condition

    def close(self, condition):
        """
        Communication close

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.control.close()
        del condition.Class[condition.test_info['Instrument']]

        return condition


    def Reset(self, condition):
        """
        Reset MCU

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        proto_info = self.reset(**msg)
        condition.measurement_info['Msg'] = proto_info

        return condition

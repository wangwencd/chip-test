# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/12/19 15:03
File: flow_MAX32670.py
"""
import time
import logging

from test.device.control.MAX32670 import MAX32670

L = logging.getLogger('Main')

class Flow_MAX32670(MAX32670):
    """
    Control flow of MAX32670
    """
    def __init__(self, cls):
        super(Flow_MAX32670, self).__init__(cls)

    def prepare(self, condition):
        """
        MAX32670 preparation work

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.init_protobuf()
        self.refresh_msg()

    def I2C_write(self, condition):
        """
        Write message from I2C

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        proto_info = self.write_I2C(msg)

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
        proto_info = self.read_I2C(msg)
        condition.measurement_info['Msg'] = proto_info

        return condition

    def GPIO_write(self, condition):
        """
        Write message from GPIO

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        proto_info = self.write_GPIO(msg)

        return condition

    def GPIO_read(self, condition):
        """
        Read message from GPIO

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        msg = condition.test_info['Msg']
        proto_info = self.read_GPIO(msg)
        condition.measurement_info['Msg'] = proto_info

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
        proto_info = self.reset(msg)
        condition.measurement_info['Msg'] = proto_info

        return condition

    def close(self, condition):
        """
        Communication close

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.control.instrument.close()
        del condition.Class[condition.test_info['Instrument']]

        return condition

    def GO_write(self, condition):
        """
        Standby GO write function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        proto_info = self.standby_go(condition.test_info['Msg'])

        return condition

    def DONE_write(self, condition):
        """
        Standby DONE write function

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        proto_info = self.standby_done(condition.test_info['Msg'])

        return condition

    def I2C_read_standby(self, condition):
        """
        Receive I2C data once

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        if isinstance(condition.test_info['Period'], str):
            period = eval(condition.test_info['Period']) / 1000

        else:
            period = float(condition.test_info['Period']) / 1000
        proto_info = self.receive_msg_standby(period)  # Receive I2C data
        self.parse_result(proto_info, 2)  # Parse result
        condition.measurement_info['Msg'] = proto_info

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
        proto_info = self.write_SPI(msg)

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
        proto_info = self.read_SPI(msg)
        condition.measurement_info['Msg'] = proto_info

        return condition

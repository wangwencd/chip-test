# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/10/24 14:20
File: flow_DHT260.py
"""
import logging
from test.device.control.DHT260 import DHT260

L = logging.getLogger('Main')

class Flow_DHT260(DHT260):
    """
    Control flow of DHT260
    """
    def __init__(self, cls):
        self.control = cls
        super().__init__(cls)

    def prepare(self, condition):
        """
        Prepare instrument for test

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.enable_temperature()
        self.enable_humidity()

        return condition

    def set(self, condition):
        """
        Set temperature and humidity

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        if 'Temperature' in condition.test_info.keys():
            self.set_temperature(condition.test_info['Temperature'])

        if 'Humidity' in condition.test_info.keys():
            self.set_humidity(condition.test_info['Humidity'])

        return condition

    def measure(self, condition):
        """
        Measure temperature and humidity

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.measurement_info['Temperature'] = self.query_temperature()
        condition.measurement_info['Humidity'] = self.query_humidity()

        return condition

    def on(self, condition):
        """
        Set channel on

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.channel_on()

        return condition

    def off(self, condition):
        """
        Set channel off

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.channel_off()

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

        return condition

    def set_temp(self, condition):
        """
        Set temperature

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.set_temperature(condition.test_info['Temperature'])

        return condition

    def set_hum(self, condition):
        """
        Set humidity

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        self.set_humidity(condition.test_info['Humidity'])

        return condition

    def measure_temp(self, condition):
        """
        Measure temperature

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.measurement_info['Temperature'] = self.query_temperature()

        return condition

    def measure_hum(self, condition):
        """
        Measure humidity

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        condition.measurement_info['Humidity'] = self.query_humidity()

        return condition

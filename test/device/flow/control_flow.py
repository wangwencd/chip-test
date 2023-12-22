# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/20 16:59
File: control_flow.py
"""
import logging

from test.device.control import Communication_dict

L = logging.getLogger('Main')

class Control_Flow(object):
    """
    Flow of instrument control
    """

    def determine_communication_method(self, name: str):
        """
        Determine base communication method of device

        Args:
            name: Communication method name

        Returns:
            value: Device class
        """
        for key, value in Communication_dict.items():
            if name == key:
                return value()

        L.error('Error: Could not find communication method of device!')
        raise EnvironmentError

    def confirm_flow_class(self, condition, name: str):
        """
        Confirm class of instrument flow

        Args:
            condition: Condition information summary
            name: Instrument name

        Returns:
            value(condition): Class of instrument flow
        """

        for key, value in condition.Class.items():
            if name == key:
                return value

    def open(self, condition):
        """
        Open power supply instrument

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        for key in condition.Class.keys():
            if key == instrument_name:
                return condition

        communication = condition.test_info['Communication']
        communication_class = self.determine_communication_method(communication)
        condition = communication_class.open_instrument(condition)
        condition.Class[instrument_name] = condition.Class[instrument_name](communication_class)

        return condition

    def prepare(self, condition):
        """
        Instrument prepare step

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.prepare(condition)

        return condition

    def on(self, condition):
        """
        Power supply channel on

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.on(condition)

        return condition

    def measure(self, condition):
        """
        Measure voltage and current of power supply

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.measurement_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.measure(condition)

        return condition

    def off(self, condition):
        """
        Power supply channel off

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.off(condition)

        return condition

    def set(self, condition):
        """
        Set voltage and current(and channel)

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.set(condition)

        return condition

    def close(self, condition):
        """
        Communication close

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.close(condition)

        return condition

    def set_voltage(self, condition):
        """
        Set current(and channel)

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.set_voltage(condition)

        return condition

    def set_current(self, condition):
        """
        Set voltage (and channel)

        Args:
            condition: Condition information summary

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = flow.set_current(condition)

        return condition

    def operate(self, condition, name):
        """
        Operate instrument according to name of step

        Args:
            condition: Condition information summary
            name: Name of operation

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.test_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = eval('flow.' + str(name))(condition)

        return condition

    def work(self, condition, name):
        """
        Operate instrument according to name of step

        Args:
            condition: Condition information summary
            name: Name of operation

        Returns:
            condition: Condition information summary
        """
        instrument_name = str(condition.measurement_info['Instrument'])
        flow = self.confirm_flow_class(condition, instrument_name)
        condition = eval('flow.' + str(name))(condition)

        return condition

# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/10/20 16:01
File: instrumentwindow_control.py
"""
import re
import logging
import traceback
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from .ui_instrumentwindow import Ui_ui_instrumentwindow
from test.device.flow.control_flow import Control_Flow
from test.condition.condition import Condition

L = logging.getLogger('Main')


class Instrumentwindow_Control(QWidget, Ui_ui_instrumentwindow):
    """
    Instrumentwindow UI control class
    """
    def __init__(self):
        """
        Init Instrumentwindow UI, and define UI slot function
        """
        super().__init__()

        """Set Ui interface according to QT designer"""
        self.setupUi(self)

        """Set icon"""
        self.setWindowIcon(QIcon('./gear.ico'))

        """Instantiate some class"""
        self.cond = Condition()
        self.flow = Control_Flow()

        """Define slot function"""
        self.pushButton_set.clicked.connect(self.set_parameter)  # Set func push button plot function
        self.pushButton_open.clicked.connect(self.open_instrument)  # Open device push button plot function
        # self.pushButton_close.clicked.connect(self.close_instrument)  # Close device push button plot function
        self.pushButton_reset.clicked.connect(self.reset_instrument)  # RST push button plot function
        self.comboBox_device.currentIndexChanged.connect(self.choose_instrument)

    def choose_instrument(self):
        """
        Choose instrument from comboBox_device, then display
        """
        instrument_name = self.comboBox_device.currentText()  # Get current text from comboBox_device
        self.stackedWidget_device.setCurrentWidget(eval('self.page_' + str(instrument_name)))

    def find_instrument_name(self):
        """
        Return instrument name from tabWidget_instrument.currentWidget

        Returns:
            new_name: Instrument name
        """
        name = self.comboBox_device.currentText()  # Get tab name from tabWidget_instrument

        return name

    def open_instrument(self):
        """
        Open device plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_instrument_name()  # Get instrument string
            self.cond.test_info['Communication'] = self.comboBox_protocol.currentText()  # Get communication string
            self.cond = self.flow.open(self.cond)  # Open instrument function of class
            L.info('Open instrument: ' + self.cond.test_info['Instrument'] +
                   ', Communication: ' + self.cond.test_info['Communication'])

        except:
            L.error(traceback.format_exc())

    # def close_instrument(self):
    #
    #     try:
    #         self.cond.test_info['Instrument'] = self.find_instrument_name()
    #         self.cond = self.flow.close(self.cond)
    #         L.info('Close instrument: ' + self.cond.test_info['Instrument'])
    #
    #     except:
    #         pass

    def reset_instrument(self):
        """
        RST plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_instrument_name()  # Get instrument string
            flow = self.flow.confirm_flow_class(self.cond, self.cond.test_info['Instrument'])  # Confirm class of flow
            flow.RST()  # Reset function of class

        except:
            L.error(traceback.format_exc())

    def set_parameter(self):
        """
        Set func plot function
        """
        try:
            self.cond.test_info['Instrument'] = self.find_instrument_name()  # Get instrument string
            flow = self.flow.confirm_flow_class(self.cond, self.cond.test_info['Instrument'])  # Confirm class of flow
            eval('self.set_' + self.cond.test_info['Instrument'])(flow)  # Go into function of specific class

        except:
            L.error(traceback.format_exc())

    def set_DG1062Z(self, flow):
        """
        Operate DG1062Z instrument, according to instrument window ui

        Args:
            flow: Class of DG1062Z control
        """
        name = self.tabWidget_DG1062Z.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_DG1062Z_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on(
                    self.comboBox_DG1062Z_channel_option_channel.currentText()  # Channel number
                )

            elif re.search('OFF', self.comboBox_DG1062Z_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off(
                    self.comboBox_DG1062Z_channel_option_channel.currentText()  # Channel number
                )

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:
            flow.query_channel_parameter(
                self.comboBox_DG1062Z_query_parameter_channel.currentText()  # Channel number
            )

        """set_mode"""
        if re.search('set_mode', name, re.I) is not None:

            if re.search('Frequency', self.comboBox_DG1062Z_set_mode_mode.currentText(), re.I) is not None:
                # Set frequency mode
                flow.set_channel_mode_frequency(
                    self.comboBox_DG1062Z_set_mode_channel.currentText()  # Channel number
                )

            elif re.search('Sample', self.comboBox_DG1062Z_set_mode_mode.currentText(), re.I) is not None:
                # Set sample rate mode
                flow.set_channel_mode_sample(
                    self.comboBox_DG1062Z_set_mode_channel.currentText()  # Channel number
                )

        """set_type"""
        if re.search('set_type', name, re.I) is not None:
            flow.set_channel_type(
                self.lineEdit_DG1062Z_set_type_type.text(),  # Type name
                self.comboBox_DG1062Z_set_type_channel.currentText()  # Channel number
            )

        """set_impedance"""
        if re.search('set_impedance', name, re.I) is not None:
            flow.set_channel_impedance(
                self.lineEdit_DG1062Z_set_impedance_impedance.text(),  # Impedance value
                self.comboBox_DG1062Z_set_impedance_channel.currentText()  # Channel number
            )

        """set_frequency"""
        if re.search('set_frequency', name, re.I) is not None:
            flow.set_channel_frequency(
                self.lineEdit_DG1062Z_set_frequency_frequency.text(),  # Frequency value
                self.comboBox_DG1062Z_set_frequency_channel.currentText()  # Channel number
            )

        """set_sample"""
        if re.search('set_sample', name, re.I) is not None:
            flow.set_channel_sample(
                self.lineEdit_DG1062Z_set_sample_sample.text(),  # Sample rate value
                self.comboBox_DG1062Z_set_sample_channel.currentText()  # Channel number
            )

        """set_sinc_type"""
        if re.search('set_sinc_type', name, re.I) is not None:
            flow.set_channel_sinc_parameter(
                self.lineEdit_DG1062Z_set_sinc_type_sample.text(),  # Sample rate value
                self.lineEdit_DG1062Z_set_sinc_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_sinc_type_offset.text(),  # Offset value
                self.comboBox_DG1062Z_set_sinc_type_channel.currentText()  # Channel number
            )

        """set_dc_type"""
        if re.search('set_dc_type', name, re.I) is not None:
            flow.set_channel_dc_parameter(
                self.lineEdit_DG1062Z_set_dc_type_offset.text(),  # Offset value
                self.comboBox_DG1062Z_set_dc_type_channel.currentText()  # Channel number
            )

        """set_harm_type"""
        if re.search('set_harm_type', name, re.I) is not None:
            flow.set_channel_harm_parameter(
                self.lineEdit_DG1062Z_set_harm_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_harm_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_harm_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_harm_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_harm_type_channel.currentText()  # Channel number
            )

        """set_noise_type"""
        if re.search('set_noise_type', name, re.I) is not None:
            flow.set_channel_noise_parameter(
                self.lineEdit_DG1062Z_set_noise_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_noise_type_offset.text(),  # Offset value
                self.comboBox_DG1062Z_set_noise_type_channel.currentText()  # Channel number
            )

        """set_pulse_type"""
        if re.search('set_pulse_type', name, re.I) is not None:
            flow.set_channel_pul_parameter(
                self.lineEdit_DG1062Z_set_pulse_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_pulse_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_pulse_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_pulse_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_pulse_type_channel.currentText()  # Channel number
            )

        """set_ramp_type"""
        if re.search('set_ramp_type', name, re.I) is not None:
            flow.set_channel_ramp_parameter(
                self.lineEdit_DG1062Z_set_ramp_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_ramp_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_ramp_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_ramp_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_ramp_type_channel.currentText()  # Channel number
            )

        """set_sin_type"""
        if re.search('set_sin_type', name, re.I) is not None:
            flow.set_channel_sin_parameter(
                self.lineEdit_DG1062Z_set_sin_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_sin_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_sin_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_sin_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_sin_type_channel.currentText()  # Channel number
            )

        """set_squ_type"""
        if re.search('set_squ_type', name, re.I) is not None:
            flow.set_channel_squ_parameter(
                self.lineEdit_DG1062Z_set_squ_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_squ_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_squ_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_squ_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_squ_type_channel.currentText()  # Channel number
            )

        """set_tri_type"""
        if re.search('set_tri_type', name, re.I) is not None:
            flow.set_channel_tri_parameter(
                self.lineEdit_DG1062Z_set_tri_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_tri_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_tri_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_tri_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_tri_type_channel.currentText()  # Channel number
            )

        """set_user_type"""
        if re.search('set_user_type', name, re.I) is not None:
            flow.set_channel_user_parameter(
                self.lineEdit_DG1062Z_set_user_type_frequency.text(),  # Frequency value
                self.lineEdit_DG1062Z_set_user_type_amplitude.text(),  # Amplitude value
                self.lineEdit_DG1062Z_set_user_type_offset.text(),  # Offset value
                self.lineEdit_DG1062Z_set_user_type_phase.text(),  # Phase value
                self.comboBox_DG1062Z_set_user_type_channel.currentText()  # Channel number
            )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_DG1062Z_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_DG1062Z_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_DG1062Z_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_DG1062Z_self_defined_write.text()  # Write command
                )

            if self.lineEdit_DG1062Z_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_DG1062Z_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_E36312A(self, flow):
        """
        Operate E36312A instrument, according to instrument window ui

        Args:
            flow: Class of E36312A control
        """
        name = self.tabWidget_E36312A.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_E36312A_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on(
                    self.comboBox_E36312A_channel_option_channel.currentText()  # Channel number
                )

            elif re.search('OFF', self.comboBox_E36312A_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off(
                    self.comboBox_E36312A_channel_option_channel.currentText()  # Channel number
                )

        """enable_remote"""
        if re.search('enable_remote', name, re.I) is not None:
            flow.enable_remote()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:
            flow.query_channel_all(
                    self.comboBox_E36312A_query_parameter_channel.currentText()  # Channel number
            )

        """set_mode"""
        if re.search('set_mode', name, re.I) is not None:

            if re.search('Independent', self.comboBox_E36312A_set_mode_mode.currentText(), re.I) is not None:
                # Enter independent mode
                flow.enter_independent_mode()

            elif re.search('Series', self.comboBox_E36312A_set_mode_mode.currentText(), re.I) is not None:
                # Enter series mode
                flow.enter_series_mode()

            elif re.search('Parallel', self.comboBox_E36312A_set_mode_mode.currentText(), re.I) is not None:
                # Enter parallel mode
                flow.enter_parallel_mode()

        """set_parameter"""
        if re.search('set_parameter', name, re.I) is not None:
            flow.set_channel_voltage_current(
                self.lineEdit_E36312A_set_parameter_voltage.text(),  # Voltage value
                self.lineEdit_E36312A_set_parameter_current.text(),  # Current value
                self.comboBox_E36312A_set_parameter_channel.currentText()  # Channel number
            )

        """set_voltage"""
        if re.search('set_voltage', name, re.I) is not None:
            flow.set_channel_voltage(
                self.lineEdit_E36312A_set_voltage_voltage.text(),  # Voltage value
                self.comboBox_E36312A_set_voltage_channel.currentText()  # Channel number
            )

        """set_current"""
        if re.search('set_current', name, re.I) is not None:
            flow.set_channel_current(
                self.lineEdit_E36312A_set_current_current.text(),  # Current value
                self.comboBox_E36312A_set_current_channel.currentText()  # Channel number
            )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_E36312A_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_E36312A_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_E36312A_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_E36312A_self_defined_write.text()  # Write command
                )

            if self.lineEdit_E36312A_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_E36312A_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_IT8811(self, flow):
        """
        Operate IT8811 instrument, according to instrument window ui

        Args:
            flow: Class of IT8811 control
        """
        name = self.tabWidget_IT8811.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_IT8811_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on()

            elif re.search('OFF', self.comboBox_IT8811_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off()

        """enable_remote"""
        if re.search('enable_remote', name, re.I) is not None:
            flow.enable_remote()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Voltage and Current', self.comboBox_IT8811_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage and current
                flow.query_all()

            elif re.search('Power', self.comboBox_IT8811_query_parameter_parameter.currentText(), re.I) is not None:
                # Query power
                flow.query_power()

        """set_cv_mode"""
        if re.search('set_cv_mode', name, re.I) is not None:
            flow.enter_CV_mode()

            if self.lineEdit_IT8811_set_cv_mode_voltage.text() != '':
                # Set voltage of CV mode
                flow.set_CV_mode_voltage(
                    self.lineEdit_IT8811_set_cv_mode_voltage.text()  # Voltage value
                )

            if self.lineEdit_IT8811_set_cv_mode_max_current.text() != '':
                # Set max current of CV mode
                flow.set_CV_mode_max_current(
                    self.lineEdit_IT8811_set_cv_mode_max_current.text()  # Current value
                )

            if self.lineEdit_IT8811_set_cv_mode_min_current.text() != '':
                # Set min current of CV mode
                flow.set_CV_mode_min_current(
                    self.lineEdit_IT8811_set_cv_mode_min_current.text()  # Current value
                )

        """set_cc_mode"""
        if re.search('set_cc_mode', name, re.I) is not None:
            flow.enter_CC_mode()

            if self.lineEdit_IT8811_set_cc_mode_current.text() != '':
                # Set current of CC mode
                flow.set_CC_mode_current(
                    self.lineEdit_IT8811_set_cc_mode_current.text()  # Current value
                )

            if self.lineEdit_IT8811_set_cc_mode_max_voltage.text() != '':
                # Set max voltage of CC mode
                flow.set_CC_mode_max_voltage(
                    self.lineEdit_IT8811_set_cc_mode_max_voltage.text()  # Voltage value
                )

            if self.lineEdit_IT8811_set_cc_mode_min_voltage.text() != '':
                # Set min voltage of CC mode
                flow.set_CC_mode_min_voltage(
                    self.lineEdit_IT8811_set_cc_mode_min_voltage.text()  # Voltage value
                )

        """set_cr_mode"""
        if re.search('set_cr_mode', name, re.I) is not None:
            flow.enter_CR_mode()

            if self.lineEdit_IT8811_set_cr_mode_resistance.text() != '':
                # Set resistance of CR mode
                flow.set_CR_mode_resistance(
                    self.lineEdit_IT8811_set_cr_mode_resistance.text()  # Resistance value
                )

            if self.lineEdit_IT8811_set_cr_mode_max_voltage.text() != '':
                # Set max voltage of CR mode
                flow.set_CR_mode_max_voltage(
                    self.lineEdit_IT8811_set_cr_mode_max_voltage.text()  # Voltage value
                )

            if self.lineEdit_IT8811_set_cr_mode_min_voltage.text() != '':
                # Set min voltage of CR mode
                flow.set_CR_mode_min_voltage(
                    self.lineEdit_IT8811_set_cr_mode_min_voltage.text()  # Voltage value
                )

        """set_cw_mode"""
        if re.search('set_cw_mode', name, re.I) is not None:
            flow.enter_CW_mode()

            if self.lineEdit_IT8811_set_cw_mode_power.text() != '':
                # Set power of CW mode
                flow.set_CW_mode_power(
                    self.lineEdit_IT8811_set_cw_mode_power.text()  # Power value
                )

            if self.lineEdit_IT8811_set_cw_mode_max_voltage.text() != '':
                # Set max voltage of CW mode
                flow.set_CW_mode_max_voltage(
                    self.lineEdit_IT8811_set_cw_mode_max_voltage.text()  # Voltage value
                )

            if self.lineEdit_IT8811_set_cw_mode_min_voltage.text() != '':
                # Set min voltage of CW mode
                flow.set_CW_mode_min_voltage(
                    self.lineEdit_IT8811_set_cw_mode_min_voltage.text()  # Voltage value
                )

            """self_defined"""
            if re.search('self_defined', name, re.I) is not None:

                if self.lineEdit_IT8811_self_defined_query.text() != '':
                    # Query
                    result = flow.control.query(
                        self.lineEdit_IT8811_self_defined_query.text()  # Query command
                    )
                    L.info(str(result))

                if self.lineEdit_IT8811_self_defined_write.text() != '':
                    # Write
                    flow.control.write(
                        self.lineEdit_IT8811_self_defined_write.text()  # Write command
                    )

                if self.lineEdit_IT8811_self_defined_read.text() != '':
                    # Read
                    result = flow.control.read(
                        self.lineEdit_IT8811_self_defined_read.text()  # Read command
                    )
                    L.info(str(result))

    def set_2400(self, flow):
        """
        Operate 2400 instrument, according to instrument window ui

        Args:
            flow: Class of 2400 control
        """
        name = self.tabWidget_2400.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_2400_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on()

            elif re.search('OFF', self.comboBox_2400_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off()

        """set_measurement"""
        if re.search('set_measurement', name, re.I) is not None:

            if re.search(
                    'Enable all measurement', self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Enable all measurement
                flow.enable_all_measurement()

            elif re.search(
                    'Disable all measurement', self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Disable all measurement
                flow.disable_all_measurement()

            elif re.search(
                    'Enable concurrent measurement', self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Enable concurrent measurement
                flow.enable_concurrent_measurement()

            elif re.search(
                    'Disable concurrent measurement', self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Disable concurrent measurement
                flow.disable_concurrent_measurement()

            elif re.search(
                    'Enable auto range for voltage measurement',
                    self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Enable auto range for voltage measurement
                flow.enable_auto_range_for_voltage_measurement()

            elif re.search(
                    'Disable auto range for voltage measurement',
                    self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Disable auto range for voltage measurement
                flow.disable_auto_range_for_voltage_measurement()

            elif re.search(
                    'Enable auto range for current measurement',
                    self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Enable auto range for current measurement
                flow.enable_auto_range_for_current_measurement()

            elif re.search(
                    'Disable auto range for current measurement',
                    self.comboBox_2400_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Disable auto range for current measurement
                flow.disable_auto_range_for_current_measurement()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Voltage and Current', self.comboBox_2400_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage and current
                flow.query_all()

            elif re.search(
                    'Voltage', self.comboBox_2400_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage
                flow.query_voltage()

            elif re.search(
                    'Current', self.comboBox_2400_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query current
                flow.query_current()

        """set_cv_mode"""
        if re.search('set_cv_mode', name, re.I) is not None:
            flow.enter_CV_mode()

            if self.lineEdit_2400_set_cv_mode_voltage.text() != '':
                # Set voltage of CV mode
                flow.set_CV_mode_voltage(
                    self.lineEdit_2400_set_cv_mode_voltage.text()  # Voltage value
                )

            if self.lineEdit_2400_set_cv_mode_max_current.text() != '':
                # Set max current of CV mode
                flow.set_CV_mode_max_current(
                    self.lineEdit_2400_set_cv_mode_max_current.text()  # Current value
                )

        """set_cc_mode"""
        if re.search('set_cc_mode', name, re.I) is not None:
            flow.enter_CC_mode()

            if self.lineEdit_2400_set_cc_mode_current.text() != '':
                # Set current of CC mode
                flow.set_CC_mode_current(
                    self.lineEdit_2400_set_cc_mode_current.text()  # Current value
                )

            if self.lineEdit_2400_set_cc_mode_max_voltage.text() != '':
                # Set max voltage of CC mode
                flow.set_CC_mode_max_voltage(
                    self.lineEdit_2400_set_cc_mode_max_voltage.text()  # Voltage value
                )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_2400_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_2400_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_2400_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_2400_self_defined_write.text()  # Write command
                )

            if self.lineEdit_2400_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_2400_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DHT260(self, flow):
        """
         Operate DHT260 instrument, according to instrument window ui

         Args:
             flow: Class of DHT260 control
         """
        name = self.tabWidget_DHT260.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_DHT260_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on()

            elif re.search('OFF', self.comboBox_DHT260_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off()

        """enable_option"""
        if re.search('enable_option', name, re.I) is not None:

            if re.search(
                    'Temperature', self.comboBox_DHT260_enable_option_switch.currentText(), re.I
            ) is not None:
                # Enable temperature
                flow.enable_temperature()

            elif re.search(
                    'Humidity', self.comboBox_DHT260_enable_option_switch.currentText(), re.I
            ) is not None:
                # Enable humidity
                flow.enable_humidity()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Temperature', self.comboBox_DHT260_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query temperature
                flow.query_temperature()

            elif re.search(
                    'Humidity', self.comboBox_DHT260_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query humidity
                flow.query_humidity()

        """set_temperature"""
        if re.search('set_temperature', name, re.I) is not None:
            flow.set_temperature(
                self.lineEdit_DHT260_set_temperature_temperature.text()  # Temperature value
            )

        """set_humidity"""
        if re.search('set_humidity', name, re.I) is not None:
            flow.set_humidity(
                self.lineEdit_DHT260_set_humidity_humidity.text()  # Humidity value
            )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_DHT260_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_DHT260_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_DHT260_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_DHT260_self_defined_write.text()  # Write command
                )

            if self.lineEdit_DHT260_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_DHT260_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DL11B(self, flow):
        """
         Operate DHT260 instrument, according to instrument window ui

         Args:
             flow: Class of DHT260 control
         """
        name = self.tabWidget_DL11B.currentWidget().objectName()  # Return specific function of instrument

        """change_resolution"""
        if re.search('change_resolution', name, re.I) is not None:
            flow.change_resolution(
                float(self.comboBox_DL11B_change_resolution_resolution.currentText())
            )

        """set_compensation"""
        if re.search('set_compensation', name, re.I) is not None:
            flow.write_temperature_compensation(
                self.lineEdit_DL11B_set_compensation_compensation.text(),
                int(self.comboBox_DL11B_set_compensation_channel.currentText())
            )

        """query_compensation"""
        if re.search('query_compensation', name, re.I) is not None:
            flow.query_temperature_compensation(
                int(self.comboBox_DL11B_query_compensation_channel.currentText())
            )

        """query_temperature"""
        if re.search('query_temperature', name, re.I) is not None:
            flow.query_temperature(
                int(self.comboBox_DL11B_query_temperature_channel.currentText())
            )

    def set_2450(self, flow):
        """
        Operate 2400 instrument, according to instrument window ui

        Args:
            flow: Class of 2400 control
        """
        name = self.tabWidget_2450.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_2450_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on()

            elif re.search('OFF', self.comboBox_2450_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off()

        """set_measurement"""
        if re.search('set_measurement', name, re.I) is not None:

            if re.search(
                    'Enable auto range for voltage measurement',
                    self.comboBox_2450_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Enable auto range for voltage measurement
                flow.enable_auto_range_for_voltage_measurement()

            elif re.search(
                    'Disable auto range for voltage measurement',
                    self.comboBox_2450_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Disable auto range for voltage measurement
                flow.disable_auto_range_for_voltage_measurement()

            elif re.search(
                    'Enable auto range for current measurement',
                    self.comboBox_2450_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Enable auto range for current measurement
                flow.enable_auto_range_for_current_measurement()

            elif re.search(
                    'Disable auto range for current measurement',
                    self.comboBox_2450_set_measurement_switch.currentText(), re.I
            ) is not None:
                # Disable auto range for current measurement
                flow.disable_auto_range_for_current_measurement()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Voltage and Current', self.comboBox_2450_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage and current
                flow.query_all()

            elif re.search(
                    'Voltage', self.comboBox_2450_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage
                flow.query_voltage()

            elif re.search(
                    'Current', self.comboBox_2450_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query current
                flow.query_current()

        """set_cv_mode"""
        if re.search('set_cv_mode', name, re.I) is not None:
            flow.enter_CV_mode()

            if self.lineEdit_2450_set_cv_mode_voltage.text() != '':
                # Set voltage of CV mode
                flow.set_CV_mode_voltage(
                    self.lineEdit_2450_set_cv_mode_voltage.text()  # Voltage value
                )

            if self.lineEdit_2450_set_cv_mode_max_current.text() != '':
                # Set max current of CV mode
                flow.set_CV_mode_max_current(
                    self.lineEdit_2450_set_cv_mode_max_current.text()  # Current value
                )

        """set_cc_mode"""
        if re.search('set_cc_mode', name, re.I) is not None:
            flow.enter_CC_mode()

            if self.lineEdit_2450_set_cc_mode_current.text() != '':
                # Set current of CC mode
                flow.set_CC_mode_current(
                    self.lineEdit_2450_set_cc_mode_current.text()  # Current value
                )

            if self.lineEdit_2450_set_cc_mode_max_voltage.text() != '':
                # Set max voltage of CC mode
                flow.set_CC_mode_max_voltage(
                    self.lineEdit_2450_set_cc_mode_max_voltage.text()  # Voltage value
                )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_2450_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_2450_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_2450_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_2450_self_defined_write.text()  # Write command
                )

            if self.lineEdit_2450_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_2450_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DMM7510(self, flow):
        """
        Operate DMM7510 instrument, according to instrument window ui

        Args:
            flow: Class of DMM7510 control
        """
        name = self.tabWidget_DMM7510.currentWidget().objectName()  # Return specific function of instrument

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Voltage and Current', self.comboBox_DMM7510_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage and current
                flow.query_voltage_current()

            else:
                option = self.comboBox_DMM7510_query_parameter_parameter.currentText()
                flow.query_one_measurement(option)

        """set_measurement_autorange"""
        if re.search('set_measurement_autorange', name, re.I) is not None:
            option = self.comboBox_DMM7510_set_measurement_autorange_option.currentText()
            flag = self.comboBox_DMM7510_set_measurement_autorange_flag.currentText()
            flow.set_one_measurement_autorange(option, flag)

        """set_measurement_speed"""
        if re.search('set_measurement_speed', name, re.I) is not None:
            option = self.comboBox_DMM7510_set_measurement_speed_option.currentText()
            speed = self.lineEdit_DMM7510_set_measurement_speed_speed.text()
            flow.set_one_measurement_speed(option, speed)

        """set_average_count"""
        if re.search('set_average_count', name, re.I) is not None:
            option = self.comboBox_DMM7510_set_average_count_option.currentText()
            num = self.lineEdit_DMM7510_set_average_count_count.text()
            flow.set_one_average_count(option, num)

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_DMM7510_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_DMM7510_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_DMM7510_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_DMM7510_self_defined_write.text()  # Write command
                )

            if self.lineEdit_DMM7510_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_DMM7510_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_B2912A(self, flow):
        """
        Operate B2912A instrument, according to instrument window ui

        Args:
            flow: Class of B2912A control
        """
        name = self.tabWidget_B2912A.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_B2912A_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on(
                    self.comboBox_B2912A_channel_option_channel.currentText()  # Channel number
                )

            elif re.search('OFF', self.comboBox_B2912A_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off(
                    self.comboBox_B2912A_channel_option_channel.currentText()  # Channel number
                )

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Voltage and Current', self.comboBox_B2912A_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage and current
                flow.query_all(
                    self.comboBox_B2912A_query_parameter_channel.currentText()
                )

            elif re.search(
                    'Voltage', self.comboBox_B2912A_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage
                flow.query_voltage(
                    self.comboBox_B2912A_query_parameter_channel.currentText()
                )

            elif re.search(
                    'Current', self.comboBox_B2912A_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query current
                flow.query_current(
                    self.comboBox_B2912A_query_parameter_channel.currentText()
                )

        """set_cv_mode"""
        if re.search('set_cv_mode', name, re.I) is not None:
            flow.enter_CV_mode(
                self.comboBox_B2912A_set_cv_mode_channel.currentText()
            )

            if self.lineEdit_B2912A_set_cv_mode_voltage.text() != '':
                # Set voltage of CV mode
                flow.set_CV_mode_voltage(
                    self.lineEdit_B2912A_set_cv_mode_voltage.text(),  # Voltage value
                    self.comboBox_B2912A_set_cv_mode_channel.currentText()
                )

            if self.lineEdit_B2912A_set_cv_mode_max_current.text() != '':
                # Set max current of CV mode
                flow.set_CV_mode_max_current(
                    self.lineEdit_B2912A_set_cv_mode_max_current.text(),  # Current value
                    self.comboBox_B2912A_set_cv_mode_channel.currentText()
                )

        """set_cc_mode"""
        if re.search('set_cc_mode', name, re.I) is not None:
            flow.enter_CC_mode(
                self.comboBox_B2912A_set_cc_mode_channel.currentText()
            )

            if self.lineEdit_B2912A_set_cc_mode_current.text() != '':
                # Set current of CC mode
                flow.set_CC_mode_current(
                    self.lineEdit_B2912A_set_cc_mode_current.text(),  # Current value
                    self.comboBox_B2912A_set_cc_mode_channel.currentText()
                )

            if self.lineEdit_B2912A_set_cc_mode_max_voltage.text() != '':
                # Set max voltage of CC mode
                flow.set_CC_mode_max_voltage(
                    self.lineEdit_2450_set_cc_mode_max_voltage.text(),  # Voltage value
                    self.comboBox_B2912A_set_cc_mode_channel.currentText()
                )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_E36312A_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_E36312A_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_E36312A_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_E36312A_self_defined_write.text()  # Write command
                )

            if self.lineEdit_E36312A_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_E36312A_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DP832(self, flow):
        """
        Operate DP832 instrument, according to instrument window ui

        Args:
            flow: Class of DP832 control
        """
        name = self.tabWidget_DP832.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_DP832_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on(
                    self.comboBox_DP832_channel_option_channel.currentText()  # Channel number
                )

            elif re.search('OFF', self.comboBox_DP832_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off(
                    self.comboBox_DP832_channel_option_channel.currentText()  # Channel number
                )

        """enable_remote"""
        if re.search('enable_remote', name, re.I) is not None:
            flow.enable_remote()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:
            flow.query_channel_all(
                    self.comboBox_DP832_query_parameter_channel.currentText()  # Channel number
            )

        """set_parameter"""
        if re.search('set_parameter', name, re.I) is not None:
            flow.set_channel_voltage_current(
                self.lineEdit_DP832_set_parameter_voltage.text(),  # Voltage value
                self.lineEdit_DP832_set_parameter_current.text(),  # Current value
                self.comboBox_DP832_set_parameter_channel.currentText()  # Channel number
            )

        """set_voltage"""
        if re.search('set_voltage', name, re.I) is not None:
            flow.set_channel_voltage(
                self.lineEdit_DP832_set_voltage_voltage.text(),  # Voltage value
                self.comboBox_DP832_set_voltage_channel.currentText()  # Channel number
            )

        """set_current"""
        if re.search('set_current', name, re.I) is not None:
            flow.set_channel_current(
                self.lineEdit_DP832_set_current_current.text(),  # Current value
                self.comboBox_DP832_set_current_channel.currentText()  # Channel number
            )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_DP832_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_DP832_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_DP832_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_DP832_self_defined_write.text()  # Write command
                )

            if self.lineEdit_DP832_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_DP832_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DP932(self, flow):
        """
        Operate DP932 instrument, according to instrument window ui

        Args:
            flow: Class of DP832 control
        """
        name = self.tabWidget_DP932.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_DP932_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on(
                    self.comboBox_DP932_channel_option_channel.currentText()  # Channel number
                )

            elif re.search('OFF', self.comboBox_DP932_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off(
                    self.comboBox_DP932_channel_option_channel.currentText()  # Channel number
                )

        """enable_remote"""
        if re.search('enable_remote', name, re.I) is not None:
            flow.enable_remote()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:
            flow.query_channel_all(
                    self.comboBox_DP932_query_parameter_channel.currentText()  # Channel number
            )

        """set_parameter"""
        if re.search('set_parameter', name, re.I) is not None:
            flow.set_channel_voltage_current(
                self.lineEdit_DP932_set_parameter_voltage.text(),  # Voltage value
                self.lineEdit_DP932_set_parameter_current.text(),  # Current value
                self.comboBox_DP932_set_parameter_channel.currentText()  # Channel number
            )

        """set_voltage"""
        if re.search('set_voltage', name, re.I) is not None:
            flow.set_channel_voltage(
                self.lineEdit_DP932_set_voltage_voltage.text(),  # Voltage value
                self.comboBox_DP932_set_voltage_channel.currentText()  # Channel number
            )

        """set_current"""
        if re.search('set_current', name, re.I) is not None:
            flow.set_channel_current(
                self.lineEdit_DP932_set_current_current.text(),  # Current value
                self.comboBox_DP932_set_current_channel.currentText()  # Channel number
            )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_DP932_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_DP932_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_DP932_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_DP932_self_defined_write.text()  # Write command
                )

            if self.lineEdit_DP932_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_DP932_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DP932U(self, flow):
        """
        Operate DP932U instrument, according to instrument window ui

        Args:
            flow: Class of DP832 control
        """
        name = self.tabWidget_DP932U.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_DP932U_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on(
                    self.comboBox_DP932U_channel_option_channel.currentText()  # Channel number
                )

            elif re.search('OFF', self.comboBox_DP932U_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off(
                    self.comboBox_DP932U_channel_option_channel.currentText()  # Channel number
                )

        """enable_remote"""
        if re.search('enable_remote', name, re.I) is not None:
            flow.enable_remote()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:
            flow.query_channel_all(
                    self.comboBox_DP932U_query_parameter_channel.currentText()  # Channel number
            )

        """set_parameter"""
        if re.search('set_parameter', name, re.I) is not None:
            flow.set_channel_voltage_current(
                self.lineEdit_DP932U_set_parameter_voltage.text(),  # Voltage value
                self.lineEdit_DP932U_set_parameter_current.text(),  # Current value
                self.comboBox_DP932U_set_parameter_channel.currentText()  # Channel number
            )

        """set_voltage"""
        if re.search('set_voltage', name, re.I) is not None:
            flow.set_channel_voltage(
                self.lineEdit_DP932U_set_voltage_voltage.text(),  # Voltage value
                self.comboBox_DP932U_set_voltage_channel.currentText()  # Channel number
            )

        """set_current"""
        if re.search('set_current', name, re.I) is not None:
            flow.set_channel_current(
                self.lineEdit_DP932U_set_current_current.text(),  # Current value
                self.comboBox_DP932U_set_current_channel.currentText()  # Channel number
            )

        """self_defined"""
        if re.search('self_defined', name, re.I) is not None:

            if self.lineEdit_DP932U_self_defined_query.text() != '':
                # Query
                result = flow.control.query(
                    self.lineEdit_DP932U_self_defined_query.text()  # Query command
                )
                L.info(str(result))

            if self.lineEdit_DP932U_self_defined_write.text() != '':
                # Write
                flow.control.write(
                    self.lineEdit_DP932U_self_defined_write.text()  # Write command
                )

            if self.lineEdit_DP932U_self_defined_read.text() != '':
                # Read
                result = flow.control.read(
                    self.lineEdit_DP932U_self_defined_read.text()  # Read command
                )
                L.info(str(result))

    def set_DL3021(self, flow):
        """
        Operate DL3021 instrument, according to instrument window ui

        Args:
            flow: Class of DL3021 control
        """
        name = self.tabWidget_DL3021.currentWidget().objectName()  # Return specific function of instrument

        """channel_option"""
        if re.search('channel_option', name, re.I) is not None:

            if re.search('ON', self.comboBox_DL3021_channel_option_switch.currentText(), re.I) is not None:
                # Channel on
                flow.channel_on()

            elif re.search('OFF', self.comboBox_DL3021_channel_option_switch.currentText(), re.I) is not None:
                # Channel off
                flow.channel_off()

        """enable_remote"""
        if re.search('enable_remote', name, re.I) is not None:
            flow.enable_remote()

        """query_parameter"""
        if re.search('query_parameter', name, re.I) is not None:

            if re.search(
                    'Voltage and Current', self.comboBox_DL3021_query_parameter_parameter.currentText(), re.I
            ) is not None:
                # Query voltage and current
                flow.query_all()

            elif re.search('Power', self.comboBox_DL3021_query_parameter_parameter.currentText(), re.I) is not None:
                # Query power
                flow.query_power()

        """set_cv_mode"""
        if re.search('set_cv_mode', name, re.I) is not None:
            flow.enter_CV_mode()

            if self.lineEdit_DL3021_set_cv_mode_voltage.text() != '':
                # Set voltage of CV mode
                flow.set_CV_mode_voltage(
                    self.lineEdit_DL3021_set_cv_mode_voltage.text()  # Voltage value
                )

            if self.lineEdit_DL3021_set_cv_mode_max_current.text() != '':
                # Set max current of CV mode
                flow.set_CV_mode_max_current(
                    self.lineEdit_DL3021_set_cv_mode_max_current.text()  # Current value
                )

            if self.lineEdit_DL3021_set_cv_mode_min_current.text() != '':
                # Set min current of CV mode
                flow.set_CV_mode_min_current(
                    self.lineEdit_DL3021_set_cv_mode_min_current.text()  # Current value
                )

        """set_cc_mode"""
        if re.search('set_cc_mode', name, re.I) is not None:
            flow.enter_CC_mode()

            if self.lineEdit_DL3021_set_cc_mode_current.text() != '':
                # Set current of CC mode
                flow.set_CC_mode_current(
                    self.lineEdit_DL3021_set_cc_mode_current.text()  # Current value
                )

            if self.lineEdit_DL3021_set_cc_mode_max_voltage.text() != '':
                # Set max voltage of CC mode
                flow.set_CC_mode_max_voltage(
                    self.lineEdit_DL3021_set_cc_mode_max_voltage.text()  # Voltage value
                )

            if self.lineEdit_DL3021_set_cc_mode_min_voltage.text() != '':
                # Set min voltage of CC mode
                flow.set_CC_mode_min_voltage(
                    self.lineEdit_DL3021_set_cc_mode_min_voltage.text()  # Voltage value
                )

        """set_cr_mode"""
        if re.search('set_cr_mode', name, re.I) is not None:
            flow.enter_CR_mode()

            if self.lineEdit_DL3021_set_cr_mode_resistance.text() != '':
                # Set resistance of CR mode
                flow.set_CR_mode_resistance(
                    self.lineEdit_DL3021_set_cr_mode_resistance.text()  # Resistance value
                )

            if self.lineEdit_DL3021_set_cr_mode_max_voltage.text() != '':
                # Set max voltage of CR mode
                flow.set_CR_mode_max_voltage(
                    self.lineEdit_DL3021_set_cr_mode_max_voltage.text()  # Voltage value
                )

            if self.lineEdit_DL3021_set_cr_mode_min_voltage.text() != '':
                # Set min voltage of CR mode
                flow.set_CR_mode_min_voltage(
                    self.lineEdit_DL3021_set_cr_mode_min_voltage.text()  # Voltage value
                )

        """set_cw_mode"""
        if re.search('set_cw_mode', name, re.I) is not None:
            flow.enter_CW_mode()

            if self.lineEdit_DL3021_set_cw_mode_power.text() != '':
                # Set power of CW mode
                flow.set_CW_mode_power(
                    self.lineEdit_DL3021_set_cw_mode_power.text()  # Power value
                )

            if self.lineEdit_DL3021_set_cw_mode_max_voltage.text() != '':
                # Set max voltage of CW mode
                flow.set_CW_mode_max_voltage(
                    self.lineEdit_DL3021_set_cw_mode_max_voltage.text()  # Voltage value
                )

            if self.lineEdit_DL3021_set_cw_mode_min_voltage.text() != '':
                # Set min voltage of CW mode
                flow.set_CW_mode_min_voltage(
                    self.lineEdit_DL3021_set_cw_mode_min_voltage.text()  # Voltage value
                )

            """self_defined"""
            if re.search('self_defined', name, re.I) is not None:

                if self.lineEdit_DL3021_self_defined_query.text() != '':
                    # Query
                    result = flow.control.query(
                        self.lineEdit_DL3021_self_defined_query.text()  # Query command
                    )
                    L.info(str(result))

                if self.lineEdit_DL3021_self_defined_write.text() != '':
                    # Write
                    flow.control.write(
                        self.lineEdit_DL3021_self_defined_write.text()  # Write command
                    )

                if self.lineEdit_DL3021_self_defined_read.text() != '':
                    # Read
                    result = flow.control.read(
                        self.lineEdit_DL3021_self_defined_read.text()  # Read command
                    )
                    L.info(str(result))


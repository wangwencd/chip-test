# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/21 11:21
File: mainwindow_control.py
"""
import os
import sys
import logging
import threading
import traceback
import configparser

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QCloseEvent

from ui import *
from .ui_mainwindow import Ui_ui_MainWindow
from .instrumentwindow_control import Instrumentwindow_Control
from .mcuwindow_control import MCUwindow_Control
from parse.multiprocess.msg_thread import Msg_Thread
from test.condition.condition import Condition
from parse.process import Parse_Process_Dict
from test.process import Test_Process_Dict
from output.process import Output_Process_Dict
from output.result.result_output import Result_Output
from parse.file.file_operation import File_Operation

L = logging.getLogger('Main')

class Mainwindow_Control(QMainWindow, Ui_ui_MainWindow):
    """
    Mainwindow UI control class
    """

    def __init__(self):
        """
        Init Mainwindow UI, and define UI slot function
        """
        super().__init__()

        """Set Ui interface according to QT designer"""
        self.setupUi(self)

        """Set icon"""
        self.setWindowIcon(QIcon('./gear.ico'))

        """Instantiate some class"""
        self.instrument_window = Instrumentwindow_Control()
        self.mcu_window = MCUwindow_Control()
        self.path = os.getcwd()
        self.cond = Condition()
        self.msg = Msg_Thread()
        self.msg.start()
        self.conf = configparser.ConfigParser()

        """Set parameter"""
        self.slot_box_select_function()
        self.read_old_config()

        """Define slot function"""
        self.radiobutton_slot_function_groups()  # radiobutton slot function groups
        self.toolBox_function.currentChanged.connect(self.slot_box_select_function)  # tool box slot function
        self.pushButton_start_start.clicked.connect(self.on)  # pushbutton start slot function
        self.pushButton_start_stop.clicked.connect(self.off)  # pushbutton stop slot function
        self.pushButton_config_folder.clicked.connect(self.slot_button_config_path)  # pushbutton config slot function
        self.pushButton_output_folder.clicked.connect(self.slot_button_output_path)  # pushbutton output slot function
        self.lineEdit_config_configpath.textChanged.connect(
            lambda: self.slot_line_config_path(self.lineEdit_config_configpath.text())
        )  # lineedit config slot function
        self.lineEdit_output_outputpath.textChanged.connect(
            lambda: self.slot_line_output_path(self.lineEdit_output_outputpath.text())
        )  # lineedit output slot function
        self.action_instrument.triggered.connect(self.show_intrumentwindow)  # instrument action slot function
        self.action_mcu.triggered.connect(self.show_mcuwindow)  # MCU action slot function

        self.msg.signal1.connect(self.get_message)
        """Show UI interface"""
        self.show()

    def radiobutton_slot_function_groups(self):
        """
        RadioButton slot function groups.
        """
        self.radioButton_battery_lab.clicked.connect(
            lambda: self.select_function('0')
        )  # radiobutton battery lab slot function
        self.radioButton_custom_test.clicked.connect(
            lambda: self.select_function('1')
        )  # radiobutton custom test slot function
        self.radioButton_lithium_test_accuracy.clicked.connect(
            lambda: self.select_function('2-0')
        )  # radiobutton lithium test accuracy slot function
        self.radioButton_lithium_test_dnl.clicked.connect(
            lambda: self.select_function('2-1')
        )  # radiobutton lithium test dnl slot function
        self.radioButton_lithium_test_deviation.clicked.connect(
            lambda: self.select_function('2-2')
        )  # radiobutton lithium test deviation slot function
        self.radioButton_lithium_test_bgr.clicked.connect(
            lambda: self.select_function('2-3')
        )  # radiobutton lithium test bgr slot function
        self.radioButton_venus_test_trim.clicked.connect(
            lambda: self.select_function('3-0')
        )  # radiobutton venus test bgr slot function
        self.radioButton_jupiter_test_ramp.clicked.connect(
            lambda: self.select_function('4-0')
        )  # radiobutton jupiter test ramp slot function
        self.radioButton_jupiter_test_ramp_multi.clicked.connect(
            lambda: self.select_function('4-1')
        )  # radiobutton jupiter test ramp multi slot function
        self.radioButton_jupiter_test_noise.clicked.connect(
            lambda: self.select_function('4-2')
        )  # radiobutton jupiter test noise slot function
        self.radioButton_natrium_test_ramp.clicked.connect(
            lambda: self.select_function('5-0')
        )  # radiobutton natrium test ramp slot function
        self.radioButton_natrium_test_noise.clicked.connect(
            lambda: self.select_function('5-1')
        )  # radiobutton natrium test noise slot function
        self.radioButton_natrium_test_temperature.clicked.connect(
            lambda: self.select_function('5-2')
        )  # radiobutton natrium test noise slot function

    def select_function(self, code):
        """
        Select function name.

        Args:
            code: Function code.
        """
        for key, value in function_name_dict.items():

            for func_value in function_dict.values():

                if code == value and self.toolBox_function.currentIndex() == func_value:
                    self.cond.func_name = key

    def slot_box_select_function(self):
        """
        ToolBox slot function.
        """
        for key, value in function_dict.items():

            if self.toolBox_function.currentIndex() == value:
                self.cond.func = key

    def slot_button_config_path(self):
        """
        PushButton config path slot function
        """
        try:
            path = QFileDialog.getExistingDirectory(None, 'Select folder', self.lineEdit_config_configpath.text())

        except:
            path = QFileDialog.getExistingDirectory(None, 'Select folder', self.path)

        self.slot_line_config_path(path)

    def slot_button_output_path(self):
        """
        PushButton output path slot function
        """
        try:
            path = QFileDialog.getExistingDirectory(None, 'Select folder', self.lineEdit_output_outputpath.text())

        except:
            path = QFileDialog.getExistingDirectory(None, 'Select folder', self.path)

        self.slot_line_output_path(path)

    def slot_line_config_path(self, path):
        """
        LineEdit config path slot function
        """
        if path == '':
            pass

        else:
            self.lineEdit_config_configpath.setText(path)  # Show confit path on config path lineEdit
            self.cond.config_path = path  # Set config path to condition.config_path

    def slot_line_output_path(self, path):
        """
        LineEdit output path slot function
        """
        if path == '':
            pass

        else:
            self.lineEdit_output_outputpath.setText(path)  # Show output path on output path lineEdit
            self.cond.saving_path = path  # Set output path to condition.saving_path

    def on(self):
        """
        Create a thread and run program.
        """
        t1 = threading.Thread(target=self.start)
        t1.daemon = True
        t1.start()

    def start(self):
        """
        Specific items in program.
        """
        self.pushButton_start_start.setEnabled(False)

        try:
            """Parsing step"""
            for key, value in Parse_Process_Dict.items():  # Choose parsing

                if key == self.cond.func:
                    self.cond = value.parse(self.cond)

            """Testing step"""
            for key, value in Test_Process_Dict.items():  # Choose testing

                if key == self.cond.func:
                    test = value()
                    self.cond = test.test(self.cond)

            """Output step"""
            for key, value in Output_Process_Dict.items():  # Choose output

                if key == self.cond.func:
                    self.cond = value.output(self.cond)

        except:
            L.error(traceback.format_exc())
        self.pushButton_start_start.setEnabled(True)
        self.pushButton_start_start.setAutoExclusive(False)
        self.pushButton_start_start.setChecked(False)
        self.pushButton_start_start.setAutoExclusive(True)

    def off(self):
        """
        Stop program.
        """


    def get_message(self, message):
        """
        Get message from queue, show message.
        """
        self.textBrowser_log.append(message)

        if self.textBrowser_log.document().blockCount() > 1000000:
            self.textBrowser_log.clear()

    def show_intrumentwindow(self):
        """
        Show instrument window
        """
        self.instrument_window.show()

    def show_mcuwindow(self):
        """
        Show mcu window
        """
        self.mcu_window.show()

    def generate_old_config(self):
        self.conf['Config'] = {}
        try:
            self.conf['Config'].update({'Function': self.cond.func})
        except:
            pass

        try:
            self.conf['Config'].update({'Function_name': self.cond.func_name})
        except:
            pass

        self.conf['Config'].update({'Config_path': self.lineEdit_config_configpath.text()})
        self.conf['Config'].update({'Output_path': self.lineEdit_output_outputpath.text()})

        Result_Output.to_ini(self.conf, path=self.path, name='old config')

    def read_old_config(self):

        try:
            file = File_Operation.find_file(self.path, 'ini')
            old_config = File_Operation.get_dataframe_from_first(file).iloc[0].to_dict()

            if 'function' in old_config.keys():

                for key, value in function_dict.items():

                    if old_config['function'] == key:
                        self.toolBox_function.setCurrentIndex(value)
                        self.cond.func = key
                        break

            if 'function_name' in old_config.keys():

                for name_key, name_value in function_name_dict.items():

                    if old_config['function_name'] == name_key:
                        key = name_key
                        value = name_value
                        break

                for radio_key, radio_value in radiobutton_name_dict.items():

                    if radio_value == value:
                        eval('self.' + radio_key + '.setChecked(True)')
                        self.cond.func_name = key
                        break

            if 'config_path' in old_config.keys():
                self.lineEdit_config_configpath.setText(old_config['config_path'])
                self.cond.config_path = old_config['config_path']

            if 'output_path' in old_config.keys():
                self.lineEdit_output_outputpath.setText(old_config['output_path'])
                self.cond.saving_path = old_config['output_path']

        except:
            pass

    def closeEvent(self, event):
        """
        Close event function, mainwindow will show a window for asking exit if clicking pushbutton,
        then main program will run output process if answer is yes.

        Args:
            event: Event of QCloseEvent
        """
        reply = QMessageBox.question(self,
                                     'Exit',
                                     'Do you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)  # Generate an asking window

        if reply == QMessageBox.Yes:  # If answer is yes
            self.generate_old_config()
            try:
                """Output step"""
                for key, value in Output_Process_Dict.items():  # Choose output

                    if key == self.cond.func:
                        self.cond = value.output(self.cond)

            except:
                pass
            event.accept()
            os._exit(0)

        elif reply == QMessageBox.No:  # If answer is no
            event.ignore()

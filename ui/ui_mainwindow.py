# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui_MainWindow(object):
    def setupUi(self, ui_MainWindow):
        ui_MainWindow.setObjectName("ui_MainWindow")
        ui_MainWindow.resize(967, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_MainWindow.sizePolicy().hasHeightForWidth())
        ui_MainWindow.setSizePolicy(sizePolicy)
        ui_MainWindow.setStyleSheet("\n"
"QMenuBar{\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QGroupBox{\n"
"    font: 75 italic 12pt \"Arial\";\n"
"}\n"
"\n"
"QTabWidget{\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QWidget{\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(216, 227, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:inset\n"
"}\n"
"\n"
"\n"
"")
        self.widget_main = QtWidgets.QWidget(ui_MainWindow)
        self.widget_main.setObjectName("widget_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox_function = QtWidgets.QToolBox(self.groupBox)
        self.toolBox_function.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_function.sizePolicy().hasHeightForWidth())
        self.toolBox_function.setSizePolicy(sizePolicy)
        self.toolBox_function.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBox_function.setObjectName("toolBox_function")
        self.page_battery_lab = QtWidgets.QWidget()
        self.page_battery_lab.setGeometry(QtCore.QRect(0, 0, 180, 69))
        self.page_battery_lab.setObjectName("page_battery_lab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_battery_lab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_battery_lab = QtWidgets.QRadioButton(self.page_battery_lab)
        self.radioButton_battery_lab.setObjectName("radioButton_battery_lab")
        self.verticalLayout_3.addWidget(self.radioButton_battery_lab)
        self.toolBox_function.addItem(self.page_battery_lab, "")
        self.page_custom_test = QtWidgets.QWidget()
        self.page_custom_test.setGeometry(QtCore.QRect(0, 0, 180, 69))
        self.page_custom_test.setObjectName("page_custom_test")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_custom_test)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_custom_test = QtWidgets.QRadioButton(self.page_custom_test)
        self.radioButton_custom_test.setObjectName("radioButton_custom_test")
        self.verticalLayout_2.addWidget(self.radioButton_custom_test)
        self.toolBox_function.addItem(self.page_custom_test, "")
        self.page_lithium_test = QtWidgets.QWidget()
        self.page_lithium_test.setGeometry(QtCore.QRect(0, 0, 180, 100))
        self.page_lithium_test.setObjectName("page_lithium_test")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_lithium_test)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_lithium_test_accuracy = QtWidgets.QRadioButton(self.page_lithium_test)
        self.radioButton_lithium_test_accuracy.setObjectName("radioButton_lithium_test_accuracy")
        self.verticalLayout.addWidget(self.radioButton_lithium_test_accuracy)
        self.radioButton_lithium_test_dnl = QtWidgets.QRadioButton(self.page_lithium_test)
        self.radioButton_lithium_test_dnl.setObjectName("radioButton_lithium_test_dnl")
        self.verticalLayout.addWidget(self.radioButton_lithium_test_dnl)
        self.radioButton_lithium_test_deviation = QtWidgets.QRadioButton(self.page_lithium_test)
        self.radioButton_lithium_test_deviation.setObjectName("radioButton_lithium_test_deviation")
        self.verticalLayout.addWidget(self.radioButton_lithium_test_deviation)
        self.radioButton_lithium_test_bgr = QtWidgets.QRadioButton(self.page_lithium_test)
        self.radioButton_lithium_test_bgr.setObjectName("radioButton_lithium_test_bgr")
        self.verticalLayout.addWidget(self.radioButton_lithium_test_bgr)
        self.toolBox_function.addItem(self.page_lithium_test, "")
        self.page_venus_test = QtWidgets.QWidget()
        self.page_venus_test.setGeometry(QtCore.QRect(0, 0, 180, 69))
        self.page_venus_test.setObjectName("page_venus_test")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_venus_test)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_venus_test_trim = QtWidgets.QRadioButton(self.page_venus_test)
        self.radioButton_venus_test_trim.setObjectName("radioButton_venus_test_trim")
        self.verticalLayout_4.addWidget(self.radioButton_venus_test_trim)
        self.toolBox_function.addItem(self.page_venus_test, "")
        self.page_jupiter_test = QtWidgets.QWidget()
        self.page_jupiter_test.setGeometry(QtCore.QRect(0, 0, 180, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_jupiter_test.sizePolicy().hasHeightForWidth())
        self.page_jupiter_test.setSizePolicy(sizePolicy)
        self.page_jupiter_test.setMinimumSize(QtCore.QSize(0, 0))
        self.page_jupiter_test.setObjectName("page_jupiter_test")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_jupiter_test)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_jupiter_test_ramp = QtWidgets.QRadioButton(self.page_jupiter_test)
        self.radioButton_jupiter_test_ramp.setObjectName("radioButton_jupiter_test_ramp")
        self.verticalLayout_5.addWidget(self.radioButton_jupiter_test_ramp)
        self.radioButton_jupiter_test_ramp_multi = QtWidgets.QRadioButton(self.page_jupiter_test)
        self.radioButton_jupiter_test_ramp_multi.setObjectName("radioButton_jupiter_test_ramp_multi")
        self.verticalLayout_5.addWidget(self.radioButton_jupiter_test_ramp_multi)
        self.radioButton_jupiter_test_noise = QtWidgets.QRadioButton(self.page_jupiter_test)
        self.radioButton_jupiter_test_noise.setObjectName("radioButton_jupiter_test_noise")
        self.verticalLayout_5.addWidget(self.radioButton_jupiter_test_noise)
        self.toolBox_function.addItem(self.page_jupiter_test, "")
        self.page_natrium_test = QtWidgets.QWidget()
        self.page_natrium_test.setGeometry(QtCore.QRect(0, 0, 163, 78))
        self.page_natrium_test.setObjectName("page_natrium_test")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_natrium_test)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_natrium_test_ramp = QtWidgets.QRadioButton(self.page_natrium_test)
        self.radioButton_natrium_test_ramp.setObjectName("radioButton_natrium_test_ramp")
        self.verticalLayout_6.addWidget(self.radioButton_natrium_test_ramp)
        self.radioButton_natrium_test_noise = QtWidgets.QRadioButton(self.page_natrium_test)
        self.radioButton_natrium_test_noise.setObjectName("radioButton_natrium_test_noise")
        self.verticalLayout_6.addWidget(self.radioButton_natrium_test_noise)
        self.radioButton_natrium_test_temperature = QtWidgets.QRadioButton(self.page_natrium_test)
        self.radioButton_natrium_test_temperature.setObjectName("radioButton_natrium_test_temperature")
        self.verticalLayout_6.addWidget(self.radioButton_natrium_test_temperature)
        self.toolBox_function.addItem(self.page_natrium_test, "")
        self.gridLayout.addWidget(self.toolBox_function, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 3, 1)
        self.groupBox_config = QtWidgets.QGroupBox(self.widget_main)
        self.groupBox_config.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_config.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox_config.setStyleSheet("QGroupBox{\n"
"    font: 75 italic 10pt \"Arial\";\n"
"    border-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(216, 227, 255);\n"
"}")
        self.groupBox_config.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_config.setFlat(False)
        self.groupBox_config.setCheckable(False)
        self.groupBox_config.setObjectName("groupBox_config")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_config)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_config_configpath = QtWidgets.QLabel(self.groupBox_config)
        self.label_config_configpath.setMinimumSize(QtCore.QSize(80, 0))
        self.label_config_configpath.setObjectName("label_config_configpath")
        self.horizontalLayout_2.addWidget(self.label_config_configpath)
        self.lineEdit_config_configpath = QtWidgets.QLineEdit(self.groupBox_config)
        self.lineEdit_config_configpath.setObjectName("lineEdit_config_configpath")
        self.horizontalLayout_2.addWidget(self.lineEdit_config_configpath)
        self.pushButton_config_folder = QtWidgets.QPushButton(self.groupBox_config)
        self.pushButton_config_folder.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_config_folder.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_config_folder.setObjectName("pushButton_config_folder")
        self.horizontalLayout_2.addWidget(self.pushButton_config_folder)
        self.gridLayout_2.addWidget(self.groupBox_config, 0, 1, 1, 1)
        self.groupBox_output = QtWidgets.QGroupBox(self.widget_main)
        self.groupBox_output.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_output.setStyleSheet("QGroupBox{\n"
"    font: 75 italic 10pt \"Arial\";\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(216, 227, 255);\n"
"}")
        self.groupBox_output.setObjectName("groupBox_output")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_output)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_output_outputpath = QtWidgets.QLabel(self.groupBox_output)
        self.label_output_outputpath.setMinimumSize(QtCore.QSize(80, 0))
        self.label_output_outputpath.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_output_outputpath.setObjectName("label_output_outputpath")
        self.horizontalLayout.addWidget(self.label_output_outputpath)
        self.lineEdit_output_outputpath = QtWidgets.QLineEdit(self.groupBox_output)
        self.lineEdit_output_outputpath.setObjectName("lineEdit_output_outputpath")
        self.horizontalLayout.addWidget(self.lineEdit_output_outputpath)
        self.pushButton_output_folder = QtWidgets.QPushButton(self.groupBox_output)
        self.pushButton_output_folder.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_output_folder.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_output_folder.setObjectName("pushButton_output_folder")
        self.horizontalLayout.addWidget(self.pushButton_output_folder)
        self.gridLayout_2.addWidget(self.groupBox_output, 1, 1, 1, 1)
        self.groupBox_start = QtWidgets.QGroupBox(self.widget_main)
        self.groupBox_start.setObjectName("groupBox_start")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_start)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButton_start_stop = QtWidgets.QPushButton(self.groupBox_start)
        self.pushButton_start_stop.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_start_stop.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Arial\";\n"
"}")
        self.pushButton_start_stop.setCheckable(True)
        self.pushButton_start_stop.setAutoExclusive(True)
        self.pushButton_start_stop.setObjectName("pushButton_start_stop")
        self.gridLayout_14.addWidget(self.pushButton_start_stop, 0, 1, 1, 1)
        self.pushButton_start_start = QtWidgets.QPushButton(self.groupBox_start)
        self.pushButton_start_start.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_start_start.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Arial\";\n"
"}")
        self.pushButton_start_start.setCheckable(True)
        self.pushButton_start_start.setAutoExclusive(True)
        self.pushButton_start_start.setObjectName("pushButton_start_start")
        self.gridLayout_14.addWidget(self.pushButton_start_start, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_start, 2, 1, 1, 1)
        self.widget_log = QtWidgets.QWidget(self.widget_main)
        self.widget_log.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_log.setObjectName("widget_log")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_log)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_log = QtWidgets.QGroupBox(self.widget_log)
        self.groupBox_log.setObjectName("groupBox_log")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_log)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_log)
        self.textBrowser_log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.gridLayout_8.addWidget(self.textBrowser_log, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_log, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_log, 3, 0, 1, 2)
        ui_MainWindow.setCentralWidget(self.widget_main)
        self.menubar = QtWidgets.QMenuBar(ui_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 23))
        self.menubar.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));")
        self.menubar.setObjectName("menubar")
        self.menu_debug = QtWidgets.QMenu(self.menubar)
        self.menu_debug.setObjectName("menu_debug")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        ui_MainWindow.setMenuBar(self.menubar)
        self.action_instrument = QtWidgets.QAction(ui_MainWindow)
        self.action_instrument.setObjectName("action_instrument")
        self.action_userguide = QtWidgets.QAction(ui_MainWindow)
        self.action_userguide.setObjectName("action_userguide")
        self.action_mcu = QtWidgets.QAction(ui_MainWindow)
        self.action_mcu.setObjectName("action_mcu")
        self.menu_debug.addAction(self.action_instrument)
        self.menu_debug.addAction(self.action_mcu)
        self.menu_help.addAction(self.action_userguide)
        self.menubar.addAction(self.menu_debug.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(ui_MainWindow)
        self.toolBox_function.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ui_MainWindow)

    def retranslateUi(self, ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        ui_MainWindow.setWindowTitle(_translate("ui_MainWindow", "Transepic_AutoTest_V2.06.00 "))
        self.groupBox.setTitle(_translate("ui_MainWindow", "Function"))
        self.radioButton_battery_lab.setText(_translate("ui_MainWindow", "Battery lab"))
        self.toolBox_function.setItemText(self.toolBox_function.indexOf(self.page_battery_lab), _translate("ui_MainWindow", "Battery lab"))
        self.radioButton_custom_test.setText(_translate("ui_MainWindow", "Custom test"))
        self.toolBox_function.setItemText(self.toolBox_function.indexOf(self.page_custom_test), _translate("ui_MainWindow", "Custom test"))
        self.radioButton_lithium_test_accuracy.setText(_translate("ui_MainWindow", "Accuracy"))
        self.radioButton_lithium_test_dnl.setText(_translate("ui_MainWindow", "DNL"))
        self.radioButton_lithium_test_deviation.setText(_translate("ui_MainWindow", "Deviation"))
        self.radioButton_lithium_test_bgr.setText(_translate("ui_MainWindow", "BGR"))
        self.toolBox_function.setItemText(self.toolBox_function.indexOf(self.page_lithium_test), _translate("ui_MainWindow", "Lithium test"))
        self.radioButton_venus_test_trim.setText(_translate("ui_MainWindow", "Trim"))
        self.toolBox_function.setItemText(self.toolBox_function.indexOf(self.page_venus_test), _translate("ui_MainWindow", "Venus test"))
        self.radioButton_jupiter_test_ramp.setText(_translate("ui_MainWindow", "Ramp"))
        self.radioButton_jupiter_test_ramp_multi.setText(_translate("ui_MainWindow", "Ramp multi"))
        self.radioButton_jupiter_test_noise.setText(_translate("ui_MainWindow", "Noise"))
        self.toolBox_function.setItemText(self.toolBox_function.indexOf(self.page_jupiter_test), _translate("ui_MainWindow", "Jupiter test"))
        self.radioButton_natrium_test_ramp.setText(_translate("ui_MainWindow", "Ramp"))
        self.radioButton_natrium_test_noise.setText(_translate("ui_MainWindow", "Noise"))
        self.radioButton_natrium_test_temperature.setText(_translate("ui_MainWindow", "Temperature"))
        self.toolBox_function.setItemText(self.toolBox_function.indexOf(self.page_natrium_test), _translate("ui_MainWindow", "Natrium test"))
        self.groupBox_config.setTitle(_translate("ui_MainWindow", "Config"))
        self.label_config_configpath.setText(_translate("ui_MainWindow", "Config path"))
        self.pushButton_config_folder.setText(_translate("ui_MainWindow", "Folder"))
        self.groupBox_output.setTitle(_translate("ui_MainWindow", "Output"))
        self.label_output_outputpath.setText(_translate("ui_MainWindow", "Output path"))
        self.pushButton_output_folder.setText(_translate("ui_MainWindow", "Folder"))
        self.groupBox_start.setTitle(_translate("ui_MainWindow", "Start"))
        self.pushButton_start_stop.setText(_translate("ui_MainWindow", "Stop"))
        self.pushButton_start_start.setText(_translate("ui_MainWindow", "Start"))
        self.groupBox_log.setTitle(_translate("ui_MainWindow", "Log"))
        self.menu_debug.setTitle(_translate("ui_MainWindow", "Debug(D)"))
        self.menu_help.setTitle(_translate("ui_MainWindow", "Help(H)"))
        self.action_instrument.setText(_translate("ui_MainWindow", "Instrument"))
        self.action_userguide.setText(_translate("ui_MainWindow", "User Guide"))
        self.action_mcu.setText(_translate("ui_MainWindow", "MCU"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mcuwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui_mcuwindow(object):
    def setupUi(self, ui_mcuwindow):
        ui_mcuwindow.setObjectName("ui_mcuwindow")
        ui_mcuwindow.resize(886, 572)
        ui_mcuwindow.setStyleSheet("#widget_main{\n"
"    background-color: rgb(247, 148, 71);\n"
"}\n"
"\n"
"\n"
"QMenuBar{\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QGroupBox{\n"
"    font: 75 italic 12pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(216, 227, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:inset\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(ui_mcuwindow)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(ui_mcuwindow)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_connection = QtWidgets.QGroupBox(self.widget)
        self.groupBox_connection.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_connection.setObjectName("groupBox_connection")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_connection)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_77 = QtWidgets.QLabel(self.groupBox_connection)
        self.label_77.setMinimumSize(QtCore.QSize(20, 0))
        self.label_77.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_77.setObjectName("label_77")
        self.gridLayout_3.addWidget(self.label_77, 0, 0, 1, 1)
        self.comboBox_device = QtWidgets.QComboBox(self.groupBox_connection)
        self.comboBox_device.setMinimumSize(QtCore.QSize(60, 0))
        self.comboBox_device.setEditable(False)
        self.comboBox_device.setObjectName("comboBox_device")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_device, 0, 1, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.groupBox_connection)
        self.label_89.setMinimumSize(QtCore.QSize(20, 0))
        self.label_89.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_89.setObjectName("label_89")
        self.gridLayout_3.addWidget(self.label_89, 1, 0, 1, 1)
        self.comboBox_protocol = QtWidgets.QComboBox(self.groupBox_connection)
        self.comboBox_protocol.setMinimumSize(QtCore.QSize(60, 0))
        self.comboBox_protocol.setEditable(False)
        self.comboBox_protocol.setObjectName("comboBox_protocol")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_protocol, 1, 1, 1, 1)
        self.pushButton_open = QtWidgets.QPushButton(self.groupBox_connection)
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout_3.addWidget(self.pushButton_open, 2, 0, 1, 2)
        self.pushButton_close = QtWidgets.QPushButton(self.groupBox_connection)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_3.addWidget(self.pushButton_close, 3, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_connection, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_write = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_write.setObjectName("pushButton_write")
        self.verticalLayout.addWidget(self.pushButton_write)
        self.pushButton_read = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_read.setObjectName("pushButton_read")
        self.verticalLayout.addWidget(self.pushButton_read)
        self.radioButton_reg_inversion = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_reg_inversion.setObjectName("radioButton_reg_inversion")
        self.verticalLayout.addWidget(self.radioButton_reg_inversion)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tabWidget_function = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_function.setObjectName("tabWidget_function")
        self.tab_I2C = QtWidgets.QWidget()
        self.tab_I2C.setObjectName("tab_I2C")
        self.formLayout = QtWidgets.QFormLayout(self.tab_I2C)
        self.formLayout.setObjectName("formLayout")
        self.label_26 = QtWidgets.QLabel(self.tab_I2C)
        self.label_26.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("font: 12pt \"Arial\";")
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_26)
        self.label_2 = QtWidgets.QLabel(self.tab_I2C)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_I2C_bus_num = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_bus_num.setText("")
        self.lineEdit_I2C_bus_num.setObjectName("lineEdit_I2C_bus_num")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_bus_num)
        self.label = QtWidgets.QLabel(self.tab_I2C)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_I2C_slave = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_slave.setText("")
        self.lineEdit_I2C_slave.setObjectName("lineEdit_I2C_slave")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_slave)
        self.label_18 = QtWidgets.QLabel(self.tab_I2C)
        self.label_18.setMinimumSize(QtCore.QSize(150, 0))
        self.label_18.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_I2C_restart = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_restart.setObjectName("lineEdit_I2C_restart")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_restart)
        self.label_32 = QtWidgets.QLabel(self.tab_I2C)
        self.label_32.setMinimumSize(QtCore.QSize(150, 0))
        self.label_32.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_32.setObjectName("label_32")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.lineEdit_I2C_frequency = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_frequency.setObjectName("lineEdit_I2C_frequency")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_frequency)
        self.label_80 = QtWidgets.QLabel(self.tab_I2C)
        self.label_80.setMinimumSize(QtCore.QSize(150, 0))
        self.label_80.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_80.setObjectName("label_80")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_80)
        self.lineEdit_I2C_rx_size = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_rx_size.setText("")
        self.lineEdit_I2C_rx_size.setObjectName("lineEdit_I2C_rx_size")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_rx_size)
        self.label_78 = QtWidgets.QLabel(self.tab_I2C)
        self.label_78.setMinimumSize(QtCore.QSize(150, 0))
        self.label_78.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_78.setObjectName("label_78")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_78)
        self.lineEdit_I2C_reg_address = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_reg_address.setText("")
        self.lineEdit_I2C_reg_address.setObjectName("lineEdit_I2C_reg_address")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_reg_address)
        self.label_79 = QtWidgets.QLabel(self.tab_I2C)
        self.label_79.setMinimumSize(QtCore.QSize(150, 0))
        self.label_79.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_79.setObjectName("label_79")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_79)
        self.lineEdit_I2C_reg_value = QtWidgets.QLineEdit(self.tab_I2C)
        self.lineEdit_I2C_reg_value.setText("")
        self.lineEdit_I2C_reg_value.setObjectName("lineEdit_I2C_reg_value")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_I2C_reg_value)
        self.tabWidget_function.addTab(self.tab_I2C, "")
        self.tab_SPI = QtWidgets.QWidget()
        self.tab_SPI.setObjectName("tab_SPI")
        self.formLayout_4 = QtWidgets.QFormLayout(self.tab_SPI)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_29 = QtWidgets.QLabel(self.tab_SPI)
        self.label_29.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_29.setStyleSheet("font: 12pt \"Arial\";")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_29.setObjectName("label_29")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_29)
        self.label_4 = QtWidgets.QLabel(self.tab_SPI)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_SPI_config = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_config.setText("")
        self.lineEdit_SPI_config.setObjectName("lineEdit_SPI_config")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_config)
        self.label_5 = QtWidgets.QLabel(self.tab_SPI)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_SPI_bus_num = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_bus_num.setObjectName("lineEdit_SPI_bus_num")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_bus_num)
        self.label_34 = QtWidgets.QLabel(self.tab_SPI)
        self.label_34.setMinimumSize(QtCore.QSize(150, 0))
        self.label_34.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_34.setObjectName("label_34")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.lineEdit_SPI_DO = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_DO.setText("")
        self.lineEdit_SPI_DO.setObjectName("lineEdit_SPI_DO")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_DO)
        self.label_84 = QtWidgets.QLabel(self.tab_SPI)
        self.label_84.setMinimumSize(QtCore.QSize(150, 0))
        self.label_84.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_84.setObjectName("label_84")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_84)
        self.lineEdit_SPI_DI = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_DI.setAutoFillBackground(False)
        self.lineEdit_SPI_DI.setText("")
        self.lineEdit_SPI_DI.setReadOnly(True)
        self.lineEdit_SPI_DI.setObjectName("lineEdit_SPI_DI")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_DI)
        self.label_82 = QtWidgets.QLabel(self.tab_SPI)
        self.label_82.setMinimumSize(QtCore.QSize(150, 0))
        self.label_82.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_82.setObjectName("label_82")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_82)
        self.lineEdit_SPI_frequency = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_frequency.setObjectName("lineEdit_SPI_frequency")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_frequency)
        self.label_83 = QtWidgets.QLabel(self.tab_SPI)
        self.label_83.setMinimumSize(QtCore.QSize(150, 0))
        self.label_83.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_83.setObjectName("label_83")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_83)
        self.lineEdit_SPI_CPOL = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_CPOL.setObjectName("lineEdit_SPI_CPOL")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_CPOL)
        self.label_85 = QtWidgets.QLabel(self.tab_SPI)
        self.label_85.setMinimumSize(QtCore.QSize(150, 0))
        self.label_85.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_85.setObjectName("label_85")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_85)
        self.lineEdit_SPI_CHPA = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_CHPA.setObjectName("lineEdit_SPI_CHPA")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_CHPA)
        self.label_86 = QtWidgets.QLabel(self.tab_SPI)
        self.label_86.setMinimumSize(QtCore.QSize(150, 0))
        self.label_86.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_86.setObjectName("label_86")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_86)
        self.lineEdit_SPI_first_bit = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_first_bit.setObjectName("lineEdit_SPI_first_bit")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_first_bit)
        self.label_87 = QtWidgets.QLabel(self.tab_SPI)
        self.label_87.setMinimumSize(QtCore.QSize(150, 0))
        self.label_87.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_87.setObjectName("label_87")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_87)
        self.lineEdit_SPI_data_size = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_data_size.setObjectName("lineEdit_SPI_data_size")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_data_size)
        self.label_88 = QtWidgets.QLabel(self.tab_SPI)
        self.label_88.setMinimumSize(QtCore.QSize(150, 0))
        self.label_88.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_88.setObjectName("label_88")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_88)
        self.lineEdit_SPI_CSPOL = QtWidgets.QLineEdit(self.tab_SPI)
        self.lineEdit_SPI_CSPOL.setObjectName("lineEdit_SPI_CSPOL")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_SPI_CSPOL)
        self.tabWidget_function.addTab(self.tab_SPI, "")
        self.tab_GPIO = QtWidgets.QWidget()
        self.tab_GPIO.setObjectName("tab_GPIO")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_GPIO)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_27 = QtWidgets.QLabel(self.tab_GPIO)
        self.label_27.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("font: 12pt \"Arial\";")
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_27)
        self.label_3 = QtWidgets.QLabel(self.tab_GPIO)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_GPIO_number = QtWidgets.QLineEdit(self.tab_GPIO)
        self.lineEdit_GPIO_number.setText("")
        self.lineEdit_GPIO_number.setObjectName("lineEdit_GPIO_number")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GPIO_number)
        self.label_19 = QtWidgets.QLabel(self.tab_GPIO)
        self.label_19.setMinimumSize(QtCore.QSize(150, 0))
        self.label_19.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_GPIO_vssel = QtWidgets.QLineEdit(self.tab_GPIO)
        self.lineEdit_GPIO_vssel.setObjectName("lineEdit_GPIO_vssel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GPIO_vssel)
        self.label_33 = QtWidgets.QLabel(self.tab_GPIO)
        self.label_33.setMinimumSize(QtCore.QSize(150, 0))
        self.label_33.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_33.setObjectName("label_33")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.lineEdit_GPIO_pad = QtWidgets.QLineEdit(self.tab_GPIO)
        self.lineEdit_GPIO_pad.setObjectName("lineEdit_GPIO_pad")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GPIO_pad)
        self.label_81 = QtWidgets.QLabel(self.tab_GPIO)
        self.label_81.setMinimumSize(QtCore.QSize(150, 0))
        self.label_81.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_81.setObjectName("label_81")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_81)
        self.lineEdit_GPIO_value = QtWidgets.QLineEdit(self.tab_GPIO)
        self.lineEdit_GPIO_value.setText("")
        self.lineEdit_GPIO_value.setObjectName("lineEdit_GPIO_value")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GPIO_value)
        self.tabWidget_function.addTab(self.tab_GPIO, "")
        self.tab_RST = QtWidgets.QWidget()
        self.tab_RST.setObjectName("tab_RST")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab_RST)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_28 = QtWidgets.QLabel(self.tab_RST)
        self.label_28.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("font: 12pt \"Arial\";")
        self.label_28.setObjectName("label_28")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_28)
        self.tabWidget_function.addTab(self.tab_RST, "")
        self.gridLayout_2.addWidget(self.tabWidget_function, 0, 1, 2, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(ui_mcuwindow)
        self.tabWidget_function.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ui_mcuwindow)

    def retranslateUi(self, ui_mcuwindow):
        _translate = QtCore.QCoreApplication.translate
        ui_mcuwindow.setWindowTitle(_translate("ui_mcuwindow", "MCU control"))
        self.groupBox_connection.setTitle(_translate("ui_mcuwindow", "Connection"))
        self.label_77.setText(_translate("ui_mcuwindow", "Device"))
        self.comboBox_device.setItemText(0, _translate("ui_mcuwindow", "MAX32670"))
        self.comboBox_device.setItemText(1, _translate("ui_mcuwindow", "F413ZH"))
        self.comboBox_device.setItemText(2, _translate("ui_mcuwindow", "F413CH"))
        self.comboBox_device.setItemText(3, _translate("ui_mcuwindow", "CH341A"))
        self.comboBox_device.setItemText(4, _translate("ui_mcuwindow", "CH347"))
        self.label_89.setText(_translate("ui_mcuwindow", "Protocol"))
        self.comboBox_protocol.setItemText(0, _translate("ui_mcuwindow", "serial"))
        self.comboBox_protocol.setItemText(1, _translate("ui_mcuwindow", "ch"))
        self.pushButton_open.setText(_translate("ui_mcuwindow", "Open deivce"))
        self.pushButton_close.setText(_translate("ui_mcuwindow", "Close deivce"))
        self.groupBox.setTitle(_translate("ui_mcuwindow", "Setting"))
        self.pushButton_write.setText(_translate("ui_mcuwindow", "Write"))
        self.pushButton_read.setText(_translate("ui_mcuwindow", "Read"))
        self.radioButton_reg_inversion.setText(_translate("ui_mcuwindow", "Reg inversion"))
        self.label_26.setText(_translate("ui_mcuwindow", "I2C function\n"
"Restart:0=off,1=on\n"
"Frequency:1=100K,2=400K,3=1M,4=4M,5=10k"))
        self.label_2.setText(_translate("ui_mcuwindow", "Bus number"))
        self.label.setText(_translate("ui_mcuwindow", "Slave address"))
        self.label_18.setText(_translate("ui_mcuwindow", "Restart"))
        self.lineEdit_I2C_restart.setText(_translate("ui_mcuwindow", "0"))
        self.label_32.setText(_translate("ui_mcuwindow", "Frequency"))
        self.lineEdit_I2C_frequency.setText(_translate("ui_mcuwindow", "1"))
        self.label_80.setText(_translate("ui_mcuwindow", "Reg number"))
        self.label_78.setText(_translate("ui_mcuwindow", "Reg address"))
        self.label_79.setText(_translate("ui_mcuwindow", "Reg value"))
        self.tabWidget_function.setTabText(self.tabWidget_function.indexOf(self.tab_I2C), _translate("ui_mcuwindow", "I2C"))
        self.label_29.setText(_translate("ui_mcuwindow", "SPI function\n"
"Config:0=off,1=on\n"
"First Bit:0=lsb,1=msb\n"
"CPOL:0=low,1=high\n"
"CPHA:0=first,1=second\n"
"Data Size:0=byte,1=harf_wd\n"
"CSPOL:0=low,1=high\n"
"Frequency:0=24M,1=12M,2=6M,3=3M,4=1.5M,5=750K,6=375K,7=187.5K\n"
""))
        self.label_4.setText(_translate("ui_mcuwindow", "Config"))
        self.label_5.setText(_translate("ui_mcuwindow", "Bus num"))
        self.lineEdit_SPI_bus_num.setText(_translate("ui_mcuwindow", "1"))
        self.label_34.setText(_translate("ui_mcuwindow", "DO"))
        self.label_84.setText(_translate("ui_mcuwindow", "DI"))
        self.label_82.setText(_translate("ui_mcuwindow", "Frequency"))
        self.lineEdit_SPI_frequency.setText(_translate("ui_mcuwindow", "7"))
        self.label_83.setText(_translate("ui_mcuwindow", "CPOL"))
        self.lineEdit_SPI_CPOL.setText(_translate("ui_mcuwindow", "1"))
        self.label_85.setText(_translate("ui_mcuwindow", "CHPA"))
        self.lineEdit_SPI_CHPA.setText(_translate("ui_mcuwindow", "1"))
        self.label_86.setText(_translate("ui_mcuwindow", "First bit"))
        self.lineEdit_SPI_first_bit.setText(_translate("ui_mcuwindow", "1"))
        self.label_87.setText(_translate("ui_mcuwindow", "Data Size"))
        self.lineEdit_SPI_data_size.setText(_translate("ui_mcuwindow", "1"))
        self.label_88.setText(_translate("ui_mcuwindow", "CSPOL"))
        self.lineEdit_SPI_CSPOL.setText(_translate("ui_mcuwindow", "0"))
        self.tabWidget_function.setTabText(self.tabWidget_function.indexOf(self.tab_SPI), _translate("ui_mcuwindow", "SPI"))
        self.label_27.setText(_translate("ui_mcuwindow", "GPIO function"))
        self.label_3.setText(_translate("ui_mcuwindow", "GPIO number"))
        self.label_19.setText(_translate("ui_mcuwindow", "GPIO voltage selection"))
        self.lineEdit_GPIO_vssel.setText(_translate("ui_mcuwindow", "0"))
        self.label_33.setText(_translate("ui_mcuwindow", "GPIO pad"))
        self.lineEdit_GPIO_pad.setText(_translate("ui_mcuwindow", "0"))
        self.label_81.setText(_translate("ui_mcuwindow", "GPIO value(Get/Set)"))
        self.tabWidget_function.setTabText(self.tabWidget_function.indexOf(self.tab_GPIO), _translate("ui_mcuwindow", "GPIO"))
        self.label_28.setText(_translate("ui_mcuwindow", "Reset function"))
        self.tabWidget_function.setTabText(self.tabWidget_function.indexOf(self.tab_RST), _translate("ui_mcuwindow", "RST"))

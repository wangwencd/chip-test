# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/19 16:03
File: main.py
"""
import sys
import setup
from PyQt5.QtWidgets import QApplication
from parse.self_logging.logger import Logger
from ui.mainwindow_control import Mainwindow_Control

Logger()
app = QApplication(sys.argv)

def main():
    """
    Main function
    """
    main = Mainwindow_Control()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

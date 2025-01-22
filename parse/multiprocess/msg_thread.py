# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/15 10:42
File: msg_thread.py
"""

import logging

from PyQt5.QtCore import QThread, pyqtSignal
from .queue import Q

L = logging.getLogger('Main')

class Msg_Thread(QThread):
    """
    Message threading class
    """
    signal1 = pyqtSignal(str)  # A signal with type str
    signal2 = pyqtSignal(bool)  # A signal with type bool
    signal3 = pyqtSignal(float)  # A signal with type float

    def __init__(self):
        """
        Initial class
        """
        super().__init__()

    def run(self):
        """
        Message thread function
        """
        while True:
            message = Q.get()

            if isinstance(message, logging.LogRecord):
                self.signal1.emit(message.msg)

            elif isinstance(message, bool):
                print('bool')
                self.signal2.emit(message)

            elif isinstance(message, float):
                self.signal3.emit(message)


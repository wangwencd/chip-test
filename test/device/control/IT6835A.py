# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/7 13:47
File: IT6835A.py
"""
import logging
from test.device.control.IT6722A import IT6722A
L = logging.getLogger('Main')

class IT6835A(IT6722A):
    """
    IT6835A control
    """
    def __init__(self, cls, name=None):
        self.control = cls
        super().__init__(cls, self.name)
        self.name = name if name else 'IT6835A'

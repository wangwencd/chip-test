# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/8/1 9:43
File: DP932U.py
"""
import logging
from test.device.control.DP832 import DP832

L = logging.getLogger('Main')

class DP932U(DP832):
    """
    DP932U control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DP932U'
        super(DP832).__init__()

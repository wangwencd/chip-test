# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/12/21 11:46
File: DP932.py
"""
import logging
from test.device.control.DP832 import DP832

L = logging.getLogger('Main')

class DP932(DP832):
    """
    DP932 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DP932'
        super(DP832).__init__()


# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/12/31 14:04
File: flow_DL3021.py
"""
import logging
from test.device.flow.flow_IT8811 import Flow_IT8811

L = logging.getLogger('Main')

class Flow_DL3021(Flow_IT8811):
    """
    Control flow of DL3021
    """
    def __init__(self, cls, name=None):
        self.name = name if name else 'DL3021'
        super().__init__(cls, self.name)
        self.control = cls

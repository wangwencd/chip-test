# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/21 10:25
File: flow_IT8811B.py
"""
import logging
from test.device.flow.flow_IT8811 import Flow_IT8811

L = logging.getLogger('Main')

class Flow_IT8811B(Flow_IT8811):
    """
    Control flow of IT8811B
    """
    def __init__(self, cls, name=None):
        self.name = name if name else 'IT8811B'
        super().__init__(cls, self.name)
        self.control = cls

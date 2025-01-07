# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2025/1/7 13:49
File: flow_IT6835A.py
"""
import logging
from test.device.flow.flow_IT6722A import Flow_IT6722A

L = logging.getLogger('Main')

class Flow_IT6835A(Flow_IT6722A):
    """
    Control flow of IT6835A
    """
    def __init__(self, cls, name=None):
        self.name = name if name else 'IT6835A'
        self.control = cls
        super(Flow_IT6835A, self).__init__(cls, self.name)

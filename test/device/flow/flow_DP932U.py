# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2024/8/1 9:44
File: flow_DP932U.py
"""
import logging
from test.device.flow.flow_DP832 import Flow_DP832

L = logging.getLogger('Main')

class Flow_DP932U(Flow_DP832):
    """
    Control flow of DP932U
    """
    def __init__(self, cls):
        super(Flow_DP932U, self).__init__(cls)

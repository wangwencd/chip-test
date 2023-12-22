# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/12/21 11:47
File: flow_DP932.py
"""
import logging
from test.device.flow.flow_DP832 import Flow_DP832

L = logging.getLogger('Main')

class Flow_DP932(Flow_DP832):
    """
    Control flow of DP932
    """
    def __init__(self, cls):
        super(Flow_DP932, self).__init__(cls)

# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/3 17:56
File: flow_F413CH.py
"""
import logging
from test.device.control.F413ZH import F413ZH
from test.device.flow.flow_MAX32760 import Flow_MAX32670

L = logging.getLogger('Main')

class Flow_F413CH(F413ZH, Flow_MAX32670):
    """
    Control flow of F413CH
    """
    def __init__(self, cls):
        super(Flow_F413CH, self).__init__(cls)

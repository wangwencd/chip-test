# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/7/3 17:54
File: F413CH.py
"""
import logging
from test.device.control.F413ZH import F413ZH

L = logging.getLogger('Main')

class F413CH(F413ZH):
    """
    F413CH control
    """
    def __init__(self, cls):
        super().__init__(cls)
        self.control = cls
        self.name = 'F413CH'

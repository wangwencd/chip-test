# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2023/3/15 14:20
File: F413ZH.py
"""
import time
import logging
from test.device.control.MAX32670 import MAX32670

L = logging.getLogger('Main')

class F413ZH(MAX32670):
    """
    F413ZH control
    """
    def __init__(self, cls):
        super().__init__(cls)
        self.control = cls
        self.name = 'F413ZH'

    # def receive_msg(self):
    #     self.control.instrument.flushInput()
    #
    #     t1 = time.time()
    #     t2 = time.time()
    #     while t2 - t1 < 0.2:
    #         try:
    #             rx_buf = ''
    #             rx_buf = self.control.instrument.read()  # 转化为整型数字
    #             if rx_buf != b'':
    #                 rx_buf = rx_buf + self.control.instrument.read_all()
    #                 # print(rx_buf)
    #                 rx_buf = self.parse_code(rx_buf)
    #                 proto_info = serial_test.receive_and_unpack_mesg(rx_buf)
    #                 if proto_info is not None:
    #                     # L.info(self.name + ' get info success!')
    #                     return proto_info
    #             time.sleep(0.001)
    #         except:
    #             pass
    #
    #         finally:
    #             t2 = time.time()
    #
    #     L.warning(self.name + ' get info fail!')
    #     return

    # def receive_msg_standby(self, period):
    #     self.control.instrument.flushInput()
    #     t1 = time.time()
    #     t2 = time.time()
    #
    #     while t2 - t1 < 1.5 * period:
    #
    #         try:
    #             rx_buf = ''
    #             rx_buf = self.control.instrument.read()  # 转化为整型数字
    #             if rx_buf != b'':
    #                 rx_buf = rx_buf + self.control.instrument.read_all()
    #                 print(rx_buf)
    #                 rx_buf = self.parse_code(rx_buf)
    #                 proto_info = serial_test.receive_and_unpack_mesg(rx_buf)
    #                 if proto_info is not None:
    #                     # L.info(self.name + ' get info success!')
    #                     return proto_info
    #             time.sleep(0.001)
    #         except:
    #             pass
    #
    #         finally:
    #             t2 = time.time()
    #
    #     L.warning(self.name + ' get info fail!')
    #     return
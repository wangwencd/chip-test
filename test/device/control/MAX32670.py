# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/12/19 15:17
File: MAX32670.py
"""
import logging
import time

from parse.multiprocess.pool_thread import pool
from parse.file.reg_operation import Reg_Operation
from package.PB_Proto.framework import PBCore, PB_Log

L = logging.getLogger('Main')

class MAX32670(object):
    """
    MAX32670 control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'MAX32670'

    @staticmethod
    def parse_code(code):
        total_length = len(code)
        cal_length = int.from_bytes(code[2: 4], byteorder='big', signed=True)

        if total_length == (cal_length + 4):
            return code

        elif total_length > (cal_length + 4):
            L.warning('Code is too long!')
            return code[0: cal_length + 4]

        elif total_length < (cal_length + 4):
            L.error('Code is wrong!')
            raise ValueError

    def parse_result(self, msg, func_flag):
        """
        Parse result and output the information

        Args:
            msg: Result structure
            func_flag: Function flag, func_flag = 1/2/3/4/5
        """
        if msg is not None:

            if func_flag == 1:  # I2C write function
                parse_result = Reg_Operation.dec_to_hex(msg['data_buf'])
                L.info(self.name + ' write address: [' + str(parse_result[0]) + '], value: ' + str(parse_result[1:]))

            elif func_flag == 2:  # I2C read function
                parse_result = Reg_Operation.dec_to_hex(msg)
                L.info(self.name + ' read value: ' + str(parse_result))

            elif func_flag == 3:  # GPIO write function
                L.info(self.name + ' write PIN: [' + str(msg['gpio_num']) + '], value: [' + str(msg['set_value']) + ']')

            elif func_flag == 4:  # GPIO write function
                L.info(self.name + ' read PIN: [' + str(msg) + '], value: [' + str(msg.get_value) + ']')

            elif func_flag == 5:  # Reset function
                L.info(self.name + ' reset')

            elif func_flag == 6:  # SPI write function
                if msg['cfg'] == 1:  # Write config
                    L.info(
                        self.name
                        + ' set'
                        + ' CPOL: ' + str(msg['cpol'])
                        + ', CPHA: ' + str(msg['cpha'])
                        + ', First bit: ' + str(msg['fstb'])
                        + ', Size: ' + str(msg['size'])
                        + ', CSPOL: ' + str(msg['cspol'])
                        + ', Frequency: ' + str(msg['freq'])
                    )
                else:
                    parse_result = Reg_Operation.dec_to_hex(msg['data_buf'])
                    L.info(
                        self.name + ' write address: [' + str(parse_result[0]) + '], value: ' + str(parse_result[1:])
                    )

            elif func_flag == 7:  # SPI read function
                parse_result = Reg_Operation.dec_to_hex(msg)
                L.info(self.name + ' read value: ' + str(parse_result))

    def write_I2C(self, msg):
        proto_info = self.com_transimit_write(
            proto_type='I2C_Proto',
            bus_num=msg['bus_num'],
            i2c_address=msg['i2c_address'],
            data_buf=msg['data_buf'],
            frequency=msg['frequency'],
        )
        self.parse_result(msg, 1)

        return proto_info

    def read_I2C(self, msg):
        proto_info = self.com_transimit_read(
            proto_type='I2C_Proto',
            bus_num=msg['bus_num'],
            i2c_address=msg['i2c_address'],
            rx_size=msg['rx_size'],
            data_buf=msg['data_buf'],
            frequency=msg['frequency'],
        )
        self.parse_result(proto_info, 2)

        return proto_info

    def write_GPIO(self, msg):
        proto_info = self.com_transimit_write(
            proto_type='GPIO_Proto',
            gpio_num=msg['gpio_num'],
            set_value=msg['set_value']
        )
        self.parse_result(msg, 3)

        return proto_info

    def read_GPIO(self, msg):
        proto_info = self.com_transimit_read(
            proto_type='GPIO_Proto',
            gpio_num=msg['gpio_num'],
            get_value=msg['get_value'])
        self.parse_result(proto_info, 4)

        return proto_info

    def reset(self, msg):
        proto_info = PBCore.com_transimit_write(
            proto_type='SYSTEM_RESET'
        )
        self.parse_result(proto_info, 5)

        return proto_info

    def pack_and_send_mesg(self, **kwargs):
        pbtype = PBCore.proto_type_dict.get(kwargs.get("proto_type"))
        proto_buf = eval('PBCore.' + PBCore.proto_pack_dict.get(pbtype))(**kwargs)
        proto_frame = PBCore.package_proto_frame(proto_buf, PBCore.proto_type_dict.get(kwargs.get("proto_type")), len(proto_buf))
        # print(len(proto_frame))
        # print(proto_frame)
        proto_info = self.control.instrument.write(proto_frame)

        return proto_info

    def receive_msg(self):
        self.control.instrument.flushInput()

        start_time = time.time()
        while True:
            try:
                rx_buf = ''
                rx_buf = self.control.instrument.read()  # 转化为整型数字
                if rx_buf != b'':
                    # time.sleep(0.01)
                    rx_buf = rx_buf + self.control.instrument.read_all()
                    # print(rx_buf)
                    rx_buf = self.parse_code(rx_buf)
                    proto_info = PBCore.receive_and_unpack_mesg(rx_buf)
                    if proto_info is not None:
                        # L.info(self.name + ' get info success!')
                        return proto_info
                # time.sleep(0.01)
            except:
                pass

            if time.time() - start_time > 0.05:
                L.warning(self.name + ' get info fail!')
                return []

    def com_transimit_read(self, **kwargs):
        self.control.instrument.flushInput()
        future_msg = pool.submit(self.receive_msg)
        self.pack_and_send_mesg(**kwargs)
        proto_info = future_msg.result()
        # print(proto_info)
        # if proto_info == -1:  # Receive error
        #     proto_info = self.com_transimit_read(**kwargs)
        return proto_info

    def com_transimit_write(self, **kwargs):
        proto_info = self.pack_and_send_mesg(**kwargs)

        return proto_info

    def write_SPI(self, msg):
        msg.update({'proto_type': 'SPI_Proto'})
        proto_info = self.com_transimit_write(**msg)
        self.parse_result(msg, 6)

        return proto_info
    def read_SPI(self, msg):
        msg.update({'proto_type': 'SPI_Proto'})
        proto_info = self.com_transimit_read(**msg)
        self.parse_result(proto_info, 7)

        return proto_info

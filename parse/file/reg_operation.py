# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/12/21 14:27
File: reg_operation.py
"""
import logging
import re

L = logging.getLogger('Main')

class Reg_Operation(object):
    """
    Register operations class
    """

    @staticmethod
    def dec_to_hex(dec_data: list):
        """
        Convert a dec list into a hex list.

        Args:
            dec_data: Dec list, format: list, e.g. [1,2,3,4].

        Returns:
            hex_data: Hex list, format: list, e.g. ['0x1','0x2','0x3','0x4'].
        """
        hex_data = []

        for data in dec_data:
            hex_data.append(hex(data).replace('0x', '').zfill(2))

        return hex_data

    @staticmethod
    def hex_to_dec(hex_data: list or str):
        """
        Convert a hex list or hex long string into a dec list.

        Args:
            hex_data: Hex list, format: list,
             e.g. ['0x1','0x2','0x3','0x4'] or '0x00,0X11,0X22,0x33' or '00, 11, 22, 33' or '00; 11; 22; 33'.

        Returns:
            dec_data: Dec list, format: list, e.g. [1,2,3,4].
        """
        dec_data = []

        if isinstance(hex_data, str):
            hex_data = re.split(',|;', hex_data)

        for data in hex_data:

            if data == '' or data.isspace():
                pass
            else:
                dec_data.append(int(data, 16))

        return dec_data

    @staticmethod
    def hex_to_one(hex_data: list):
        """
        Convert a hex list or hex long string into one hex data.

        Args:
            hex_data: Hex list, format: list,
             e.g. ['0x1','0x2','0x3','0x4'] or '0x00,0X11,0X22,0x33' or '00, 11, 22, 33' or '00; 11; 22; 33'.

        Returns:
            one_data: Hex data, format: string, e.g. '0x1122'.
        """
        one_data = ''

        if isinstance(hex_data, str):
            hex_data = re.split(',|;', hex_data)

        for data in hex_data:

            if re.search('0x', data, re.I) is not None:
                one_data = one_data + data.lower().split('0x')[1]

            else:
                one_data = one_data + data
        one_data = one_data.replace(' ', '')

        return '0x' + one_data

    @staticmethod
    def dec_to_one(dec_data: list):
        """
        Convert a dec list into one hex data.

        Args:
            dec_data: Dec list, format: list, e.g. [1,2,3,4].

        Returns:
            one_data: Dec data, format: int, e.g. 123456.
        """
        hex_data = Reg_Operation.dec_to_hex(dec_data)
        hex_data = Reg_Operation.hex_to_one(hex_data)
        one_data = int(hex_data, 16)

        return one_data

if __name__ == '__main__':
    # result1 = Reg_Operation.hex_to_one([])
    result3 = Reg_Operation.dec_to_hex([1])
    result4 = Reg_Operation.dec_to_one([11, 22, 33])
    result5 = Reg_Operation.dec_to_one([11,22,33])
    # result6 = Reg_Operation.hex_to_one('00, 11, 22, 33')
    # result7 = Reg_Operation.hex_to_one('00; 11; 22; 33')
    # result8 = Reg_Operation.hex_to_one('00; ')
    x = 1
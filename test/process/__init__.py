# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/16 11:47
File: __init__.py
"""
import setup

from test.process.test_custom_test import Test_Custom_Test
from test.process.test_battery_lab import Test_Battery_Lab
from test.process.test_lithium import Test_Lithium
from test.process.test_venus import Test_Venus
from test.process.test_jupiter import Test_Jupiter
from test.process.test_natrium import Test_Natrium

Test_Process_Dict = {
    'Item': 'Process',
    'Custom': Test_Custom_Test,
    'Battery': Test_Battery_Lab,
    'Lithium': Test_Lithium,
    'Venus': Test_Venus,
    'Jupiter': Test_Jupiter,
    'Natrium': Test_Natrium,
}

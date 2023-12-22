# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/5 13:49
File: __init__.py
"""
from parse.process.parse_custom_test import Parse_Custom_Test
from parse.process.parse_battery_lab import Parse_battery_Lab
from parse.process.parse_lithium import Parse_Lithium
from parse.process.parse_venus import Parse_Venus
from parse.process.parse_jupiter import Parse_Jupiter
from parse.process.parse_natrium import Parse_Natrium

Parse_Process_Dict = {
    'Item': 'Process',
    'Custom': Parse_Custom_Test,
    'Battery': Parse_battery_Lab,
    'Lithium': Parse_Lithium,
    'Venus': Parse_Venus,
    'Jupiter': Parse_Jupiter,
    'Natrium': Parse_Natrium,
}
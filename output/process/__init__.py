# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/5 11:09
File: __init__.py
"""
from output.process.output_battery_lab import Output_Battery_Lab
from output.process.output_custom_test import Output_Custom_Test
from output.process.output_lithium import Output_Lithium
from output.process.output_venus import Output_Venus
from output.process.output_jupiter import Output_Jupiter
from output.process.output_natrium import Output_Natrium

Output_Process_Dict = {
    'Item': 'Process',
    'Battery': Output_Battery_Lab,
    'Custom': Output_Custom_Test,
    'Lithium': Output_Lithium,
    'Venus': Output_Venus,
    'Jupiter': Output_Jupiter,
    'Natrium': Output_Natrium,
}

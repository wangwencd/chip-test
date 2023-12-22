# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/11/23 10:51
File: pool_thread.py
"""
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=10)

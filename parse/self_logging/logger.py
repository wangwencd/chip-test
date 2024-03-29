# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/7/19 14:36
File: logger.py
"""

import os
import logging
import logging.handlers
import time

from parse.file.project_path import pro_path
from parse.file.file_operation import File_Operation
from parse.multiprocess.queue import Q

class Logger:
    """
    Logging class, create log and save
    """
    def __init__(self):
        """
        Init func, Set name, format, saving path and level
        """
        self.log = logging.getLogger('Main') # Set name
        self.log_format = logging.Formatter(
            '%(asctime)s - %(module)s - %(funcName)s - %(levelname)s: %(message)s'
        ) # Set formatter

        self.create_logfile() # Create log file
        self.set_handler() # Create handler

        self.log.setLevel('DEBUG') # Set level

    def create_logfile(self):
        """
        Create log file and store path
        """
        self.path = pro_path + '/log/'
        File_Operation.create_file(self.path)  # Create log file

    def set_handler(self):
        """
        Create handler and set format
        """
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) # Get current time

        """Create FileHandler and StreamHandler"""
        # fh = logging.FileHandler(self.path + current_time + '.log', encoding='utf-8')
        sh = logging.StreamHandler()
        qh = logging.handlers.QueueHandler(Q)
        rt = logging.handlers.RotatingFileHandler(
            filename=self.path + current_time + '.log',
            maxBytes=50 * 1024 * 1024,
            backupCount=10,
            encoding='utf-8'
        )

        """Set formatter of handler"""
        # fh.setFormatter(self.log_format)
        sh.setFormatter(self.log_format)
        qh.setFormatter(self.log_format)
        rt.setFormatter(self.log_format)

        """Add handler to logger"""
        # self.log.addHandler(fh)
        self.log.addHandler(sh)
        self.log.addHandler(qh)
        self.log.addHandler(rt)

        listener = logging.handlers.QueueListener(qh, sh, rt)

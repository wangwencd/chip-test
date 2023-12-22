# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/9/5 8:48
File: result_output.py
"""
import os
import time
import numpy as np

class Result_Output:

    @staticmethod
    def to_csv(data, path=None, name=None, header='', length='6'):
        """
        Output result data into a csv file

        Args:
            data: Data info
            path: Saving path, project path would be used if path don't exist
            header: Header info, using to generate column name
            length: Result saving length
        """
        fmt = '%.' + str(length) + 'f'
        if name is None:
            current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())  # Get current time

            if path == None: # If there is no path
                np.savetxt(
                    os.getcwd() + '/' + current_time + '.csv',
                    data,
                    fmt=fmt,
                    delimiter=',',
                    header=header,
                    comments=''
                )

            else: # If there is a path
                np.savetxt(
                    path + '/' + current_time + '.csv',
                    data,
                    fmt=fmt,
                    delimiter=',',
                    header=header,
                    comments=''
                )

        else:

            if path == None: # If there is no path
                np.savetxt(
                    os.getcwd() + '/' + name + '.csv',
                    data,
                    fmt=fmt,
                    delimiter=',',
                    header=header,
                    comments=''
                )

            else: # If there is a path
                np.savetxt(
                    path + '/' + name + '.csv',
                    data,
                    fmt=fmt,
                    delimiter=',',
                    header=header,
                    comments=''
                )

    @staticmethod
    def to_bin(data, path=None):
        """"""

    @staticmethod
    def to_png(plt, path, name=None):
        if name is None:
            current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())  # Get current time

            if path is None:  # If there is no path
                plt.savefig(
                    os.getcwd() + '/' + current_time + '.png'
                )

            else:  # If there is a path
                plt.savefig(
                    path + '/' + current_time + '.png'
                )

        else:
            if path is None:  # If there is no path
                plt.savefig(
                    os.getcwd() + '/' + name + '.png'
                )

            else:  # If there is a path
                plt.savefig(
                    path + '/' + name + '.png'
                )

    @staticmethod
    def to_ini(data, path=None, name=None):

        if name is None:
            current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())  # Get current time

            if path is None:  # If there is no path
                with open(os.getcwd() + '/' + current_time + '.ini', 'w') as cfg:
                    data.write(cfg)

            else:  # If there is a path
                with open(path + '/' + current_time + '.ini', 'w') as cfg:
                    data.write(cfg)

        else:
            if path is None:  # If there is no path
                with open(os.getcwd() + '/' + name + '.ini', 'w') as cfg:
                    data.write(cfg)

            else:  # If there is a path
                with open(path + '/' + name + '.ini', 'w') as cfg:
                    data.write(cfg)



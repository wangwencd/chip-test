import os
import sys
import logging
import time
import Serial_Operation
import threading
import serial
import serial.tools.list_ports

PBCorelog = logging.getLogger("PBlog")
Stm_log = logging.getLogger("Stm_log")
natrium_log = logging.getLogger("natrium_log")
STMLog_stop_event = threading.Event()
natrium_log_stop_event = threading.Event()
Stm32_com = 'Stm32_COM'
CH340_com = 'CH340_COM'

logdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')

PBCorelog_file = os.path.join(logdir, 'PBCorelog.txt')
PBhandler = logging.FileHandler(PBCorelog_file)
PBformatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s\n')
PBhandler.setFormatter(PBformatter)
PBCorelog.addHandler(PBhandler)
PBhandler.terminator = ''
PBCorelog.setLevel(logging.DEBUG)

STMlog_file = os.path.join(logdir, 'STMlog.txt')


def com_Stmlog_receive(stop_event, file):
    handler = logging.FileHandler(file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    Stm_log.addHandler(handler)
    handler.terminator = ''
    Stm_log.setLevel(logging.DEBUG)
    Stm_log.debug("\r\n**********start*************\r\n")
    while not stop_event.is_set():
        try:
            rx_buf = ''
            rx_buf = Serial_Operation.Stm32_COM.read()  # 转化为整型数字
            if rx_buf != b'':
                time.sleep(0.01)
                rx_buf = rx_buf + Serial_Operation.Stm32_COM.read_all()
                Stm_log.error(rx_buf.decode())
                print(rx_buf.decode())
        except:
            Stm_log.error("Stm32_COM read error")
            print("Stm32_COM read error")
        time.sleep(0.01)
    Serial_Operation.Stm32_COM.close()


def com_natrium_log_receive(stop_event, file, lable):
    handler = logging.FileHandler(file)
    formatter = logging.Formatter('')
    handler.setFormatter(formatter)
    natrium_log.addHandler(handler)
    natrium_log.setLevel(logging.DEBUG)
    natrium_log.info(lable)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    handler.terminator = ''
    natrium_log.addHandler(handler)
    natrium_log.setLevel(logging.DEBUG)
    while not stop_event.is_set():
        try:
            rx_buf = ''
            rx_buf = Serial_Operation.CH340_COM.read()  # 转化为整型数字
            if rx_buf != b'':
                time.sleep(0.02)
                rx_buf = rx_buf + Serial_Operation.CH340_COM.read_all()
                natrium_log.info(rx_buf.decode())
                print(rx_buf.decode())
        except:
            natrium_log.error("CH340_COM read error")
            print("CH340_COM read error")
        # time.sleep(0.01)
    natrium_log.removeHandler(handler)
    Serial_Operation.CH340_COM.close()


def STMLOG_Init(file=STMlog_file):
    Serial_Operation.serial_open(Stm32_com)
    if Stm32_com in Serial_Operation.check_comlist():
        t1 = threading.Thread(target=com_Stmlog_receive, args=(STMLog_stop_event, file,))
        Serial_Operation.com_flush(Stm32_com)
        STMLog_stop_event.clear()
        t1.start()


def STMLOG_DeInit():
    Serial_Operation.serial_close(Stm32_com)
    STMLog_stop_event.set()


def Natrium_Log_Init(file, lable):
    Serial_Operation.serial_open(CH340_com)
    if CH340_com in Serial_Operation.check_comlist():
        t2 = threading.Thread(target=com_natrium_log_receive, args=(natrium_log_stop_event, file,
                                                                    lable,))
        Serial_Operation.com_flush(CH340_com)
        natrium_log_stop_event.clear()
        t2.start()


def Natrium_Log_DeInit():
    Serial_Operation.serial_close(CH340_com)
    natrium_log_stop_event.set()

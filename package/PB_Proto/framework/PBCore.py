# -*- coding: utf-8 -*-
import time
import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'framework'))
import I2C_Core
import GPIO_Core
import PRINTF_pb2
import SPI_Core

import Serial_Operation
import PB_Log

Link_com = 'Link_COMM'

pb_magic = 254
start_magic = pb_magic.to_bytes(1, "big")
end_num = 255
end_type = end_num.to_bytes(1, "big")
proto_type_dict = {'Print': 0, 'I2C_Proto': 1, 'GPIO_Proto': 2, 'SPI_Proto': 3, 'SYSTEM_RESET': 42, 'Standby_GO': 100,
                   'Standby_DONE': 101}

proto_pack_dict = {0: 'Print_pack', 1: 'I2C_Proto_pack', 2: 'GPIO_Proto_pack', 3: 'SPI_Proto_pack', 42: 'SYSTEM_RESET_pack',
                   100: 'Standby_GO_pack'}
proto_unpack_dict = {0: 'Print_unpack', 1: 'I2C_Proto_unpack', 2: 'GPIO_Proto_unpack', 3: 'SPI_Proto_unpack', 42: 'SYSTEM_RESET_unpack',
                     100: 'Standby_GO_unpack'}

standby_buf = b'\xfe\x01\x00\x0e\x08\x01\x10\x08\x18\x01 \x02(20\x008\x05\xff\xff'
DelayMs = 333


def check_dir(path, indicate):
    if os.path.basename(path).lower() == indicate:
        return path
    if os.path.dirname(path) == path:
        return ''
    return check_dir(os.path.dirname(path),indicate)


def Standby_GO_pack(buf):
    DelayByte = DelayMs.to_bytes(4, 'big')
    buf = DelayByte + standby_buf
    return buf


def Standby_GO_unpack(buf):
    return buf


def SYSTEM_RESET_pack(**kwargs):
    return bytes(0)


def SYSTEM_RESET_unpack(buf):
    return buf


def Print_unpack(buf):
    pb_info = PRINTF_pb2.PRINTF()
    pb_info.ParseFromString(buf)
    return pb_info


def setprintfmesg(mesg):
    mesg.test_num = 40
    return mesg


def Print_pack(**kwargs):
    PRINTF_in = PRINTF_pb2.PRINTF()
    PRINTF_message = setprintfmesg(PRINTF_in)
    return PRINTF_message.SerializeToString()


def GPIO_Proto_unpack(buf):
    return GPIO_Core.GPIO_Proto_unpack_core(buf)


def GPIO_Proto_pack(**kwargs):
    return GPIO_Core.GPIO_Proto_pack_core(**kwargs)


def I2C_Proto_unpack(buf):
    return I2C_Core.I2C_Proto_unpack_core(buf)


def I2C_Proto_pack(**kwargs):
    return I2C_Core.I2C_Proto_pack_core(**kwargs)


def SPI_Proto_unpack(buf):
    return SPI_Core.SPI_Proto_unpack_core(buf)


def SPI_Proto_pack(**kwargs):
    return SPI_Core.SPI_Proto_pack_core(**kwargs)


def package_proto_frame(prto_buf, pb_type, buf_size):
    proto_info_t = start_magic + pb_type.to_bytes(1, 'big') + buf_size.to_bytes(2, "big") + prto_buf + 2 * end_type
    return proto_info_t


def receive_and_unpack_mesg(buf):
    magic = buf[0]
    # print(datasize)
    # print(len(data))
    if magic != pb_magic:
        # print(buf)
        return
    ptype = buf[1]
    datasize = int.from_bytes(buf[2:4], "big")
    data = buf[4:datasize + 4]
    unpack = globals()[proto_unpack_dict.get(ptype)](data)
    return unpack


def pack_and_send_mesg(**kwargs):
    pbtype = proto_type_dict.get(kwargs.get("proto_type"))
    proto_buf = globals()[proto_pack_dict.get(pbtype)](**kwargs)
    proto_frame = package_proto_frame(proto_buf, proto_type_dict.get(kwargs.get("proto_type")), len(proto_buf))
    # print(len(proto_frame))
    # print(proto_frame)
    Serial_Operation.Link_COMM.write(proto_frame)


async def com_receive():
    start_time = time.time()
    while True:
        try:
            rx_buf = ''
            rx_buf = Serial_Operation.Link_COMM.read()  # 转化为整型数字
            if rx_buf != b'':
                #await asyncio.sleep(0.01)
                rx_buf = rx_buf + Serial_Operation.Link_COMM.read_all()
                # print(rx_buf)
                # print(len(rx_buf))
                return receive_and_unpack_mesg(rx_buf)
            # await asyncio.sleep(0.001)
        except:
            pass
        if time.time() - start_time > 0.05:
            print("get Link_COMM data timeout")
            PB_Log.PBCorelog.error("get Link_COMM data timeout")
            return -1


def COMM_Init():
    Serial_Operation.serial_open(Link_com)


def COMM_DeInit():
    Serial_Operation.serial_close(Link_com)


def check_comlist():
    return Serial_Operation.check_comlist()


def com_flush(com):
    Serial_Operation.com_flush(com)
    pass

def com_transimit_read(**kwargs):
    com_flush(Link_com)
    event = com_receive()
    loop = asyncio.get_event_loop()
    task = loop.create_task(event)
    pack_and_send_mesg(**kwargs)
    loop.run_until_complete(task)
    #print(task.result())
    return task.result()

def com_transimit_write(**kwargs):
    pack_and_send_mesg(**kwargs)


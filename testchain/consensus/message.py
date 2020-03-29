""" message.py

This file defines the structure and methods of class Message.
"""

__all__ = ["Message", "JoinMessage", "ReJoinMessage", "SyncMessage", "ReSyncMessage", "QuitMessage"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


from testchain.data.block import *
import json
import struct
import time


class Message:
    def __init__(self, msg_type: str='null'):
        self.dict = {
            'type': msg_type,
            'timestamp': time.time()
        }
        return

    def update_dict(self, key: str, value):
        self.dict.update({key: value})
        return 

    def to_bytes(self):
        return struct.pack('!s', json.dumps(self.dict))

    @staticmethod
    def to_message(msg_bytes: bytes):
        obj = json.loads(struct.unpack('!s', msg_bytes))
        msg = Message()
        for (key, value) in obj.items():
            msg.update_dict(key, value)
        return msg


class JoinMessage(Message):
    def __init__(self):
        super(JoinMessage, self).__init__('join')
        return


class ReJoinMessage(Message):
    def __init__(self, size: int, blk_hash: str):
        super(ReJoinMessage, self).__init__('re_join')
        self.update_dict('size', size)
        self.update_dict('blk_hash', blk_hash)
        return


class SyncMessage(Message):
    def __init__(self, blk_id: int):
        super(SyncMessage, self).__init__('sync')
        self.update_dict('blk_id', blk_id)
        return


class ReSyncMessage(Message):
    def __init__(self, blk: Block):
        super(ReSyncMessage, self).__init__('re_sync')
        self.update_dict('blk', blk)
        return


class QuitMessage(Message):
    def __init__(self):
        super(QuitMessage, self).__init__('quit')
        return

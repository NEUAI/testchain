""" block.py

This file defines the structure and methods of class Block.
"""


__all__ = ["Block"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


from testchain.data.transaction import *
import hashlib
import struct
import time


class Block:
    def __init__(self, prev_block):
        self.id = prev_block.id + 1
        self.prev_hash = prev_block.hash()
        self.nonce = 0
        self.timestamp = 0
        self.txs = []
        return

    def to_bytes(self):
        self.timestamp = time.time()
        ret = struct.pack('!l64sldl', self.id, self.prev_hash, self.nonce, self.timestamp, len(self.txs))
        for tx in self.txs:
            ret += tx.to_bytes()
        return ret

    def hash(self):
        return hashlib.sha256().update(self.to_bytes()).hexdigest()

    def append_tx(self, tx: Transaction):
        self.txs.append(tx)
        return

    @staticmethod
    def to_block(tx_bytes: bytes):

        return

    def __del__(self):
        for tx in self.txs:
            del tx
        return

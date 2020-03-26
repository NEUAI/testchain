""" block.py

This file defines the structure and methods of class Block.
"""


__all__ = ["Block"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


from testchain.data.transaction import *
import struct


class Block:
    def __init__(self, prev_block):
        self.id = prev_block.id + 1
        self.prev_hash = prev_block.hash()
        self.txs = []
        self.nonce = 0
        self.timestamp = 0
        return

    def to_bytes(self):
        return

    def hash(self):
        return

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

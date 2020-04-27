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
    def __init__(self, blk_id: int, prev_hash: str, timestamp: float=0):
        self.id = blk_id
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.txs = []
        return

    def to_bytes(self):
        self.timestamp = time.time()
        ret = struct.pack('!Q64sdQ', self.id, self.prev_hash, self.timestamp, len(self.txs))
        for tx in self.txs:
            ret += tx.to_bytes()
        return ret

    def hash(self):
        return hashlib.sha256().update(self.to_bytes()).hexdigest()

    def append_tx(self, tx: Transaction):
        self.txs.append(tx)
        return

    @staticmethod
    def to_block(blk_bytes: bytes):
        (blk_id, prev_hash, timestamp, txs_len) = struct.unpack('!Q64sdQ', blk_bytes[0:88])
        blk = Block(blk_id, prev_hash, timestamp)
        for i in range(txs_len):
            blk.append_tx(Transaction.to_transaction(blk_bytes[88+i*16:88+(i+1)*16]))
        return blk

    def __del__(self):
        for tx in self.txs:
            del tx
        return

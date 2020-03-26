""" chain.py

This file defines the structure and methods of class Chain.
"""

__all__ = ["Chain"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'

from testchain.data.block import *


class Chain:
    def __init__(self):
        self.blocks = []
        return

    def append_blk(self, blk: Block):
        self.blocks.append(blk)
        return

    def __del__(self):
        for blk in self.blocks:
            del blk
        return

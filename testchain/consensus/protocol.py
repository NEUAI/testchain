""" protocol.py

This file defines the structure and methods of class Protocol.
"""

__all__ = ["Protocol"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


from testchain.data.chain import *
from testchain.network.p2p import *
import threading


class Protocol(threading.Thread):
    def __init__(self):
        super(Protocol, self).__init__()
        self.chain = Chain()
        self.network = P2P()
        return

    def run(self):

        return

    def handle_msg(self, msg: bytes):

        return

    def __del__(self):
        del self.network
        del self.chain
        return

""" protocol.py

This file defines the structure and methods of class Protocol.
"""

__all__ = ["Protocol"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


from testchain.data.chain import *
from testchain.network.p2p import *
from testchain.consensus.message import *
import threading


class Protocol(threading.Thread):
    def __init__(self):
        super(Protocol, self).__init__()
        self.chain = Chain()
        self.network = P2P()
        return

    def run(self):
        msg = JoinMessage()
        self.network.send(msg.to_bytes())
        del msg
        try:
            while True:
                data, address = self.network.receive()
                self.handle_msg(data, address)
        except KeyboardInterrupt:
            msg = QuitMessage()
            self.network.send(msg.to_bytes())
            del msg
        return

    def handle_msg(self, msg_bytes: bytes, address: str):

        return

    def __del__(self):
        del self.network
        del self.chain
        return

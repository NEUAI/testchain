""" transaction.py

This file defines the structure and methods of class Transaction.
"""


__all__ = ["Transaction"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


import socket
import struct


class Transaction:
    def __init__(self, address_in: str, address_out: str, amount: float):
        self.address_in = address_in
        self.address_out = address_out
        self.amount = amount
        return

    def to_bytes(self):
        return socket.inet_aton(self.address_in) + socket.inet_aton(self.address_out) + struct.pack('>f', self.amount)

    @staticmethod
    def to_transaction(tx_bytes: bytes):
        address_in = socket.inet_ntoa(tx_bytes[0:4])
        address_out = socket.inet_ntoa(tx_bytes[4:8])
        amount = struct.unpack('>f', tx_bytes[8:12])[0]
        return Transaction(address_in, address_out, amount)

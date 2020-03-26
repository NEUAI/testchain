""" p2p.py

This file defines the structure and methods of class P2P.
"""

__all__ = ["P2P"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


import socket


class P2P:
    def __init__(self, port=8000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(('', port))
        self.ip = P2P.get_ip()
        self.ip_table = [self.ip]
        self.port = port
        return

    @staticmethod
    def get_ip():
        return socket.gethostbyname(socket.getfqdn(socket.gethostname()))

    def send(self, data: bytes, address='<broadcast>'):
        self.sock.sendto(data, (address, self.port))

    def receive(self):
        data, address = self.sock.recvfrom(65535)
        while address[0] == self.ip:
            data, address = self.sock.recvfrom(65535)
        return data, address

    def __del__(self):
        self.sock.close()
        return


""" message.py

This file defines the structure and methods of class Message.
"""

__all__ = ["Message"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


class Message:
    def __init__(self):
        self.dict = {}
        return

    def update_dict(self, key: str, value):
        self.dict.update({key: value})
        return 

    def to_bytes(self):
        raise NotImplementedError

    @staticmethod
    def to_message(msg_data):
        raise NotImplementedError

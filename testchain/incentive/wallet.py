""" wallet.py

This file defines the structure and methods of class Wallet.
"""


__all__ = ["Wallet"]
__version__ = '1.0'
__author__ = 'Zhengpeng Ai'


class Wallet:
    def __init__(self, coin: float = 0.0):
        self.coin = coin
        return

    def get_coin(self):
        return self.coin

    def add_coin(self, amount: float):
        self.coin += amount
        return

    def sub_coin(self, amount: float):
        self.coin -= amount
        return

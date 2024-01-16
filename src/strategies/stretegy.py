# -*- coding: utf-8 -*-
'''
Created on: Tues Jan 16 2024
@author: Mohit Raj Rathor
'''

# Base Strategy Module

class Stretegy:
    def __init__(self) -> None:
        """
        Strategy class:
            Blueprint for making strategies.
        """
        self.description = "this is a base moving average crossover Strategy."
        self.
        

    def buy_signal(self)->bool:
        """
        returns True when buying condition is true.
        """
        pass

    def sell_signal(self)->bool:
        """
        returns True when selling condition is true.
        """
        pass

    def exit_signal(self)->bool:
        """
        returns True when exiting condition is true.
        """
        pass

    def add_data(self)->None:
        pass

    def position_sizing(self)->int:
        pass

    def stoploss_traling(self)->float:
        pass

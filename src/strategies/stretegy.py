# -*- coding: utf-8 -*-
'''
Created on: Tues Jan 16 2024
@author: Mohit Raj Rathor
'''

# Base Strategy Module

class Stretegy:
    def __init__(self, description:str="this is a base moving average crossover Strategy.", sl_percent:float=0.25, target:float=1) -> None:
        """
        Strategy class:
            Blueprint for making strategies.
        """
        self.description = description
        self.sl_percent = sl_percent
        self.target = target
        

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
        """
        method to add data for backtesting.
        """
        pass

    def position_sizing(self)->int:
        """
        method to decied position sizing.
        """
        pass


    def stoploss_traling(self)->float:
        """
        method to determine and take action on stoploss trailing.
        """
        pass




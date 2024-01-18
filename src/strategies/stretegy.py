# -*- coding: utf-8 -*-
'''
Created on: Tues Jan 16 2024
@author: Mohit Raj Rathor
'''

# Base Strategy Module

class Stretegy:
    def __init__(self, sl_percent:float=0.25, target:float=1, total_risk:float=5) -> None:
        """
        Strategy class:
            Blueprint for making strategies.

            param: 
                sl_percent -> define stoploss percent. | default = 0.25 %
                target -> define target to get. | default = 1 %
        """
        self.description = "This is a base moving average crossover Strategy."
        self.sl_percent = sl_percent
        self.target = target
        self.total_risk = total_risk
        

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


    def __str__(self):
        return f"Strategy class object\nDescription: {self.description}\nTotal Risk: {self.total_risk}% \nRisk TO Reward: {self.target / self.sl_percent}"

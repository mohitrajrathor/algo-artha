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
                total_risk -> total risk defined on the capital. | default = 5 %
        """
        self.description = "This is a base Strategy class."
        self.sl_percent = sl_percent
        self.target = target
        self.total_risk = total_risk
        

    def buy_signal(self)->bool:
        """
        returns True when buying condition is true.
        """
        print("No buy signal defined may be you are using base strategy class.\nPlease use a defined strategy like MovingAverageCrossover strategy defined in strategy library.")
        return False

    def sell_signal(self)->bool:
        """
        returns True when selling condition is true.
        """
        print("No sell signal defined may be you are using base strategy class.\nPlease use a defined strategy like MovingAverageCrossover strategy defined in strategy library.")
        return False

    def exit_signal(self)->bool:
        """
        returns True when exiting condition is true.
        """
        print("No exit signal defined may be you are using base strategy class.\nPlease use a defined strategy like MovingAverageCrossover strategy defined in strategy library.")
        return False

    def position_sizing(self)->int:
        """
        method to decied position sizing.
        """
        print("No position sizing method defined may be you are using base strategy class.\nPlease use a defined strategy like MovingAverageCrossover strategy defined in strategy library.")
        return 0

    def stoploss_traling(self)->float:
        """
        method to determine and take action on stoploss trailing.
        """
        print("No stoploss trailing defined may be you are using base strategy class.\nPlease use a defined strategy like MovingAverageCrossover strategy defined in strategy library.")
        return 0

    def __str__(self):
        return f"Strategy class object\nDescription: {self.description}\nTotal Risk: {self.total_risk}% \nRisk TO Reward: {self.target / self.sl_percent}"
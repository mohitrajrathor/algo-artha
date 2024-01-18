# -*- coding: utf-8 -*-
"""
created on Sun Jan 14 2024

@author: Mohit Raj Rathor
"""


# libraries required
from strategies.stretegy import Stretegy



# trader class
class Trader:
    def __init__(self) -> None:
        pass


# backTrader class
class BackTest:
    def __init__(self, capital:float=10000, risk:float=5) -> None:
        """
        BackTest class:
            Blueprint for backtesting strategies.
        """
        self.capital = capital
        self.risk = risk
                

    def add_data(self):
        """
        Method to add data for back-testing strategies. 
        """
        pass

    def deploy_strategy(self, strategy:Stretegy):
        """
        Method to add strategy to Backtest instance.
        """
        pass

    def run(self):
        """
        Method to add th
        """
        pass



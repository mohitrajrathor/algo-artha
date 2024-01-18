# -*- coding: utf-8 -*-
'''
created on thus jan 18 2024

@author Mohit Raj Rathor
'''

# library
from strategy import Stretegy, cross_above, cross_below


# Moving Average crossover strategy.

class MovingAverageCrossover(Stretegy):
    """
    Strategy class: MovingAverageCrossover Strategy
    Description: simple moving average crossover strategy that buy when faster moving average crosses slower moving average upside from down, And sell on vice verse.

    params: 
        fastMA (int) -> period of faster moving average. | DEFAULT = 20
        slowMA (int) -> period of slower moving average. | DEFAULT = 50
    """
    def __init__(self,fastMA:int=20, slowMA:int=50, sl_percent: float = 0.25, target: float = 1, total_risk: float = 5) -> None:
        super().__init__(sl_percent, target, total_risk)
        self.fastMA = fastMA
        self.slowMA = slowMA

    def buy_signal(self, fastMA_series, slowMA_series) -> bool:
        '''
        method to generate buying signal.
        '''
        if cross_above(fastMA_series, slowMA_series):
            return True
        else: return False
        
    def sell_signal(self, fastMA_series, slowMA_series) -> bool:
        '''
        method to generate selling signal.
        '''
        if cross_below(fastMA_series, slowMA_series):
            return True
        else: return False
        
    def exit_signal(self) -> bool:
        '''
        method to generate exit signal. 
        '''
        pass
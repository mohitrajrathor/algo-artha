"""
created on - Tuesday 07th may 2024
@author: Mohit Raj Rathor
"""

import pandas as pd 
from screener import Screener


#### RSI Momentum Screener
class RSIMomentumScreener(Screener):
    def __init__(self) -> None:
        """
        RSI Momentum Screener:
        Screen stocks on RSI-14 periods and RSI SMA-100 periods as follows 
        if RSI corssed above SMA-100 of RSI-14 and RSI-14 is below 30 in 
        previous 30 periods(or say days) then it is considered as momentum ins this screener.

        
        """
        super().__init__()
        self.info = "RSI Momentum Screener"

    def condition(self, data: pd.DataFrame) -> bool:
        


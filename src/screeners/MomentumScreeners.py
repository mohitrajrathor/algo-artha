# -*- coding: utf-8 -*-
"""
created on wed jan 17 2024
@author: Mohit Raj Rathor
"""

# momentum stocks screener scripts


# import screener class from ./src dir
import pandas as pd
from screener import Screener
import pandas_ta  

# error
class DataNotValid(Exception):
    pass

class MomentumScreener(Screener):
    def __init__(self) -> None:
        super().__init__()

    def get_data(self, symbol: str, days: int = 300, exchange=".NS") -> pd.DataFrame:
        return super().get_data(symbol, days, exchange)

    def condition(self, data: pd.DataFrame) -> bool:
        for col in "open high low close volume".split():
            if col not in data.columns:
                raise DataNotValid("Data Does not valid.")

        data['vol20sma'] = pandas_ta.sma(data['volume'], length=20)
        if not (data['vol20sma'].iloc[-1] < data['volume'].iloc[-1] and data['vol20sma'].iloc[-1] > 100000):
            return False
        
        data['sma20'] = pandas_ta.sma(close=data['close'], length=20)
        data['sma50'] = pandas_ta.sma(close=data['close'], length=50)
        if not (data['sma20'].iloc[-1] > data['sma50'].iloc[-1]):
            return False
        
        data['rsi'] = pandas_ta.rsi(close=data['close'], length=14)
        if not (data['rsi'].iloc[-1] > 50):
            return False
        
        if not (data['close'].iloc[-1] > data['close'].iloc[-2]):
            return False
        
        return True
    
    def screen(self, symbols:list[str]) -> list[str]:
        return super().screen(symbols)
    
        



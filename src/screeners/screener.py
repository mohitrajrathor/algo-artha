# -*- coding : utf-8 -*-
"""
Created on - Mon Jan 01 2024 23:37 IST
@author : Mohit Raj Rathor
"""

# screener class

from pandas.core.api import DataFrame as DataFrame
import yfinance as yf
import pandas as pd 
import pandas_ta
import datetime as dt 
from pprint import pprint
import os


############### utils functions ###############


############### Screeners ###############

#### Basic screener
class Screener:
    def __init__(self) -> None:
        """
        Base class for screeners to show how to make screener.
        Screen stocks on Daily historical data basis.
        """
        pass

        def __str__(self) -> str:
            return f"Screener class\n{self.info}"

    def get_data(self, symbol:str, days:int=300, exchange=".NS") -> pd.DataFrame:
        """
        fatch data from yahoo finance using yfinance.
        param:
            symbol -> symbol of stocks for screening
            days -> no. days data you want to filter
            exchange -> '.NS' for NSE or '.BO' for "BSE".
        return -> pd.DataFrame (
                index -> 'date'
                columns -> ['open', 'high', 'low', 'close', 'adj close', 'volume']
        )
            
        """
        # setting dates
        start_date = (dt.datetime.now() - dt.timedelta(days=days)).strftime("%Y-%m-%d")
        data = yf.download(tickers=symbol+".NS", start=start_date)
        os.system("cls")
        # lowering case
        data.index.name = "date"
        data.columns = data.columns.str.lower()     
        return data
    
    def condition(self, data:pd.DataFrame)->bool:
        """
        Apply condition on given data then return wheather the stock is satisfy given condition or not.
        Default condition -> return True is given stocks data's latest adj. close is above 20 
        exponential moving average.
        param:
            data -> pd.DataFrame
        return: bool
        """
        ema20 = pandas_ta.ema(data['adj close'], length=20)
        if ema20.iloc[-1] <= data['adj close'].iloc[-1]: 
            return True
        else: 
            return False
        
    def screen(self, symbols:list[str])->list[str]:
        """
        Screen stocks using self.get_data and self.condition functions
        param: Nil
        return: list[str] (of filtered stocks)
        """
        screened_sym = []
        for i in symbols:
            if self.condition(self.get_data(i)):
                screened_sym.append(i)
            
        screened_sym = [i.split('.')[0] for i in screened_sym]      # removing .NS from end
        return screened_sym
    


class IntradayScreener(Screener):
    """
    base class for all intraday screener
    """
    def __init__(self, symbols: list[str], info: str = None) -> None:
        super().__init__(symbols, info)

    def fetch_data():
        ...



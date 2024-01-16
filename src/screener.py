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


############### utils functions ###############


############### Screeners ###############

#### Basic screener
class Screener:
    def __init__(self, symbols:list[str] , info:str=None) -> None:
        """
        Base class for screeners to show how to make screener.
        Screen stocks on Daily historical data basis.
        """
        self.symbols = symbols
        if info is None:
            self.info = "Screen stocks from given symbols that are above 20 moving average."
        else:
            self.info = info

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
        
    def screen(self)->list[str]:
        """
        Screen stocks using self.get_data and self.condition functions
        param: Nil
        return: list[str] (of filtered stocks)
        """
        screened_sym = []
        for i in self.symbols:
            if self.condition(self.get_data(i)):
                screened_sym.append(i)
            
        screened_sym = [i.split('.')[0] for i in screened_sym]      # removing .NS from end
        return screened_sym
    
#### previous day's top gainer and looser screener
class Top_gainer_looser_screener(Screener):
    def __init__(self, symbols: list[str], info: str = None) -> None:
        super().__init__(symbols, info)
        self.info = "Screen previous day's top gainer and looser stocks of given list."       # over-write self.info of screenr class


    def get_data(self, symbol:list[str], exchange=".NS") -> DataFrame:
        """
        fatch data from yahoo finance using yfinance.
        param:
            symbol -> symbol of stocks for screening
            exchange -> '.NS' for NSE or '.BO' for "BSE".
        return -> pd.DataFrame (
                index -> 'date'
                columns -> ['open', 'high', 'low', 'close', 'adj close', 'volume']
        )
            NOTE : it will return data of all stocks simultenously
        """
        symbols = [sym+exchange for sym in self.symbols]
        start_date = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y-%m-%d") 
        data = yf.download(tickers=symbols, start=start_date) 
        data = data.stack()      
        data.index.names = ['Date', 'Symbol']
        data = data.reset_index()
        return data
    
    def condition(self, data: DataFrame) -> dict:
        # let's get insights from data
        data['change'] = ((data['Adj Close'] - data['Open']) / data['Open'] * 100).round(2)

        # get the gainers
        gainers = data.sort_values(by=["change"], ascending=False).iloc[:10]['Symbol'].to_list()
        gainers = [i.split('.')[0] for i in gainers]

        # get the loosers
        loosers = data.sort_values(by=["change"], ascending=True).iloc[:10]['Symbol'].to_list()
        loosers = [i.split('.')[0] for i in loosers]

        print()

        result = {
            'gainers' : gainers,
            'looser' : loosers
        }

        return result

    def screen(self) -> dict:
        return self.condition(self.get_data(self.symbols))

class IntradayScreener(Screener):
    """
    base class for all intraday screener
    """
    def __init__(self, symbols: list[str], info: str = None) -> None:
        super().__init__(symbols, info)

    def fetch_data():
        ...

    
# testing 
if __name__ == "__main__":
    """test functioning of the code"""
    ...
# -*- coding: utf-8 -*-
'''
created on wed jan 17 2024

@auther: Mohit Raj Rathor
'''

# bullish screener scripts

from pandas import DataFrame
from screener import Screener
import yfinance as yf
import datetime as dt






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
# screener class

import yfinance as yf
import pandas as pd 
import pandas_ta
import datetime as dt 


class Screener:
    def __init__(self, symbols:list[str] , info:str=None) -> None:
        """
        Base class for screeners to show how to make screener.
        Screen stocks on Daily historical data basis.
        """
        self.symbols = symbols
        if info is None:
            self.info = "Base screener class"
        else:
            self.info = info

    def get_data(self, symbol:str, days:int = 300) -> pd.DataFrame:
        """
        fatch data from yahoo finance using yfinance.
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
            
        return screened_sym
    

class Top_gainer_looser_screener(Screener):
    def __init__(self, symbols: list[str], info: str = None) -> None:
        super().__init__(symbols, info)


class tp:
    def __init__(self) -> None:
        print(self)


    
# testing 
if __name__ == "__main__":
    any = tp()

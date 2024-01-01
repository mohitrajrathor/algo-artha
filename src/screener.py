# screener class

import yfinance as yf
import pandas as pd 
import pandas_ta


class Screener:
    def __init__(self, symbols:list[str] , info:str=None) -> None:
        """
        Base class for screeners
        """
        self.symbols = symbols
        if info is None:
            self.info = "Base screener class"
        else:
            self.info = info

    def get_data(self, symbol:str) -> pd.DataFrame:
        """
        fatch data from yahoo finance using yfinance.
        return -> pd.DataFrame (
                index -> 'date'
                columns -> ['open', 'high', 'low', 'close', 'adj close', 'volume']
        )
            
        """
        data = pd.DataFrame(symbol)
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
        pass

    

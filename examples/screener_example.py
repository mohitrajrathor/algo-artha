# example program to create a momentum screener

# import screener class from ./src dir
import pandas as pd
import sys
sys.path.append('./src/')
from screeners.screener import Screener
import pandas_ta
from pprint import pprint                    # for better data view.

# error
class DataNotValid(Exception):
    pass


# now make a momentum screener using base Screener class bluprint.
# and we can also use pre defined data fatching method created in it.
class MomentumScreener(Screener):
    def __init__(self) -> None:
        super().__init__()

    def get_data(self, symbol: str, days: int = 300, exchange=".NS") -> pd.DataFrame:
        return super().get_data(symbol, days, exchange)

    # we need to change the conditions for momentum screener.
    def condition(self, data: pd.DataFrame) -> bool:
        # validate data 
        for col in "open high low close volume".split():
            if col not in data.columns:
                raise DataNotValid("Data Does not valid.")
        
        # condition 01: volume should be above 20 sma
        data['vol20sma'] = pandas_ta.sma(data['volume'], length=20)
        if not (data['vol20sma'].iloc[-1] < data['volume'].iloc[-1] and data['vol20sma'].iloc[-1] > 100000):
            return False
        
        # condtion 02: 20 sma should be above 50 sma
        data['sma20'] = pandas_ta.sma(close=data['close'], length=20)
        data['sma50'] = pandas_ta.sma(close=data['close'], length=50)
        if not (data['sma20'].iloc[-1] > data['sma50'].iloc[-1]):
            return False
        
        # condtion 03: rsi-14 should be above 50
        data['rsi'] = pandas_ta.rsi(close=data['close'], length=14)
        if not (data['rsi'].iloc[-1] > 50):
            return False
        

        # condition 04: should be close above previous day's high
        if not (data['close'].iloc[-1] > data['close'].iloc[-2]):
            return False
        
        return True
    

    # let's add screen func.
    def screen(self, symbols:list[str]) -> list[str]:
        return super().screen(symbols)
    
    # now all set.


# let's test it 
    
if __name__ == "__main__":
    nifty200 = pd.read_csv("./data/nifty_200.csv")['Symbol'].to_list()
    momentum_screener = MomentumScreener()

    pprint(momentum_screener.screen(nifty200))


        



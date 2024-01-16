# -*- coding: utf-8 -*-
"""
Creaded on Mon Jan 01 06:14:00 2024

@auther: Mohit Raj Rathor
"""
# intraday live alert script.


# libraries uesd
from shoonya.api_helper import ShoonyaApiPy
import yaml
import os
from pprint import pprint
import pyotp
from utils import *
import pandas as pd
import datetime as dt 
from screener import Top_gainer_looser_screener
import warnings
warnings.filterwarnings(action="ignore")        # ignore warnings.


############# Constants ##############
DATA_DIR = './data/'
SD_DIR = './screend_data/'              # directory to store screened data.


############### Variables ###############
bullish_stocks = []
bearish_stocks = []
rsi_below_30 = []
rsi_above_70 = []
all_stocks_to_watch = []

############### functions ###############

# live data fatching and prepossesing using BROKER API
def fatch_live_data(sym, days=5, interval:str = "5") -> pd.DataFrame:
    start_time = (dt.datetime.now() - dt.timedelta(days=5)).timestamp()
    ret = api.get_time_price_series(
        exchange="NSE", 
        token=str(nse_master['Token'].loc['SBIN']),
        starttime=start_time, interval=interval
    )
    data = pd.DataFrame(ret)
    data.columns = [
        'stat',
        'time',
        'ssboe',
        'open',
        'high',
        'low',
        'close',
        'vwap',
        'intvolume',
        'oi',
        'v',
        'oi'
    ]
    data = data.set_index("time")
    return data

# track 5 min high crossover
def _5_min_high_breakout(symlist:list[str]) -> None:
    for sym in symlist:
        data = fatch_live_data(sym=sym, days=5, interval=5)
        last_close = float(data['close'].iloc[0])
        prev_close = float(data['close'].iloc[1])
        _5_min_high = float(data['high'].loc[dt.datetime.now().strftime("%d-%m-%Y 09:15:00")])
        if prev_close <= _5_min_high < last_close:
            # displaying to terminal and notifying about alert.
            display_bullish_alert(sym=sym, msg="5 Minute HIGH breakout !", time=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            notify(
                title="5 Minute HIGH Breakout",
                msg=f"Symbol - {sym}\n\
                    trading @{last_close}",
                time=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            )
    
    print("Scan complete at", Colors.YELLOW+dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+Colors.END)

# 5 min low breakout
def _5_min_low_breakout(symlist:list[str]) -> None:
    for sym in symlist:
        data = fatch_live_data(sym=sym, days=5, interval=5)
        last_close = float(data['close'].iloc[0])
        prev_close = float(data['close'].iloc[1])
        _5_min_low = float(data['low'].loc[dt.datetime.now().strftime("%d-%m-%Y 09:15:00")])
        if prev_close >= _5_min_low > last_close:
            # displaying to terminal and notifying about alert.
            display_bullish_alert(sym=sym, msg="5 Minute LOW breakout !", time=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            notify(
                title="5 Minute LOW Breakout",
                msg=f"Symbol - {sym}\n\
                    trading @{last_close}",
                time=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            )
    
    print("Scan complete at", Colors.YELLOW+dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+Colors.END)


# 1 HOUR RSI is above 70 OR below 30.
def rsi_alert(symlist:list[str]) -> list:
    ...







############# PRE-REQUIRED THING SETUP #############

# defining api object & login
api = ShoonyaApiPy()

# Now login 
with open("./config/cred.yml") as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)            # fatching login credentials

try:
    ret = api.login(
        userid=cred['user'],
        password=cred['pwd'],
        twoFA=pyotp.TOTP(cred['totptoken']).now(),
        vendor_code=cred['vc'],
        api_secret=cred['apikey'],
        imei=cred['imei']
    )
except Exception as e:
    print("Error :", e)
    exit()
else:
    print("----> Successfully login")
    

################## Data Preparation ###################

nse_master = pd.read_csv(DATA_DIR+'shoonya_masters/NSE_symbols.txt', index_col="Symbol")     # NSE master file   
nifty_200 = pd.read_csv(DATA_DIR+"nifty_200.csv")['Symbol'].to_list()                        # nifty 200 stocks list

# Display progress
print(f"----> Data prepared successfully.")



##### ----> selecting stocks to watch:
# ----> Last day's top gainers and Loosers
gl_screener = Top_gainer_looser_screener(nifty_200)
gl_stocks = gl_screener.screen()        # this will return a list

# append screened stocks to pre-defined list
bullish_stocks.extend(gl_stocks['gainers'])     
bearish_stocks.extend(gl_stocks['gainers'])

# display success msg
print("----> Previous day's top gainer and looser fatched.")

# |||| ADD MORE SCREENER BELOW |||| #


# ----> Add all screened stocks to all_stocks_to_watch
all_stocks_to_watch.extend(bullish_stocks)
all_stocks_to_watch.extend(bearish_stocks)


########## MAIN-LOOP ##########
count = 1
while True:
    # first of all remove all the text from the terminal to display efficiently.
    os.system("cls")



    # now printing the previous day's top gainer and loosers
    print(Colors.GREEN+ "Gainer:" +Colors.END,"\t",Colors.RED+ "Looser:" +Colors.END)
    print("-"*50)

    for gainer, looser in zip(bullish_stocks, bearish_stocks):
        print(Colors.GREEN+ gainer +Colors.END,"\t",Colors.RED+ looser +Colors.END)




    print("Loop no:", count)
    count += 1
    if cross_time(tg_time=dt.datetime.now().strftime("%Y-%m-%d 09:20:00")) and not cross_time(tg_time=dt.datetime.now().strftime("%Y-%m-%d 11:30:00")):
        # scan for 5 min high breakout
        print("starting 5 min high breakout scan ...")
        _5_min_high_breakout(bullish_stocks)

        # scan for 5 min low breakout
        print("starting 5 min low breakout scan ...")
        _5_min_low_breakout(bearish_stocks)
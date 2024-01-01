# -*- coding: utf-8 -*-
"""
Creaded on Mon Jan 01 06:14:00 2024

@auther: Mohit Raj Rathor
"""
# intraday live alert script.


from shoonya.api_helper import ShoonyaApiPy
import yaml
from pprint import pprint
import pyotp
from utils import *
import pandas as pd
import time
import datetime as dt 


############# Constants ##############
DATA_DIR = './data/'
SD_DIR = './screend_data/'              # directory to store screened data.


############# functions #############



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
    print("sussefully login")
    

################## Data Preparation ###################

# preparing list of symbols for consistently data fatching.
refreshed = refresh_shoonya_symbols_files()         # before that let's refresh the token symbols list provided by shoonya.

if not refreshed:
    terminate(reason="master file can't refreshed cause error in future, terminating program!")

nse_master = pd.read_csv(DATA_DIR+'shoonya_masters/NSE_symbols.txt', index_col="Symbol")       

# reading nifty-200 symbols list
nifty_200 = pd.read_csv(DATA_DIR+"nifty_200.csv")['Symbol'].to_list()


# stocks to watch
watchlist = nifty_200               # this watchlist will be used to screen data.



################# Screening pre-open market's top gainer and looser ################


################# Tracking 5 min breakout stocks #################
def is_5_min_breakout(sym:str)->bool:
    curr_time = dt.datetime.now()
    start = curr_time - dt.timedelta(days=5)
    ret = api.get_time_price_series(
        exchange="NSE", token=str(nse_master['Token'].loc[sym]), 
        starttime=start.timestamp(), 
        interval="5" 
    )
    data = pd.DataFrame(ret)
    _5_min_high = float(data[data['time'] == "01-01-2024 09:15:00"]['intc'])
    curr_close = float(data['intc'].loc[0])
    prev_close = float(data['intc'].loc[1])
    if prev_close < _5_min_high < curr_close:
        return True
    else: return False
    


def crossed_5_min_high():
    for i in watchlist:
        if is_5_min_breakout(i):
            display_bullish_alert(sym=i, msg="5 Minute Breakout", d_time=dt.datetime.now())

################# MAIN LOOP ################## 
while True : 
    if cross_time("2024-01-01 09:20:00"):
        crossed_5_min_high()
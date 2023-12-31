# intraday live alert script.
from shoonya.api_helper import ShoonyaApiPy
import yaml
from pprint import pprint
import pyotp
from utils import *
import pandas as pd

############# Constants ##############
DATA_DIR = './data/'
SD_DIR = './screend_data/'              # directory to store screened data.

############# PRE-REQUIRED THING SETUP #############

# defining api object & login
api = ShoonyaApiPy()

def login(cred:dict) -> str:
    """
    Login to Shoonya api
    params
        cred -> Dict containing credential data of the shoonya api.
    return -> response fatch from shoonya or None (if some error occured).    
    """
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
        return None
    else:
        return ret
    
    
# Now login 
    
with open("./config/cred.yml") as f:
    cred_data = yaml.load(f, Loader=yaml.FullLoader)            # fatching login credentials

response = login(cred_data)

# pprint(response)

################## Data Preparation ###################

# preparing list of symbols for consistently data fatching.
refreshed = refresh_shoonya_symbols_files()         # before that let's refresh the token symbols list provided by shoonya.

if not refreshed:
    terminate(reason="master file can't refreshed cause error in future, terminating program!")

nse_master = pd.read_csv(DATA_DIR+'shoonya_master/NSE_symbols.txt', index_col="Symbol")       

# reading nifty-200 symbols list
nifty_200 = pd.read_csv(DATA_DIR+"nifty_200.csv")['Symbol'].to_list()



################# Screening pre-open market's top gainer and looser ################

# python file for handling trading logices.
from broker_api.shoonya import *
import logging
import yaml
from pyotp import TOTP

class Trader:
    def __init__(self, api:Api) -> None:
      self.api = api


if __name__ == "__main__":
    from pprint import pprint
    import datetime as dt



    api = Api()
    nse_trader = Trader(api=api)
    with open("./configs/shoonya_api_configs.yaml", 'r') as api_config:
       cred = yaml.safe_load(api_config)

    # login 
    nse_trader.api.login(
       userid=cred['userId'],
       password=cred['password'],
       twoFA=TOTP(cred['twoFA']).now(),
       vendor_code=cred['vendorCode'],
       api_secret=cred['apiSecret'],
       imei=cred['imei']
    )

    enddate = dt.datetime.today()
    startdate = enddate - dt.timedelta(days=20)
    ret=api.get_daily_price_series(exchange="NSE",tradingsymbol="PAYTM-EQ",startdate=startdate.timestamp() ,enddate=enddate.timestamp())

    print(ret)
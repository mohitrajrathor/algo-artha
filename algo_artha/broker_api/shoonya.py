# python file to handle shoonya api functionality
import requests
import zipfile
import os
import io
import logging
from NorenRestApiPy.NorenApi import NorenApi
import concurrent.futures



# constants
ROOT_URL = 'https://api.shoonya.com/'

# functions
def download_masters(path:str='')-> None:
    """
    Method to find master scripts provided by shoonya.
    Master Files these files contains security infomation.
    """
    MASTER_FILES = [
        'NSE_symbols.txt.zip',
        'NFO_symbols.txt.zip',
        'CDS_symbols.txt.zip',
        'MCX_symbols.txt.zip',
        'BSE_symbols.txt.zip',
        'BFO_symbols.txt.zip',
        'NCX_symbols.txt.zip'
    ]
    for file in MASTER_FILES:
        logging.info(f"downloading {file}...")
        url = ROOT_URL + file
        r = requests.get(url, allow_redirects=True)
        with io.BytesIO() as ziph:
            ziph.write(r.content)
            try:
                with zipfile.ZipFile(ziph) as z:
                    z.extractall(path=path)
                    logging.info(f"{file} donwloaded.")
            except:
                logging.warning("Invalid file.")
    logging.info("files download.")
                    
class Order:
     def __init__(self, buy_or_sell:str=None, product_type:str=None,
                 exchange:str=None, tradingsymbol:str=None, 
                 price_type:str=None, quantity:int=None, 
                 price:float=None, trigger_price:float=None, discloseqty:int=0,
                 retention:str='DAY', remarks:str="tag",
                 order_id:str=None):
        self.buy_or_sell=buy_or_sell
        self.product_type=product_type
        self.exchange=exchange
        self.tradingsymbol=tradingsymbol
        self.quantity=quantity
        self.discloseqty=discloseqty
        self.price_type=price_type
        self.price=price
        self.trigger_price=trigger_price
        self.retention=retention
        self.remarks=remarks
        self.order_id=None


# class to handle api object
class Api(NorenApi):
    def __init__(self) -> None:
        NorenApi.__init__(self, host=ROOT_URL+'NorenWClientTP/', websocket=ROOT_URL+'NorenWSTP/')
        global api
        api = self

    def place_basket(self, orders):
        resp_err = 0
        resp_ok  = 0
        result   = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_url = {executor.submit(self.place_order, order): order for order in  orders}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
            try:
                result.append(future.result())
            except Exception as exc:
                print(exc)
                resp_err = resp_err + 1
            else:
                resp_ok = resp_ok + 1

        return result
                
    def placeOrder(self,order: Order):
        ret = NorenApi.place_order(self, buy_or_sell=order.buy_or_sell, product_type=order.product_type,
                            exchange=order.exchange, tradingsymbol=order.tradingsymbol, 
                            quantity=order.quantity, discloseqty=order.discloseqty, price_type=order.price_type, 
                            price=order.price, trigger_price=order.trigger_price,
                            retention=order.retention, remarks=order.remarks)

        return ret
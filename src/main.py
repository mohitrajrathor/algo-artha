# app program
from shoonya.api_helper import ShoonyaApiPy
import yaml
from pprint import pprint
import pyotp

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

pprint(response)
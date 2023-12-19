# app program
from shoonya.api_helper import ShoonyaApiPy
import yaml
from pprint import pprint
import pyotp

# defining api object & login
api = ShoonyaApiPy()

with open("./config/cred.yml") as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    # pprint(cred)

ret = api.login(
    userid=cred['user'],
    password=cred['pwd'],
    twoFA=pyotp.TOTP(cred['totptoken']).now(),
    vendor_code=cred['vc'],
    api_secret=cred['apikey'],
    imei=cred['imei']
)

print("totp : ", pyotp.TOTP(cred['totptoken']).now())
print("printing response : ")
# pprint(ret)

pprint(api.get_holdings())



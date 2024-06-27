# python file for handling trading logices.
from broker_api.shoonya import *
import logging

# initialization
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class Trader:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    download_masters('./data/shoonya/')
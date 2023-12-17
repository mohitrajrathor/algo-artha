# Auther - Mohit Raj Rathor
# python file to create and store screeners from base screener class.

import pandas as pd

class Scanner:
    def __init__(self, data:pd.DataFrame) -> None:
        """
        base screener class
            params : 
                data -> pandas datframe consist ["time", "open", "high", "low", "close", "volume"]

        """
        self.data = data

    def scan_result(self) -> pd.DataFrame:
        pass 
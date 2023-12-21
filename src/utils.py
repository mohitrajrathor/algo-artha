# python class for wirting utility functions.
import requests
import zipfile
import os

# color codes used for terminals.
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"



def display_status() -> None:
    """
    display status of the application in the format like it 
Connection-Status - <Active or Inactive>          Time - <hh:mm:ss dd-MM-yyyy | None>
username : <Name in >
user-id : <user id>
    """
    format = "Connection-Status - "+



def refresh_shoonya_symbols_files() -> None:
    """
    function to fatch all the masters files povided by shoonya api.
    """

    # exchanges - list 
    exchanges = ['NSE', 'NFO', 'CDS', 'MCX', 'BSE', 'BFO']

    for exch in exchanges:
        print(f"Downloading {Colors.BLUE}{exch}_symbols.txt{Colors.END} ")
        response = requests.get(f"https://api.shoonya.com/{exch}_symbols.txt.zip")
        open("temp.zip", "wb+").write(response.content)         # writing zip file. 
        try:
            with zipfile.ZipFile("temp.zip") as z:              # extracting zip_file
                z.extractall("./data/shoonya_symbols/")
        except:
            print("    "+Colors.RED+f"Error : Invalid File '{exch}_symbols.txt'"+Colors.END)

        os.remove("temp.zip")          # removing temp.zip file.


if __name__ == "__main__":
    # downloading all shoonya symbol files.
    refresh_shoonya_symbols_files()
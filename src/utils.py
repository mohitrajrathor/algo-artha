# python class for wirting utility functions.
import requests
import zipfile
import os
import time
import datetime as dt
from plyer import notification
import pandas as pd


########## ERRORS ##########

class MisMatchError(Exception):
    """
    raise error when the given list of columns is not equals the stocks list passed.
    """
    pass



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



############### MESSAGE FUNCTIONS ##############

def display_bullish_alert(sym:str,msg:str, time:str=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) -> None:
    message = Colors.YELLOW+f"{time}"+Colors.END+f" : {sym} "+Colors.GREEN+f"{msg}"+Colors.END
    print(message)

def display_bearish_alert(sym:str, msg:str, time:str=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) -> None:
    message = Colors.YELLOW+f"{time}"+Colors.END+f" : {sym} "+Colors.RED+f"{msg}"+Colors.END
    print(message)

# ----> desktop alert function
def notify(title:str, msg:str, time:str)-> None:

    notification.notify(
        title=title+"\nat "+time,
        message=msg,
        timeout=10
    )


def display_screened_stocks(stocks_lists:list[list[str]], columns:list[str], screen_type: str = "") -> None:
    """
    param:
        stocks_list -> list of screend list of stocks
        columns -> list of names of columns
        screen_type -> Either 'bullish' (add green color to the data) or 'bearish' (add red color to the data) or empty string.
    """

    # table creation and header adding
    if len(stocks_lists) != len(columns):
        raise MisMatchError("Numbers of columns does not match with numbers of stocks list given.")
    
    # giving the color code to the data
    if screen_type == "bullish":
        prefix = Colors.GREEN
        sufix = Colors.END
    
    elif screen_type == "bearish":
        prefix = Colors.RED
        sufix = Colors.END

    else:
        prefix = ""
        sufix = ""

    # printing tables
    table = PrettyTable(columns)
    flag = False
    index = 0
    while not flag:
        temp = 0
        temp_list = []
        for lst in stocks_lists:
            try:
                temp_list.append(prefix+lst[index]+sufix)
            except IndexError:
                temp_list.append(" ")
                temp += 1
        
        index += 1

        if temp == len(stocks_lists):
            break
        else:
            table.add_row(temp_list)

    print(table)
    # END OF FUNCTION





# ----> DISPLAY STATUS
def display_status() -> None:
    """
    display status of the application in the format like it 
Connection-Status - <Active or Inactive>          Time - <hh:mm:ss dd-MM-yyyy | None>
username : <Name in >
user-id : <user id>
    """
    format = "Connection-Status - "+""



############## CROSS FUNCTIONS ##############

def cross_time(tg_time:str) -> bool:
    ''' 
    return ture if given time is passed.
    param -> tg_time 
                pass time in '<year>-<month>-<day> <hour>:<minute>:<second>'
    '''
    curr_time = dt.datetime.now()
    target_time = dt.datetime.now().strptime(tg_time, "%Y-%m-%d %H:%M:%S")

    if curr_time > target_time: return True
    else: return False



############## REPEATING FUNCTIONS ##############
    
def refresh_shoonya_symbols_files() -> bool:
    """
    function to fatch all the masters files povided by shoonya api.
    """
    # exchanges - list 
    exchanges = ['NSE', 'NFO', 'CDS', 'MCX', 'BSE', 'BFO']

    try:
        for exch in exchanges:
            print(f"Downloading {Colors.BLUE}{exch}_symbols.txt{Colors.END} ")
            response = requests.get(f"https://api.shoonya.com/{exch}_symbols.txt.zip")
            open("temp.zip", "wb+").write(response.content)         # writing zip file. 
            try:
                with zipfile.ZipFile("temp.zip") as z:              # extracting zip_file
                    z.extractall("./data/shoonya_masters/")
            except:
                print("    "+Colors.RED+f"Error : Invalid File '{exch}_symbols.txt'"+Colors.END)

            os.remove("temp.zip")          # removing temp.zip file.
    except Exception as e:
        print(f"Can't refresh master files\nError : {e}")
        return False
    else :
        return True
    
def terminate(reason:str = None, intime:int=3) -> None:
    if reason is None:
        print(Colors.RED+"Terminating Program in 3 second."+Colors.END, sep="")
    else:
        print(Colors.YELLOW+f"Warning : {reason}"+Colors.END)
        print(Colors.RED+"Terminating Program in 3 second."+Colors.END, sep="")
    # stating timer 
    for i in range(intime):
        print("..", sep="")
        time.sleep(1)
    # exit from the program.
    exit()
    return None 


if __name__ == "__main__":
    # To test program write below.
    ...
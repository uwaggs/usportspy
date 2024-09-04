from . import helpers as h
import pandas as pd

'''
Rugby
'''
def rugby_get_schedule(gender):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    if gender not in ["w"]:
        raise h.UsportspyError("'gender' must be 'w' since only Women's Rugby is available for USPORTS currently.")

    if gender == "m":
        url = ""
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/rugby_schedule/Womens_rugby_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for rugby schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)
    
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')

    return df




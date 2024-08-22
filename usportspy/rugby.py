from . import helpers as h
import pandas as pd

'''
Rugby
'''
def rugby_get_schedule(gender):
    gender = "FEMALE" # We only have Womens Rugby data available for now, this will change in the future
    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/rugby_schedule/Mens_rugby_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/rugby_schedule/Womens_rugby_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting rugby schedule for {gender}. Ensure 'gender' is either 'MALE' or 'FEMALE'."
        raise h.UsportspyError(message, err)
    
    df = df.drop(columns=['Unnamed: 0'])

    return df




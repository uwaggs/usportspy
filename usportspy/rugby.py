from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Rugby
'''
def rugby_get_schedule(gender):
    """
    Fetches the Rugby schedule based on gender.

    Parameters
    ----------
    gender : str
        Must be either "m" (men's) or "w" (women's). Currently, only women's data is available.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the Rugby schedule. Columns include:
        `date`, `away`, `away_score`, `home`, `home_score`, `status`, `notes`,
        `month`, `conference`, `division`, `exhibition`, `postseason`, `season`.

    Examples
    --------
    >>> from usportspy import rugby_get_schedule
    >>> rugby_get_schedule("w").head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    if gender not in ["w"]:
        raise h.UsportspyError("'gender' must be 'w' since only Women's Rugby is available for U SPORTS currently.")

    if gender == "m":
        url = ""
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/rugby_schedule/Womens_rugby_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for rugby schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)
    
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')

    return clean_names(df)
from . import helpers as h
import pandas as pd

'''
Soccer
'''
def soccer_get_schedule(gender):
    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/Soccer_Schedule/mens_msoc_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/Soccer_Schedule/womens_wsoc_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting soccer schedule for {gender}. Ensure 'gender' is either 'MALE' or 'FEMALE'."
        raise h.UsportspyError(message, err)

    return df


def soccer_get_team_box_score(gender, seasons=[]):
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/soccer_team_box_score/{prefix}_team_box_score_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting soccer team box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def soccer_get_player_box_score(gender, seasons=[]):
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/soccer_player_box_score/{prefix}_player_box_score_{season}.csv"
        err, df = h.get_data(url)

        if err:
            message = f"Error getting soccer player box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def soccer_get_pbp(gender, seasons=[]):
    prefix = "mens_msoc" if gender == "MALE" else "womens_wsoc"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/Soccer_pbp/{prefix}_pbp_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting soccer play-by-play for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


from . import helpers as h
import pandas as pd

'''
Ice Hockey
'''
def ice_hockey_get_schedule(gender):
    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/hockey_schedule/mens_mice_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/hockey_schedule/womens_wice_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting ice hockey schedule for {gender}. Ensure 'gender' is either 'MALE' or 'FEMALE'."
        raise h.UsportspyError(message, err)

    return df


def ice_hockey_get_team_box_score(gender, seasons=[]):
    gender = "FEMALE" # Only Womens Field Hockey is available in USPORTS currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/hockey_team_box_score/{prefix}_team_box_score_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting ice hockey team box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df

    
def ice_hockey_get_player_box_score(gender, seasons=[]):
    gender = "FEMALE" # Only Womens Field Hockey is available in USPORTS currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/hockey_player_box_score/{prefix}_player_box_score_{season}.csv"
        err, df = h.get_data(url)

        if err:
            message = f"Error getting ice hockey player box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def ice_hockey_get_pbp(gender, seasons=[]):
    gender = "FEMALE" # Only Womens Field Hockey is available in USPORTS currently
    prefix = "mens_mice" if gender == "MALE" else "womens_wice"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/hockey_pbp/{prefix}_pbp_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting ice hockey play-by-play for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df




from . import helpers as h
import pandas as pd

'''
Basketball
'''
def basketball_get_schedule(gender):
    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/basketball_schedule/mens_bkb_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/basketball_schedule/womens_bkb_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting basketball schedule for {gender}. Ensure 'gender' is either 'MALE' or 'FEMALE'."
        raise h.UsportspyError(message, err)

    return df


def basketball_get_team_box_score(gender, seasons=[]):
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/basketball_team_box_score/{prefix}_team_box_score_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting basketball team box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df

    
def basketball_get_player_box_score(gender, seasons=[]):
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/basketball_player_box_score/{prefix}_player_box_score_{season}.csv" 
        err, df = h.get_data(url)

        if err:
            message = f"Error getting basketball player box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def basketball_get_pbp(gender, seasons=[]):
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/basketball_pbp/{prefix}_pbp_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting basketball play-by-play for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


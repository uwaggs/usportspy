from . import helpers as h
import pandas as pd


'''
Football
'''
def fb_get_schedule(gender):
    gender = "MALE" # USPORTS only has Men's Football currently
    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/football_schedule/fball_schedule.csv"
    else:
        url = ""
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting football schedule for {gender}. Ensure 'gender' is either 'MALE' or 'FEMALE'."
        raise h.UsportspyError(message, err)

    return df


def fb_get_returns(gender, seasons=[]):
    gender = "MALE" # USPORTS only has Men's Football currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()
    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_returns/returns_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting football team box scores for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_offence(gender, seasons=[]):
    gender = "MALE" # USPORTS only has Men's Football currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()
    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_offence/offence_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting football team offence data for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_defence(gender, seasons=[]):
    gender = "MALE" # USPORTS only has Men's Football currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()
    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_defence/defence_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting football team defence data for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_kicking(gender, seasons=[]):
    gender = "MALE" # USPORTS only has Men's Football currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()
    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_kicking/kicking_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting football team kicking data for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_pbp(gender, seasons=[]):
    gender = "MALE" # USPORTS only has Men's Football currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()
    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_pbp/fb_pbp_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting football play-by-play data for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_scoring_summaries(gender, seasons=[]):
    gender = "MALE" # USPORTS only has Men's Football currently
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()
    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_scoring_summaries/scoring_summaries_{season}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error getting football team scoring summaries for {gender} in {season}. Ensure 'gender' is either 'MALE' or 'FEMALE' and 'seasons' contains a valid season."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'])

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df



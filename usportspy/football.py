from . import helpers as h
import pandas as pd


'''
Football
'''
def fb_get_schedule(gender):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")
    
    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/football_schedule/fball_schedule.csv"
    else:
        url = ""
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for football schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return df


def fb_get_returns(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("football_returns", seasons)
    else:
        seasons = h.available_seasons("football_returns")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_returns/returns_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_offence(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("football_offence", seasons)
    else:
        seasons = h.available_seasons("football_offence")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_offence/offence_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team offence data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_defence(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("football_defence", seasons)
    else:
        seasons = h.available_seasons("football_defence")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_defence/defence_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team defence data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_kicking(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("football_kicking", seasons)
    else:
        seasons = h.available_seasons("football_kicking")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_kicking/kicking_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team kicking data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_pbp(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("football_pbp", seasons)
    else:
        seasons = h.available_seasons("football_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_pbp/fb_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fb_get_scoring_summaries(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["MALE"]:
        raise h.UsportspyError("'gender' must be 'MALE' since only Mens Football is available for USPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("football_scoring_summaries", seasons)
    else:
        seasons = h.available_seasons("football_scoring_summaries")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/football_scoring_summaries/scoring_summaries_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team scoring summaries for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df



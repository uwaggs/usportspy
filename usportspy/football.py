from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Football
'''
def fb_get_schedule(gender):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/Updated_Schedules/fball_schedule.csv"
    else:
        url = ""
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for football schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def fb_get_returns(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_returns", seasons)
    else:
        seasons = h.available_seasons("fball_returns")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_returns/fball_returns_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def fb_get_offence(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_offence", seasons)
    else:
        seasons = h.available_seasons("fball_offence")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_offence/fball_offence_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team offence data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def fb_get_defence(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_defence", seasons)
    else:
        seasons = h.available_seasons("fball_defence")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_defence/fball_defence_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team defence data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def fb_get_kicking(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_kicking", seasons)
    else:
        seasons = h.available_seasons("fball_kicking")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_kicking/fball_kicking_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team kicking data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def fb_get_pbp(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_pbp", seasons)
    else:
        seasons = h.available_seasons("fball_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_pbp/fball_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def fb_get_scoring_summaries(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_scoring_summaries", seasons)
    else:
        seasons = h.available_seasons("fball_scoring_summaries")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_scoring_summaries/fball_scoring_summaries_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team scoring summaries for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)

def fb_get_team(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_team", seasons)
    else:
        seasons = h.available_seasons("fball_team")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_team/fball_team_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)
def fb_get_drive_summaries(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("fball_drive_summaries", seasons)
    else:
        seasons = h.available_seasons("fball_drive_summaries")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/fball_drive_summaries/fball_drive_summaries_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for football team drive summaries for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)

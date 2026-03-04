from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Volleyball
'''
def volleyball_get_schedule(gender):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/Updated_Schedules/mvball_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/Updated_Schedules/wvball_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for volleyball schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def volleyball_get_team_box_score(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mvball" if gender == "m" else "wvball"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season(f"{prefix}_team_box", seasons)
    else:
        seasons = h.available_seasons(f"{prefix}_team_box")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/{prefix}_team_box/{prefix}_team_box_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for volleyball team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


    
def volleyball_get_player_box_score(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mvball" if gender == "m" else "wvball"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season(f"{prefix}_player_box", seasons)
    else:
        seasons = h.available_seasons(f"{prefix}_player_box")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/{prefix}_player_box/{prefix}_player_box_{h.year_to_season(season)}.csv"

        if err:
            message = f"Error making request for volleyball player box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def volleyball_get_pbp(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mvball" if gender == "m" else "wvball"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("volleybal_pbp", seasons)
    else:
        seasons = h.available_seasons("volleybal_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/{prefix}_pbp/{prefix}_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for volleyball play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


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
        url = "https://github.com/uwaggs/usports-data/releases/download/volleyball_schedule/mens_vball_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/volleyball_schedule/womens_vball_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for volleyball schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def volleyball_get_team_box_score(gender, seasons=[]):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("volleyball_team_box_score", seasons)
    else:
        seasons = h.available_seasons("volleyball_team_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/volleyball_team_box_score/{prefix}_team_box_score_{h.year_to_season(season)}.csv"
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

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("volleyball_player_box_score", seasons)
    else:
        seasons = h.available_seasons("volleyball_player_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/volleyball_player_box_score/{prefix}_vb_player_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url)

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

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("volleybal_pbp", seasons)
    else:
        seasons = h.available_seasons("volleybal_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/volleybal_pbp/{prefix}_vb_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for volleyball play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


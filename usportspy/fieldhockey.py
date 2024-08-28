from . import helpers as h
import pandas as pd

'''
Field Hockey
'''
def fh_get_schedule(gender):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")
    
    if gender not in ["FEMALE"]:
        raise h.UsportspyError("'gender' must be 'FEMALE' since only Womens Field Hockey is available for USPORTS currently.")

    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/field_hockey_schedule/mens_fh_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/field_hockey_schedule/womens_fh_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for field hockey schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return df


def fh_get_team_box_score(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["FEMALE"]:
        raise h.UsportspyError("'gender' must be 'FEMALE' since only Womens Field Hockey is available for USPORTS currently.")

    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("field_hockey_team_box_score", seasons)
    else:
        seasons = h.available_seasons("field_hockey_team_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/field_hockey_team_box_score/{prefix}_team_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making reqeust for field hockey team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df

    
def fh_get_player_box_score(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["FEMALE"]:
        raise h.UsportspyError("'gender' must be 'FEMALE' since only Womens Field Hockey is available for USPORTS currently.")
    
    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("field_hockey_player_box_score", seasons)
    else:
        seasons = h.available_seasons("field_hockey_player_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/field_hockey_player_box_score/{prefix}_player_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url)

        if err:
            message = f"Error making a request for field hockey player box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def fh_get_pbp(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender not in ["FEMALE"]:
        raise h.UsportspyError("'gender' must be 'FEMALE' since only Womens Field Hockey is available for USPORTS currently.")

    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("field_hockey_pbp", seasons)
    else:
        seasons = h.available_seasons("field_hockey_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/field_hockey_pbp/{prefix}_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for field hockey play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


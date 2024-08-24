from . import helpers as h
import pandas as pd

'''
Soccer
'''
def soccer_get_schedule(gender):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/Soccer_Schedule/mens_msoc_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/Soccer_Schedule/womens_wsoc_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for soccer schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return df


def soccer_get_team_box_score(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("soccer_team_box_score", seasons)
    else:
        seasons = h.available_seasons("soccer_team_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/soccer_team_box_score/{prefix}_team_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making a request for soccer team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def soccer_get_player_box_score(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    prefix = "mens" if gender == "MALE" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("soccer_player_box_score", seasons)
    else:
        seasons = h.available_seasons("soccer_player_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/soccer_player_box_score/{prefix}_player_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url)

        if err:
            message = f"Error making request for soccer player box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


def soccer_get_pbp(gender, seasons=[]):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    prefix = "mens_msoc" if gender == "MALE" else "womens_wsoc"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("Soccer_pbp", seasons)
    else:
        seasons = h.available_seasons("Soccer_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/Soccer_pbp/{prefix}_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for soccer play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


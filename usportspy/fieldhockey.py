from . import helpers as h
import pandas as pd
from janitor import clean_names


'''
Field Hockey
'''
def fh_get_schedule(gender):
    """
    Fetches the schedule for Field Hockey games.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "w" is supported currently.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns: `date`, `away`, `away_score`, `home`, 
        `home_score`, `status`, `notes`, `month`, `box_scores`, `conference`, 
        `division`, `exhibition`, `post_season`, and `season`.
    
    Examples
    --------
    >>> from usportspy import fh_get_schedule
    >>> schedule_female = fh_get_schedule("w")
    >>> print(schedule_female.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    if gender not in ["w"]:
        raise h.UsportspyError("'gender' must be 'w' since only Women's Field Hockey is available for U SPORTS currently.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/field_hockey_schedule/mens_fh_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/field_hockey_schedule/womens_fh_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for field hockey schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def fh_get_team_box_score(gender, seasons=[]):
    """
    Fetches the team box scores for Field Hockey games.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "w" is supported.
    seasons : list of int, optional
        List of seasons (starting year) to filter by.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns: `player`, `team`, `sh`, `sog`, `g`, `a`, `ds`,
        `min`, `yellow_card`, `red_card`, `game_id`, `sog_against`, `ga`, `sv`,
        `goalie_mins`, `game_date`, `season`, and `season_type`.

    Examples
    --------
    >>> from usportspy import fh_get_team_box_score
    >>> team_box_scores_female = fh_get_team_box_score("w", [2018, 2019])
    >>> print(team_box_scores_female.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["w"]:
        raise h.UsportspyError("'gender' must be 'w' since only Women's Field Hockey is available for U SPORTS currently.")

    prefix = "mens" if gender == "m" else "womens"
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

    return clean_names(combined_df)

    
def fh_get_player_box_score(gender, seasons=[]):
    """
    Fetches the player box scores for Field Hockey games.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "w" is supported.
    seasons : list of int, optional
        List of seasons (starting year) to filter by.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns: `player`, `team`, `sh`, `sog`, `g`, `a`, `ds`, 
        `min`, `yellow_card`, `red_card`, `game_id`, `sog_against`, `ga`, `sv`, 
        `goalie_mins`, `game_date`, `season`, and `season_type`.

    Examples
    --------
    >>> from usportspy import fh_get_player_box_score
    >>> player_box_scores_female = fh_get_player_box_score("w", [2018, 2019])
    >>> print(player_box_scores_female.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["w"]:
        raise h.UsportspyError("'gender' must be 'w' since only Women's Field Hockey is available for U SPORTS currently.")
    
    prefix = "mens" if gender == "m" else "womens"
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

    return clean_names(combined_df)


def fh_get_pbp(gender, seasons=[]):
    """
    Fetches the play-by-play data for Field Hockey games.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "w" is supported.
    seasons : list of int, optional
        List of seasons (starting year) to filter by.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns: `time`, `event`, `quarters`, `game_id`, 
        `season`, and `season_type`.

    Examples
    --------
    >>> from usportspy import fh_get_pbp
    >>> pbp_female = fh_get_pbp("w", [2018, 2019])
    >>> print(pbp_female.head())
    """
    
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["w"]:
        raise h.UsportspyError("'gender' must be 'w' since only Women's Field Hockey is available for U SPORTS currently.")

    prefix = "mens" if gender == "m" else "womens"
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

    return clean_names(combined_df)
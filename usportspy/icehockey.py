from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Ice Hockey
'''
def ice_hockey_get_schedule(gender):
    """
    Fetches the ice hockey schedule for the specified gender.

    Parameters
    ----------
    gender : str
        Must be either "m" (men) or "w" (women).

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the ice hockey schedule. Columns include:
        `date`, `away`, `away_score`, `home`, `home_score`, `status`, `notes`,
        `month`, `box_scores`, `conference`, `division`, `exhibition`,
        `postseason`, `season`.

    Examples
    --------
    >>> from usportspy import ice_hockey_get_schedule
    >>> ice_hockey_get_schedule("w").head()
    >>> ice_hockey_get_schedule("m").head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/hockey_schedule/mens_mice_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/hockey_schedule/womens_wice_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for ice hockey schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def ice_hockey_get_team_box_score(gender, seasons=[]):
    """
    Fetches team-level box score data for ice hockey.

    Parameters
    ----------
    gender : str
        Must be either "m" or "w". Only "w" is currently supported.
    seasons : list of int, optional
        List of season start years (e.g., [2022, 2023]). If not provided,
        all available seasons are returned.

    Returns
    -------
    pandas.DataFrame
        Team-level box scores. Example columns include:
        `team`, `goals_p1`, `goals_p2`, ..., `shots_total`, `game_id`,
        `season`, `season_type`.

    Examples
    --------
    >>> from usportspy import ice_hockey_get_team_box_score
    >>> ice_hockey_get_team_box_score("w", [2021]).head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("hockey_team_box_score", seasons)
    else:
        seasons = h.available_seasons("hockey_team_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/hockey_team_box_score/{prefix}_team_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for ice hockey team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)

    
def ice_hockey_get_player_box_score(gender, seasons=[]):
    """
    Fetches player-level box score data for ice hockey.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "w" is currently supported.
    seasons : list of int, optional
        List of season start years. If not provided, all available seasons are returned.

    Returns
    -------
    pandas.DataFrame
        Player-level stats. Columns may include:
        `skaters`, `pos`, `g`, `a`, `plus_minus`, `s`, `team`, goalie stats,
        `game_id`, `season`, `season_type`.

    Examples
    --------
    >>> from usportspy import ice_hockey_get_player_box_score
    >>> ice_hockey_get_player_box_score("w", [2020]).head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("hockey_player_box_score", seasons)
    else:
        seasons = h.available_seasons("hockey_player_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/hockey_player_box_score/{prefix}_player_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url)

        if err:
            message = f"Error making request for ice hockey player box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def ice_hockey_get_pbp(gender, seasons=[]):
    """
    Fetches play-by-play (PBP) data for U SPORTS ice hockey games.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "w" is currently supported.
    seasons : list of int, optional
        List of season start years. If not provided, returns all seasons.

    Returns
    -------
    pandas.DataFrame
        Play-by-play data with columns such as:
        `event`, `period`, `game_id`, `away_team`, `home_team`,
        `season`, `season_type`.

    Examples
    --------
    >>> from usportspy import ice_hockey_get_pbp
    >>> ice_hockey_get_pbp("w", [2019]).head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens_mice" if gender == "m" else "womens_wice"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("hockey_pbp", seasons)
    else:
        seasons = h.available_seasons("hockey_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/hockey_pbp/{prefix}_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for ice hockey play-by-play data for Gender: {gender} for Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)
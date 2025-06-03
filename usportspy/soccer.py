from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Soccer
'''
def soccer_get_schedule(gender):
    """
    Fetch soccer schedule for a specified gender.

    Parameters
    ----------
    gender : str
        Specifies the gender of the teams. Must be either "m" (men's) or "w" (women's).

    Returns
    -------
    pandas.DataFrame
        A DataFrame with columns:
        `date`, `away`, `away_score`, `home`, `home_score`, `status`, `notes`, `month`,
        `box_scores`, `conference`, `division`, `exhibition`, `postseason`, `season`.

    Examples
    --------
    >>> from usportspy import soccer_get_schedule
    >>> soccer_get_schedule("m").head()
    >>> soccer_get_schedule("w").head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/Soccer_Schedule/mens_msoc_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/Soccer_Schedule/womens_wsoc_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for soccer schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def soccer_get_team_box_score(gender, seasons=[]):
    """
    Fetch team box score data for soccer.

    Parameters
    ----------
    gender : str
        Gender of the teams. Must be "m" for men's or "w" for women's.
    seasons : list of int, optional
        List of season starting years (e.g., [2022, 2023]).
        If None, returns all available seasons.

    Returns
    -------
    pandas.DataFrame
        Team-level box score statistics with columns including:
        `team`, `goals_1`, `goals_2`, `goals_total`, `shots_1`, ..., `corners_2ot`, 
        `season`, `season_type`.

    Examples
    --------
    >>> soccer_get_team_box_score("m", [2021, 2022]).head()
    >>> soccer_get_team_box_score("w").head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
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

    return clean_names(combined_df)


def soccer_get_player_box_score(gender, seasons=[]):
    """
    Fetch player box score data for soccer.

    Parameters
    ----------
    gender : str
        Gender of the teams. Must be "m" or "w".
    seasons : list of int, optional
        List of season starting years. If not provided, returns all seasons.

    Returns
    -------
    pandas.DataFrame
        Player-level statistics with columns:
        `player`, `sh`, `sog`, `g`, `a`, `min`, `yellow_card`, `red_card`, `player_links`,
        `game_id`, `sog_against`, `ga`, `sv`, `game_date`, `season`, `season_type`.

    Examples
    --------
    >>> soccer_get_player_box_score("m", [2019]).head()
    >>> soccer_get_player_box_score("w").head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
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

    return clean_names(combined_df)


def soccer_get_pbp(gender, seasons=[]):
    """
    Fetch play-by-play data for soccer games.

    Parameters
    ----------
    gender : str
        Either "m" or "w".
    seasons : list of int, optional
        List of starting years to include. If empty, returns all.

    Returns
    -------
    pandas.DataFrame
        Play-by-play events with columns:
        `time`, `event`, `game_id`, `away`, `home`, `season`, `season_type`.

    Examples
    --------
    >>> soccer_get_pbp("w", [2021]).head()
    >>> soccer_get_pbp("m").head()
    """
    
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens_msoc" if gender == "m" else "womens_wsoc"
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

    return clean_names(combined_df)
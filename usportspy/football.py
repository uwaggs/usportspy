from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Football
'''
def fb_get_schedule(gender):
    """
    Fetches the Football schedule.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns: `date`, `away`, `away_score`, `home`, 
        `home_score`, `status`, `notes`, `month`, `box_scores`, 
        `conference`, `division`, `exhibition`, `postseason`, `season`.

    Examples
    --------
    >>> from usportspy import fb_get_schedule
    >>> schedule_male = fb_get_schedule("m")
    >>> print(schedule_male.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/football_schedule/fball_schedule.csv"
    else:
        url = ""
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for football schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def fb_get_returns(gender, seasons=[]):
    """
    Fetches Football returns data for specified seasons.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.
    seasons : list of int, optional
        List of seasons (starting years). If not provided, all seasons are returned.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns like:
        `player`, `punting_returns_no`, `punting_returns_yds`, `kickoff_returns_td`,
        `interception_returns_td`, `team`, `game_id`, `season`, `season_type`.

    Examples
    --------
    >>> returns = fb_get_returns("m", [2019, 2021])
    >>> print(returns.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

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

    return clean_names(combined_df)


def fb_get_offence(gender, seasons=[]):
    """
    Fetches Football offensive stats for specified seasons.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.
    seasons : list of int, optional
        List of starting years of the seasons to filter.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns like:
        `player`, `passing_yds`, `rushing_att`, `receiving_td`, `fumble_lost`, 
        `team`, `game_id`, `season`, `season_type`.

    Examples
    --------
    >>> offence = fb_get_offence("m", [2019, 2021])
    >>> print(offence.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

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

    return clean_names(combined_df)


def fb_get_defence(gender, seasons=[]):
    """
    Fetches Football defensive stats for specified seasons.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.
    seasons : list of int, optional
        List of starting years of the seasons to filter.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns like:
        `player`, `solo`, `ast`, `sacks`, `int`, `br_up`, `team`, `game_id`, `season`, `season_type`.

    Examples
    --------
    >>> defence = fb_get_defence("m", [2019, 2021])
    >>> print(defence.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

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

    return clean_names(combined_df)


def fb_get_kicking(gender, seasons=[]):
    """
    Fetches Football kicking stats for specified seasons.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.
    seasons : list of int, optional
        List of starting years of the seasons to filter.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns like:
        `player`, `punting_no`, `kicking_fgm`, `kicking_pts`, 
        `kickoffs_avg`, `kickoffs_ob`, `team`, `game_id`, `season`, `season_type`.

    Examples
    --------
    >>> kicking = fb_get_kicking("m", [2019, 2021])
    >>> print(kicking.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

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

    return clean_names(combined_df)


def fb_get_pbp(gender, seasons=[]):
    """
    Fetches Football play-by-play data.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.
    seasons : list of int, optional
        List of starting years of the seasons to filter.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns:
        `downs`, `event`, `quarter`, `game_id`, `away_team`, 
        `home_team`, `season`, `season_type`.

    Examples
    --------
    >>> pbp = fb_get_pbp("m", [2019, 2021])
    >>> print(pbp.head())
    """
    
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

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

    return clean_names(combined_df)


def fb_get_scoring_summaries(gender, seasons=[]):
    """
    Fetches Football scoring summaries.

    Parameters
    ----------
    gender : str
        Must be "m" or "w". Only "m" is supported.
    seasons : list of int, optional
        List of starting years of the seasons to filter.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns:
        `prd`, `time`, `scoring_summary`, `away_score`, `home_score`, 
        `away_team`, `home_team`, `game_id`, `season`, `season_type`.

    Examples
    --------
    >>> scoring = fb_get_scoring_summaries("m", [2019, 2021])
    >>> print(scoring.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender not in ["m"]:
        raise h.UsportspyError("'gender' must be 'm' since only Men's Football is available for U SPORTS currently.")

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

    return clean_names(combined_df)
from . import helpers as h
import pandas as pd
from janitor import clean_names

'''
Basketball Functions
'''
def basketball_get_schedule(gender):
    """
    Fetch basketball schedule for a specified gender.

    Parameters
    ----------
    gender: str
        Specifies the gender of the teams. Must be either "m" (men's) or "w" (women's).

    Returns
    -------
    pandas.DataFrame
        A DataFrame with columns: 
        `date`, `away`, `away_score`, `home`, `home_score`, `status`, `notes`, 
        `month`, `box_scores`, `conference`, `division`, `exhibition`, 
        `postseason`, and `season`.

    Examples
    --------
    >>> from usportspy import basketball_get_schedule
    >>> basketball_get_schedule("m").head()
    >>> basketball_get_schedule("w").head()
    """
    
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/basketball_schedule/mens_bkb_schedule.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/basketball_schedule/womens_bkb_schedule.csv"
    
    err, df = h.get_data(url) 
    if err:
        message = f"Error making request for basketball schedule for Gender: {gender}."
        raise h.UsportspyError(message, err)

    return clean_names(df)


def basketball_get_team_box_score(gender, seasons=[]):
    """
    Fetch team box score data for basketball teams.

    Parameters
    ----------
    gender : str
        Gender of the teams. Must be "m" for men's or "w" for women's.
    seasons : list of int, optional
        List of season starting years to include (e.g., [2018, 2019]).
        If None, returns data for all available seasons.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with team-level box score statistics. Columns include:
        `field_goals_made`, `field_goals_attempted`, `field_goal_percentage`, 
        `three_point_field_goals_made`, `three_point_field_goals_attempted`, 
        `three_point_field_goal_percentage`, `free_throws_made`, 
        `free_throws_attempted`, `free_throw_percentage`, `rebounds`, 
        `assists`, `turnovers`, `points_off_turnovers`, 
        `second_chance_points`, `points_in_the_paint`, `fastbreak_points`, 
        `bench_points`, `largest_lead`, `trends`, `team_name`, `game_id`, 
        `date`, `q1`, `q2`, `q3`, `q4`, `total`, `time_of_largest_lead`, 
        `ot`, `x2ot`, `x3ot`, `season`, `season_type`.

    Examples
    --------
    >>> basketball_get_team_box_score("m", [2018, 2019]).head()
    >>> basketball_get_team_box_score("w", [2018, 2019]).head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("basketball_team_box_score", seasons)
    else:
        seasons = h.available_seasons("basketball_team_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/basketball_team_box_score/{prefix}_team_box_score_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for basketball team box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)

    
def basketball_get_player_box_score(gender, seasons=[]):
    """
    Fetch player box score data for basketball players.

    Parameters
    ----------
    gender : str
        Gender of the teams. Must be "m" or "w".
    seasons : list of int, optional
        List of season starting years. If not provided, returns all seasons.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with player-level stats. Columns include:
        `player`, `min`, `fgm`, `fga`, `three_pm`, `three_pa`, `ftm`, `fta`, 
        `oreb`, `dreb`, `reb`, `ast`, `stl`, `blk`, `to`, `pf`, `pts`, 
        `starter`, `player_number`, `player_links`, `date`, `game_id`, 
        `team_name`, `season`, `season_type`.

    Examples
    --------
    >>> basketball_get_player_box_score("m", [2018, 2019]).head()
    >>> basketball_get_player_box_score("w", [2018, 2019]).head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")
    
    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("basketball_player_box_score", seasons)
    else:
        seasons = h.available_seasons("basketball_player_box_score")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/basketball_player_box_score/{prefix}_player_box_score_{h.year_to_season(season)}.csv" 
        err, df = h.get_data(url)

        if err:
            message = f"Error making request for basketball player box scores for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)


def basketball_get_pbp(gender, seasons=[]):
    """
    Fetch player box score data for basketball players.

    Parameters
    ----------
    gender : str
        Gender of the teams. Must be "m" or "w".
    seasons : list of int, optional
        List of season starting years. If not provided, returns all seasons.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with player-level stats. Columns include:
        `player`, `min`, `fgm`, `fga`, `three_pm`, `three_pa`, `ftm`, `fta`, 
        `oreb`, `dreb`, `reb`, `ast`, `stl`, `blk`, `to`, `pf`, `pts`, 
        `starter`, `player_number`, `player_links`, `date`, `game_id`, 
        `team_name`, `season`, `season_type`.

    Examples
    --------
    >>> basketball_get_player_box_score("m", [2018, 2019]).head()
    >>> basketball_get_player_box_score("w", [2018, 2019]).head()
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    prefix = "mens" if gender == "m" else "womens"
    combined_df = pd.DataFrame()

    if len(seasons):
        h.validate_season("basketball_pbp", seasons)
    else:
        seasons = h.available_seasons("basketball_pbp")

    for season in seasons:
        url = f"https://github.com/uwaggs/usports-data/releases/download/basketball_pbp/{prefix}_pbp_{h.year_to_season(season)}.csv"
        err, df = h.get_data(url) 

        if err:
            message = f"Error making request for basketball play-by-play data for Gender: {gender} and Seasons: {seasons}."
            raise h.UsportspyError(message, err)

        # Drop the 'Unnamed: 0' column
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return clean_names(combined_df)
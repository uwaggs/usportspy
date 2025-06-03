from . import helpers as h
from janitor import clean_names

'''
Swimming Functions
'''
def swimming_team_rankings():
    """
    Fetches the rankings of U SPORTS swimming teams.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing team rankings with columns:
        `rank`, `team`, `count`, `gender`, and `date`.

    Examples
    --------
    >>> from usportspy import swimming_team_rankings
    >>> df = swimming_team_rankings()
    >>> print(df.head())
    """

    url = "https://github.com/uwaggs/usports-data/releases/download/swimming_team_rankings/swimming_team_rankings.csv"        
    err, df = h.get_data(url)
    if err:
        message = f"Error getting swimming team rankings."
        raise h.UsportspyError(message, err)
    return clean_names(df)


def swimming_athlete_rankings():
    """
    Fetches the rankings of U SPORTS swimming athletes.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with athlete rankings. Columns:
        `season`, `gender`, `rank`, `athlete_university`, `age`, `team`, `conference`,
        `date`, `meet`, `time`, `fina`, `event`, `date_collected`.

    Examples
    --------
    >>> from usportspy import swimming_athlete_rankings
    >>> df = swimming_athlete_rankings()
    >>> print(df.head())
    """

    url = "https://github.com/uwaggs/usports-data/releases/download/swimming_athlete_rankings/swimming_athlete_rankings.csv"        
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting swimming athlete rankings."
        raise h.UsportspyError(message, err)
    return clean_names(df)
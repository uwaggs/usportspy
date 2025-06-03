from . import helpers as h
from janitor import clean_names

'''
Cross-Country Functions
'''
def xc_team_rankings(gender, seasons = [], universities = []):
    """
    Fetches the rankings of cross-country teams.

    Parameters
    ----------
    gender : str
        Must be either "m" (men's) or "w" (women's).
    seasons : list of int, optional
        List of seasons (starting year) to filter by.
        If not provided, all seasons are included.
    universities : list of str, optional
        List of university names to filter by.
        If not provided, all universities are included.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing cross-country team rankings with columns:
        `season`, `gender`, `date`, `week`, `ranking`, `university`, `pts`.

    Examples
    --------
    >>> from usportspy import xc_team_rankings
    >>> team_rankings = xc_team_rankings("m", seasons=[2023])
    >>> print(team_rankings.head())
    """
    
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    g = "MEN" if gender == "m" else "WOMEN"

    url = "https://github.com/uwaggs/usports-data/releases/download/xc_team_rankings/xc_team_rankings.csv"
    err, df = h.get_data(url) 

    if err:
        message = f"Error making request for cross-country team rankings for Gender: {gender} and Seasons: {seasons} and Universities:{universities}."
        raise h.UsportspyError(message, err)
    
    
    df = df.loc[df['Gender'].isin([g])]

    if len(seasons):
        df = df.loc[df['Season'].isin(seasons)]
    
    if len(universities):
        df = df.loc[df['University'].isin(universities)]


    return clean_names(df)


def xc_rosters(gender, seasons = [], universities = []):
    """
    Fetches the rosters of cross-country teams.

    Parameters
    ----------
    gender : str
        Must be either "m" (men's) or "w" (women's).
    seasons : list of int, optional
        List of seasons (starting year) to filter by.
        If not provided, all seasons are included.
    universities : list of str, optional
        List of university names to filter by.
        If not provided, all universities are included.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing athlete roster details with columns:
        `university`, `name`, `sex`, `birthday`, `program_position`, 
        `eligibility`, `hometown`, `type`, `recorded_date`.

    Examples
    --------
    >>> from usportspy import xc_rosters
    >>> rosters = xc_rosters("w", seasons=[2024])
    >>> print(rosters.head())
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    g = "M" if gender == "m" else "F"
    
    url = "https://github.com/uwaggs/usports-data/releases/download/xc_rosters/xc_rosters.csv"
    err, df = h.get_data(url) 
   
    if err:
        message = f"Error making request for cross-country roster data for Gender: {gender} and Seasons: {seasons} and Universities: {universities}."
        raise h.UsportspyError(message, err)

    def get_season(date):
        _, _, year = date.split("-")[0].split("/")
        return int(year)

    
    df = df.loc[df["Sex"].isin([g])]

    if len(seasons):
        df = df[df["Recorded Date"].apply(lambda x: get_season(str(x)) in seasons)]

    
    if len(universities):
        df = df.loc[df['University'].isin(universities)]

    return clean_names(df)


def xc_meet_results(seasons = [], universities = []):
    """
    Fetches the meet results of cross-country events.

    Parameters
    ----------
    seasons : list of int, optional
        List of seasons (starting year) to filter by.
        If not provided, all seasons are included.
    universities : list of str, optional
        List of university names to filter by.
        If not provided, all universities are included.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing meet results with columns:
        `date`, `name`, `location`, `results`.

    Examples
    --------
    >>> from usportspy import xc_meet_results
    >>> meet_results = xc_meet_results([2022])
    >>> print(meet_results.head())
    """

    url = "https://github.com/uwaggs/usports-data/releases/download/xc_meet_results/xc_meet_results.csv"
    err, df = h.get_data(url)
    if err:
        message = f"Error making request for cross-country meet results for Seasons: {seasons} and Universities: {universities}."
        raise h.UsportspyError(message, err)

    def get_season(date):
        if "-" in date:
            month, _, year = date.split("-")[1].split("/")
        else:
            month, _, year = date.split("/")

        if month in ["09", "10", "11", "12"]:
            return int(year)
        else:
            return int(year) - 1

    if len(seasons):
        df = df[df["Date"].apply(lambda x: get_season(str(x)) in seasons)]

    if len(universities):
        df = df.loc[df['University'].isin(universities)]


    return clean_names(df)


def xc_universities():
    """
    Fetches the list of universities with cross-country teams.

    Returns
    -------
    pandas.DataFrame
        A DataFrame listing universities with columns:
        `university`, `conference`, `link`, `team_version`, `athlete_version`.

    Examples
    --------
    >>> from usportspy import xc_universities
    >>> universities = xc_universities()
    >>> print(universities.head())
    """

    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_universities/tnf_universities.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error making request for cross-country university data."
        raise h.UsportspyError(message, err)

    return clean_names(df)
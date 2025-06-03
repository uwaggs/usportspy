from . import helpers as h
from janitor import clean_names

'''
Track and Field Functions
'''
def tnf_athlete_rankings(gender, seasons = [], athlete_names = [], events = [], universities = []):
    """
    Fetches U SPORTS track and field athlete rankings with optional filters.

    Parameters
    ----------
    gender : str
        "m" for men's or "w" for women's.
    seasons : list of int, optional
        List of season starting years (e.g., [2022]).
    athlete_names : list of str, optional
        List of athlete names to filter by.
    events : list of str, optional
        List of event names to filter by.
    universities : list of str, optional
        List of university names to filter by.

    Returns
    -------
    pandas.DataFrame
        Athlete rankings with columns such as:
        `rank`, `athlete_name`, `university`, `performance`, `meet`, `date`, `event`, `season`.

    Examples
    --------
    >>> tnf_athlete_rankings("m", seasons=[2022], events=["60-meter"])
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    g = "men" if gender == "m" else "women"

    seasons = [f"{season}/{season + 1}" for season in seasons]

    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_athlete_rankings/tnf_athlete_rankings.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error making request for track and field athlete rankings for Gender: {gender} and Seasons: {seasons} and Athlete Names: {athlete_names} and Events: {events} and Universities: {universities}."
        raise h.UsportspyError(message, err)

    df = df.loc[df['Gender'].isin([g])]

    if len(athlete_names):
        df = df.loc[df['Athlete Name'].isin(athlete_names)]

    if len(events):
        df = df.loc[df['Event'].isin(events)]

    if len(universities):
        df = df.loc[df['University'].isin(universities)]

    if len(seasons):
        df = df.loc[df['Season'].isin(seasons)]



    return clean_names(df)


def tnf_team_rankings(gender, seasons = [], universities = []):
    """
    Fetches U SPORTS track and field team rankings with optional filters.

    Parameters
    ----------
    gender : str
        "m" or "w".
    seasons : list of int, optional
        Starting years of the season (e.g., [2023]).
    universities : list of str, optional
        University names to filter by.

    Returns
    -------
    pandas.DataFrame
        Team rankings with columns like:
        `season`, `gender`, `ranking`, `university`, `pts`, `recorded_date`.

    Examples
    --------
    >>> tnf_team_rankings("w", seasons=[2023])
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    g = "Men" if gender == "m" else "Women"

    seasons = [f"{season}/{season + 1}" for season in seasons]

    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_team_rankings/tnf_team_rankings.csv"
    err, df = h.get_data(url) 

    if err:
        message = f"Error making request for track and field team rankings for Gender: {gender} and Seasons: {seasons} and Universities: {universities}."
        raise h.UsportspyError(message, err)
    
    df = df.loc[df['Gender'].isin([g])]

    if len(seasons):
        df = df.loc[df['Season'].isin(seasons)]
    
    if len(universities):
        df = df.loc[df['University'].isin(universities)]


    return clean_names(df)


def tnf_rosters(gender, seasons = [], universities = []):
    """
    Fetches U SPORTS track and field rosters.

    Parameters
    ----------
    gender : str
        "m" or "w".
    seasons : list of int, optional
        Starting years of the season.
    universities : list of str, optional
        University names to filter by.

    Returns
    -------
    pandas.DataFrame
        Roster information with columns like:
        `university`, `name`, `sex`, `birthday`, `eligibility`, 
        `hometown`, `type`, `recorded_date`.

    Examples
    --------
    >>> tnf_rosters("m", seasons=[2024], universities=["Guelph"])
    """

    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    g = "M" if gender == "m" else "F"

    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_rosters/tnf_rosters.csv"
    err, df = h.get_data(url) 
   
    if err:
        message = f"Error making a request for track and field roster data for Gender: {gender} and Seasons: {seasons} and Universities: {universities}."
        raise h.UsportspyError(message, err)
    
    def get_season(date):
        _, _, year = date.split("-")[0].split("/")
        return int(year)


    df = df.loc[df['Sex'].isin([g])]

    if len(seasons):
        df = df[df["Recorded Date"].apply(lambda x: get_season(str(x)) in seasons)]

    if len(universities):
        df = df.loc[df['University'].isin(universities)]

    return clean_names(df)


def tnf_meet_results(seasons = [], universities = []):
    """
    Fetches U SPORTS track and field meet results.

    Parameters
    ----------
    seasons : list of int, optional
        List of season starting years (e.g., [2022]).
    universities : list of str, optional
        University names to filter by.

    Returns
    -------
    pandas.DataFrame
        Meet results with columns: `date`, `name`, `location`, `results`.

    Examples
    --------
    >>> tnf_meet_results(seasons=[2022])
    """

    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_meet_results/tnf_meet_results.csv"
    err, df = h.get_data(url)
    if err:
        message = f"Error making request for track and field meet results for Seasons: {seasons} and Universities: {universities}."
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


def tnf_universities():
    """
    Fetches a list of U SPORTS track and field universities.

    Returns
    -------
    pandas.DataFrame
        University metadata. Columns: 
        `university`, `conference`, `link`, `team_version`, `athlete_version`.

    Examples
    --------
    >>> tnf_universities()
    """

    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_universities/tnf_universities.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error making request for track and field university data."
        raise h.UsportspyError(message, err)

    return clean_names(df)
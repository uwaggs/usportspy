import requests
import pandas as pd
from io import StringIO
import re

'''
Helper functions and classes
'''
class UsportspyError(Exception):
    """
    Custom exception for the usportspy package.

    Parameters
    ----------
    message : str
        Main error message.
    detailed_err : Exception, optional
        Original exception for traceback context.

    Examples
    --------
    >>> raise UsportspyError("Something went wrong")
    >>> raise UsportspyError("Fetch failed", detailed_err=e)
    """

    def __init__(self, message="", detailed_err=None):
        if detailed_err:
            super().__init__(f"{message}\n\nTrue Error:\n{repr(detailed_err)}")
        else:
            super().__init__(f"{message}")


def get_data(url):
    """
    Retrieves CSV data from a remote URL.

    Parameters
    ----------
    url : str
        URL to the CSV file.

    Returns
    -------
    tuple
        (error, DataFrame): Returns (None, df) if successful, or (Exception, None) if failed.

    Examples
    --------
    >>> err, df = get_data("https://example.com/data.csv")
    >>> if err: print("Error:", err)
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content)
        return None, df 
    except Exception as e:
        return e, None


def year_to_season(year):
    """
    Converts a start year to U SPORTS season format (e.g., 2023 → '2023-24').

    Parameters
    ----------
    year : int
        Starting year of the season.

    Returns
    -------
    str
        Season string in format 'YYYY-YY'.

    Examples
    --------
    >>> year_to_season(2023)
    '2023-24'
    """

    return f"{year}-{str((year % 100) + 1).zfill(2)}"


def available_seasons(tag):
    """
    Gets available seasons for a given GitHub release tag.

    Parameters
    ----------
    tag : str
        GitHub release tag (e.g., 'basketball_team_box_score').

    Returns
    -------
    list of int
        Sorted list of available starting years.

    Raises
    ------
    Exception
        If the GitHub API request fails.

    Examples
    --------
    >>> available_seasons("basketball_team_box_score")
    [2018, 2019, 2020]
    """

    response = requests.get(f"https://api.github.com/repos/uwaggs/usports-data/releases/tags/{tag}")

    if response.status_code == 200:
        release_data = response.json()
        
        assets = release_data.get("assets", [])
        
        pattern = re.compile(r'.*\d{4}-\d{2}\.csv$')
        file_list = [asset["name"] for asset in assets if pattern.match(asset["name"])]

        seasons = sorted([int(season[-11:-7]) for season in file_list])

        return seasons
    else:
        raise Exception(f"Failed to retrieve release data: {response.status_code} {response.reason}")
    

def validate_season(tag, seasons):
    """
    Validates that all requested seasons are available.

    Parameters
    ----------
    tag : str
        GitHub release tag.
    seasons : list of int
        List of starting years to validate.

    Raises
    ------
    UsportspyError
        If any requested seasons are not found in available seasons.

    Examples
    --------
    >>> validate_season("basketball_team_box_score", [2020, 2022])
    """
    
    a_seasons = available_seasons(tag)

    bad_seasons_requested = sorted(list(set(seasons).difference(set(a_seasons))))
    if len(bad_seasons_requested):
        raise UsportspyError(f"Invalid seaon(s): {bad_seasons_requested}\nPlease only use available seasons from: {a_seasons}")


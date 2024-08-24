import requests
import pandas as pd
from io import StringIO
import re

'''
Helper functions and classes
'''
class UsportspyError(Exception):
    def __init__(self, message="", detailed_err=None):
        if detailed_err:
            super().__init__(f"{message}\n\nTrue Error:\n{repr(detailed_err)}")
        else:
            super().__init__(f"{message}")


def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content)
        return None, df 
    except Exception as e:
        return e, None


def year_to_season(year):
    return f"{year}-{str((year % 100) + 1).zfill(2)}"


def available_seasons(tag):
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
    a_seasons = available_seasons(tag)

    bad_seasons_requested = sorted(list(set(seasons).difference(set(a_seasons))))
    if len(bad_seasons_requested):
        raise UsportspyError(f"Invalid seaon(s): {bad_seasons_requested}\nPlease only use available seasons from: {a_seasons}")


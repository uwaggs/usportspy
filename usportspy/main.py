import requests
import pandas as pd
from io import StringIO

def wrestling_athlete_rankings(gender, weight):
    if gender == "MALE":
        url = "https://github.com/uwaggs/wrestling/releases/download/wrestling_athlete_rankings/mens_athlete.csv"
    else:
        url = "https://github.com/uwaggs/wrestling/releases/download/wrestling_athlete_rankings/womens_athlete.csv"
        
    response = requests.get(url)
    response.raise_for_status()  
    
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df = df[df['Weight Category'] == str(weight) + 'kg']
    df = df.reset_index(drop=True)
    return df


def wrestling_team_rankings(gender):
    if gender == "MALE":
        url = "https://github.com/uwaggs/wrestling/releases/download/wrestling_team_rankings/mens_team.csv"
    else:
        url = "https://github.com/uwaggs/wrestling/releases/download/wrestling_team_rankings/womens_team.csv"
        
    response = requests.get(url)
    response.raise_for_status()  
    
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    
    return df



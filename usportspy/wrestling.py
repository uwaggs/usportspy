from . import helpers as h
from janitor import clean_names

'''
Wrestling Functions
'''
def wrestling_athlete_rankings(gender, weight=None):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_athlete_rankings/mens_athlete.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_athlete_rankings/womens_athlete.csv"

    err, df = h.get_data(url) 
    if err:
        raise h.UsportspyError(f"Error making request for wrestling athlete rankings for Gender: {gender} and Weight: {weight}kg.", err)

    if weight:
        df = df[df['Weight Category'] == str(weight) + 'kg']

    df = df.reset_index(drop=True)
    if len(df) == 0:
        raise h.UsportspyError(f"Error: {weight}kg is unavailable.")

    return clean_names(df)


def wrestling_team_rankings(gender):
    if gender not in ["m", "w"]:
        raise h.UsportspyError("'gender' must be either 'm' or 'w'.")

    if gender == "m":
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_team_rankings/mens_team.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_team_rankings/womens_team.csv"
        
    err, df = h.get_data(url) 
    if err:
        raise h.UsportspyError(f"Error making request for wrestling team rankings for Gender: {gender}.", err)

    return clean_names(df) 



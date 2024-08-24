from . import helpers as h

'''
Wrestling Functions
'''
def wrestling_athlete_rankings(gender, weight=None):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_athlete_rankings/mens_athlete.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_athlete_rankings/womens_athlete.csv"

    err, df = h.get_data(url) 
    if err:
        raise h.UsportspyError(f"Error makign request for wrestling athlete rankings for Gender: {gender} and Weight: {weight}kg.", err)

    if weight:
        df = df[df['Weight Category'] == str(weight) + 'kg']

    df = df.reset_index(drop=True)
    return df


def wrestling_team_rankings(gender):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    if gender == "MALE":
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_team_rankings/mens_team.csv"
    else:
        url = "https://github.com/uwaggs/usports-data/releases/download/wrestling_team_rankings/womens_team.csv"
        
    err, df = h.get_data(url) 
    if err:
        raise h.UsportspyError(f"Error makign request for wrestling team rankings for Gender: {gender}.", err)

    return df 



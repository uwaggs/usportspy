from . import helpers as h


'''
Swimming Functions
'''
def swimming_team_rankings():
    url = "https://github.com/uwaggs/usports-data/releases/download/swimming_team_rankings/swimming_team_rankings.csv"        
    err, df = h.get_data(url)
    if err:
        message = f"Error getting swimming team rankings."
        raise h.UsportspyError(message, err)
    return df 


def swimming_athlete_rankings():
    url = "https://github.com/uwaggs/usports-data/releases/download/swimming_athlete_rankings/swimming_athlete_rankings.csv"        
    err, df = h.get_data(url) 
    if err:
        message = f"Error getting swimming athlete rankings."
        raise h.UsportspyError(message, err)
    return df



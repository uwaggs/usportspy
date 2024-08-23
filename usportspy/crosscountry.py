from . import helpers as h

'''
Cross-Country Functions
'''
def xc_team_rankings(gender, seasons = [], universities = []):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    g = "MEN" if gender == "MALE" else "WOMEN"

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


    return df


def xc_rosters(gender, seasons = [], universities = []):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    g = "M" if gender == "MALE" else "F"
    
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

    return df


def xc_meet_results(seasons = [], universities = []):
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


    return df


def xc_universities():
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_universities/tnf_universities.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error making request for cross-country university data."
        raise h.UsportspyError(message, err)

    return df



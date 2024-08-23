from . import helpers as h


'''
Track and Field Functions
'''
def tnf_athlete_rankings(gender, seasons = [], athlete_names = [], events = [], universities = []):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    g = "men" if gender == "MALE" else "women"

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



    return df


def tnf_team_rankings(gender, seasons = [], universities = []):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    g = "Men" if gender == "MALE" else "Women"

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


    return df


def tnf_rosters(gender, seasons = [], universities = []):
    if gender not in ["MALE", "FEMALE"]:
        raise h.UsportspyError("'gender' must be either 'MALE' or 'FEMALE'.")

    g = "M" if gender == "MALE" else "F"

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

    return df


def tnf_meet_results(seasons = [], universities = []):
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


    return df


def tnf_universities():
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_universities/tnf_universities.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error making request for track and field university data."
        raise h.UsportspyError(message, err)

    return df



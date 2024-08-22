from . import helpers as h


'''
Track and Field Functions
'''
def tnf_athlete_rankings(athlete_names = [], events = [], universities = [], seasons = []):
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_athlete_rankings/tnf_athlete_rankings.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error getting track and field athlete rankings for athlete_names={athlete_names} events={events} and universities={universities} and seasons={seasons}."
        raise h.UsportspyError(message, err)

    if len(athlete_names):
        df = df.loc[df['Athlete Name'].isin(athlete_names)]

    if len(events):
        df = df.loc[df['Event'].isin(events)]

    if len(universities):
        df = df.loc[df['University'].isin(universities)]

    if len(seasons):
        df = df.loc[df['Season'].isin(seasons)]



    return df

def tnf_team_rankings(seasons = [], genders = [], universities = []):
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_team_rankings/tnf_team_rankings.csv"
    err, df = h.get_data(url) 

    if err:
        message = f"Error getting track and field team rankings for seasons={seasons} and genders={genders} and universities={universities}."
        raise h.UsportspyError(message, err)
    
    if len(seasons):
        df = df.loc[df['Season'].isin(seasons)]
    
    if len(genders):
        df = df.loc[df['Gender'].isin(genders)]

    if len(universities):
        df = df.loc[df['University'].isin(universities)]


    return df


def tnf_rosters(seasons = [], universities = []):
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_rosters/tnf_rosters.csv"
    err, df = h.get_data(url) 
   
    if err:
        message = f"Error getting track and field roster data for seasons={seasons} and universities={universities}."
        raise h.UsportspyError(message, err)

    if len(seasons):
        df = df.loc[df['Season'].isin(seasons)]
    
    if len(universities):
        df = df.loc[df['University'].isin(universities)]

    return df


def tnf_meet_results(seasons = [], universities = []):
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_meet_results/tnf_meet_results.csv"
    err, df = h.get_data(url)
    if err:
        message = f"Error getting track and field meet results for seasons={seasons} and universities={universities}."
        raise h.UsportspyError(message, err)

    def get_season(date):
        if "-" in date:
            month, day, year = date.split("-")[1].split("/")
        else:
            month, day, year = date.split("/")


        if month in ["11", "12"]:
            return f"{year}/{int(year) + 1}"
        else:
            return f"{int(year) - 1}/{year}"

    if len(seasons):
        df = df[df["Date"].apply(lambda x: get_season(str(x)) in seasons)]

    if len(universities):
        df = df.loc[df['University'].isin(universities)]


    return df



def tnf_universities():
    url = "https://github.com/uwaggs/usports-data/releases/download/tnf_universities/tnf_universities.csv"
    err, df = h.get_data(url)

    if err:
        message = f"Error getting track and field university data."
        raise h.UsportspyError(message, err)

    return df



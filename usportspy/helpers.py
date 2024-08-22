import requests
import pandas as pd
from io import StringIO


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



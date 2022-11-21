"""
Purpose of this module is to make an api request and load data into the postgres database.
"""
import json
import pandas as pd
import requests


env_vars = json.load(open('environments.json'))
URL_PATH = env_vars['data_collection']['URL_PATH']
DATA_PATH = env_vars['common']['DATA_PATH'] 
FILE_NAME = env_vars['common']['DATA']


def is_new():
    # Todo
    """Check if the file modified time is greater than the one we currently have."""
    return True

def get_data():
    """Make a url request and get the data"""
    if (URL_PATH and DATA_PATH) and is_new():
        resp = requests.get(URL_PATH)
        with open(f'{DATA_PATH}/{FILE_NAME}', 'wb') as f:
            f.write(resp.content)
        

if __name__=='__main__':
    try:
        get_data()
    except Exception as e:
        print(f"Exception raised: {e}")

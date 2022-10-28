"""
Purpose of this module is to make an api request and load data into the postgres database.
"""
import os
import pandas as pd
import requests

def get_data():
    data = None
    """Make a url request and get the data"""
    url_path = os.environ.get('URL_PATH', None)
    data_loc = os.environ.get('DATA_PATH', None)
    if url_path and data_loc:
        resp = requests.get(url_path)
        with open(f'{data_loc}/dataset.csv', 'wb+') as f:
            f.write(resp.content)
        return True


if __name__=='__main__':
    if get_data():
        print("Success!")
    else:    
        print("Fail")    
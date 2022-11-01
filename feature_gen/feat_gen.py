import os
import pandas as pd
from pathlib import Path


DATA = os.environ.get('DATA', False)
DATA_PATH = os.environ.get('DATA_PATH', False)
COL_NAMES = os.environ.get('COLUMN_NAMES', None).split(',')


class NoDataError(Exception):
    def __init__(self, data_path=None):
        self.data_path = data_path

    def __str__(self):
        return f"No dataset present in the location. {self.data_path}"

class FeatGen:
    def __init__(self) -> None:
        self.df = None

    def does_file_exist(func):
        def wrapper(obj):
            p = Path(DATA_PATH +'/'+ DATA)           
            if p.exists():
                func(obj)
            else:
                raise NoDataError(data_path=DATA_PATH)
        return wrapper
    
    @does_file_exist
    def load_data(self):
        self.df = pd.read_csv(DATA_PATH +'/'+ DATA, header=None, names=COL_NAMES)
        print (self.df.head(5))

    def save_features(self):
        self.df.to_csv(f'{DATA_PATH}/df_cleaned.csv')

if __name__ == '__main__':
    features = FeatGen()
    features.load_data()
    features.save_features()
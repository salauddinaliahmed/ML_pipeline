import json
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from feat_gen_utils import process_col

env_vars = json.load(open('environments.json'))
DATA_PATH = env_vars['common']['DATA_PATH']
DATA = env_vars['common']['DATA']
COL_NAMES = env_vars['feature_gen']['COLUMN_NAMES'].split(',')

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
                raise NoDataError(data_path=p)
        return wrapper
    
    @does_file_exist
    def load_data(self):
        self.df = pd.read_csv(DATA_PATH +'/'+ DATA, header=None, names=COL_NAMES)
        
    def pre_process(self):
        self.df = process_col(self.df, column='sex')
    
    def save_features(self, df=None, fname="dataset"):
        if df is None:
            df = self.df
        df.to_csv(f'{DATA_PATH}/{fname}.csv', index=False)

    def create_train_test(self):
        # Features and target variable
        X = self.df.iloc[:,0:-1]
        y = self.df.iloc[:,-1]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.30, random_state=42
        )
        work = {
            'X_train': X_train,
            'X_test': X_test,
            'y_train': y_train,
            'y_test': y_test
        }
        list(
            map(lambda data: self.save_features(df=data[1], fname=data[0]), work.items())
        )


if __name__ == '__main__':
    features = FeatGen()
    features.load_data()
    features.pre_process()
    features.save_features()
    features.create_train_test()
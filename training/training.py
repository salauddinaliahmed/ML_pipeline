import json
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression


env_vars = json.load(open('environments.json'))
TRAINED_MODEL = MODEL =env_vars['common']['TRAINED_MODEL']
DATA_PATH=env_vars['common']['DATA_PATH']

class Train:
    X_train, y_train = env_vars['training']['TRAIN_DS'].split(",")
    X_test, y_test = env_vars['training']['TEST_DS'].split(",")

    def __init__(self) -> None:
        self.clf = LinearRegression()
        self.model = None
        self.X_train = pd.read_csv(f'{DATA_PATH}/{Train.X_train}.csv')
        self.y_train = pd.read_csv(f'{DATA_PATH}/{Train.y_train}.csv')
        self.X_test = pd.read_csv(f'{DATA_PATH}/{Train.X_test}.csv')
        self.y_test = pd.read_csv(f'{DATA_PATH}/{Train.y_test}.csv')

    def _save_model(self):
        pickle.dump(self.model, open(f'{DATA_PATH}/{MODEL}', 'wb'))
        
    def train(self):
        self.model = self.clf.fit(self.X_train, self.y_train)
        self._save_model()

    def test(self):
        model_accuracy = self.clf.score(self.X_test, self.y_test)
        print(model_accuracy)


if __name__ == "__main__":
    t = Train()
    t.train()
    t.test()

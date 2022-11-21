import pickle
import json


env_vars = json.load(open('environments.json'))
TRAINED_MODEL = env_vars['common']['TRAINED_MODEL']
DATA_PATH = env_vars['common']['DATA_PATH']


class Infer:
    MODEL_FILE_PATH = DATA_PATH+'/'+TRAINED_MODEL
    def __init__(self):
        self.model = pickle.load(open(Infer.MODEL_FILE_PATH, 'rb'))
    
    def mock_data(self):
        mockdata = [[2,96,74,31,1624,796,599,582]]
        print("Predicted age: ", self.model.predict(mockdata))


if __name__ == '__main__':
    i = Infer()
    i.mock_data()

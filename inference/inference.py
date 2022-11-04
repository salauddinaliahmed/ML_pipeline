import pickle
import os

class Infer:
    MODEL_FILE_PATH = os.environ.get('DATA_PATH')+'/'+os.environ.get('TRAINED_MODEL')
    def __init__(self):
        self.model = pickle.load(open(Infer.MODEL_FILE_PATH, 'rb'))
    
    def mock_data(self):
        mockdata = [[2,96,74,31,1624,796,599,582]]
        print("Predicted age: ", self.model.predict(mockdata))


if __name__ == '__main__':
    i = Infer()
    i.mock_data()

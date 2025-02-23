import pickle
import traceback
from ClassInfo import Product

class FileUtil:
    @staticmethod
    def saveModel(model, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(model, f)
            return True
        except:
            traceback.print_exc()
            return False

    @staticmethod
    def loadModel(filename):
        try:
            with open(filename, 'rb') as f:
                model = pickle.load(f)
            return model
        except:
            traceback.print_exc()
            return None

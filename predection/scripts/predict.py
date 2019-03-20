import sys, os
import pickle

import numpy

import warnings
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    x = numpy.array([[float(i) for i in sys.argv[1:]]])
    models = pickle.load(open('../model/model.pkl', 'rb'))
    preds = 0
    for model in models:
        preds += model.predict(x) / len(models)
    print(preds[0])
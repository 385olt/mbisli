import os
import pickle

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

data = pickle.load(open(basedir + '/data.dat', 'rb'))
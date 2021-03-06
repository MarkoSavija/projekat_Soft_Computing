#import potrebnih biblioteka
import cv2
import glob
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pandas as pd
 
 # keras
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD

def convert_output(outputs):
    return np.eye(len(outputs))

#parsiranje podataka o slikama iz csv fajlova
#uzimam sve podatke iz .csv datoteke osim prvog clana jer je to naziv slike
#podaci predstavljaju opis slike
def parse(csv):
  img_dsc = pd.read_csv(csv)
  data = img_dsc[1:]

  return data

def create_ann():  
  ann = Sequential()
  # Postavljanje slojeva neurona mreze 'ann'
  ann.add(Dense(input_dim=1441, output_dim=128,init="glorot_uniform"))
  ann.add(Activation("sigmoid"))
  ann.add(Dense(input_dim=128, output_dim=3,init="glorot_uniform"))
  ann.add(Activation("sigmoid"))
  return ann
    
def train_ann(ann, X_train, y_train):
  print 'Obucavanje . . .'
  X_train = np.array(X_train, np.float32)
  y_train = np.array(y_train, np.float32)

  # definisanje parametra algoritma za obucavanje
  sgd = SGD(lr=0.01, momentum=0.9)
  ann.compile(loss='mean_squared_error', optimizer=sgd)

  # obucavanje neuronske mreze
  ann.fit(X_train, y_train, nb_epoch=500, batch_size=1, verbose = 0, shuffle=False, show_accuracy = False) 
    
  return ann

dsc = []
csvFolderPath = '/csv_files'

for csvPath in glob.glob(csvFolderPath + '/*.csv'):
  dsc.append(parse(csvPath))

alphabet = ['audi','mercedes']   #definisem alfabet
target = convert_output(alphabet)  #pretvara u eye matricu
ann = create_ann()
ann = train_ann(ann, dsc, target)   #data-input podaci    target-output
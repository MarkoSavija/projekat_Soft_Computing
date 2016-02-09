import cv2
import glob
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from sklearn import datasets
from sklearn import svm

def parse(csv):
  img_dsc = np.genfromtxt(csv, delimiter = ',')
  data = img_dsc[~np.isnan(img_dsc)]

  return data

dsc = []
csvFolderPath = '/home/student/Logo_tracker_aplikacija/clt/csv_files'

for csvPath in glob.glob(csvFolderPath + '/*.csv'):
  dsc.append(parse(csvPath)) #ovo mi je ustvari logo.data

logo_targets = ['audi','mercedes']

clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(dsc, logo_targets)  
svm.SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

#testiranje

test_dsc = []
testFolderPath = '/home/student/Logo_tracker_aplikacija/clt/test_files'

for csvPath in glob.glob(testFolderPath + '/*.csv'):
  test_dsc.append(parse(csvPath)) #ovo mi je ustvari logo.data

#clf.predict(test_dsc[0])
print len(dsc[0]) 

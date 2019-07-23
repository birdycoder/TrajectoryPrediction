#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : SVMevaluation.py
# @Author: Jeff Liu
# @Date  : 2019/6/17
# @Desc  : model training and evaluation using cross validation

from sklearn import svm
import numpy as np
import os
from sklearn import preprocessing
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from preprocess import Endalarm
import time
song = os.path.dirname(os.getcwd())+'/preprocess/song.mp3'
'''training data and test data setting'''
feature_data = np.load(os.path.dirname(os.getcwd())+'/processedDATA/ftrVecData-th8-fre100(dirNote).npy', encoding="latin1")
# trk_list = np.load(os.path.dirname(os.getcwd())+'/processedDATA/lenSortDATA(72X48)th8.npy', encoding="latin1")

X = feature_data
Y = np.load(os.path.dirname(os.getcwd())+'/processedDATA/LabelY.npy', encoding="latin1")

start = time.time()
clf = svm.SVC(C=1, cache_size=600, gamma=1/len(feature_data[0]), kernel='rbf', decision_function_shape='ovo', max_iter=-1, class_weight= 'balanced')
score = cross_val_score(clf, X, Y, cv = 5)
end = time.time()
print('running time: '+ str(end - start))
print(score)
dump(clf, 'SVMmodel(dirNote)CV.joblib')
Endalarm.alarm(song)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : svm_prediction.py
# @Author: Jeff Liu
# @Date  : 2019/5/30
# @Desc  :

from sklearn import svm
import numpy as np
import os
from sklearn import preprocessing
from joblib import dump, load
from preprocess import Endalarm


def model_evaluate(model, testX, testY):
    total = len(testX)
    accuracy = 0.0
    for idx, vec in enumerate(testX):
        if model.predict([vec]) == testY[idx]:
            accuracy += 1
        print('sample '+ str(idx) + ' done')
    accuracy = accuracy / total
    return accuracy


def get_res(model, testX):
    res = []
    for idx, vec in enumerate(testX):
        res.append(model.predict([vec]))
    return res


def getDirectLabel(pos, pre):
    if pos - pre > 46 :
        return 1
    elif pos - pre < -46:
        return 2
    elif pos - pre < 0:
        return 3
    else:
        return 4

'''training data and test data setting'''
feature_data = np.load(os.path.dirname(os.getcwd())+'/processedDATA/ftrVecData-th8-fre100(vote&dir).npy', encoding="latin1")
# trk_list = np.load(os.path.dirname(os.getcwd())+'/processedDATA/lenSortDATA(72X48)th8.npy', encoding="latin1")

X = feature_data
Y = np.load(os.path.dirname(os.getcwd())+'/processedDATA/LabelY.npy', encoding="latin1")

# for trk in trk_list:
#     Y.append(getDirectLabel(trk[-1], trk[-2]))

# np.save(os.path.dirname(os.getcwd())+'/processedDATA/LabelY.npy', Y)

length = int(len(X)*0.8)

train_X = X[:length]
train_Y = Y[:length]

test_X = X[length:]
test_Y = Y[length:]


bool_eva = 0
train_model = 'SVMmodel(vote&dir).joblib'
test_model = 'SVMmodel(vote&dir).joblib'
song = 'song.mp3'

import time

if not bool_eva:
    clf = svm.SVC(C=3, cache_size=1000, gamma=0.001, kernel='rbf', decision_function_shape='ovo', max_iter=-1)

    # clf.gamma =
    # clf.class_weight = 'balanced'
    # clf.max_iter = -1


    # train
    start = time.time()
    print('train begin...')
    clf.fit(train_X, train_Y)
    print('train finished')
    end = time.time()
    print('running time:'+str((end - start)/60.0)+ ' mins')

    # model save
    dump(clf, train_model)
    print('Evaluation begin')
    trainres = clf.score(train_X[:1000], train_Y[:1000])
    testres = clf.score(test_X[:], test_Y[:])
    print(trainres)
    print(testres)
    Endalarm.alarm(song)


if bool_eva:
    # model load
    clf = load(test_model)
    # clf.C = 2
    # clf.max_iter = 100
    # clf.fit(train_X, train_Y)
    # a = get_res(clf, test_X[:1000])
    print('Evaluation begin')
    trainres = clf.score(train_X[:1000], train_Y[:1000])
    testres = clf.score(test_X[:], test_Y[:])
    # res = clf.score(train_X[:100], train_Y[:100])

    # res = model_evaluate(clf, train_X[:10000], train_Y[:10000])
    print(trainres)
    print(testres)
    Endalarm.alarm(song)

    # C = 1, no scale
    # model iter: until tol, fitness = 40.55%
    # ftrVec X: ftrVecData-th8-fre100(dire).npy,
    # based on the last move of corresponding fss(1,2,3,4),
    # Y: based on on direction of the last move (1,2,3,4)

    # C = 1, with scale
    # model iter: until tol(1e-3), fitness = 43.9%
    # featureVec X: ftrVecData-th8-fre100(dire2)
    # based on the move after corresponding fss(+1,-1, 48, -48), (preprocess: scale) \
    # Y: based on direction of the last move (1,2,3,4)

    # C = 1, no scale
    # model iter: until tol, fitness = 43.5%
    # ftrVec X: ftrVecData-th8-fre100(dirNote).npy,
    # based on the move after corresponding fss(1,2,3,4),
    # Y: based on on direction of the last move (1,2,3,4)

    # C = 1, no scale
    # model iter: until tol, fitness = 42.75%
    # ftrVec X: ftrVecData-th8-fre100(basic).npy,
    # based on the existance of corresponding fss(1 if exist, else 0),
    # Y: based on direction of the last move (1,2,3,4)

    # C = 3, no scale no weight balanced
    # model iter: until tol, fitness = 37%
    # ftrVec X: ftrVecData-th8-fre100(votelast).npy,
    # based on the existance of corresponding fss(1 if exist, else 0),and last match fss vote direction
    # Y: based on direction of the last move (1,2,3,4)

    #
    # C=1, cache_size=1000, gamma=0.1, kernel='rbf', decision_function_shape='ovo', max_iter=-1
    # 44.86%

    # C=1, cache_size=1000, gamma=0.05, kernel='rbf', decision_function_shape='ovo', max_iter=-1
    # 46.12%

    # C=1, cache_size=1000, gamma=0.01, kernel='rbf', decision_function_shape='ovo', max_iter=-1
    # 43.4%

    # C=3, cache_size=1000, gamma=0.05, kernel='rbf', decision_function_shape='ovo', max_iter=-1
    # 47.08%

    # C=5, cache_size=1000, gamma=0.05, kernel='rbf', decision_function_shape='ovo', max_iter=-1
    # 46.54%

    # C=3, cache_size=1000, gamma=0.05, kernel='rbf', decision_function_shape='ovo', class_weight='balanced', max_iter=-1)
    # 46.98%

    # vote&dir
    # C = 3, cache_size = 1000, gamma = 0.05, kernel = 'rbf', decision_function_shape = 'ovo', max_iter = -1
    # train ac 86.8, test ac 38.85

    # C=3, cache_size=1000, gamma=0.01, kernel='rbf', decision_function_shape='ovo', max_iter=-1
    # 78.5， 44.5

    # C=3, cache_size=1000, gamma=0.006, kernel='rbf', decision_function_shape='ovo', max_iter=-1)
    # 72.9 45.69
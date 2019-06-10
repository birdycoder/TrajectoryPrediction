#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : svm_prediction.py
# @Author: Jeff Liu
# @Date  : 2019/5/30
# @Desc  :

from sklearn import svm
import numpy as np
import os
feature_data = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/featureVecData-th200.npy', encoding="latin1")
label = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/after_label_arr(72X48).npy', encoding="latin1")
X = feature_data

Y = []
length = int(len(X)*0.8)
for trk in label:
    Y.append(trk[-1])

train_X = X[:length]
train_Y = Y[:length]

test_X = X[length:]
test_Y = Y[length:]

clf = svm.SVC(gamma='scale', decision_function_shape='ovo', max_iter=2)

from joblib import dump, load
clf = load('SVMmodel.joblib')


def model_evaluate(model, testX, testY):
    total = len(testX)
    accuracy = 0.0
    for idx, vec in enumerate(testX):
        if model.predict([vec]) == testY[idx]:
            accuracy += 1
        print('sample '+ str(idx) + ' done')
    accuracy = accuracy / total
    return accuracy

res = model_evaluate(clf, test_X[:100], test_Y[:100])
print(res)
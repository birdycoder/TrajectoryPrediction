#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : SGD.py
# @Author: Jeff Liu
# @Date  : 2019/5/29
# @Desc  :

from sklearn.linear_model import SGDClassifier
import numpy as np
import os

feature_data = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/featureVecData-th200.npy', encoding="latin1")
label = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/after_label_arr(72X48).npy', encoding="latin1")
X = feature_data

Y = []
for trk in label:
    Y.append(trk[-1])

length = int(len(X)*0.8)
train_X = X[:length]
train_Y = Y[:length]

test_X = X[length:]
test_Y = Y[length:]

clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=1)




from joblib import dump, load
# dump(clf, 'SGDmodel.joblib')


def model_evaluate(model, testX, testY):
    total = len(testX)
    accuracy = 0.0
    for idx, vec in enumerate(testX):
        if model.predict([vec]) == testY[idx]:
            accuracy += 1
        print('sample '+ str(idx) + ' done')
    accuracy = accuracy / total
    return accuracy

clf = load('SGDmodel.joblib')

res = model_evaluate(clf, test_X, test_Y)
print(res)

# 14% accuracy
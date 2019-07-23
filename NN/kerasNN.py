#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : kerasNN.py
# @Author: Jeff Liu
# @Date  : 2019/5/29
# @Desc  :

from keras.preprocessing import sequence
from keras import models, regularizers
from keras import layers
from keras import utils
from keras.models import load_model
import numpy as np
import os
from preprocess import Endalarm
song = 'song.mp3'

X = np.load(os.path.dirname(os.getcwd())+'/processedDATA/ftrVecData-th8-fre100(vote&dir).npy', encoding="latin1")
# trk_list = np.load(os.path.dirname(os.getcwd())+'/processedDATA/lenSortDATA(72X48)th8.npy', encoding="latin1")
Y = np.load(os.path.dirname(os.getcwd())+'/processedDATA/LabelY.npy', encoding="latin1")

length = int(len(X)*0.8)

train_X = X[:length]
train_Y = Y[:length]-1

test_X = X[length:]
test_Y = Y[length:]-1

train_Y = utils.to_categorical(train_Y, 4)
test_Y = utils.to_categorical(test_Y, 4)

input_dim = len(X[0])
def build_model(input_dim, output_dim):
    model = models.Sequential()
    model.add(layers.Dense(1024, activation='relu', input_shape=(input_dim,),
                           kernel_regularizer = regularizers.l2(0.01)
                           ))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(1024, activation='relu', kernel_regularizer = regularizers.l2(0.01)))
    model.add(layers.Dense(output_dim, activation='sigmoid'))
    # compile model
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

def build_CNN():
    model = models.Sequential()
    model.add(layers.Conv1D(filters=64, kernel_size=5, activation='relu', input_shape=(2843, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(4, activation='softmax', kernel_regularizer = regularizers.l2(0.01)))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


m_name = 'MLP2.h5'
Cname = 'CNN.h5'
import time
start = time.time()
option = 2
if option == 0:
    nn = build_model(input_dim, 4)
    nn.fit(train_X, train_Y, batch_size=100, epochs=20, verbose=1, validation_data=(test_X, test_Y))
    nn.save(m_name)

if option == 1:
    nn = load_model(m_name)
    nn.fit(train_X, train_Y, batch_size=40, epochs=100, verbose=1, validation_data=(test_X, test_Y))
    nn.save(m_name)

if option == 2:
    len_feature = len(train_X[0])
    X_train_r = np.zeros((len(train_X), 2843, 2))
    X_train_r[:, :, 0] = train_X[:, :2843]
    X_train_r[:, :, 1] = train_X[:, 2843:]

    X_test_r = np.zeros((len(test_Y), 2843, 2))
    X_test_r[:, :, 0] = test_X[:, :2843]
    X_test_r[:, :, 1] = test_X[:, 2843:]


    nn = build_CNN()
    nn.fit(X_train_r, train_Y, batch_size=20, epochs=6, verbose=1, validation_data=(X_test_r, test_Y))
    nn.save(Cname)

if option == 3:
    len_feature = len(train_X[0])
    X_train_r = np.zeros((len(train_X), 2843, 2))
    X_train_r[:, :, 0] = train_X[:, :2843]
    X_train_r[:, :, 1] = train_X[:, 2843:]

    X_test_r = np.zeros((len(test_Y), 2843, 2))
    X_test_r[:, :, 0] = test_X[:, :2843]
    X_test_r[:, :, 1] = test_X[:, 2843:]
    nn = load_model(Cname)
    nn.fit(X_train_r, train_Y, batch_size=20, epochs=2, verbose=1, validation_data=(X_test_r, test_Y))
    nn.save(Cname)


end = time.time()
print('running time:')
print((end-start)/3600.0)
Endalarm.alarm(song)
# 30 epoch
# loss: 0.3420 - acc: 0.8500 - val_loss: 2.8234 - val_acc: 0.4833
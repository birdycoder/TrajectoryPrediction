#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LSTM.py
# @Author: Jeff Liu
# @Date  : 2019/7/17
# @Desc  :

from keras import models, regularizers
from keras import layers
from keras import utils
from keras.models import load_model
import numpy as np
import os
from preprocess import Endalarm
import time
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

X_train_r = np.zeros((len(train_X), 2843, 2))
X_train_r[:, :, 0] = train_X[:, :2843]
X_train_r[:, :, 1] = train_X[:, 2843:]

X_test_r = np.zeros((len(test_Y), 2843, 2))
X_test_r[:, :, 0] = test_X[:, :2843]
X_test_r[:, :, 1] = test_X[:, 2843:]


num_train = 10000
num_test = 1000

X_train_r = X_train_r[:num_train]
train_Y = train_Y[:num_train]

X_test_r = X_test_r[:num_test]
test_Y = test_Y[:num_test]


from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np



# 期望输入数据尺寸: (batch_size, timesteps, data_dim)
# 请注意，我们必须提供完整的 batch_input_shape，因为网络是有状态的。
# 第 k 批数据的第 i 个样本是第 k-1 批数据的第 i 个样本的后续。
def build_model():
    model = Sequential()
    model.add(LSTM(32, return_sequences=True,   input_shape=(2843, 2)))
    model.add(LSTM(32, return_sequences=True))
    model.add(LSTM(32))
    model.add(Dense(4, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    return model

option = 2
start = time.time()
if option == 1:

    model = build_model()
    model.fit(X_train_r, train_Y,
              batch_size=100, epochs=5, shuffle=False, verbose=1,
              validation_data=(X_test_r, test_Y))
    model.save('lstm_model.h5')

if option == 2:
    model = load_model('lstm_model.h5')
    model.fit(X_train_r, train_Y,
              batch_size=100, epochs=5, shuffle=False, verbose=1,
              validation_data=(X_test_r, test_Y))
    model.save('lstm_model.h5')

song = 'song.mp3'
end = time.time()
print('running time:')
print((end-start)/60.0)
Endalarm.alarm(song)
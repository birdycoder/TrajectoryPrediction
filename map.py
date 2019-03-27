#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : map.py
# @Author: Jeff Liu
# @Date  : 2019/2/17
# @Desc  :

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import math

'''Global setting'''
m_width = 720
m_height = 480

g_width = 72
g_height = 48

cell_width = m_width/g_width
cell_height = m_height/g_height

#control bool value
bool_data_extract = 0
bool_tran = 0
bool_label = 0

'''map discretization function'''
def trk_trans(trk):
    '''
    Transform the each cordinate to according discretization vertex
    :param trk: track
    :type trk: ndarray
    :return: none
    :rtype: none
    '''
    for pos in trk:
        x = (pos[0]/cell_width)
        y = (pos[1]/cell_height)
        pos[0] = x
        pos[1] = y

def trk_shrink(trk):
    '''
    shrink the track
    :param trk: track after transformation
    :type trk: ndarray
    :return: track after shrinking
    :rtype: ndarray
    '''
    new_trk = []
    for idx in range(len(trk)-1):
        if not cord_equal(trk[idx],trk[idx+1]):
            new_trk.append(trk[idx])
    new_trk.append(trk[-1])
    return np.array(new_trk)


def cord_equal(cord1, cord2):
    '''
    Check if two cordinate is equal
    :param cord1: cordinate1
    :type cord1: list
    :param cord2: cordinate2
    :type cord2: list
    :return: bool
    :rtype: bool
    '''
    return cord1[0] == cord2[0] and cord1[1] == cord2[1]

'''Datafile extraction'''
if bool_data_extract == 1:
    dataFile = 'matlab_tracklets.mat'
    data_original = scipy.io.loadmat(dataFile)
    _trks_original = data_original['trks'][0]
    data_train = _trks_original[0:]

    trk_list = []
    for trk in data_train[:]:
        trk_x = trk[1]
        trk_y = trk[2]
        path = []
        for pos in range(len(trk_x)):
            node = np.array([int(trk_x[pos][0]), int(trk_y[pos][0])])
            path.append(node)
        path = np.array(path)
        trk_list.append(path)
        print ('track added')
    trk_array = np.array(trk_list)
    np.save('trk_arr.npy',trk_array)


if bool_tran == 1:
    '''Read data (numpy array)'''
    trk_arr = np.load('trk_arr.npy')

    '''track transform and shrink'''
    for trk in trk_arr[:]:
        trk_trans(trk)
    print ('transform done')

    for idx in range(len(trk_arr)):
        trk_arr[idx] = trk_shrink(trk_arr[idx])
    print ('shrinking done')
    np.save('after_tran_arr.npy', trk_arr)



af_arr = np.load('after_tran_arr.npy')

'''label function'''
def trkToLabel(trk):
    trk_label = []
    for pos in trk:
        label = (pos[0]-1)*g_height + pos[1]
        trk_label.append(label)
    return trk_label

if bool_label == 1:
    label_arr = []
    for trk in af_arr:
        label_arr.append(trkToLabel(trk))
    after_label_arr = np.array(label_arr)
    np.save('after_label_arr.npy', after_label_arr)

af_label_arr = np.load('after_label_arr.npy',encoding="latin1")


# number of tracks
num_trk = len(af_label_arr)
# transfer label track to list type
af_label_arr.tolist()

'''train set and test set setup
    80% training set and rest test set'''
train_set = af_label_arr[:(int(num_trk*0.8))]
test_set = af_label_arr[(int(num_trk*0.8)):]




import Predict as Pre
import Evaluation as Eva
from prefixspan import PrefixSpan


num_step = 1
tset = test_set[:2000]
res = Eva.evaluate(train_set, tset, 2)



print ('hh')


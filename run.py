#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: Jeff Liu
# @Date  : 2019/3/29
# @Desc  : main func


# map size
m_width = 720
m_height = 480

# defining grid size
g_width = 72
g_height = 48
mode = 2

# cell size(depending on the grid size)
cell_width = m_width/g_width
cell_height = m_height/g_height

# control bool value
bool_data_extract = 0
bool_tran = 0
bool_label = 0

import map
import Evaluation as eva
import numpy as np

def run(mode, g_width, g_height):
    data = np.load('Transformed_DATA/after_label_arr'+'('+ str(g_width) + 'X' + str(g_height)+')' + '.npy', encoding="latin1")

    # number of tracks
    num_trk = len(data)
    # transfer label track to list type
    data.tolist()

    '''train set and test set setup
        80% training set and rest test set'''
    train_set = data[:(int(num_trk * 0.8))]
    test_set = data[(int(num_trk * 0.8)):]
    if mode == 1:
        res = eva.evaluate(train_set, test_set, 2)
        print('Predicting the last step of each track according its second last step')
        print('Accuracy: ' + str(res))
    if mode == 2:
        res = eva.seq_evaluate(train_set, test_set, 4, 3)
        print('Predicting the last step of each track according its second and third last step(sequence)')
        print('Accuracy: ' + str(res))


run(mode, g_width, g_height)
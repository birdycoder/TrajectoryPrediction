#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: Jeff Liu
# @Date  : 2019/3/29
# @Desc  : main func

import map
import Evaluation as eva
import numpy as np

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
        res = eva.seq_evaluate(train_set, test_set[:100], 4, 3)
        print('Predicting the last step of each track according its second and third last step(sequence)')
        print('Accuracy: ' + str(res))


run(mode, g_width, g_height)

# grid size: 72x48
# predict the last step according to the last second step
#res = Eva.evaluate(train_set, tset, 2)
# one step result: 38.76%

# predict last step according to the previous two step
# two_step_res = Eva.seq_evaluate(train_set, tset, 3, 2)
# two step accuracy = 50.76%

# predict last step according to the previous 3 steps
# two_step_res = Eva.seq_evaluate(train_set, tset, 4, 3)
# two step accuracy = 58.72%


# grid size: 36x24
# 1.predict the last step according to the last second step
# accuracy: 40.86%
# 2.predict last step according to previous two step
# accuracy = 55.84%




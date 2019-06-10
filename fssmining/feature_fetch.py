#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : feature_fetch.py
# @Author: Jeff Liu
# @Date  : 2019/5/28
# @Desc  : frequent sub-sequence feature fetch

import numpy as np


def seq_match(seq, trk):
    if len(seq) >= len(trk):
        return False
    len_seq = len(seq)
    for pos in range(len(trk) - len_seq):
        if trk[pos:(pos + len_seq)] == seq and pos != len(trk) - len_seq:
            return True
    return False


def feature_fetch(fssset, trk):
    feature_vec = np.zeros(len(fssset))
    for fss_id, fss in enumerate(fssset):
        if seq_match(fss[0], trk):
            feature_vec[fss_id] = 1
    return feature_vec

import os
from map import g_width, g_height
data = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/after_label_arr'+'('+ str(g_width) + 'X' + str(g_height)+')' + '.npy', encoding="latin1")


def get_featurevec(threshold, data):
    fssdata = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/confssData2-th'+str(threshold)+'.npy', encoding="latin1")
    vec_list = []
    for idx, sample in enumerate(data):
        vec = feature_fetch(fssdata, sample)
        vec_list.append(vec)
        print('sample '+str(idx)+' done')
    vec_list = np.array(vec_list)
    np.save(os.path.dirname(os.getcwd())+'/Transformed_DATA/featureVecData-th'+str(threshold)+'.npy', vec_list)


feature_data = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/featureVecData-th200.npy', encoding="latin1")

count = 0
new_list = []
for idx, sample in enumerate(data):
    temp = np.append(feature_data[idx], sample[-1])
    new_list.append(temp)

new_list = np.array(new_list)
np.save(os.path.dirname(os.getcwd())+'/FeatureDATA/featureData-th200.npy', new_list)

print('a')
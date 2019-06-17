#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : feature_fetch.py
# @Author: Jeff Liu
# @Date  : 2019/5/28
# @Desc  : frequent sub-sequence feature fetch

import numpy as np
import os
# first version seq_match
# def seq_match(seq, trk):
#     if len(seq) >= len(trk):
#         return False
#     len_seq = len(seq)
#     for pos in range(len(trk) - len_seq):
#         if trk[pos:(pos + len_seq)] == seq and pos != len(trk) - len_seq:
#             return True
#     return False


def get_direct_label(pos, pre):
    if pos - pre > 46 :
        return 1
    elif pos - pre < -46:
        return 2
    elif pos - pre < 0:
        return 3
    else:
        return 4


def seq_match(seq, trk):
    if len(seq) >= len(trk):
        return False
    seq = seq[:-1]
    len_seq = len(seq)
    for pos in range(len(trk) - len_seq + 1):
        if trk[pos:(pos + len_seq)] == seq and pos != len(trk) - len_seq:
            return get_direct_label(trk[pos + len_seq], trk[pos + len_seq - 1])
    return False


def feature_fetch(fssset, trk):
    '''
    return the feature vector(method: if consists of fss, set to 1)
    :param fssset:
    :type fssset:
    :param trk:
    :type trk:
    :return:
    :rtype:
    '''
    feature_vec = np.zeros(len(fssset))
    for fss_id, fss in enumerate(fssset):
        if seq_match(fss[0], trk):
            feature_vec[fss_id] = 1
    return feature_vec

def feature_fetch_dire(fssset, trk):
    '''
    return the feature vector(method: vector based on the last move of the fss)
    :param fssset:
    :type fssset:
    :param trk:
    :type trk:
    :return:
    :rtype:
    '''
    feature_vec = np.zeros(len(fssset))
    for fss_id, fss in enumerate(fssset):
        flag = seq_match(fss[0], trk)
        if flag:
            feature_vec[fss_id] = flag
    return feature_vec

def direct_ftr_fetch(fssset, trk):
    pass


def get_featurevec(fssdata, dataset):
    # fssdata = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/confssData-th'+str(threshold)+'.npy', encoding="latin1")
    vec_list = []
    for idx, sample in enumerate(dataset):
        vec = feature_fetch_dire(fssdata, sample)
        vec_list.append(vec)
        print('sample '+str(idx)+' done')
    vec_list = np.array(vec_list)
    np.save(os.path.dirname(os.getcwd())+'/processedDATA/ftrVecData-th8-fre100(dirNote).npy', vec_list)
    return vec_list


# def get_direction(pre, pos):
#     res = pos - pre
#     return res



#

feature = np.load(os.path.dirname(os.getcwd())+'/processedDATA/featureVecData-th8-fre100.npy', encoding="latin1")

fssdata = np.load(os.path.dirname(os.getcwd())+'/processedDATA/confssDATAth8fre100.npy', encoding="latin1")
raw_data = np.load(os.path.dirname(os.getcwd())+'/processedDATA/lenSortDATA(72X48)th8.npy', encoding="latin1")

res = get_featurevec(fssdata, raw_data)

# count = 0
# for idx, vec in enumerate(res):
#     if vec.max() == 0:
#         print(idx)
#         count += 1

# data = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/after_label_arr'+'('+ str(72) + 'X' + str(48)+')' + '.npy', encoding="latin1")
#
#
# new_list = []
# for idx, sample in enumerate(data):
#     feature_data[idx][-1] = get_direction(sample[-2], sample[-1])
#     new_list.append(feature_data[idx])
#
#
# new_list = np.array(new_list)
# np.save(os.path.dirname(os.getcwd())+'/FeatureDATA/featureData-th200(direct).npy', new_list)


print('a')
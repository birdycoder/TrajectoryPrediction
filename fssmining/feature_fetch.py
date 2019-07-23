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
    '''

    :param pos:
    :type pos:
    :param pre:
    :type pre:
    :return:
    :rtype:
    '''
    if pos - pre > 46 :
        # up
        return 1
    elif pos - pre < -46:
        # down
        return 2
    elif pos - pre < 0:
        # left
        return 3
    else:
        # right
        return 4

# old version seq_match:
# def seq_match(seq, trk):
#     if len(seq) >= len(trk):
#         return False
#     seq = seq[:-1]
#     len_seq = len(seq)
#     for pos in range(len(trk) - len_seq + 1):
#         if trk[pos:(pos + len_seq)] == seq and pos != len(trk) - len_seq:
#             return get_direct_label(trk[pos + len_seq], trk[pos + len_seq - 1])
#     return False


# dirNote seq_match
# def seq_match(seq, trk):
#     if len(seq) >= len(trk):
#         return False
#     seq = seq[:-1]
#     len_seq = len(seq)
#     if trk[-len_seq:] == seq:
#         return 10
#     for pos in range(len(trk) - len_seq + 1):
#         if trk[pos:(pos + len_seq)] == seq and pos != len(trk) - len_seq:
#             return get_direct_label(trk[pos + len_seq], trk[pos + len_seq - 1])
#     return False


# last match fss vote version seq_match
def seq_match(seq, trk):
    if len(seq) >= len(trk):
        return False
    seq = seq[:-1]
    len_seq = len(seq)
    if trk[-len_seq:] == seq:
        return 10
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


def dir_count(fssset, fss):
    dict = {1:0, 2:0, 3:0, 4:0}
    for sample in fssset:
        if len(sample[0]) != len(fss):
            pass
        elif sample[0][:-1] == fss[:-1]:
            dict[get_direct_label(sample[0][-1], sample[0][-2])] += 1
        else:
            pass
    return dict



def feature_fetch_vote(fssset, trk):
    '''
    return the feature vector(method: vector based on the last move of the fss)
    :param fssset:
    :type fssset:
    :param trk:
    :type trk:
    :return:
    :rtype:
    '''
    feature_vec = np.zeros(len(fssset)+4)
    for fss_id, fss in enumerate(fssset):
        flag = seq_match(fss[0], trk)
        if flag:
            if flag == 10:
                # last match fss exist
                dict = dir_count(fssset, fss[0])
                for idx in range(1,5):
                    feature_vec[-idx] = dict[-idx + 5]
            else:
                feature_vec[fss_id] = flag
    return feature_vec

# test
# a = [[[1,2,3],10],[[1,2,4],11],[[1,2,1],7]]
# trk = [1,2,3]
# res = dir_count(a, trk)

def get_featurevec(fssdata, dataset):
    # fssdata = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/confssData-th'+str(threshold)+'.npy', encoding="latin1")
    vec_list = []
    for idx, sample in enumerate(dataset):
        vec = feature_fetch_vote(fssdata, sample)
        vec_list.append(vec)
        print('sample '+str(idx)+' done')
    vec_list = np.array(vec_list)
    np.save(os.path.dirname(os.getcwd())+'/processedDATA/ftrVecData-th8-fre100(vote&dir).npy', vec_list)
    return vec_list









# feature = np.load(os.path.dirname(os.getcwd())+'/processedDATA/ftrVecData-th8-fre100(votelast).npy', encoding="latin1")

fssdata = np.load(os.path.dirname(os.getcwd())+'/processedDATA/confssDATAth8fre100.npy', encoding="latin1")
raw_data = np.load(os.path.dirname(os.getcwd())+'/processedDATA/lenSortDATA(72X48)th8.npy', encoding="latin1")

res = get_featurevec(fssdata, raw_data)
from preprocess import Endalarm
song = 'song.mp3'
Endalarm.alarm(song)
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
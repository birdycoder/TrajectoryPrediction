#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Predict.py
# @Author: Jeff Liu
# @Date  : 2019/3/22
# @Desc  : Prediction method

def includeTrk(pos, arr):
    '''
    return all sequences that consist of step pos
    :param pos: label of step
    :type pos: int
    :param arr: Training set
    :type arr: list
    :return: list of all sequences that consist of step pos
    :rtype: list
    '''
    list = []
    for trk in arr:
        if pos in trk:
            list.append(trk)
    return list

def seqInclude(seq, arr):
    res = []
    seq_len = len(seq)
    for trk in arr:
        check = True
        pos_id = 0
        while(check and pos_id<=(len(trk) - seq_len)):
            if trk[pos_id:(pos_id+ seq_len)] == seq:
                res.append(trk)
                check = False
            pos_id+=1
    return res

def seqNextStep(current_seq, train_set):
    '''predict the next step according to current sequence'''
    arr = seqInclude(current_seq, train_set)
    len_seq = len(current_seq)
    if arr:
        nextstep = nextStep(current_seq[-1], arr)
        return nextstep
    else:
        '''No prior knowledge, randomly pick a surrounding cell'''
        return current_seq[-1]+1


def major(arr, current_step):
    '''
    Return the most possible next step according to current step
    :param arr: Training set
    :type arr: list
    :param current_step: label of current step
    :type current_step: int
    :return: most possible label of the next step
    :rtype: int
    '''
    dict = {}
    for trk in arr:
        for pos in range(len(trk)):
            if trk[pos] == current_step and pos != len(trk)-1:
                pre_step = dict.get(trk[pos+1], 0)
                if pre_step:
                    dict[trk[pos+1]]+=1
                else:
                    dict[trk[pos+1]] = 1
    return max(dict, key=dict.get)




def nextStep(current_step, train_set):
    '''predict the next step according to current step'''
    arr = includeTrk(current_step, train_set)
    if arr:
        nextstep = major(arr, current_step)
        return nextstep
    else:
        '''No prior knowledge, randomly pick a surrounding cell'''
        return current_step + 1

# def trk_predict(train_set, test_set, depend_trk, num_step):
#     '''
#     :param train_set:
#     :type train_set:
#     :param test_set:
#     :type test_set:
#     :param depend_trk:
#     :type depend_trk:
#     :param num_step:
#     :type num_step:
#     :return:
#     :rtype:
#     '''
#     res = []
#     for trk in test_set:
#         depend_seq = trk[:depend_trk]
#         pre_step = nextStep()
#     current_pos = trk[current_step]
#     for idx in range(num_step):
#         nextstep = nextStep(current_pos, train_set)
#         res.append(nextstep)
#         current_pos = nextstep
#     return res
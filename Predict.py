#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Predict.py
# @Author: Jeff Liu
# @Date  : 2019/3/22
# @Desc  : Prediction method


import map
import random

def stepInBorder(step):
    if step < map.g_height or step > map.g_width*(map.g_height-1):
        pass
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


def rand_walk(cur_step):
    option = [cur_step+1, cur_step-1, cur_step-map.g_height, cur_step+map.g_height]
    nextstep = random.choice(option)
    # elif stepInUp(cur_step):
    #     option = [cur_step-1, cur_step - map.g_height, cur_step+map.g_height]
    #     nextstep = random.choice(option)
    # elif stepIndown(cur_step):
    #     option = [cur_step + 1, cur_step - map.g_height, cur_step + map.g_height]
    #     nextstep = random.choice(option)
    # elif stepInLeft(cur_step):
    #     option = [cur_step + 1, cur_step - 1, cur_step + map.g_height]
    #     nextstep = random.choice(option)
    # elif stepInRight(cur_step):
    #     option = [cur_step + 1, cur_step - 1, cur_step - map.g_height]
    #     nextstep = random.choice(option)
    return nextstep



def majorSeq(arr, current_seq):
    dict = {}
    len_seq = len(current_seq)
    for trk in arr:
        for pos in range(len(trk)-len_seq):
            if trk[pos:(pos+len_seq)] == current_seq and pos != len(trk)-len_seq:
                pre_step = trk[(pos+len_seq)]
                num_prestep = dict.get(pre_step, 0)
                if num_prestep:
                    dict[pre_step] += 1
                else:
                    dict[pre_step] = 1
    if dict:
        return max(dict, key=dict.get)
    else:
        print('randomly pick a step')
        nextstep = rand_walk(current_seq[-1])
        return nextstep

def seqNextStep(current_seq, train_set):
    '''predict the next step according to current sequence'''
    arr = seqInclude(current_seq, train_set)
    if arr:
        nextstep = majorSeq(arr, current_seq)
        return nextstep
    else:
        '''No prior knowledge, randomly pick a surrounding cell'''
        print('randomly pick a step')
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
    if dict:
        return max(dict, key=dict.get)
    else:
        return current_step+1


def nextStep(current_step, train_set):
    '''predict the next step according to current step'''
    arr = includeTrk(current_step, train_set)
    if arr:
        nextstep = major(arr, current_step)
        return nextstep
    else:
        '''No prior knowledge, randomly pick a surrounding cell'''
        return current_step + 1

def majorTerm(arr, current_seq):
    dict = {}
    len_seq = len(current_seq)
    for trk in arr:
        for pos in range(len(trk)-len_seq):
            if trk[pos:(pos+len_seq)] == current_seq and pos != len(trk)-len_seq:
                pre_Term = trk[-1]
                num_Term = dict.get(pre_Term, 0)
                if num_Term:
                    dict[pre_Term] += 1
                else:
                    dict[pre_Term] = 1
    if dict:
        return max(dict, key=dict.get)
    else:
        print('randomly pick a step')
        nextstep = rand_walk(current_seq[-1])
        return nextstep


def terminPredict(current_seq, train_set):
    arr = seqInclude(current_seq, train_set)
    if arr:
        terminal = majorTerm(arr, current_seq)
        return terminal
    else:
        '''No prior knowledge, randomly pick a surrounding cell'''
        print('randomly pick a step')
        return current_seq[-1]+1

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
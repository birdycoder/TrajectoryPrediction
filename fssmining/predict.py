#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : predict.py
# @Author: Jeff Liu
# @Date  : 2019/5/16
# @Desc  : using frequent sub sequence for mining

import random
import map
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

import numpy as np
import os
print(os.getcwd())
print(os.path.dirname(os.getcwd()))

def nextStep(fss_set, cur_step):
    cand_fss = []
    for idx, seq in enumerate(fss_set):
        if cur_step in seq[0] and seq[0][-1]!= cur_step:
            cand_fss.append(seq)
    if cand_fss:
        cand_fss = np.array(cand_fss)
        major_trk = cand_fss[np.argmax(cand_fss[:,1])][0]
        nextstep = major_trk[major_trk.index(cur_step)+1]
        return nextstep
    print('random walk')
    return rand_walk(cur_step)


def seq_match(seq, trk):
    if len(seq) >= len(trk):
        return False
    len_seq = len(seq)
    for pos in range(len(trk) - len_seq):
        if trk[pos:(pos + len_seq)] == seq and pos != len(trk) - len_seq:
            return True
    return False


def longest_match(seq, fss_set):
    cand_fss = fss_set
    seq_len = 2
    while(cand_fss and seq_len<=len(seq)):
        new_cand = []
        for trk in cand_fss:
            if seq_match(seq[-seq_len:], trk[0]):
                new_cand.append(trk)
        if not new_cand:
            return cand_fss
        cand_fss = new_cand
        seq_len += 1
    return cand_fss



def seqNextStep(fss_set, cur_trk):
    '''predict the next step according to current sequence'''
    cand_fss = []
    cur_step = cur_trk[-1]
    for idx, seq in enumerate(fss_set):
        if cur_step in seq[0] and seq[0][-1]!= cur_step:
            cand_fss.append(seq)
    if cand_fss:
        res_cand = longest_match(cur_trk, cand_fss)
        res_cand = np.array(res_cand)
        major_trk = res_cand[np.argmax(res_cand[:, 1])][0]
        nextstep = major_trk[major_trk.index(cur_step) + 1]
        return nextstep
    else:
        '''No prior knowledge, randomly pick a surrounding cell'''
        print('randomly pick a step')
        return rand_walk(cur_step)



def evaluate(train_set, test_set, pos_seq):
    '''
    For each track in test_set
    predict the last (pos_seq-1) step according to last (pos_seq) step
    return the accuracy
    :param train_set: train set, majority vote is based on the set
    :type train_set: list
    :param test_set: test set
    :type test_set: list
    :param pos_seq: prediction according position
    :type pos_seq: int
    :return: accuracy
    :rtype: float
    '''
    accuracy = 0.0
    idx = 0
    for trk in test_set:
        current_seq = trk[-pos_seq]
        pre_nextStep = nextStep(train_set, current_seq)
        true_nextStep = trk[-pos_seq+1]
        accuracy+= (true_nextStep == pre_nextStep)
        print('Track ' + str(idx)+ ' done')
        idx+=1
    accuracy = accuracy/len(test_set)
    return accuracy

def seq_evaluate(train_set, test_set, ktt_pos):
    '''
    :param train_set:
    :type train_set:
    :param test_set:
    :type test_set:
    :param ktt_pos:
    :type ktt_pos:
    :return:
    :rtype:
    '''
    accuracy = 0.0
    idx = 0
    for trk in test_set:
        cur_trk = trk[:-ktt_pos]
        pre_nextStep = seqNextStep(train_set, cur_trk)
        true_nextStep = trk[-ktt_pos]
        accuracy += (true_nextStep == pre_nextStep)
        print('Track ' + str(idx) + ' done')
        idx += 1
    accuracy = accuracy / len(test_set)
    return accuracy

g_width = 72
g_height = 48
data = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/after_label_arr'+'('+ str(g_width) + 'X' + str(g_height)+')' + '.npy', encoding="latin1")
fssdata = np.load(os.path.dirname(os.getcwd())+'/Transformed_DATA/confssData-th100.npy', encoding="latin1")
print(len(fssdata))

# number of tracks
num_trk = len(data)
# transfer label track to list type
data.tolist()

'''train set and test set setup
    80% training set and rest test set'''
train_set = data[:(int(num_trk * 0.8))]
test_set = data[(int(num_trk * 0.8)):]


print(seq_evaluate(fssdata, test_set, 1))

#72*48, 50th, last step, 33.04%
#72*48, 100th, last step, 31.30%
#72*48, 200th, last step, 27.96%

#seq, last step, 200th, 27.39%
#seq, last step, 100th, 31.92%
#seq, last step, 50th, 33.89%
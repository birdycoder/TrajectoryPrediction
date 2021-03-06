#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : evaluation.py
# @Author: Jeff Liu
# @Date  : 2019/5/26
# @Desc  : evaluation method

import fssmining.predict as fspre
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
        pre_nextStep = fspre.nextStep(train_set, current_seq)
        true_nextStep = trk[-pos_seq+1]
        accuracy+= (true_nextStep == pre_nextStep)
        print('Track ' + str(idx)+ ' done')
        idx+=1
    accuracy = accuracy/len(test_set)
    return accuracy

def seq_evaluate(train_set, test_set, start_pos, seq_len):
    accuracy = 0.0
    idx = 0
    for trk in test_set:
        current_seq = trk[-start_pos:(-start_pos+seq_len)]
        pre_nextStep = fspre.seqNextStep(current_seq, train_set)
        true_nextStep = trk[-start_pos+seq_len]
        accuracy += (true_nextStep == pre_nextStep)
        print('Track ' + str(idx) + ' done')
        idx += 1
    accuracy = accuracy / len(test_set)
    return accuracy
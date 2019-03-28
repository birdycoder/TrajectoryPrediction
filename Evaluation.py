#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Evaluation.py
# @Author: Jeff Liu
# @Date  : 2019/3/22
# @Desc  : Evaluation method

import Predict as pre
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
        pre_nextStep = pre.nextStep(current_seq, train_set)
        true_nextStep = trk[-pos_seq+1]
        accuracy+= (true_nextStep == pre_nextStep)
        print('Track ' + str(idx)+ ' done')
        idx+=1
    accuracy = accuracy/len(test_set)
    return accuracy
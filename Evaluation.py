#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Evaluation.py
# @Author: Jeff Liu
# @Date  : 2019/3/22
# @Desc  : Evaluation method

import Predict as pre
def evaluate(train_set, test_set, pos_seq):
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
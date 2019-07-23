#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : trk_sort.py
# @Author: Jeff Liu
# @Date  : 2019/6/13
# @Desc  : track scan according to track length

import numpy as np
import os


def trk_sort(threshold, dataset):
    '''
    sort out track that have length longer than threshold
    :param threshold:
    :type threshold:
    :param dataset:
    :type dataset:
    :return:
    :rtype:
    '''
    res = []
    for trk in dataset:
        if len(trk) >= threshold:
            res.append(trk)
    return res

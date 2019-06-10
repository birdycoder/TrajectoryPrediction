#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Fss.py
# @Author: Jeff Liu
# @Date  : 2019/5/14
# @Desc  : mining frequent sub-sequence

from prefixspan import PrefixSpan
import numpy as np


g_width = 72
g_height = 48


def isConse(seq):
    for idx in range(len(seq)-1):
        if seq[idx+1] != seq[idx]+48 and seq[idx+1] != seq[idx]-48 and seq[idx+1] != seq[idx]-1 and seq[idx+1] != seq[idx]+1 and \
                        seq[idx+1] != seq[idx] -47 and seq[idx+1] != seq[idx]-49 and seq[idx+1] != seq[idx]+47 and seq[idx+1] != seq[idx]+49:
            return False
    return True
bool_extractdata = 1
bool_extract_con_fss = 1


def fssextract(threshold):
    data = np.load('Transformed_DATA/after_label_arr'+'('+ str(g_width) + 'X' + str(g_height)+')' + '.npy', encoding="latin1")
    data_num = int(len(data)*0.8)
    data = data[:data_num]
    ps = PrefixSpan(data)
    #res = ps.frequent(threshold, filter=lambda patt, matches: len(patt) >= 2)
    res = ps.frequent(threshold)

    list = []
    for i in res:
        record = []
        record.append(i[1])
        record.append(i[0])
        list.append(record)
    npdata = np.array(list)
    np.save('Transformed_DATA/fssData2-th'+str(threshold)+'.npy',npdata)


def confss_tran(threshold):
    fssdata = np.load('Transformed_DATA/fssData2-th'+str(threshold)+'.npy', encoding="latin1")
    cand_seq = fssdata[..., 0]
    con_fss = []
    for idx in range(len(cand_seq)):
        if isConse(cand_seq[idx]):
            con_fss.append(fssdata[idx])

    con_fss = np.array(con_fss)
    np.save('Transformed_DATA/confssData2-th'+str(threshold)+'.npy', con_fss)


fssextract(200)
confss_tran(200)
# if bool_extractdata:
#     data = np.load('Transformed_DATA/after_label_arr'+'('+ str(g_width) + 'X' + str(g_height)+')' + '.npy', encoding="latin1")
#     data_num = int(len(data)*0.8)
#     data = data[:data_num]
#     ps = PrefixSpan(data)
#     #print(ps.topk(5, filter=lambda patt, matches: len(patt) >= 2))
#     res = ps.frequent(200, filter=lambda patt, matches: len(patt) >= 2)
#
#     list = []
#     for i in res:
#         record = []
#         record.append(i[1])
#         record.append(i[0])
#         list.append(record)
#
#     npdata = np.array(list)
#     np.save('Transformed_DATA/fssData-th200.npy',npdata)
#
# if bool_extract_con_fss:
#     fssdata = np.load('Transformed_DATA/fssData-th200.npy', encoding="latin1")
#     cand_seq = fssdata[...,0]
#
#     con_fss = []
#     for idx in range(len(cand_seq)):
#         if isConse(cand_seq[idx]):
#             con_fss.append(fssdata[idx])
#
#     con_fss_200 = np.array(con_fss)
#     np.save('Transformed_DATA/confssData-th200.npy',con_fss_200)




print('a')


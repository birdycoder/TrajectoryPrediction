#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Jeff Liu
# @Date  : 2019/3/16
# @Desc  : for testing

from prefixspan import PrefixSpan

db = [
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2],
]

ps = PrefixSpan(db)
print(ps.topk(5, filter=lambda seq, matches: len(seq) == 2))


print ('haha')
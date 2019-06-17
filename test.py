#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Jeff Liu
# @Date  : 2019/3/16
# @Desc  : for testing

def numSquares(n):
    """
    :type n: int
    :rtype: int
    """

    residual = n
    count = 0
    while (residual != 0):
        max = 1
        while (max * max <= n):
            max += 1
        residual = n - (max - 1) * (max - 1)
        count += 1
    return count
numSquares(12)
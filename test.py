#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Jeff Liu
# @Date  : 2019/3/16
# @Desc  : for testing

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = len(nums)

    start = 1
    end = total

    while (start <= end):
        if start == end:
            return start
        mid = int((end + start) / 2)
        count = counter(nums, start, mid)
        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1
    return start


def counter(arr, start, end):
    res = 0
    for i in arr:
        if i >= start and i <= end:
            res += 1
    return res

print(findDuplicate([1,2,3,4,4]))


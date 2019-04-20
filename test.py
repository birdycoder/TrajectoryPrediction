#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Jeff Liu
# @Date  : 2019/3/16
# @Desc  : for testing


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Iterate over nums backwards to avoid index errors when deleting dups
    for i in range(len(nums) - 1, -1, -1):
        # If current num is the same as the previous, delete it
        if i != 0 and nums[i] == nums[i - 1]:
            del nums[i]

    return nums

b = removeDuplicates([1,1,2,2,3,3,4,4])
print ('haha')
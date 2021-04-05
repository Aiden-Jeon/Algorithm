"""
title: relative-sort-array
date: 2021-04-04
- problem number: 1122
- difficult: Easy  
- https://leetcode.com/problems/relative-sort-array/  

---

## Define input, output
- Input:
    - Two arrays are given, arr1 and arr2  
    - arr2 is distinct and it is subset of arr1
- Output: 
    - arr2_1: ordered values which are in arr2
    - arr2_2: values which are not in arr2 with ascending order
    - concat arr2_1, arr2_2

"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_dict = {v: 0 for v in arr2}
        not_order_dict = {}
        result = []
        for v in arr1:
            if v in order_dict:
                order_dict[v] += 1
            else:
                not_order_dict.setdefault(v, 0)
                not_order_dict[v] += 1
        for v in arr2:
            sub_result = [v] * order_dict[v]
            result.extend(sub_result)
        for v in sorted(not_order_dict):
            sub_result = [v] * not_order_dict[v]
            result.extend(sub_result)
        return result

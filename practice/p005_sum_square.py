#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 22:38
# @Author  : oubin
# @File    : p005_sum_square.py
# @Software: PyCharm
# 求前n个数的平方合

def sum_of_squire(n):
    result = 0
    for number in range(1, n + 1):
        result += number * number
    return result


print("sum of suqare 3: ", sum_of_squire(3))

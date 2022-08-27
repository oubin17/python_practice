#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 22:47
# @Author  : oubin
# @File    : p006_get_even_number.py
# @Software: PyCharm

# 输出begin到end之内的偶数

begin = 1
end = 100


def even_number(begin, end):
    result = []
    for number in range(begin, end):
        if number % 2 == 0:
            result.append(number)
    return result


result = [item for item in range(begin, end) if item % 2 == 0]
print(f"begin: {begin}, end : {end} 之内的偶数有：", even_number(begin, end))
print(f"begin: {begin}, end : {end} 之内的偶数有：", result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 23:30
# @Author  : oubin
# @File    : p002_number_factorial.py
# @Software: PyCharm
def get_factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


print("factorial 6 = ", get_factorial(5))
print("factorial 10 = ", get_factorial(10))

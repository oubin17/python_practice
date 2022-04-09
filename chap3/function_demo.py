#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 21:40
# @Author  : oubin
# @File    : function_demo.py
# @Software: PyCharm

def calc(a, b):
    c = a + b
    return c


print(calc(1, 2))


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))

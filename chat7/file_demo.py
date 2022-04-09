#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/9 17:33
# @Author  : oubin
# @File    : file_demo.py
# @Software: PyCharm
file = open('text.txt', 'r')
print(file.readlines())
file.close()

with open('text.txt', 'r') as file:
    print(file.read())

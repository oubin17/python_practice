#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 22:17
# @Author  : oubin
# @File    : select_demo.py
# @Software: PyCharm
money = 1000 # 余额
s = int(input("请输入取款金额："))
if money >= s:
    print("余额充足，剩余", money - s)

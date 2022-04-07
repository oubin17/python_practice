#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 21:06
# @Author  : oubin
# @File    : fload_demo.py
# @Software: PyCharm


n1 = 1.1
n2 = 2.2
print(n1 + n2)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

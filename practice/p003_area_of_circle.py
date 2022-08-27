#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 23:38
# @Author  : oubin
# @File    : p003_area_of_circle.py
# @Software: PyCharm
# 计算圆的面积
import math


def area_of_circle(r):
    result = math.pi * r * r
    print(f"area_of_circle {r} = ", result)
    print(f"area_of_circle {r} = ", round(result, 2))




area_of_circle(5)

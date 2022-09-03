#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 21:23
# @Author  : oubin
# @File    : p009_file_size.py
# @Software: PyCharm
# 文件大小求和
import os.path

print(os.path.getsize("./p000_article.txt"))

sum_size = 0
for file in os.listdir("."):
    if os.path.isfile(file):
        print(file)
        sum_size += os.path.getsize(file)
print(f"所有文件大小：{sum_size}")

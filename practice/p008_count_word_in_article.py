#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 21:14
# @Author  : oubin
# @File    : p008_count_word_in_article.py
# @Software: PyCharm
# 统计出现最多的单次
word_count = {}

with open("./p000_article.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
print(word_count)

# 打印前10个

print(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10])

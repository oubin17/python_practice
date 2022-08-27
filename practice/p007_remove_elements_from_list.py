#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 22:54
# @Author  : oubin
# @File    : p007_remove_elements_from_list.py
# @Software: PyCharm
# 用列表中移除其他列表存在的元素

lista = [3, 5, 5, 7, 9, 11]
listb = [5, 9]


def remove_element(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista

sorted()
print(f"from: {lista} remove: {listb}, result: ", remove_element(lista, listb))

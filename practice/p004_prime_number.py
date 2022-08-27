#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 23:49
# @Author  : oubin
# @File    : p004_prime_number.py
# @Software: PyCharm
# 打印素数
def print_primes(begin, end):
    for number in range(begin, end + 1):
        if is_prime(number):
            print(f"{number} is a prime")


def is_prime(number):
    if number in [1, 2]:
        return True
    for index in range(2, number):
        if number % index == 0:
            return True


begin = 11
end = 20

print_primes(begin, end)

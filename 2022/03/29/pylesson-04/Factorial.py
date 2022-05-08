#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Factorial
@time: 2022-04-21
"""
def fac(m: int) -> int:
    res = 1
    for k in range(m):
        res *= k + 1
    return res
m = int(input("请输入一个正整数: "))
print("%d! = %d" % (m, fac(m)))

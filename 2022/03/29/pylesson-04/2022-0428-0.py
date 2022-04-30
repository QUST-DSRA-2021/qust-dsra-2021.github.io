#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Factorial 阶乘
@time: 2022-04-28
"""
def factorial(x: int) -> int:
    return factorial(x - 1) * x if x else 1
if __name__ == "__main__":
    m = int(input("请输入一个整数(>1): "))
    print("%d! = %d" % (m, factorial(m)))
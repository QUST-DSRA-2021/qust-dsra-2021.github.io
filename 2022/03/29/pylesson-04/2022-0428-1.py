#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Fibonacci 序贯
@time: 2022-04-28
"""
def fibonacci(x: int) -> int:
    return 1 if x <= 2 else fibonacci(x - 1) + fibonacci(x - 2)
if __name__ == "__main__":
    m = int(input("请输入一个整数(>1): "))
    print("fib(%d) = %d" % (m, fibonacci(m)))
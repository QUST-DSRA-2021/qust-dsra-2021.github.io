#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 辗转相除
@time: 2022-04-28
"""
def _gcd(v: int, u: int) -> int:
    if not u: # 如若较小的数为零则最大公约数为另一个数
        return v
    r = v % u # 定义变量作为取余的数, 减少稍后的运算量
    return _gcd(u, r) if r else u
def gcd(v: int, u: int) -> int: # 这个函数先行处理输入的两个整数
    assert v >= 0 and u >= 0, "Input nums must be non-negative integers!"
    assert v != 0 or u != 0, "Both input nums cannot be zero at the same time!"
    # 而后藉由 `_gcd(v, u)` 进行递归地辗转相除
    return _gcd(v, u) if v >= u else _gcd(u, v)
if __name__ == "__main__":
    v, u = eval(input("请输入两个整数, 以逗号分割: "))
    print("自然数 %d 与 %d 的最大公约数为 %d" % (v, u, gcd(v, u)))
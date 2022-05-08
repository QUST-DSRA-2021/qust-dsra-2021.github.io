#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 判断回文数问题
@time: 2022-04-26 07:39:39
"""
def is_palindrome(m: int) -> bool:
    s = str(m)
    return s == s[ :: (-1) ]
if __name__ == "__main__":
    x = int(input("请输入一个自然数: "))
    print("%s%s回文数" % (x, "是" if is_palindrome(x) else "不是"))
#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 判断奇偶数
@time: 2022-04-21
"""
def oddjudge(ミク: int) -> bool:
    # 偶数在对2取余意义下值为零, 奇数在对2取余意义下值为一,
    # 利用此性质进行逻辑运算, 可以得知一个数是否为偶数与其在对2取余意义下的bool值相反
    # 亦即 x为偶数 = ┐ (x % 2)
    return not(ミク % 2)
if __name__ == "__main__": # 连续传参并使用条件表达式进行运算与输出
    ミク = eval(input("请输入一个整数: "))
    if not isinstance(ミク, int): # 使用`isinstance`判断类型
        print("The input must be Integer-typed!")
    else:
        print("该数为%s。" % ("偶数" if oddjudge(ミク) else "奇数"))
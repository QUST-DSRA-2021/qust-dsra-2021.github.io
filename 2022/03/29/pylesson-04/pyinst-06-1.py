#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 06-1 Exception Processing
@time: 2022-04-14 13:39:39
"""
try:
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 定义字母列表
    idx = eval(input("请输入一个整数: ")) # 输入
except NameError: # 处理异常: NameError
    print("输入错误! 请输入整数!!")
except: # 处理其他异常
    print("产生其他异常!!")
else: # 若无问题则输出
    print("第%d个字母为%s" % (idx, alp[idx - 1]))
#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 判断用户输入的整数是否能够被5和7整除
@time: 2022-03-29 20:21:39
"""
num = int(input("请输入一个整数："))
if (num % 5) or (num % 7): # 如若表达式`(num % r)`的值为真则说明`num`对`r`取余结果不为零,
                           # 即说明`num`不能为`r`所整除,
                           # 如若`num`对5或7中某一个取余结果不为零则说明不能为其中一个所整除,
                           # 反之, 其他情况便是`num`能够为5和7所整除的情形
    print("%s不能够为5和7整除" % num)
else:
    print("%s能够为5和7整除" % num)
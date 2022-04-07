#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 输入一个数，输出其绝对值。
@time: 2022-03-29 20:10:39
"""
val = eval(input("请输入一个数：")) # 读取用户输入的数值,
                                    # 由于可能是整数也有可能是浮点故使用built-in的`eval`进行转换
print("%s的绝对值是%s" % (val, abs(val))) # 调用built-in的`abs`计算绝对值,
                                          # 如若输入虚部不为零的复数, 则输出其模,
                                          # 并借用字符串对取余运算符的重载的效果, 格式化生成其中的内容,
                                          # 使用`print`进行输出
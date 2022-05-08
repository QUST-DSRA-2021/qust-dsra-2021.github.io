#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 06-4 Radius
@time: 2022-04-14 13:39:39
"""
import numpy as np # 使用 NumPy 中定义的 Pi 数值
try: # 使用户输入半径(radius)并计算面积(area)
    radius = eval(input("请输入所求圆的半径: "))
    area = np.pi * (radius ** 2)
    if isinstance(radius, complex): # 处理输入为复数的情形
        raise ValueError("错误输入! 输入应为实数而非复数!!")
except NameError: # 处理输入不为数的情形
    print("错误输入! 输入应当是一个数!!")
except Exception as err: # 处理其他情形
    print("其他错误:", err)
else: # 如若没有问题则输出
    print("所求圆的面积为:", area)
#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance-02
@time: 2022-04-07 12:39:39
"""
valpm25 = eval(input("Input PM2.5 Value:"))
assert valpm25 >= 0, "Invalid Input! which isnot a Positive Integer!!"
if 0 <= valpm25 < 35:
    print("空气优质，快去户外运动！")
elif 35 <= valpm25 < 75:
    print("空气良好，适度户外运动！")
else:
    print("空气污染，请小心！")
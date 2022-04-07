#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance-03 猜数游戏
@time: 2022-04-07 12:39:39
"""
# 加载模块
import random
# 设置预设的目标, 并使用户输入其猜测的数
numpreset, numguessed = random.randint(0, 9), int(input("Input the Number you Guessed:"))
# 创建计数器
times = 1
# 处理异常输入
assert 0 <= numguessed <= 9, "Invalid Input! which isnot in Range [0, 9]!!"
# 判断并输出
while numguessed != numpreset:
    if numguessed > numpreset:
        numguessed = int(input("Sorry Wrong, which is Greater than the Target, Try Again:"))
    else:
        numguessed = int(input("Sorry Wrong, which is Less than the Target, Try Again:"))
    assert 0 <= numguessed <= 9, "Invalid Input! which isnot in Range [0, 9]!!"
    times += 1
else:
    print("Correct Answer after Guessing %d Times! Congratulations!!" % times)
#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance-03 猜数游戏
@time: 2022-04-07 12:39:39
"""
# 加载模块
import random
# 设置预设的目标
numpreset = random.randint(0, 100)
# 创建计数器
times = 1
# 并使用户输入其猜测的数
try:
    numguessed = int(input("输入你所猜测的数字: " or "Input the Number you Guessed: "))
    assert 0 <= numguessed <= 100, "错误输入! 输入的数字需在 [0, 100] 内!!" or "Invalid Input! which isnot in Range [0, 100]!!"
    # 判断并输出
    while numguessed != numpreset:
        if numguessed > numpreset:
            numguessed = int(input("抱歉, 猜错了, 比预设的数字大, 请重试: " or "Sorry Wrong, which is Greater than the Target, Try Again: "))
        else:
            numguessed = int(input("抱歉, 猜错了, 比预设的数字小, 请重试: " or "Sorry Wrong, which is Less than the Target, Try Again: "))
        assert 0 <= numguessed <= 100, "错误输入! 输入的数字需在 [0, 100] 内!!" or "Invalid Input! which isnot in Range [0, 100]!!"
        times += 1
# 处理异常输入
except ValueError:
    print("错误输入! 输入的内容必须为整数!" or "Invalid Input! which isnot an Integer!!")
else:
    print(("猜测%d次之后正确! 恭喜!!" or "Correct Answer after Guessing %d Times! Congratulations!!") % times)
#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 06-0 Monte Carlo
@time: 2022-04-14 13:39:39
"""
import random, math, time
class Constants(object):
    NUM_DARTS = 10000
hits = 0
time.clock() # 标准库 time 的钟表计时启动
for k in range(Constants.NUM_DARTS): # 迭代开始
    x, y = random.random(), random.random() # 随机一个坐标落点
    dist = math.sqrt(x ** 2 + y ** 2) # 计算距离
    if dist <= 1.: # 如若打中则加一
        hits += 1
pi = 4 * hits / Constants.NUM_DARTS # 计算 Pi 数值
print("Pi值是{}".format(pi)) # 输出计算得到的 Pi 数值
print("运行时间是: {:5.5}s".format(time.clock())) # 输出运行时间
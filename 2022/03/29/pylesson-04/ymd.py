#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance
@time: 2022-04-07 12:39:39
"""
# 加载模块
import time
# 输入并计算然后输出
print("It's the %d-th Day in that Year." % time.strptime(input("Input the Date: "), "%Y-%m-%d").tm_yday)
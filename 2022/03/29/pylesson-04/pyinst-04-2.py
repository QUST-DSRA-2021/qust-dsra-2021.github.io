#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 04-2 文本进度条
@time: 2022-03-29 16:14:39
"""
import time
class Constants(object):
    NUM_DOTS = 39
    TIME_SEPARATE = .1
if __name__ == "__main__":
    print("Starting", end="")
    for k in range(Constants.NUM_DOTS + 1):
        time.sleep(Constants.TIME_SEPARATE / 2)
        print("." if k else "\"", end="")
        time.sleep(Constants.TIME_SEPARATE / 2)
    print("Done!")
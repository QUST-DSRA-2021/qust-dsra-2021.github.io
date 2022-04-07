#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 04-3 文本风格
@time: 2022-03-29 16:14:39
"""
import time
class Constants(object):
    TIME_DISPLAY = 39
if __name__ == "__main__":
    time_start = time.time()
    while True:
        for ch in [ "/", "-", "|", "\\", "|" ]:
            print("%s\r" % ch, end="")
        if time.time() - time_start >= Constants.TIME_DISPLAY:
            break
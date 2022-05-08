#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 03-2 天天向上I (Deprecated!!)
@time: 2022-03-24 13:39
"""

# Constants / 声明并维护常量
class Constants(object):
    VAL_BASE = 1.
    VAL_PROGRESS_PER_DAY = .01
    FLAG_INCLUDING_WEEKEND = True # Including weekends or not / 是否包含周末
    FLAG_CONSERVATIVE = False # Estimating conservatively or not / 如若不包含周末, 则是否保守估计

# The main process / 主函数(过程)
def init() -> None:
    num_days, res = 365, 1.
    if not Constants.FLAG_INCLUDING_WEEKEND:
        if Constants.FLAG_CONSERVATIVE:
            num_days -= (num_days // 7) * 2
        else:
            num_days = (num_days // 7) * 5
    for k in range(num_days):
        if k % 7 >= 3:
            res *= 1 + Constants.VAL_PROGRESS_PER_DAY
    print("The result after progressing everyday for 365 days is: %.3f" % res)

if __name__ == "__main__":
    init()

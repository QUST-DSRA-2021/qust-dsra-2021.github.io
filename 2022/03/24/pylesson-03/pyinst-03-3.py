#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 03-3 天天向上II
@time: 2022-03-24 13:39
"""

# Constants / 声明并维护常量
class Constants(object):
    VAL_BASE = 1.
    VAL_PROGRESS_PER_DAY = .01
    NUM_DAYS_PER_TERM = 10
    FLAG_CONSERVATIVE = False # Estimating conservatively or not / 是否保守估计

# The main process / 主函数(过程)
def init() -> None:
    num_days, res = 365, 1.
    if Constants.NUM_DAYS_PER_TERM >= 2:
        num_days = (num_days // Constants.NUM_DAYS_PER_TERM) * ((Constants.NUM_DAYS_PER_TERM // 7 * 4) + max(Constants.NUM_DAYS_PER_TERM % 7 - 3 - 1, 0))
    else:
        num_days = (num_days // 7 * 4) + max(num_days % 7 - 3, 0)
    res *= (1 + Constants.VAL_PROGRESS_PER_DAY) ** num_days
    print("The result after progressing everyday for 365 days is: %.3f" % res)

if __name__ == "__main__":
    init()

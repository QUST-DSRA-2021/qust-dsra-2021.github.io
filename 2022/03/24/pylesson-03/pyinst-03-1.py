#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 03-1 重量计算
@time: 2022-03-24 13:39
"""

# Constants / 声明并维护常量
class Constants(object):
    VAL_RATE = 16.5 / 100
    WEIGHT_INCREASE = .5

# The main process / 主函数(过程)
def init() -> None:
    w_current = eval(input("Input Current Weight: "))
    for k in range(10):
        w_current += Constants.WEIGHT_INCREASE
        print("In %s year(s), his weight on the earth is %s, that on the moon is %.3f" % (
            k + 1,
            w_current,
            w_current * Constants.VAL_RATE
            ))

if __name__ == "__main__":
    init()

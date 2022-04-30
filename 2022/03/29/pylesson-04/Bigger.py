#!/usr/bin/env Python
# -*- codingL utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Bigger
@time: 2022-04-21
"""
def bigger(v, u) -> int:
    return v if v >= u else u
print("较大值为%d" % bigger(*eval(input("请输入两个整数 (用逗号隔开): "))))

#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 数值比较问题
@time: 2022-04-06 15:39:39
"""
nums = eval(input("请输入第一个数:")), eval(input("请输入第二个数:"))
if nums[0] != nums[1]:
    print("较大者为:%s" % max(nums[0], nums[1]))
else:
    print("两个数相同,数值为:%s" % nums[0])
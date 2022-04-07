#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 输出其是否为闰年
@time: 2022-03-29 20:30:39
"""
num = int(input("请输入一个年份：")) # 输入年份
class Constants(object): # 把后面需要频繁输出的字符串使用类进行维护
    STR_IS_LEAP = "%s年是闰年" % num
    STR_IS_COMMON = "%s年不是闰年" % num
# 闰年的判断: 一个年份如若能为4所整除则为闰年,
# 但其中能为100所整除者为平年,
# 如若又有能为400整除的反而又是闰年,
# 所以我们先判断是否可以为400所整除,
# 其剩下能为100所整除者为平年,
# 再剩下能为4所整除者又为闰年.
if not num % 400:
    print(Constants.STR_IS_LEAP)
elif not num % 100:
    print(Constants.STR_IS_COMMON)
elif not num % 4:
    print(Constants.STR_IS_LEAP)
else:
    print(Constants.STR_IS_COMMON)
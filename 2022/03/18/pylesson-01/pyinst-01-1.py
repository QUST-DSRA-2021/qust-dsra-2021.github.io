#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 01-1 温度转换
@time: 2022-03-17 14:39
"""

def init(): # The Main Function / 主函数
    st = input("Enter the Temperature with its Unit (For Instance: \"39C\") -> ").lower()
    assert st[-1] in ["f", "c"], "Invalid Input! The Program Only Supports Converting Temperature formatted in Fahrenheit Scale or Centigrade Scale." # Check the Input whether it's Valid, or raise the AssertionError. / 检查输入是否有效, 如若输入无效则通过assert抛出AssertionError
    if (st[-1] == "f"): # Converting Temperature Value in Fahrenheit Scale / 转换华氏温度
        print("Converted Temperature: %.2fC" % (eval(st[ : (-1) ]) * 1.8 + 32))
    else: # Converting Temperature Value in Centigrade Scale / 转换摄氏温度
        print("Converted Temperature: %.2fF" % ((eval(st[ : (-1) ]) - 32) * 5 / 9))

if __name__ == "__main__":
    init()

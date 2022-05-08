#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 03-4 回文数判断
@time: 2022-03-24 13:39
"""

# Constants / 声明并维护常量
class Constants(object):
    STR_TRUE = "The input num can be reversed."
    STR_FALSE = "The input num cannot be reversed!"

# The main process / 主函数(过程)
def init() -> None:
    s, arr, flag = input(), [], True
    while not s:
        s = input()
    if len(s) == 1:
        print(Constants.STR_TRUE)
        return
    m = int(s)
    while m:
        arr.append(m % 10)
        m //= 10
    for k in range(len(arr) // 2):
        if (arr[k] != arr[-1 - k]):
            flag = False
    print(Constants.STR_TRUE if flag else Constants.STR_FALSE)

if __name__ == "__main__":
    #print("The input num can be reversed." if ((lambda x : x == x[ : : (-1) ])(input())) else "The input num cannot be reversed!")
    init()

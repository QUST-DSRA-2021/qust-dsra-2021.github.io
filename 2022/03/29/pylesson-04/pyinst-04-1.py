#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 04-1 田字格输出
@time: 2022-03-29 16:14:39
"""
def printside(len_hor: int = 5, num_hor: int = 2, num_indent_spaces: int = 4, flag: bool = 1) -> None:
    chrs = "+-" if flag else "| " # 选择绘制的内容
    print(" " * num_indent_spaces + chrs[0] + (chrs[1] * len_hor + chrs[0]) * num_hor) # 根据给定尺寸进行绘制
def printgrid(len_hor: int = 5, len_ver: int = 4, num_hor: int = 2, num_ver: int = 2, num_indent_spaces: int = 4) -> None:
    printside(len_hor, num_hor, num_indent_spaces) # 先画出来最上一行的边
    for k in range(num_ver):
        for l in range(len_ver):
            printside(len_hor, num_hor, num_indent_spaces, 0) # 填充每行的空白
        printside(len_hor, num_hor, num_indent_spaces) # 封住每行下侧的边
    print()
if __name__ == "__main__":
    printgrid(4, 2, *([int(input("输入你要的阶数: "))] * 2)) # 使用星号表达式来实现参数重复利用
    #printgrid(9, 3, 9, 3, 9)
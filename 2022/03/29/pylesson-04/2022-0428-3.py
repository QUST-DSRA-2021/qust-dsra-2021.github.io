#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title:
@time: 2022-04-28
"""
import turtle
def koch(m:int=5, length:int=2) -> None:
    if m != 0:
        koch(m - 1, length)
        turtle.left(60)
        koch(m - 1, length)
        turtle.right(120)
        koch(m - 1, length)
        turtle.left(60)
        koch(m - 1, length)
    else:
        turtle.forward(length)
if __name__ == "__main__":
    turtle.setup(1300, 600, 720, 200) # 画布初始化 (以及笔触和画布颜色)
    turtle.pencolor("#002b36")
    turtle.screensize(bg="#fdf6e3")
    turtle.penup() # 抬笔, 前往初始位置
    turtle.forward(-420)
    turtle.pendown() # 落笔, 开始绘制
    koch() # 调用递归绘制Koch曲线的函数, 默认阶数为5
    turtle.mainloop() # 使Tk窗体进入mainloop过程等待下一步操作
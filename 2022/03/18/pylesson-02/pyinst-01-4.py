#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 01-4 使用Python的Turtle模块，绘制等边三角形
@time: 2022-03-17 14:35
"""

# Importing Python Modules / 导入Python相关模块
import turtle

# Constants / 声明需要的常量
class Base16Solarized(object): # Solarized by GitHub@altercation
    BASES = {
        "00":   "#002b36",
        "07":   "#fdf6e3",
        }
    COLORS = {
        "yellow":    "#b58900",
        "orange":    "#cb4b16",
        "red":       "#dc322f",
        "magenta":   "#d33682",
        "violet":    "#6c71c4",
        "blue":      "#268bd2",
        "cyan":      "#2aa198",
        "green":     "#859900",
        }
class Constants(object):
    CANVAS_POSITION = (650, 500, 720, 200)
    DEFAULT_PENSIZE = 25
    LEN_EDGE = 128

def init(): # The Main Function / 主函数
    # Initialization / 初始化
    turtle.setup(Constants.CANVAS_POSITION[0], Constants.CANVAS_POSITION[1], Constants.CANVAS_POSITION[2], Constants.CANVAS_POSITION[3]) # Setting Position & Scale of Canvas / 设置画布的位置与尺寸
    # About Color-Control of Turtle: https://docs.python.org/3.6/library/turtle.html#color-control
    turtle.pencolor(Base16Solarized.BASES["00"]) # Setting Colors of Foreground / 设置前景颜色
    turtle.screensize(bg = Base16Solarized.BASES["07"]) # Setting Colors of Background / 设置背景颜色

    # Drawing Outer Triangle / 绘制外层三角形
    turtle.penup() # Disable Drawing / 提笔
    turtle.forward(Constants.LEN_EDGE * (-1)) # Move Left to the Initial Position / 向左移至初始位置
    turtle.pendown() # Enable Drawing / 落笔
    for k in range(3): # Repeat Thrice / 重复三次
        turtle.forward(Constants.LEN_EDGE * 2) # Move Forward / 向前进
        turtle.setheading(120 * (k + 1)) # Turn Left via Setting the Direction / 通过设置方向角度来进行左转

    # Drawing Inner Triangle / 绘制内层三角形
    turtle.penup()
    turtle.forward(Constants.LEN_EDGE) # Move Left to the Starter of Inner Triangle / 向左移至内层三角形的起点
    turtle.pendown()
    for k in range(3): # Repeat Thrice / 重复三次
        turtle.setheading(k * 120 + 60)
        turtle.forward(Constants.LEN_EDGE)

    # Waiting for Manually Exit / 等待手动退出
    turtle.mainloop()

if __name__ == "__main__":
    init()

#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 01-2 使用Python的Turtle模块，绘制彩色蟒蛇
@time: 2022-03-17 14:39
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
    CANVAS_POSITION = (650, 350, 720, 200)
    DISTANCE_INITIAL_MOVING = -250
    DEFAULT_PENSIZE = 25
    BIAS_ANGLE = 39
    NUM_PHASES = 4
    LEN_HEAD = 39
    LEN_NECK = 15.6

def init(): # The Main Function / 主函数
    # Initialization / 初始化
    turtle.setup(Constants.CANVAS_POSITION[0], Constants.CANVAS_POSITION[1], Constants.CANVAS_POSITION[2], Constants.CANVAS_POSITION[3]) # Setting Position & Scale of Canvas / 设置画布的位置与尺寸
    # About Color-Control of Turtle: https://docs.python.org/3.6/library/turtle.html#color-control
    turtle.pencolor(Base16Solarized.BASES["00"]) # Setting Colors of Foreground / 设置前景颜色
    turtle.screensize(bg = Base16Solarized.BASES["07"]) # Setting Colors of Background / 设置背景颜色

    turtle.penup() # Temporarily Disable the Drawing Function / 提笔
    turtle.forward(Constants.DISTANCE_INITIAL_MOVING) # Move Left to the Initial Position / 向左移至初始位置

    turtle.pendown() # Enable the Drawing Function / 落笔
    turtle.pensize(Constants.DEFAULT_PENSIZE) # Setting the Pensize / 设置笔触大小
    turtle.pencolor(Base16Solarized.COLORS["violet"]) # Setting the Pencolor / 设置笔触颜色
    turtle.setheading(Constants.BIAS_ANGLE * (-1)) # Setting the Initial Direction / 设置初始方向偏角

    for eachkey in [ "red", "cyan", "yellow", "blue" ]: # Colors of Each Phase / 各段的颜色
        turtle.pencolor(Base16Solarized.COLORS[eachkey]) # Setting the Pencolor / 设置笔触颜色
        # Drawing "the Body" as Arcs / 以圆弧形式绘制蛇体
        turtle.circle(Constants.BIAS_ANGLE, Constants.BIAS_ANGLE * 2)
        turtle.circle(Constants.BIAS_ANGLE * (-1), Constants.BIAS_ANGLE * 2)

    turtle.pencolor(Base16Solarized.COLORS["violet"]) # Returning to the Default Pencolor / 恢复笔触颜色
    # Drawing "the Neck" & "the Head" / 绘制脖颈及头部
    turtle.circle(Constants.BIAS_ANGLE, Constants.BIAS_ANGLE)
    turtle.forward(Constants.LEN_HEAD)
    turtle.circle(Constants.LEN_NECK, 180)
    turtle.forward(Constants.LEN_HEAD * 2 / 3)

    # Waiting for Manually Exit / 等待手动退出
    turtle.mainloop()

if __name__ == "__main__":
    init()

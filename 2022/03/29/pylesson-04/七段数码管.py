#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 七段数码管
@time: 2022-04-12 10:29:39 (乐正绫7th发售日快乐!!)
"""
import turtle
class Constants(object):
    """
    +--c--+
    |     |
    d     b
    |     |
    +--a--+
    |     |
    e     g
    |     |
    +--f--+
    """
    STR_TODRAW = "20070831"
    CANVAS_POSITION = (650, 350, 720, 200)
    DEFAULT_PENSIZE = 3.9
    FLAGS_TODRAW = [
        [ 0, 1, 1, 1, 1, 1, 1 ], # 0
        [ 0, 1, 0, 0, 0, 0, 1 ], # 1
        [ 1, 1, 1, 0, 1, 1, 0 ], # 2
        [ 1, 1, 1, 0, 0, 1, 1 ], # 3
        [ 1, 1, 0, 1, 0, 0, 1 ], # 4
        [ 1, 0, 1, 1, 0, 1, 1 ], # 5
        [ 1, 0, 1, 1, 1, 1, 1 ], # 6
        [ 0, 1, 1, 0, 0, 0, 1 ], # 7
        [ 1, 1, 1, 1, 1, 1, 1 ], # 8
        [ 1, 1, 1, 1, 0, 1, 1 ], # 9
        ]
    FLAGS_TURNING = [ 1, 1, 1, 0, 1, 1, 0 ]
def draw_empty(length:int=4) -> None:
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()
def draw_forward(todraw:bool=True, length:int=40, left_turning:bool=False) -> None:
    draw_empty()
    if not todraw:
        draw_empty(length - 8)
    else:
        turtle.forward(length - 8)
    draw_empty()
    if left_turning:
        turtle.left(90)
def draw_digital(digit) -> None:
    for k in range(7):
        draw_forward(Constants.FLAGS_TODRAW[digit][k], left_turning=Constants.FLAGS_TURNING[k])
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
def draw_string(st:str=Constants.STR_TODRAW) -> None:
    for eachdigit in st:
        draw_digital(int(eachdigit))
def init() -> None:
    # Turtle Initialization
    turtle.setup(*Constants.CANVAS_POSITION)
    turtle.pensize(Constants.DEFAULT_PENSIZE)
    turtle.pencolor("#2aa198")
    turtle.screensize(bg="#fdf6e3")
    turtle.penup()
    turtle.left(180)
    turtle.forward(256)
    turtle.left(180)
    turtle.pendown()
    # Drawing Digits
    draw_string()
    # Tk Mainloop
    turtle.mainloop()
if __name__ == "__main__":
    init()
#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 02-5 绘制无角正方形
"""

import turtle

for k in range(4):
    # 跳过每条边前面的空白
    turtle.penup()
    turtle.forward(20)
    # 绘制边
    turtle.pendown()
    turtle.forward(160)
    # 舍弃最后一段, 并终止循环
    if k == 3:
        break
    # 跳过每条边后面的空白
    turtle.penup()
    turtle.forward(20)
    # 转向
    turtle.left(90)

turtle.mainloop()

#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 02-6 绘制六芒星
"""

import turtle

turtle.penup()
turtle.setpos(-150,20)

turtle.pendown()
turtle.left(30)
turtle.forward(100)
turtle.left(60)

for k in range (5):
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.left(60)

turtle.forward(100)
turtle.right(120)
turtle.forward(100)

for k in range(6):
    turtle.forward(100)
    turtle.right(60)

turtle.mainloop()

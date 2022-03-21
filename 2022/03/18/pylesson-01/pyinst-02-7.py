#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 02-7 绘制方形螺线
"""

import turtle

turtle.seth(90)

for k in range(39):
    for l in range(2):
        turtle.left(90)
        turtle.fd(5 * k + 5)

turtle.done()

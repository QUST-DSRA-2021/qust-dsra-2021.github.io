#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Tree of Recursion
@time: 2022-04-28
"""
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("solarized-light")
"""
rt = tkinter.Tk() # 创建窗体
cv = tkinter.Canvas(rt, bg="#fdf6e3") # 在窗体内创建画布
"""
RATE_DECAY = 1.28
def treeplot(lenbranch:float=30., x0:float=180., y0:float=225., delta=np.pi/12, theta0=np.pi/2, order=10, ratedecay=1.):
    if order != 0:
        x1 = x0 + lenbranch * np.cos(theta0) # 计算终点坐标
        y1 = y0 + lenbranch * np.sin(theta0)
        #cv.create_line(x0, y0, x1, y1, activefill="#002b36") # 画线
        plt.plot([x0, x1], [y0, y1])
        treeplot(lenbranch / ratedecay, x1, y1, delta, theta0 + delta, order-1, ratedecay)
        treeplot(lenbranch / ratedecay, x1, y1, delta, theta0 - delta, order-1, ratedecay)
treeplot(ratedecay=RATE_DECAY) # 调用递归函数
"""
cv.pack()
rt.mainloop() # 进入消息循环
"""
plt.title("Rate of length-decay of branch = %s" % RATE_DECAY)
plt.show()
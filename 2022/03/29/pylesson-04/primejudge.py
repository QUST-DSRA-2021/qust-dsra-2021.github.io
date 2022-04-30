#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 判断素数
@time: 2022-04-21
"""
import numpy as np
def primejudge(ミク: int) -> bool:
    """
    只有一次的判断不需要Eratosthenes筛法
    """
    for k in range(2, (np.sqrt(ミク)).astype(int) + 1): # 循环判断其左侧因子
        if not (ミク % k): # 如若存在整数因子则可以整除待判断的整数
            return False # 遂返回「伪」
    return True # 不存在可以整除之的整数因子则表明其不为素数, 则返回「真」
if __name__ == "__main__": # 连续传参并使用条件表达式进行运算与输出
    ミク = eval(input("请输入一个整数: "))
    if not isinstance(ミク, int): # 使用`isinstance`判断类型
        print("The input must be Integer-typed!")
    else:
        print("该数%s素数。" % ("是" if primejudge(ミク) else "不是"))
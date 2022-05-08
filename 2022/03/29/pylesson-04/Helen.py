"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: 根据Helen公式计算三角形面积
@time: 2022-04-21
"""
import numpy as np
def judgetriangle(a, b, c): # 用于判断三个数是否能作为三角形三边的函数
    return (a + b > c) and (b + c > a) and (c + a > b)
def helen(a, b, c): # 根据海伦公式求解三角形面积
    q = (a + b + c) / 2 # 中间量 q = (a + b + c) / 2
    return np.sqrt(q * (q - a) * (q - b) * (q - c)) # 面积 S = sqrt(q * (q - a) * (q - b) * (q - c))
if __name__ == "__main__":
    a, b, c = eval(input("请输入三角形三边: "))
    for each in a, b, c: # 利用 for-each 结构进行循环判断
        if not isinstance(each, int) and not isinstance(each, float): # 利用`isinstance`判断类型
            print("输入类型错误。")
            break
    else: # 如若输入类型没有问题
        if not judgetriangle(a, b, c): # 判断三边边长是否能构成三角形
            print("输入的三边无法构成一个三角形!")
        else: # 无误则计算面积
            print("三角形面积S = %s" % helen(a, b, c))
#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: sandyzikun
@title: BMI Calculation
@time: 2022-03-29 11:20
"""
# 输入 BMI
val_height, val_weight = eval(input("Input value of BMI, seperate them by comma: "))
# 计算 BMI
val_bmi = val_weight / (val_height ** 2)
# 输出 BMI
print("BMI Value: %.2f" % val_bmi)
# 断言要求 BMI >= 0
assert val_bmi >= 0, "Ensure Value of BMI > 0."
# 赋初始值
res_wto, res_dom = "", ""
# 判断
if val_bmi < 18.5:
    res_wto, res_dom = "偏瘦", "偏瘦"
elif 18.5 <= val_bmi < 24:
    res_wto, res_dom = "正常", "正常"
elif 24 <= val_bmi < 25:
    res_wto, res_dom = "正常", "偏胖"
elif 25 <= val_bmi < 28:
    res_wto, res_dom = "偏胖", "偏胖"
elif 28 <= val_bmi < 30:
    res_wto, res_dom = "偏胖", "肥胖"
else:
    res_wto, res_dom = "肥胖", "肥胖"
# 输出结论
print("根据输入得到的BMI数值在国际上情况为「%s」在国内情况为「%s」" % (res_wto, res_dom))
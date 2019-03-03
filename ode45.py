#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/1/4

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-

# 本程序是用四阶龙格库塔法求解课本（数值计算方法 马东升）P242页的例7-3
# fun为指定的导数的函数
# rf4为四阶龙格库塔法

def fun(x, y):
    f = y - (2 * x / y)

    return f

# input
#     x0,y0:初始给出的x0值，y0值
#     h   ：步长
#     N   ：迭代次数
# print
#    x1,y1:每次迭代输出的结果
def rf4(x0, y0, h, N):
    n = 1
    while (n != N):
        x1 = x0 + h

        k1 = fun(x0, y0)
        k2 = fun(x0 + h / 2, y0 + h * k1 / 2)
        k3 = fun(x0 + h / 2, y0 + h * k2 / 2)
        k4 = fun(x1, y0 + h * k3)

        y1 = y0 + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print("%.2f, %.6f" % (x1, y1))
        n = n + 1
        x0 = x1
        y0 = y1

def main():
    rf4(0, 1, 0.2, 10)

main()

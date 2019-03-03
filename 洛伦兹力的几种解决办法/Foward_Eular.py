#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/1/14


# 参考：https://blog.csdn.net/u011702002/article/details/78118857

__author__='Deqian Bai'

import numpy as np

"""

移动方程：

t时刻的位置P(x,y,z)

steps：dt的大小

sets：相关参数

"""


def move(P, steps, sets):
    x, y, z = P
    sgima, rho, beta = sets
    # 各方向的速度近似
    dx = sgima * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [x + dx * steps, y + dy * steps, z + dz * steps]

# 设置sets参数

sets = [10., 28., 3.]
t = np.arange(0, 30, 0.01)

# 位置1：

P0 = [0., 1., 0.]
P = P0
d = []
for v in t:
    P = move(P, 0.01, sets)
    d.append(P)
dnp = np.array(d)

# 位置2：
P02 = [0., 1.01, 0.]
P = P02
d = []

for v in t:
    P = move(P, 0.01, sets)

    d.append(P)
dnp2 = np.array(d)

"""
画图
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()

ax = Axes3D(fig)
ax.plot(dnp[:, 0], dnp[:, 1], dnp[:, 2])
ax.plot(dnp2[:, 0], dnp2[:, 1], dnp2[:, 2])

plt.show()

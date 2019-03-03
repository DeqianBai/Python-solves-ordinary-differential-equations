#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/1/9

# -*- coding: utf8 -*-
import numpy as np
from scipy.integrate import odeint
import scipy.integrate as integrate
"""
移动方程：
t时刻的位置P(x,y,z)
steps：dt的大小
sets：相关参数
"""


def move(P, steps):
    x = P[0]
    y = P[1]
    z = P[2]

    # 各方向的速度近似
    dx = 10* (y - x)
    dy = x * (28 - z) - y
    dz = x * y - 3 * z

    return np.array([dx, dy, dz])


# 设置sets参数
sets = [10., 28., 3.]
t = np.arange(0, 30, 0.01)

# 位置1：
P0 = np.array([0., 1., 0.])
# P = P0
# d = []
# for v in t:
#     P = move(P, 0.01, sets)
#     d.append(P)
# dnp = np.array(d)


dnp=odeint(move, P0, t, )

# 位置2：
#P02 = [0., 1.01, 0.]

#P = P02
#d = []
#for v in t:
#    P = move(P, 0.01, sets)
#    d.append(P)
#dnp2 = np.array(d)
"""
画图
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(dnp[:, 0], dnp[:, 1], dnp[:, 2])
#ax.plot(dnp2[:, 0], dnp2[:, 1], dnp2[:, 2])
plt.show()
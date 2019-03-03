# ！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/1/14

# 参考：
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D


def twoBody(y, t, mu):
    """
    Two Body function returns the derivative of the state space variables.
INPUTS:
    --- t ---
        A scalar time value.

    --- y ---
        A 6x1 array of the state space of a particle in 3D space
OUTPUTS:
    --- ydot ---
        The derivative of y for the two-body problem

"""

    r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)

    ydot = np.empty((6,))

    ydot[0] = y[3]
    ydot[1] = y[4]
    ydot[2] = y[5]
    ydot[3] = (-mu / (r ** 3)) * y[0]
    ydot[4] = (-mu / (r ** 3)) * y[1]
    ydot[5] = (-mu / (r ** 3)) * y[2]

    return ydot


# In m and m/s
# first three are the (x, y, z) position
# second three are the velocities in those same directions respectively
Y0 = np.array([-5614924.5443320004,
               -2014046.755686,
               2471050.0114869997,
               -673.03650300000004,
               582.41158099999996,
               1247.7034980000001])

mu = 3.986004418 * 10 ** 14

t = np.linspace(0., 351., 100)

solution = odeint(twoBody, Y0, t, args=(mu,))

print(solution.size)
print(solution.shape)
print(solution.ndim)
x = solution[:, 0]
y = solution[:, 1]
z = solution[:, 2]
dx = solution[:, 3]
dy = solution[:, 4]
dz = solution[:, 5]

mpl.rcParams['legend.fontsize'] = 10

fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.plot(x, y, z, label='position')
ax.legend()

fig2 = plt.figure(2)
plt.plot(t, dx, label='x velocity')
plt.plot(t, dy, label='y velocity')
plt.plot(t, dz, label='z velocity')
plt.legend()
_ = plt.ylim()

plt.show()

#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/1/14

# 参考： http://www.voidcn.com/article/p-wggekgmj-bpy.html

from scipy.integrate import odeint
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

from IPython import display

fig = plt.figure()
ax = fig.gca(projection='3d')

def lorenz(w, t, p, r, b):
    # 位置矢量w， 三个参数p, r, b
    x, y ,z = w.tolist()
    # 分别计算dx/dt, dy/dt, dz/dt
    return p * (y-x), x*(r-z)-y, x*y-b*z

t = np.arange(0, 50, 0.01)

# 设定初始值
initial_val = (0.0, 1.00, 0.0)

track = odeint(lorenz, initial_val, t, args=(10.0, 28.0, 3.0))
X, Y, Z = track[:,0], track[:,1], track[:,2]

ax.plot(X, Y, Z, label='lorenz')
ax.legend()
plt.show()

# display.Latex(r"$\frac{dx}{dt}=\sigma\cdot(y-x) \\ \frac{dy}{dt}=x\cdot(\rho-z)-y \\ \frac{dz}{dt}=xy-\beta z$")
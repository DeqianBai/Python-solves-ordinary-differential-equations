# -*- coding: utf-8 -*-
"""
Created on Wed Dec 04 20:57:55 2013

@author: Administrator
"""
import numpy as np
def f(x):
    return x - np.log(x) - 2
jingdu = 1
x = 3.14619
deltx = 0.0001
n = 0
while jingdu > 10e-5:
    n = n + 1
    x1 = x    
    x = x - f(x) / ((f(x + deltx) - f(x)) / deltx)
    jingdu = np.abs(x - x1)
print( x, n)
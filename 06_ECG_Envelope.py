# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:53:22 2021

@author: cagda
"""

from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import bspline, cubic, quadratic
#get ready to use ECG signal
ecg = electrocardiogram()

fs = 360
lower=17000
upper=18000
duration=upper-lower



x = ecg[lower:upper]
tx=np.arange(len(x)) / fs

nx=x+np.random.uniform(0,0.9,len(x))
plt.figure()
plt.subplot(3,1,1)
plt.plot(x)
plt.subplot(3,1,2)
plt.plot(nx)

plt.subplot(3,1,3)
#second orde bspline
x_bspline=bspline(nx, 2)
plt.plot(tx, x_bspline,label='2nd  bspline')
"""
#second orde bspline
x_bspline=bspline(x, 10)
plt.plot(tx, x_bspline,label='10th  bspline')

x_quad=quadratic(x)
plt.plot(tx, x_quad,label='quadratic')

x_cubic=cubic(x)
plt.plot(tx, x_quad,label='cubic')

plt.legend()
plt.grid()
"""

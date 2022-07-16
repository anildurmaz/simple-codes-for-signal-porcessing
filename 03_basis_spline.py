# -*- coding: utf-8 -*-
"""
@author: A.C.SECKIN
"""

from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import bspline, cubic, quadratic

#get ready to use ECG signal
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
# sample abnormal signal
x = ecg[17000:17500]
# generating time axis values
tx = np.arange(x.size) / fs
plt.figure()
plt.plot(tx, x,label='raw signal')

#second orde bspline
x_bspline=bspline(x, 2)
plt.plot(tx, x_bspline,label='2nd  bspline')

#second orde bspline
x_bspline=bspline(x, 10)
plt.plot(tx, x_bspline,label='10th  bspline')

x_quad=quadratic(x)
plt.plot(tx, x_quad,label='quadratic')

x_cubic=cubic(x)
plt.plot(tx, x_quad,label='cubic')

plt.legend()
plt.grid()
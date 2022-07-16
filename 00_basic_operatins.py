# -*- coding: utf-8 -*-
"""
@author: A.C.SECKIN
"""

from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np

#get ready to use ECG signal
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
# sample abnormal signal
x = ecg[17000:18000]
# generating time axis values
tx = np.arange(x.size) / fs
plt.figure()
plt.subplot(321)
plt.title("Raw signal")
plt.plot(tx, x)
plt.grid()

modulator=np.sin(2*np.pi*3*tx)
plt.subplot(322)
plt.title("Modulator Signal")
plt.plot(tx, modulator)

y = x*modulator
plt.subplot(323)
plt.title("multipled")
plt.plot(tx, y)
plt.grid()

y = x+modulator
plt.subplot(324)
plt.title("addtion")
plt.plot(tx, y)
plt.grid()


#gradient or derivative of the signal
dx=np.gradient(x)
# generating time axis values
tdx = np.arange(x.size) / fs
plt.subplot(325)
plt.title("Gradient/derivative")
plt.plot(tdx, dx)
#plt.plot(tx, x, "r",tdx, dx, "b")
plt.grid()
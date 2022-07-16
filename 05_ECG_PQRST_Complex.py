# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:46:29 2021

@author: cagda
"""

# -*- coding: utf-8 -*-
"""
@author: A.C.Seckin
"""

from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np

#get ready to use ECG signal
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
#lower and upper index for investigation
lower=17000
upper=18000
# generating time axis values
time = np.arange(ecg.size) / fs
plt.figure()
plt.title("ECG mV/s")
plt.plot(time, ecg)
plt.xlabel("time in s")
plt.ylabel("ECG in mV")
# zooming specific area
plt.xlim(lower/fs,upper/fs)
plt.ylim(-1.2, 2.2)

plt.show()


# find peaks
from scipy.signal import find_peaks
# get specific range of ecg signal

##############################################################################
####ALL R points #############################################################
##############################################################################
x = ecg[lower:upper]
p_allR, p_allRproperties = find_peaks(x, distance=150)
plt.figure()
plt.title("ALL R points")
plt.plot(x)
plt.plot(p_allR, x[p_allR], "x")
plt.show()
##############################################################################
####ALL PRT points ###########################################################
##############################################################################
p_allPRT, p_allPRTproperties = find_peaks(x, prominence=[0.2],distance=30)
plt.figure()
plt.title("All PRT points")
plt.plot(x)
plt.plot(p_allPRT, x[p_allPRT], "x")
plt.show()
##############################################################################
####ALL QS points ############################################################
##############################################################################
p_allQS, p_allQRproperties = find_peaks(x*(-1), prominence=[0.1],distance=30)
plt.figure()
plt.title("ALL QS points")
plt.plot(x)
plt.plot(p_allQS, x[p_allQS], "x")
plt.show()
##############################################################################
####ALL PQRST points ############################################################
##############################################################################
p_allPQRST = np.concatenate((p_allPRT,p_allQS))
p_allPQRST.sort(kind='mergesort')
plt.figure()
plt.title("All PQRS points")
plt.plot(x)
plt.plot(p_allPQRST, x[p_allPQRST], "x")
plt.show()
##############################################################################
####Abnormal R################################################################
##############################################################################
p_abnormalR, p_abnormalRproperties = find_peaks(x, prominence=1, width=20)
p_abnormalRproperties["prominences"]
p_abnormalRproperties["widths"]
plt.figure()
plt.title("Abnormal R")
plt.plot(x)
plt.plot(p_abnormalR, x[p_abnormalR], "x")
plt.vlines(x=p_abnormalR, ymin=x[p_abnormalR] - p_abnormalRproperties["prominences"],
           ymax = x[p_abnormalR], color = "C1")
plt.hlines(y=p_abnormalRproperties["width_heights"], xmin=p_abnormalRproperties["left_ips"],
           xmax=p_abnormalRproperties["right_ips"], color = "C1")
plt.show()

##############################################################################
####Abnormal S################################################################
##############################################################################
p_abnormalS, p_abnormalSproperties = find_peaks(x*(-1), prominence=[2],width=100)
p_abnormalSproperties["prominences"]
p_abnormalSproperties["widths"]
plt.figure()
plt.title("Abnormal S")
plt.plot(x)
plt.plot(p_abnormalS, x[p_abnormalS], "x")
plt.show()


##############################################################################
### Normal PQRS###############################################################
##############################################################################
p_normal=p_allPQRST
for i_abnormal in p_abnormalR:
    print(i_abnormal)
    p_normal=np.delete(p_normal, np.where(p_normal==i_abnormal))
for i_abnormal in p_abnormalS:
    print(i_abnormal)
    p_normal=np.delete(p_normal, np.where(p_normal==i_abnormal))

plt.figure()
plt.title("Nomral PQRS")
plt.plot(x)
plt.plot(p_normal, x[p_normal], "x")
plt.show()
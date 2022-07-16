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

x = ecg[lower:upper]
#select peaks above 0
peaks, properties = find_peaks(x, height=0)
# for below 0
# peaks, _ = find_peaks(x, height=(None, 0))  
plt.figure()
plt.title("Peaks-above 0")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()

#select specific function
border = np.sin(np.linspace(0, 2 * np.pi, x.size))
peaks, _ = find_peaks(x, height=(-border, border))
plt.figure()
plt.title("Peaks-specific function")
plt.plot(x)
plt.plot(-border, "--", color="gray")
plt.plot(border, ":", color="gray")
plt.plot(peaks, x[peaks], "x")
plt.show()

#find peaks with distance hoping
peaks, _ = find_peaks(x, distance=150)
plt.figure()
plt.title("Peaks-distance hoping")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()

# find prominence point
"""
Strategy to compute a peak’s prominence:
    1- Extend a horizontal line from the current peak to the left and right until 
    the line either reaches the window border (see wlen) or intersects the 
    signal again at the slope of a higher peak. An intersection with a peak of 
    the same height is ignored.
    
    2- On each side find the minimal signal value within the interval defined
    above. These points are the peak’s bases.
    
    3- The higher one of the two bases marks the peak’s lowest contour line. 
    The prominence can then be calculated as the vertical difference between 
    the peaks height itself and its lowest contour line.
"""
peaks, properties = find_peaks(x, prominence=(None, 0.6))
properties["prominences"].max()
plt.figure()
plt.title("Peaks-prominences")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()

peaks, properties = find_peaks(x, prominence=1, width=20)
properties["prominences"]
properties["widths"]
plt.figure()
plt.title("Peaks-prominences-width")
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
           ymax = x[peaks], color = "C1")
plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
           xmax=properties["right_ips"], color = "C1")
plt.show()
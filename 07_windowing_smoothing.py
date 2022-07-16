# -*- coding: utf-8 -*-
"""
@author: A.C.Seckin
"""

from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pandas as pd

#get ready to use ECG signal
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
#lower and upper index for investigation
lower=17000
upper=18000
# generating time axis values
x = pd.Series(ecg[lower:upper])

rm=x.rolling(window=33,min_periods=1).mean()

plt.plot(x)
plt.plot(rm)

def moving_average(arr, window):
    ret = np.cumsum(arr)
    ret[window:] = ret[window:] - ret[:-window]
    return ret[window - 1:] / window

def exponential_smoothing(series, alpha):
    results = np.zeros_like(series)
    results[0] = series[0] 
    for t in range(1, series.shape[0]):
        results[t] = alpha * series[t] + (1 - alpha) * results[t - 1]

    return results
def double_exponential_smoothing(series, alpha, beta, n_preds=2):
    n_record = series.shape[0]
    results = np.zeros(n_record + n_preds)
    level = series[0]
    results[0] = series[0]
    trend = series[1] - series[0]
    for t in range(1, n_record + 1):
        if t >= n_record:
            # forecasting new points
            value = results[t - 1]
        else:
            value = series[t]

        previous_level = level
        level = alpha * value + (1 - alpha) * (level + trend)
        trend = beta * (level - previous_level) + (1 - beta) * trend 
        results[t] = level + trend
    if n_preds > 1:
        results[n_record + 1:] = level + np.arange(2, n_preds + 1) * trend

    return results

def getfeature(data):
    fmean=np.mean(data)
    fstd=np.std(data)
    fmax=np.max(data)
    fmin=np.min(data)
    return fmean,fstd,fmax,fmin
def windowFeatureExtraction(raw_data,ws,hop,dfname):
    wfmean=[]
    wfstd=[]
    wfmax=[]
    wfmin=[]
    for i in range(ws,len(raw_data),hop):
       m,s,ma,mi= getfeature(raw_data.iloc[i-ws+1:i,0])
       wfmean.append(m)
       wfstd.append(s)
       wfmax.append(ma)
       wfmin.append(mi)
    return wfmean, wfstd, wfmax, wfmin



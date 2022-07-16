# -*- coding: utf-8 -*-
"""
@author: A.C.SECKIN
"""

from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import bspline, cubic, quadratic
from scipy.stats import gmean, hmean,kurtosis,skew,gstd, entropy,pearsonr,spearmanr

def RMS(x):
    return np.sqrt(np.mean(np.square(x)))
def crest_factor(x):
    return np.max(np.abs(x))/RMS(x)

#get ready to use ECG signal
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
# sample abnormal signal
x = ecg[17237:17840]
# generating time axis values
tx = np.arange(x.size) / fs
plt.subplot(3,1,1)
plt.plot(tx, x,label='raw signal')
plt.grid()

abnormal_x = ecg[17622:17840]
plt.subplot(3,2,3)
plt.plot(abnormal_x)
plt.grid()
# sample normal signal
normal_x = ecg[17237:17455]
plt.subplot(3,2,4)
plt.plot(normal_x)
plt.grid()

avsn_pearson=pearsonr(abnormal_x, normal_x)
avsn_spearmanr=spearmanr(abnormal_x, normal_x)

# abnormal descriptive statistics
a_mean=np.mean(abnormal_x)
a_std=np.std(abnormal_x)
a_max=np.max(abnormal_x)
a_min=np.min(abnormal_x)
a_pp=a_max-a_min
a_rms=RMS(abnormal_x)
a_crest=crest_factor(abnormal_x)
a_gmean=gmean(abnormal_x)
a_hmean=hmean(abs(abnormal_x))
a_kurtosis=kurtosis(abnormal_x)
a_skew=skew(abnormal_x)
a_gstd=gstd(abs(abnormal_x))
a_entropy_2=entropy(abnormal_x,base=2)
a_entropy_10=entropy(abnormal_x,base=10)

# normal descriptive statistics
n_mean=np.mean(abnormal_x)
n_std=np.std(abnormal_x)
n_max=np.max(abnormal_x)
n_min=np.min(abnormal_x)
n_pp=a_max-a_min
n_rms=RMS(abnormal_x)
n_crest=crest_factor(abnormal_x)
n_gmean=gmean(normal_x)
n_hmean=hmean(abs(normal_x))
n_kurtosis=kurtosis(normal_x)
n_skew=skew(normal_x)
n_gstd=gstd(abs(normal_x))
n_entropy_2=entropy(normal_x,base=2)
n_entropy_10=entropy(normal_x,base=10)
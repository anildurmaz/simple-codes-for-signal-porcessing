# -*- coding: utf-8 -*-
"""
@author: A.C.SECKIN
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

#A custom signal generation from a logical sequence
logic_sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
plt.subplot(421)
plt.plot(logic_sig)
plt.title('Logical signal')
plt.grid()

#A noise signal generation
noise_sig =rng.standard_normal(len(logic_sig))
plt.subplot(423)
plt.plot(noise_sig )
plt.title('Noise signal')
plt.grid()

#A random/noise over logical signal 
noise_logical_sig = logic_sig+ noise_sig
plt.subplot(425)
plt.plot(noise_logical_sig)
plt.title('Sum of noise and logical signal')
plt.grid()

# cross correlation between noise signal and 
corr = signal.correlate(noise_logical_sig, logic_sig, mode='same') / 128
plt.subplot(427)
plt.plot(corr)
plt.axhline(0.5, ls=':')
plt.title('Cross-correlated with rectangular pulse')
plt.margins(0, 0.1)
plt.grid()
plt.show()

# cross correlation lag between noise signal and 
lags = signal.correlation_lags(len(noise_logical_sig), len(logic_sig))
plt.subplot(426)
plt.plot(lags)
plt.axhline(0.5, ls=':')
plt.title('cross correlation lag')
plt.grid()
plt.show()

# normalized cross correlation between noise signal and 
n_corr= corr/np.max(corr)
plt.subplot(428)
plt.plot(n_corr)
plt.axhline(0.5, ls=':')
plt.title('Normalized cross correlation')
plt.grid()
plt.show()

"""
Correlated signal lag 
"""
#get ready to use ECG signal
from scipy.misc import electrocardiogram
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
# generating time axis values
time = np.arange(ecg.size) / fs
# sample abnormal signal
abnormal_x = ecg[17622:17840]
plt.figure()
plt.subplot(3,2,1)
plt.plot(abnormal_x)
plt.grid()
# sample normal signal
normal_x = ecg[17237:17425]
plt.subplot(3,2,2)
plt.plot(normal_x)
plt.grid()
# Raw ECG signal as searching space
y = ecg[17200:19000]
plt.subplot(3,1,2)
plt.plot(y)
plt.grid()

plt.subplot(3,1,3)
#centr_axis=np.arange(-len(y)/2,len(y)/2)
plt.plot((y-np.mean(y))/np.max(np.abs(y)))
plt.grid()

# searching abnormal signal with correlation
abnormal_correlation = signal.correlate(y,abnormal_x, mode="full")
abnormal_correlation =abnormal_correlation/np.max(abnormal_correlation)
abnormal_lags = signal.correlation_lags( y.size, abnormal_x.size, mode="full")
abnormal_lag = lags[np.argmax(abnormal_correlation)]
plt.subplot(3,1,3)

plt.subplot(3,1,3)
plt.plot(abnormal_lags,abnormal_correlation)
plt.grid()

# searching normal signal with correlation
normal_correlation = signal.correlate( y, normal_x, mode="full")
normal_correlation =normal_correlation/np.max(normal_correlation)
normal_lags = signal.correlation_lags( y.size,normal_x.size, mode="full")
normal_lag = lags[np.argmax(normal_correlation)]

plt.subplot(3,1,3)
plt.plot(normal_lags,normal_correlation)
plt.grid()

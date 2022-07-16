# -*- coding: utf-8 -*-
"""
@author: A.Ç.SEÇKİN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_signal(sample_duration, sample_freq, signal_type, signal_freq):
    """
    Create some signals to work with, e.g. if we were to sample at 100 Hz
    (100 times per second) and collect the data for 10 seconds, resulting
    in 1000 samples in total. Then we would specify sample_duration = 10,
    sample_freq = 100.
    
    Apart from that, we will also give the option of generating sine or cosine
    wave and the frequencies of these signals
    """
    raw_value = 2 * np.pi * signal_freq * np.arange(0, sample_duration, 1. / sample_freq)
    if signal_type == 'cos':
        return np.cos(raw_value)
    elif signal_type == 'sin':
        return np.sin(raw_value)
    

def dft(x):
    """Compute the Discrete Fourier Transform of the 1d ndarray x."""
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    
    # complex number in python are denoted by the j symbol,
    # instead of i that we're showing in the formula
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)
#Correlation
# change default style figure and font size
plt.rcParams['figure.figsize'] = 8, 6
plt.rcParams['font.size'] = 12
plt.style.use('fivethirtyeight')

# dissimilar signals have low correlation
signal1 = create_signal(10, 100, 'sin', 0.1)
signal2 = create_signal(10, 100, 'cos', 0.1)
plt.plot(signal1, label='Sine')
plt.plot(signal2, label='Cosine')
plt.title('Correlation={:.1f}'.format(np.dot(signal1, signal2)))
plt.legend()
plt.show()

# similar signals have high correlation
signal1 = create_signal(10, 100, 'sin', 0.1)
signal2 = create_signal(10, 100, 'sin', 0.1)
plt.plot(signal1, label='Sine 1')
plt.plot(signal2, label='Sine 2', linestyle='--')
plt.title('Correlation={}'.format(np.dot(signal1, signal2)))
plt.legend()
plt.show()

# Fourier Transformation
# reminder:
# sample_duration means we're collecting the data for x seconds
# sample_freq means we're sampling x times per second
sample_duration = 10
sample_freq = 100
signal_type = 'sin'
num_samples = sample_freq * sample_duration
num_components = 4

components = np.zeros((num_components, num_samples))
components[0] = create_signal(sample_duration, sample_freq, signal_type, 1)
components[1] = create_signal(sample_duration, sample_freq, signal_type, 3)
components[2] = create_signal(sample_duration, sample_freq, signal_type, 5)
components[3] = create_signal(sample_duration, sample_freq, signal_type, 7)

signal = 1 * components[0] + (1/3) * components[1] + (1/5) * components[2] + (1/7) * components[3]

fig, ax = plt.subplots(nrows=num_components+1, sharex=True, figsize=(12,8))
for i in range(num_components):
    ax[i].plot(components[i])
    ax[i].set_ylim((-1.1, 1.1))
    ax[i].set_title('Component {}'.format(i))
    ax[i].set_ylabel('Amplitude')

ax[i+1].plot(signal )
ax[i+1].set_title('Result')
ax[i+1].set_ylabel('Amplitude')

ax[num_components ].set_xlabel('Samples')
plt.tight_layout()

fft_result = np.fft.fft(signal)
print('length of fft result: ', len(fft_result))
fft_result[:5]
plt.figure()
plt.plot(np.abs(fft_result))
plt.xlim((-5, 120))  # notice that we limited the x-axis to 120 to focus on the interesting part
plt.ylim((-5, 520))
plt.xlabel('K')
plt.ylabel('|DFT(K)|')
plt.show()

dft_result = dft(signal)
print('result matches:', np.allclose(dft_result, fft_result))
plt.figure()
plt.plot(np.abs(dft_result))
plt.xlim((-5, 120))
plt.ylim((-5, 520))
plt.xlabel('K')
plt.ylabel('|DFT(K)|')
plt.show()
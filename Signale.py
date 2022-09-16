from random import random
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def rechteck(freq, amp, duration):
    zeit = np.linspace(0, duration, int(freq*duration*1000))
    rect = amp*signal.square(2*np.pi*freq*zeit, duty=0.3)
    noise = rect+np.random.random_sample(len(sin))
    return noise


def sin(freq, amp, duration):
    zeit = np.linspace(0, duration, int(freq*duration*1000))
    sin = amp*np.sin(2*np.pi*freq*zeit)
    noise = sin+np.random.random_sample(len(sin))
    return noise


def dreieck(freq, amp, duration):
    zeit = np.linspace(0, duration, int(freq*duration*1000))
    dreieck = amp*signal.sawtooth(2*np.pi*freq*zeit, width=0.5)
    noise = dreieck+np.random.random_sample(len(sin))
    return noise

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def rechteck(freq, amp, duration):
    zeit = np.linspace(0, duration, int(freq*duration*100))
    rect = amp*signal.square(2*np.pi*freq*zeit, duty=0.3)
    return rect


def sin(freq, amp, duration):
    zeit = np.linspace(0, duration, int(freq*duration*100))
    sin = amp*np.sin(2*np.pi*freq*zeit)
    return sin


def dreieck(freq, amp, duration):
    zeit = np.linspace(0, duration, int(freq*duration*100))
    dreieck = amp*signal.sawtooth(2*np.pi*freq*zeit, width=0.5)
    return dreieck

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def rechteck(freq, amp, duration):
    zeit = np.linspace(0, 2, int(freq*duration))
    rect = amp*signal.square(2*np.pi*freq*zeit, duty=0.3)
    return rect


def sin(freq, amp, duration):
    zeit = np.linspace(0, 2, int(freq*duration))
    sin = amp*np.sin(2*np.pi*freq*zeit)
    return sin


def dreieck(freq, amp, duration):
    zeit = np.linspace(0, 2, int(freq*duration))
    dreieck = amp*signal.sawtooth(2*np.pi*freq*zeit, width=0.5)
    return dreieck

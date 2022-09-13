import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def rechteck(freq, amp):
    zeit = np.linspace(0, 2, 1000)
    rect = amp*signal.square(2*np.pi*freq*zeit, duty=0.3)

    plt.figure(figsize=(10, 4))
    plt.plot(zeit, rect)
    plt.xlabel('Zeit (s)')
    plt.ylabel('Amplitude')
    plt.show()


def sin(freq, amp):
    zeit = np.linspace(0, 2, 1000)
    sin = amp*np.sin(2*np.pi*freq*zeit)
    plt.figure(figsize=(10, 4))
    plt.plot(zeit, sin)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
    return sin


def dreieck(freq, amp):
    zeit = np.linspace(0, 2, 1000)
    dreieck = amp*signal.sawtooth(2*np.pi*freq*zeit, width=0.5)
    plt.figure(figsize=(10, 4))
    plt.plot(zeit, dreieck)
    plt.xlabel('Zeit (s)')
    plt.ylabel('Amplitude')
    plt.show()

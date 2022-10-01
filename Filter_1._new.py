import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def Filter(freq, dauer, a1, a2, b1, b2, data):
    a = (a1, a2)
    b = (b1, b2)
    # Plot von dem Frequenzantwort.
    w, h = freqz(b, a, fs=freq, worN=8000)
    plt.plot(w, np.abs(h), 'b')
    plt.xlim(0, 0.5 * freq)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    plt.show()
    n = int(dauer * freq)  # Anzahl von samples
    t = np.linspace(0, dauer, n, endpoint=False)
    # Filterung von der Daten
    y = lfilter(b, a, data)
    # 2 график ось y, это сигнал после трансформации фурье
    data_freq = np.fft.fft(data)
    freq_samples = np.fft.fftfreq(len(data), d=2)
    plt.subplot(2, 1, 2)
    plt.plot(freq_samples, data_freq)
    plt.xlabel('Frequenz (s)')
    plt.ylabel('Amplitude')
    plt.subplots_adjust(hspace=0.35)
    plt.show()
    # Darstellung von der gefilterten und nicht gefilterten Daten (zusammen)
    plt.plot(t, data, 'b-', label='data')
    plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.show()
    return y


T = 5.0         # seconds
n = int(T * 30)  # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
dataa = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + \
    0.5*np.sin(12.0*2*np.pi*t)
Filter(30, 5, 1, -0.423333, 0.2877831895970474, 0.2877831895970474, dataa)

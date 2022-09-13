import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def Filter(freq, dauer, a1, a2, b1, b2, data):
    a = (a1, a2)
    b = (b1, b2)
    cutoff = 3.667

    # Plot von dem Frequenzantwort.
    w, h = freqz(b, a, fs=freq, worN=8000)
    plt.subplot(2, 1, 1)
    plt.plot(w, np.abs(h), 'b')
    plt.xlim(0, 0.5 * freq)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.grid()

    n = int(dauer * freq)  # Anzahl von samples
    t = np.linspace(0, dauer, n, endpoint=False)

    # Filterung von der Daten
    y = lfilter(b, a, data)

    # Darstellung von der gefilterten und nicht gefilterten Daten (zusammen)
    plt.subplot(2, 1, 2)
    plt.plot(t, data, 'b-', label='data')
    plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()

    plt.subplots_adjust(hspace=0.35)
    plt.show()
    return y

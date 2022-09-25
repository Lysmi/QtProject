import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_bandpass(lowcut, highcut, fs, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)

    w, h = freqz(b, a, fs=fs, worN=2000)

    plt.plot(w, np.abs(h), 'b')
    plt.xlim(0, 0.5 * fs)
    plt.title("Bandpass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.grid() #Frequenzgang von dem Bandpassfilter, Заплотал поведение бандпаса, этот график вынести отдельным окном, а графики 2 и 3 сделать сабплотами
    plt.show()
    return y

def Filter(freq, dauer,data):


    n = int(dauer * freq)  # Anzahl von samples
    t = np.linspace(0, dauer, n, endpoint=False)

    # Filterung von der Daten
    y = butter_bandpass_filter(data, 10, 14, freq, order=1)


    data_freq = np.fft.fft(data)  # 2 график ось y, это сигнал после трансформации фурье
    freq_samples = np.fft.fftfreq(len(data), d=2)


    plt.subplot(2, 1, 2)
    plt.plot(freq_samples, data_freq)
    plt.xlabel('Frequenz (s)')
    plt.ylabel('Amplitude')
    plt.subplots_adjust(hspace=0.35)
    plt.title("2")
    plt.show()

    # Darstellung von der gefilterten und nicht gefilterten Daten (zusammen)
    plt.plot(t, data, 'b-', label='data')
    plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.title("3")
    plt.show()

    return y

T = 5.0         # seconds
n = int(T * 30) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
dataa= np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)
Filter(30,5,dataa)
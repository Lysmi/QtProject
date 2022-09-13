import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False) # Erzeugung von Butterworth-Filter

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Filter Eigenschaften.
order = 6
fs = 30.0       # Sample rate, Hz
cutoff = 3.667  # Grenzfrequenz von dem Filter, Hz

# Berechnung von den Filterkoeffizienten ( fuer die Frequenzantwort ).
b, a = butter_lowpass(cutoff, fs, order)

# Plot von dem Frequenzantwort.
w, h = freqz(b, a, fs=fs, worN=8000) #Berechung von dem Frequenzantwort
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Frequenzgang von  dem tiefpass Filter")
plt.xlabel('Frequency [Hz]')
plt.grid()




T = 5.0         # Sekunden
n = int(T * fs) # Anzahl von samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filterung von der Daten
y = butter_lowpass_filter(data, cutoff, fs, order)

#Darstellung von der gefilterten und nicht gefilterten Daten (zusammen)
plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()
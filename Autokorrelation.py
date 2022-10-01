import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def akf(data, freq, dauer):
    #
    # Mittelwert
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # normalizierte Daten
    ndata = data - mean

    acorr = np.correlate(ndata, ndata, 'full')[len(ndata) - 1:]
    acorr = acorr / var / len(ndata)

    t = np.linspace(0, 2, 1000)
    return acorr
    # plt.plot(t, data, 'b-')
    # plt.plot(t, acorr, 'g-', linewidth=2)
    # plt.xlabel('Time [sec]')
    # plt.grid()
    # plt.legend()

    # plt.subplots_adjust(hspace=0.35)
    # plt.show()

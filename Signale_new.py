import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
def rechteck (freq, amp):
    freq = 2
    amp = 2
    zeit = np.linspace(0, 2, 1000)
    rect = amp*signal.square(2*np.pi*freq*zeit, duty=0.3)

    #Макс и Алина, по поводу графиков в 1 задании, их должно быть 2. 1 график-это сигнал считываемый с распбери пай
    #(по факту это сигнал который вы делаете через Abtastfrequenz
    #2 график это сигнал после трансформации фурье ( 1 в 1 как в этой функции второй сабплот)
    #для треугольника и синуса все то же самое

    rect_freq=np.fft.fft(rect) # 2 график ось y, это сигнал после трансформации фурье
    freq_samples=np.fft.fftfreq(1000,d=2)# 2 график ось х, это массив частот

    plt.subplot(2, 1, 1)
    plt.plot(zeit, rect)
    plt.xlabel('Zeitr (s)')
    plt.ylabel('Amplitude')


    plt.subplot(2, 1, 2)

    plt.plot(freq_samples, rect_freq)
    plt.xlabel('Frequenz (s)')
    plt.ylabel('Amplitude')
    plt.subplots_adjust(hspace=0.35)
    plt.show()
    return rect, rect_freq

def sin (freq, amp):
    freq = 2
    amp = 2
    zeit = np.linspace(0, 2, 1000)
    sin = amp*np.sin(2*np.pi*freq*zeit)

    sin_freq = np.fft.fft(sin)  # 2 график ось y, это сигнал после трансформации фурье
    freq_samples = np.fft.fftfreq(1000, d=2)

    plt.subplot(2, 1, 1)
    plt.plot(zeit, sin)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')


    plt.subplot(2, 1, 2)

    plt.plot(freq_samples, sin_freq)
    plt.xlabel('Frequenz (s)')
    plt.ylabel('Amplitude')
    plt.subplots_adjust(hspace=0.35)
    plt.show()
    return sin, sin_freq

def dreieck (freq,amp):
    freq = 2
    amp = 2
    zeit = np.linspace(0, 2, 1000)
    dreieck=amp*signal.sawtooth(2*np.pi*freq*zeit, width=0.5)

    dreieck_freq = np.fft.fft(dreieck)  # 2 график ось y, это сигнал после трансформации фурье
    freq_samples = np.fft.fftfreq(1000, d=2)  # 2 график ось х, это массив частот

    plt.subplot(2, 1, 1)
    plt.plot(zeit, dreieck)
    plt.xlabel('Zeit (s)')
    plt.ylabel('Amplitude')


    plt.subplot(2, 1, 2)

    plt.plot(freq_samples, dreieck_freq)
    plt.xlabel('Frequenz (s)')
    plt.ylabel('Amplitude')
    plt.subplots_adjust(hspace=0.35)
    plt.show()
    return dreieck,dreieck_freq


a=rechteck(2,3)
b=sin(3.14,1)

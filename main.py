from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, PlotDataItem, mkBrush, mkColor, mkPen
import sys  # We need sys so that we can pass argv to QApplication
import mainForm
import os
import Signale
from Filter import Filter
import Filter_new
import pyqtgraph
import bandpass
import Signale_new
import Autokorrelation
import ReadADC_V01


class MainWindow(QtWidgets.QMainWindow, mainForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_2.clicked.connect(
            lambda: secondExperiment(
                self.v2_frequenz.value(),
                self.v2_duration.value(),
                self.v2_a1.value(),
                self.v2_a2.value(),
                self.v2_b1.value(),
                self.v2_b2.value(),
                self.upGraphicsView_2, self.downGraphicsView_2, self.v2_signaltype.currentText())
        )
        self.pushButton_5.clicked.connect(
            lambda: firstExperiment(
                self.v1_frequenz.value(),
                self.v1_duration.value(),
                self.upGraphicsView, self.downGraphicsView, self.v1_signaltype.currentText())
        )
        self.pushButton_6.clicked.connect(
            lambda: thirdExperiment(
                67,
                self.v3_duration.value(),
                self.upGraphicsView_3, self.downGraphicsView_3, self.v3_signaltype.currentText())
        )
        self.pushButton_7.clicked.connect(
            lambda: forthExperiment(
                self.v4_frequenz.value(),
                self.v4_duration.value(),
                self.upGraphicsView_4, self.downGraphicsView_4, self.v4_signaltype.currentText())
        )
        self.upGraphicsView.setBackground(mkColor(0.82))
        self.upGraphicsView.setTitle('Echte Daten')
        self.upGraphicsView.setLabel('left', text='Amplitude(Vt)')
        self.upGraphicsView.setLabel('bottom', text='Zeit(Sec)')

        self.downGraphicsView.setBackground(mkColor(0.82))
        self.downGraphicsView.setTitle('Signal im Frequenzbereich')
        self.downGraphicsView.setLabel(
            'left', text='Amplitude Normalisiert(Vt)')
        self.downGraphicsView.setLabel('bottom', text='Frequenz(Hz)')

        self.upGraphicsView_2.setBackground(mkColor(0.82))
        self.upGraphicsView_2.setTitle('Signal im Frequenzbereich')
        self.upGraphicsView_2.setLabel('left', text='Amplitude(Vt)')
        self.upGraphicsView_2.setLabel('bottom', text='Zeit(Sec)')

        self.downGraphicsView_2.setBackground(mkColor(0.82))
        self.downGraphicsView_2.setTitle('Gefiltertes Signal')
        self.downGraphicsView_2.setLabel('left', text='Amplitude(Vt)')
        self.downGraphicsView_2.setLabel('bottom', text='Frequenz(Hz)')

        self.upGraphicsView_3.setBackground(mkColor(0.82))
        self.upGraphicsView_3.setTitle('Gefiltertes Signal')
        self.upGraphicsView_3.setLabel('left', text='Amplitude')
        self.upGraphicsView_3.setLabel('bottom', text='Zeit [s]')

        self.downGraphicsView_3.setBackground(mkColor(0.82))
        self.downGraphicsView_3.setTitle('Fouriertransformation')
        self.downGraphicsView_3.setLabel(
            'left', text='Amplitude Normalisiert(Vt)')
        self.downGraphicsView_3.setLabel('bottom', text='Frequenz(Hz)')

        self.upGraphicsView_4.setBackground(mkColor(0.82))
        self.upGraphicsView_4.setTitle('Autokorrelation')
        self.upGraphicsView_4.setLabel('left', text='Amplitude(Vt)')
        self.upGraphicsView_4.setLabel('bottom', text='Zeit [s]')


def forthExperiment(freq, duration, qtGraphUp, qtGraphDown, type):
    data = []
    if type == "Sinus":
        data = Signale.sin(2, 10, duration)
    elif type == "Rechteck":
        data = Signale.rechteck(2, 10, duration)
    elif type == "Dreieck":
        data = Signale.dreieck(2, 10, duration)
    elif type == "ADC":
        data = ReadADC_V01.ADCSignale(freq, duration)
    multiple = int(2000/freq)
    multiple = 1 if multiple < 1 else multiple
    readedDataY = data[::multiple]
    readedDataX = [i*multiple for i in range(len(readedDataY))]
    filterRes = Autokorrelation.akf(readedDataY, freq, duration)

    plotGraphWithData(filterRes, readedDataY, qtGraphUp)


def thirdExperiment(freq, duration, qtGraphUp, qtGraphDown, type):
    data = []
    if type == "Sinus":
        data = Signale.sin(2, 10, duration)
    elif type == "Rechteck":
        data = Signale.rechteck(2, 10, duration)
    elif type == "Dreieck":
        data = Signale.dreieck(2, 10, duration)
    elif type == "ADC":
        data = ReadADC_V01.ADCSignale(freq, duration)
    multiple = int(2000/freq)
    multiple = 1 if multiple < 1 else multiple
    readedDataY = data[::multiple]
    readedDataX = [i*multiple for i in range(len(readedDataY))]

    filterRes = bandpass.Filter(freq, duration, readedDataY)

    plotGraphWithXY((filterRes[2], filterRes[3]), qtGraphDown)
    plotGraph(filterRes[0], qtGraphUp, 'b')


def secondExperiment(freq, duration, a1, a2, b1, b2, qtGraphUp, qtGraphDown, type):
    if (a1 == 0):
        return
    data = []
    if type == "Sinus":
        data = Signale.sin(2, 10, duration)
    elif type == "Rechteck":
        data = Signale.rechteck(2, 10, duration)
    elif type == "Dreieck":
        data = Signale.dreieck(2, 10, duration)
    elif type == "ADC":
        data = ReadADC_V01.ADCSignale(freq, duration)
    multiple = int(2000/freq)
    multiple = 1 if multiple < 1 else multiple
    readedDataY = data[::multiple]
    readedDataX = [i*multiple for i in range(len(readedDataY))]

    filterRes = Filter_new.Filter(freq, duration, a1, a2, b1, b2, readedDataY)
    plotGraph(filterRes[0], qtGraphUp)
    plotGraph(filterRes[1], qtGraphDown, "b")


def firstExperiment(freq, duration, qtGraphUp, qtGraphDown, type):
    data = []
    if type == "Sinus":
        data = Signale_new.sin(2, 10, duration)
    elif type == "Rechteck":
        data = Signale_new.rechteck(2, 10, duration)
    elif type == "Dreieck":
        data = Signale_new.dreieck(2, 10, duration)
    elif type == "ADC":
        data = ReadADC_V01.ADCSignale(freq, duration)
    multiple = int(2000/freq)
    multiple = 1 if multiple < 1 else multiple
    readedDataY = data[::multiple]
    readedDataX = [i*multiple for i in range(len(readedDataY))]
    plotGraph(data[0], qtGraphUp)
    plotGraph(data[1], qtGraphDown, 'b')


def plotGraph(graph, qtGraph: PlotWidget, color='r'):
    qtGraph.clear()
    qtGraph.plot(graph, pen=mkPen(color=color, width=2), symbol=None,)
    qtGraph.autoRange()


def plotGraphWithXY(graph, qtGraph: PlotWidget, color='r'):
    qtGraph.clear()
    qtGraph.plot(graph[0], graph[1], pen=mkPen(
        color=color, width=2), symbol=None)
    qtGraph.autoRange()


def plotGraphWithData(graph, data, qtGraph: PlotWidget):
    qtGraph.clear()
    if type(graph) is tuple:
        qtGraph.plot(graph[0], graph[1], pen=mkPen(
            color='r', width=2), symbol=None, )
    else:
        qtGraph.plot(graph, pen=mkPen(color='r', width=2), symbol=None, )
    qtGraph.plot(data, pen=mkPen(color='b', width=2), symbol=None, )
    qtGraph.autoRange()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

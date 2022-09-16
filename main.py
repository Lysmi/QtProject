from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, PlotDataItem, mkBrush, mkColor, mkPen
import sys  # We need sys so that we can pass argv to QApplication
import mainForm
import os
import Signale
from Filter import Filter
import pyqtgraph


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
        self.upGraphicsView.setBackground(mkColor(0.82))
        self.upGraphicsView.setTitle('Real Data')
        self.upGraphicsView.setLabel('left', text='Amplitude(Vt)')
        self.upGraphicsView.setLabel('bottom', text='Time(Sec)')

        self.downGraphicsView.setBackground(mkColor(0.82))
        self.downGraphicsView.setTitle('Readed Data')
        self.downGraphicsView.setLabel('left', text='Amplitude(Vt)')
        self.downGraphicsView.setLabel('bottom', text='Time(Sec)')

        self.upGraphicsView_2.setBackground(mkColor(0.82))
        upGraphicsView2Legend = self.upGraphicsView_2.addLegend(offset=(2, 2),
                                                                pen=mkPen(mkColor(0.0)), brush=mkBrush(mkColor(0.95)), labelTextColor=mkColor(0.0))
        upGraphicsView2Legend.addItem(PlotDataItem(
            range(100), pen=mkPen(color='b')), 'Data')
        upGraphicsView2Legend.addItem(PlotDataItem(
            range(100), pen=mkPen(color='r')), 'Filtered Readed Data')
        self.downGraphicsView.setLabel('left', text='Amplitude(Vt)')
        self.downGraphicsView.setLabel('bottom', text='Time(Sec)')

        self.downGraphicsView_2.setBackground(mkColor(0.82))
        self.downGraphicsView_2.setTitle('Filter Frequency Response')
        self.downGraphicsView_2.setLabel('left', text='Amplitude(Vt)')
        self.downGraphicsView_2.setLabel('bottom', text='Angular Frequency')

        self.upGraphicsView_3.addLegend()
        self.upGraphicsView_3.setBackground(mkColor(0.82))

        self.downGraphicsView_3.setBackground(mkColor(0.82))

        self.upGraphicsView_4.setBackground(mkColor(0.82))

        self.downGraphicsView_4.setBackground(mkColor(0.82))


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
    multiple = int(2000/freq)
    multiple = 1 if multiple < 1 else multiple
    readedDataY = data[::multiple]
    readedDataX = [i*multiple for i in range(len(readedDataY))]

    filterRes = Filter(freq, duration, a1, a2, b1, b2, readedDataY)
    plotGraphWithData((readedDataX, filterRes[0]), data, qtGraphUp)
    plotGraphWithXY(filterRes[1], qtGraphDown)


def firstExperiment(freq, duration, qtGraphUp, qtGraphDown, type):
    data = []
    if type == "Sinus":
        data = Signale.sin(2, 10, duration)
    elif type == "Rechteck":
        data = Signale.rechteck(2, 10, duration)
    elif type == "Dreieck":
        data = Signale.dreieck(2, 10, duration)
    multiple = int(2000/freq)
    multiple = 1 if multiple < 1 else multiple
    readedDataY = data[::multiple]
    readedDataX = [i*multiple for i in range(len(readedDataY))]
    plotGraph(data, qtGraphUp)
    plotGraphWithXY((readedDataX, readedDataY), qtGraphDown, 'b')


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

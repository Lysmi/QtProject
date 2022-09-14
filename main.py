from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget
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
        self.upGraphicsView.setBackground(pyqtgraph.mkColor(0.82))
        self.downGraphicsView.setBackground(pyqtgraph.mkColor(0.82))
        self.upGraphicsView_2.setBackground(pyqtgraph.mkColor(0.82))
        self.downGraphicsView_2.setBackground(pyqtgraph.mkColor(0.82))
        self.upGraphicsView_3.setBackground(pyqtgraph.mkColor(0.82))
        self.downGraphicsView_3.setBackground(pyqtgraph.mkColor(0.82))
        self.upGraphicsView_4.setBackground(pyqtgraph.mkColor(0.82))
        self.downGraphicsView_4.setBackground(pyqtgraph.mkColor(0.82))


def secondExperiment(freq, duration, a1, a2, b1, b2, qtGraphUp, qtGraphDown, type):
    if (a1 == 0):
        return
    data = []
    if type == "Sinus":
        data = Signale.sin(freq, 10, duration)
    elif type == "Rechteck":
        data = Signale.rechteck(freq, 10, duration)
    elif type == "Dreieck":
        data = Signale.dreieck(freq, 10, duration)
    filterRes = Filter(freq, duration, a1, a2, b1, b2, data)
    plotGraphWithData(filterRes[0], data, qtGraphUp)
    plotGraphWithXY(filterRes[1], qtGraphDown)


def firstExperiment(freq, duration, qtGraphUp, qtGraphDown, type):
    data = []
    if type == "Sinus":
        data = Signale.sin(freq, 10, duration)
    elif type == "Rechteck":
        data = Signale.rechteck(freq, 10, duration)
    elif type == "Dreieck":
        data = Signale.dreieck(freq, 10, duration)
    plotGraph(data, qtGraphUp)


def plotGraph(graph, qtGraph: PlotWidget):
    qtGraph.clear()
    qtGraph.plot(graph, pen=pyqtgraph.mkPen(color='r'), symbol=None, )
    qtGraph.autoRange()


def plotGraphWithXY(graph, qtGraph: PlotWidget):
    qtGraph.clear()
    qtGraph.plot(graph[0], graph[1], pen=pyqtgraph.mkPen(
        color='r'), symbol=None)
    qtGraph.autoRange()


def plotGraphWithData(graph, data, qtGraph: PlotWidget):
    qtGraph.clear()
    qtGraph.plot(graph, pen=pyqtgraph.mkPen(color='r'), symbol=None, )
    qtGraph.plot(data, pen=pyqtgraph.mkPen(color='b'), symbol=None, )
    qtGraph.autoRange()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

from PyQt5 import QtWidgets

import sys  # We need sys so that we can pass argv to QApplication
import mainForm
import os
import Signale
import Filter_1


class MainWindow(QtWidgets.QMainWindow, mainForm.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # plot data: x, y values
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    a = Signale.sin(3, 10)+Signale.sin(1, 15)-Signale.sin(4, 5)
    Filter_1.Filter(5, 200, 0.000223213, 0.00035454, 0.00656, 0.0055, a)
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

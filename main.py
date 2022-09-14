from PyQt5 import QtWidgets

import sys  # We need sys so that we can pass argv to QApplication
import mainForm
import os
import Signale
import Filter


class MainWindow(QtWidgets.QMainWindow, mainForm.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # plot data: x, y values
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

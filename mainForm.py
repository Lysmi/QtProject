# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled11.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget as QtGraph
import pyqtgraph
import Signale

import pyqtgraph as pg
import numpy as np

from Filter import Filter


class Ui_MainWindow(object):
    def tab_2_making(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background: rgb(161, 169, 180)")
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 520, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:  rgb(210, 210, 210)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 600, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setIndent(70)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(530, 90, 491, 91))
        self.textEdit_2.setStyleSheet("background:  rgb(210, 210, 210)")
        self.textEdit_2.setObjectName("textEdit_2")
        self.upGraphicsView_2 = QtGraph(self.tab_2, pyqtgraph.mkColor(0.82))
        self.upGraphicsView_2.setGeometry(QtCore.QRect(530, 200, 491, 201))
        self.upGraphicsView_2.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.upGraphicsView_2.setObjectName("upGraphicsView_2")
        self.downGraphicsView_2 = QtGraph(self.tab_2, pyqtgraph.mkColor(0.82))
        self.downGraphicsView_2.setGeometry(QtCore.QRect(530, 420, 491, 201))
        self.downGraphicsView_2.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.downGraphicsView_2.setObjectName("downGraphicsView_2")
        self.v2_signaltype = QtWidgets.QComboBox(self.tab_2)
        self.v2_signaltype.setGeometry(QtCore.QRect(130, 90, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_signaltype.setFont(font)
        self.v2_signaltype.setStyleSheet("background: rgb(210, 210, 210)")
        self.v2_signaltype.setObjectName("v2_signaltype")
        self.v2_signaltype.addItem("")
        self.v2_signaltype.addItem("")
        self.v2_signaltype.addItem("")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 150, 351, 321))
        self.groupBox_2.setStyleSheet("background: rgb(210, 210, 210)")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 80, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(10, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.v2_frequenz = QtWidgets.QSpinBox(self.groupBox_2)
        self.v2_frequenz.setGeometry(QtCore.QRect(230, 50, 62, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.v2_frequenz.sizePolicy().hasHeightForWidth())
        self.v2_frequenz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_frequenz.setFont(font)
        self.v2_frequenz.setStyleSheet("background: rgb(255, 255, 255)")
        self.v2_frequenz.setObjectName("v2_frequenz")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(10, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(10, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(10, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(10, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.v2_duration = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.v2_duration.setGeometry(QtCore.QRect(230, 80, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_duration.setFont(font)
        self.v2_duration.setStyleSheet("background: rgb(255, 255, 255)")
        self.v2_duration.setObjectName("v2_duration")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(300, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(300, 85, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.v2_a1 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.v2_a1.setGeometry(QtCore.QRect(50, 150, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_a1.setFont(font)
        self.v2_a1.setStyleSheet("background: rgb(255, 255, 255)\n"
                                 "")
        self.v2_a1.setObjectName("v2_a1")
        self.v2_a2 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.v2_a2.setGeometry(QtCore.QRect(50, 190, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_a2.setFont(font)
        self.v2_a2.setStyleSheet("background: rgb(255, 255, 255)")
        self.v2_a2.setObjectName("v2_a2")
        self.v2_b1 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.v2_b1.setGeometry(QtCore.QRect(50, 230, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_b1.setFont(font)
        self.v2_b1.setStyleSheet("background: rgb(255, 255, 255)")
        self.v2_b1.setObjectName("v2_b1")
        self.v2_b2 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.v2_b2.setGeometry(QtCore.QRect(50, 270, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v2_b2.setFont(font)
        self.v2_b2.setStyleSheet("background: rgb(255, 255, 255)")
        self.v2_b2.setObjectName("v2_b2")
        self.experiment.addTab(self.tab_2, "")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 699)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.experiment = QtWidgets.QTabWidget(self.centralwidget)
        self.experiment.setGeometry(QtCore.QRect(0, 0, 1050, 700))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.experiment.sizePolicy().hasHeightForWidth())
        self.experiment.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.experiment.setFont(font)
        self.experiment.setAutoFillBackground(False)
        self.experiment.setStyleSheet("background: rgb(161, 169, 180)")
        self.experiment.setDocumentMode(True)
        self.experiment.setTabsClosable(False)
        self.experiment.setMovable(False)
        self.experiment.setTabBarAutoHide(False)
        self.experiment.setObjectName("experiment")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("background: rgb(161, 169, 180)")
        self.tab_1.setObjectName("tab_1")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(200, 20, 600, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setIndent(70)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit.setGeometry(QtCore.QRect(530, 90, 491, 91))
        self.textEdit.setStyleSheet("background:  rgb(210, 210, 210)")
        self.textEdit.setObjectName("textEdit")
        self.upGraphicsView = QtGraph(self.tab_1, pyqtgraph.mkColor(0.82))
        self.upGraphicsView.setGeometry(QtCore.QRect(530, 200, 491, 201))
        self.upGraphicsView.setStyleSheet("border: 1px solid rgb(30, 30, 30)")
        self.upGraphicsView.setObjectName("upGraphicsView")
        self.downGraphicsView = QtGraph(self.tab_1, pyqtgraph.mkColor(0.82))
        self.downGraphicsView.setGeometry(QtCore.QRect(530, 420, 491, 201))
        self.downGraphicsView.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.downGraphicsView.setObjectName("downGraphicsView")
        self.v1_signaltype = QtWidgets.QComboBox(self.tab_1)
        self.v1_signaltype.setGeometry(QtCore.QRect(130, 90, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v1_signaltype.setFont(font)
        self.v1_signaltype.setStyleSheet("background: rgb(210, 210, 210)")
        self.v1_signaltype.setObjectName("v1_signaltype")
        self.v1_signaltype.addItem("")
        self.v1_signaltype.addItem("")
        self.v1_signaltype.addItem("")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 520, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background:  rgb(210, 210, 210)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 150, 351, 321))
        self.groupBox_5.setStyleSheet("background: rgb(210, 210, 210)")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setGeometry(QtCore.QRect(10, 80, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.v1_frequenz = QtWidgets.QSpinBox(self.groupBox_5)
        self.v1_frequenz.setGeometry(QtCore.QRect(230, 50, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v1_frequenz.setFont(font)
        self.v1_frequenz.setStyleSheet("background: rgb(255, 255, 255)")
        self.v1_frequenz.setObjectName("v1_frequenz")
        self.v1_duration = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.v1_duration.setGeometry(QtCore.QRect(230, 80, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v1_duration.setFont(font)
        self.v1_duration.setStyleSheet("background: rgb(255, 255, 255)")
        self.v1_duration.setObjectName("v1_duration")
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        self.label_35.setGeometry(QtCore.QRect(300, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox_5)
        self.label_36.setGeometry(QtCore.QRect(300, 85, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.experiment.addTab(self.tab_1, "")

        self.tab_2_making()

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 600, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setIndent(70)
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(530, 90, 491, 91))
        self.textEdit_3.setStyleSheet("background:  rgb(210, 210, 210)")
        self.textEdit_3.setObjectName("textEdit_3")
        self.upGraphicsView_3 = QtGraph(self.tab_3, pyqtgraph.mkColor(0.82))
        self.upGraphicsView_3.setGeometry(QtCore.QRect(530, 200, 491, 201))
        self.upGraphicsView_3.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.upGraphicsView_3.setObjectName("upGraphicsView_3")
        self.downGraphicsView_3 = QtGraph(self.tab_3, pyqtgraph.mkColor(0.82))
        self.downGraphicsView_3.setGeometry(QtCore.QRect(530, 420, 491, 201))
        self.downGraphicsView_3.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.downGraphicsView_3.setObjectName("downGraphicsView_3")
        self.v3_signaltype = QtWidgets.QComboBox(self.tab_3)
        self.v3_signaltype.setGeometry(QtCore.QRect(130, 90, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v3_signaltype.setFont(font)
        self.v3_signaltype.setStyleSheet("background: rgb(210, 210, 210)")
        self.v3_signaltype.setObjectName("v3_signaltype")
        self.v3_signaltype.addItem("")
        self.v3_signaltype.addItem("")
        self.v3_signaltype.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 150, 351, 321))
        self.groupBox_3.setStyleSheet("background: rgb(210, 210, 210)")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.v3_frequenz = QtWidgets.QSpinBox(self.groupBox_3)
        self.v3_frequenz.setGeometry(QtCore.QRect(230, 50, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v3_frequenz.setFont(font)
        self.v3_frequenz.setStyleSheet("background: rgb(255, 255, 255)")
        self.v3_frequenz.setObjectName("v3_frequenz")
        self.v3_duration = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.v3_duration.setGeometry(QtCore.QRect(230, 80, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v3_duration.setFont(font)
        self.v3_duration.setStyleSheet("background: rgb(255, 255, 255)")
        self.v3_duration.setObjectName("v3_duration")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(300, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(300, 85, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 520, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background:  rgb(210, 210, 210)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.experiment.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(200, 20, 600, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setIndent(70)
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(530, 90, 491, 91))
        self.textEdit_4.setStyleSheet("background:  rgb(210, 210, 210)")
        self.textEdit_4.setObjectName("textEdit_4")
        self.v4_signaltype = QtWidgets.QComboBox(self.tab_4)
        self.v4_signaltype.setGeometry(QtCore.QRect(130, 90, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v4_signaltype.setFont(font)
        self.v4_signaltype.setStyleSheet("background: rgb(210, 210, 210)")
        self.v4_signaltype.setObjectName("v4_signaltype")
        self.v4_signaltype.addItem("")
        self.v4_signaltype.addItem("")
        self.v4_signaltype.addItem("")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.upGraphicsView_4 = QtGraph(self.tab_4, pyqtgraph.mkColor(0.82))
        self.upGraphicsView_4.setGeometry(QtCore.QRect(530, 200, 491, 201))
        self.upGraphicsView_4.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.upGraphicsView_4.setObjectName("upGraphicsView_4")
        self.downGraphicsView_4 = QtGraph(self.tab_4, pyqtgraph.mkColor(0.82))
        self.downGraphicsView_4.setGeometry(QtCore.QRect(530, 420, 491, 201))
        self.downGraphicsView_4.setStyleSheet(
            "border: 1px solid rgb(30, 30, 30)")
        self.downGraphicsView_4.setObjectName("downGraphicsView_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 520, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background:  rgb(210, 210, 210)")
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 150, 351, 321))
        self.groupBox_4.setStyleSheet("background: rgb(210, 210, 210)")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(10, 80, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.v4_frequenz = QtWidgets.QSpinBox(self.groupBox_4)
        self.v4_frequenz.setGeometry(QtCore.QRect(230, 50, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v4_frequenz.setFont(font)
        self.v4_frequenz.setStyleSheet("background: rgb(255, 255, 255)")
        self.v4_frequenz.setObjectName("v4_frequenz")
        self.v4_duration = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.v4_duration.setGeometry(QtCore.QRect(230, 80, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.v4_duration.setFont(font)
        self.v4_duration.setStyleSheet("background: rgb(255, 255, 255)")
        self.v4_duration.setObjectName("v4_duration")
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(300, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(300, 85, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.experiment.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 20))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.experiment.setCurrentIndex(0)

        # мне похер, я Донбасянен
        # Подключение кнопак

        self.pushButton_2.clicked.connect(
            lambda: secondExperiment(
                self.v2_frequenz.value(),
                self.v2_duration.value(),
                self.v2_a1.value(),
                self.v2_a2.value(),
                self.v2_b1.value(),
                self.v2_b2.value(),
                self.upGraphicsView_2)
        )

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "Praktikumsversuch 1: Digitale Signalverarbeitung"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Kurzbeschreibung: Analysieren Sie die Effekte der Abtastfrequenz anhand der vorgegebenen Versuchsbeschreibung.</span></p></body></html>"))
        self.v1_signaltype.setItemText(0, _translate("MainWindow", "Sinus"))
        self.v1_signaltype.setItemText(1, _translate("MainWindow", "Rechteck"))
        self.v1_signaltype.setItemText(2, _translate("MainWindow", "Dreieck"))
        self.label_9.setText(_translate("MainWindow", " Signaltyp:"))
        self.pushButton_5.setText(_translate(
            "MainWindow", "Start Aufzeichnung"))
        self.label_17.setText(_translate("MainWindow", "ADC:"))
        self.label_18.setText(_translate("MainWindow", "Abtastfrequenz:"))
        self.label_34.setText(_translate("MainWindow", "Aufzeichnungsdauer:"))
        self.label_35.setText(_translate("MainWindow", "Hz"))
        self.label_36.setText(_translate("MainWindow", "sec"))
        self.experiment.setTabText(self.experiment.indexOf(
            self.tab_1), _translate("MainWindow", "Versuch 1"))
        self.pushButton_2.setText(_translate(
            "MainWindow", "Start Aufzeichnung"))
        self.label_3.setText(_translate(
            "MainWindow", "Praktikumsversuch 2: Digitale Signalverarbeitung"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Kurzbeschreibung: Realisieren Sie durch Eingabe der FIR-Filterkoeffizienten digitale Hoch- und Tiefpassfilter.</span></p></body></html>"))
        self.v2_signaltype.setItemText(0, _translate("MainWindow", "Sinus"))
        self.v2_signaltype.setItemText(1, _translate("MainWindow", "Rechteck"))
        self.v2_signaltype.setItemText(2, _translate("MainWindow", "Dreieck"))
        self.label_8.setText(_translate("MainWindow", " Signaltyp:"))
        self.label_19.setText(_translate("MainWindow", "ADC:"))
        self.label_20.setText(_translate("MainWindow", "Abtastfrequenz:"))
        self.label_21.setText(_translate("MainWindow", "Aufzeichnungsdauer:"))
        self.label_22.setText(_translate(
            "MainWindow", "FIR-Filterkoeffizienten:"))
        self.label_23.setText(_translate("MainWindow", "a1:"))
        self.label_24.setText(_translate("MainWindow", "a2:"))
        self.label_25.setText(_translate("MainWindow", "b1:"))
        self.label_26.setText(_translate("MainWindow", "b2:"))
        self.label_27.setText(_translate("MainWindow", "Hz"))
        self.label_28.setText(_translate("MainWindow", "sec"))
        self.experiment.setTabText(self.experiment.indexOf(
            self.tab_2), _translate("MainWindow", "Versuch 2"))
        self.label_4.setText(_translate(
            "MainWindow", "Praktikumsversuch 3: Digitale Signalverarbeitung"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Kurzbeschreibung: Hinter der Übertragungsfunktion verbirgt sich ein Filter. Welches? Wählen Sie geeignete Signalformen aus und analzsieren Sie das Ausgangssignal.</span></p></body></html>"))
        self.v3_signaltype.setItemText(0, _translate("MainWindow", "Sinus"))
        self.v3_signaltype.setItemText(1, _translate("MainWindow", "Rechteck"))
        self.v3_signaltype.setItemText(2, _translate("MainWindow", "Dreieck"))
        self.label_7.setText(_translate("MainWindow", " Signaltyp:"))
        self.label_12.setText(_translate("MainWindow", "ADC:"))
        self.label_13.setText(_translate("MainWindow", "Abtastfrequenz:"))
        self.label_14.setText(_translate("MainWindow", "Aufzeichnungsdauer:"))
        self.label_29.setText(_translate("MainWindow", "Hz"))
        self.label_30.setText(_translate("MainWindow", "sec"))
        self.pushButton_6.setText(_translate(
            "MainWindow", "Start Aufzeichnung"))
        self.experiment.setTabText(self.experiment.indexOf(
            self.tab_3), _translate("MainWindow", "Versuch 3"))
        self.label_5.setText(_translate(
            "MainWindow", "Praktikumsversuch 4: Digitale Signalverarbeitung"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Kurzbeschreibung: Ermitteln Sie aus der Autokorrelationsfunktion, die Periodendauer sowie die Energie des Eingangssignals.</span></p></body></html>"))
        self.v4_signaltype.setItemText(0, _translate("MainWindow", "Sinus"))
        self.v4_signaltype.setItemText(1, _translate("MainWindow", "Rechteck"))
        self.v4_signaltype.setItemText(2, _translate("MainWindow", "Dreieck"))
        self.label_6.setText(_translate("MainWindow", " Signaltyp:"))
        self.pushButton_7.setText(_translate(
            "MainWindow", "Start Aufzeichnung"))
        self.label_15.setText(_translate("MainWindow", "ADC:"))
        self.label_16.setText(_translate("MainWindow", "Abtastfrequenz:"))
        self.label_31.setText(_translate("MainWindow", "Aufzeichnungsdauer:"))
        self.label_32.setText(_translate("MainWindow", "Hz"))
        self.label_33.setText(_translate("MainWindow", "sec"))
        self.experiment.setTabText(self.experiment.indexOf(
            self.tab_4), _translate("MainWindow", "Versuch 4"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))


def secondExperiment(freq, duration, a1, a2, b1, b2, qtGraph):
    data = Signale.sin(freq, 10, duration)
    plotGraph(Filter(
        freq, duration, a1, a2, b1, b2, data), qtGraph)


def plotGraph(graph, qtGraph: QtGraph):
    qtGraph.clear()
    qtGraph.plot(graph, pen=(0, 1), symbol=None, )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

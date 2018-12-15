# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\django\yueApp\yue\yueui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.latitudelabel = QtWidgets.QLabel(self.centralwidget)
        self.latitudelabel.setGeometry(QtCore.QRect(100, 100, 31, 16))
        self.latitudelabel.setObjectName("latitudelabel")
        self.longitudelabel = QtWidgets.QLabel(self.centralwidget)
        self.longitudelabel.setGeometry(QtCore.QRect(100, 60, 31, 16))
        self.longitudelabel.setObjectName("longitudelabel")
        self.longitudelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.longitudelineEdit.setGeometry(QtCore.QRect(148, 56, 133, 20))
        self.longitudelineEdit.setObjectName("longitudelineEdit")
        self.laditudelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.laditudelineEdit.setGeometry(QtCore.QRect(148, 100, 133, 20))
        self.laditudelineEdit.setObjectName("laditudelineEdit")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(90, 160, 51, 31))
        self.startButton.setObjectName("startButton")
        self.messagelabel = QtWidgets.QLabel(self.centralwidget)
        self.messagelabel.setGeometry(QtCore.QRect(160, 150, 181, 51))
        self.messagelabel.setText("")
        self.messagelabel.setObjectName("messagelabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.crawl)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.latitudelabel.setText(_translate("MainWindow", "纬度："))
        self.longitudelabel.setText(_translate("MainWindow", "经度："))
        self.startButton.setText(_translate("MainWindow", "开始"))

    def crawl(self):
        pass

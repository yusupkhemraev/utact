# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(523, 199)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 60, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 401, 31))
        self.lineEdit.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.lineEdit.setObjectName("lineEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setEnabled(True)
        self.timeEdit.setGeometry(QtCore.QRect(75, 150, 101, 31))
        self.timeEdit.setAcceptDrops(False)
        self.timeEdit.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setReadOnly(False)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setKeyboardTracking(True)
        self.timeEdit.setProperty("showGroupSeparator", False)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(185, 150, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 241, 31))
        self.label.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 251, 31))
        self.label_2.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(325, 150, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 180, 101, 20))
        self.label_3.setStyleSheet("color: rgb(171, 171, 171);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AppLaunches"))
        self.pushButton.setText(_translate("MainWindow", "Обзор"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "H:mm"))
        self.pushButton_3.setText(_translate("MainWindow", "Запуск"))
        self.label.setText(_translate("MainWindow", "Укажите время для запуска "))
        self.label_2.setText(_translate("MainWindow", "Укажите путь до программы"))
        self.pushButton_2.setText(_translate("MainWindow", "Другой путь"))
        self.label_3.setText(_translate("MainWindow", "by Khemraev Yusup"))
import icon_rc

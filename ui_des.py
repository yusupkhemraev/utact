# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desSVvaIu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(666, 245)
        MainWindow.setMinimumSize(QSize(561, 203))
        MainWindow.setMaximumSize(QSize(12121212, 12122121))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(666, 245))
        self.centralwidget.setMaximumSize(QSize(666, 245))
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"QCheckBox{\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	color: #fff;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(18)
        self.main_header.setFont(font)
        self.main_header.setStyleSheet(u"background-color: #3c3c3c;")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 0, 0)
        self.logo_name = QLabel(self.main_header)
        self.logo_name.setObjectName(u"logo_name")
        font1 = QFont()
        font1.setFamily(u"Fulbo Retro")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.logo_name.setFont(font1)
        self.logo_name.setStyleSheet(u"color: #fff;")
        self.logo_name.setIndent(-1)

        self.horizontalLayout.addWidget(self.logo_name, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.horizontalWidget = QWidget(self.main_header)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        font2 = QFont()
        font2.setPointSize(14)
        self.horizontalWidget.setFont(font2)
        self.horizontalWidget.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	font: 16pt \"dripicons-v2\";\n"
"	color: #fff;\n"
"	background-color: #3c3c3c;\n"
"}\n"
"\n"
"QPushButton#close_window_button:hover{\n"
"	background-color: rgb(232, 17, 25);\n"
"}\n"
"\n"
"QPushButton#close_window_button{\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton#restore_window_button{\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QPushButton#minimize_window_button{\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton#restore_window_button:hover{\n"
"	background-color: #636363;\n"
"}\n"
"\n"
"QPushButton#minimize_window_button:hover{\n"
"	background-color: #636363;\n"
"\n"
"}\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.horizontalWidget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        font3 = QFont()
        font3.setFamily(u"dripicons-v2")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.minimize_window_button.setFont(font3)
        self.minimize_window_button.setStyleSheet(u"")
        self.minimize_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.close_window_button = QPushButton(self.horizontalWidget)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMaximumSize(QSize(50, 50))
        self.close_window_button.setFont(font3)
        self.close_window_button.setStyleSheet(u"")
        self.close_window_button.setIconSize(QSize(24, 24))
        self.close_window_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.horizontalWidget, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.main_header)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setEnabled(True)
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.body.setFont(font4)
        self.body.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"	font: 87 16pt \"Fulbo Premier\";\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"	background-color: #57bee6;\n"
"}\n"
"\n"
"QPushButton#pushButton_2{\n"
"	background-color: #57bee6;\n"
"}\n"
"\n"
"QPushButton#pushButton_3{\n"
"	background-color: #57bee6;\n"
"}\n"
"\n"
"QPushButton#pushButton:disabled{\n"
"	color: rgb(172, 172, 172);\n"
"	background-color: rgb(63, 139, 167);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:disabled{\n"
"	color: rgb(172, 172, 172);\n"
"	background-color: rgb(63, 139, 167);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:disabled{\n"
"	color: rgb(172, 172, 172);\n"
"	background-color: rgb(63, 139, 167);\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"	background-color: #3b839d;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"	background-color: #3b839d;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"	background-color: #3b839d;\n"
"}\n"
"\n"
"QLineEdit#lineEdit{\n"
"	color:#fff;\n"
"	border: none;\n"
"	background-color: rgb(77, 77, 77);\n"
"}\n"
"\n"
"QTimeEdit#tim"
                        "eEdit{\n"
"	border: none;\n"
"	color: #fff; \n"
"	font: 63 24pt \"Montserrat SemiBold\";\n"
"}\n"
"\n"
"QCheckBox{\n"
"	\n"
"	font: 63 12pt \"Montserrat SemiBold\";\n"
"}\n"
"\n"
"QCheckBox:indicator {\n"
"	width: 161px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/icons/icons/checked.png);\n"
"}")
        self.timeEdit = QTimeEdit(self.body)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setEnabled(True)
        self.timeEdit.setGeometry(QRect(30, 140, 101, 41))
        font5 = QFont()
        font5.setFamily(u"Montserrat SemiBold")
        font5.setPointSize(24)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.timeEdit.setFont(font5)
        self.timeEdit.setAcceptDrops(False)
        self.timeEdit.setStyleSheet(u"")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setReadOnly(False)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setKeyboardTracking(True)
        self.timeEdit.setProperty("showGroupSeparator", False)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(False)
        self.pushButton_3 = QPushButton(self.body)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QRect(150, 140, 131, 41))
        font6 = QFont()
        font6.setFamily(u"Montserrat SemiBold")
        font6.setPointSize(11)
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"")
        self.label_3 = QLabel(self.body)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(548, 192, 111, 20))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color: rgb(50, 50, 50);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton = QPushButton(self.body)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 40, 101, 41))
        self.pushButton.setFont(font6)
        self.pushButton.setStyleSheet(u"")
        self.pushButton_2 = QPushButton(self.body)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(310, 140, 131, 41))
        font8 = QFont()
        font8.setFamily(u"Montserrat SemiBold")
        font8.setPointSize(11)
        font8.setBold(False)
        font8.setWeight(50)
        self.pushButton_2.setFont(font8)
        self.pushButton_2.setStyleSheet(u"")
        self.checkBox = QCheckBox(self.body)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(471, 153, 161, 20))
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setIconSize(QSize(24, 24))
        self.checkBox.setCheckable(True)
        self.checkBox.setAutoRepeatInterval(100)
        self.checkBox.setTristate(False)
        self.lineEdit = QLineEdit(self.body)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 40, 471, 41))
        self.lineEdit.setFont(font6)
        self.lineEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"uTact", None))
        self.logo_name.setText(QCoreApplication.translate("MainWindow", u"Utact", None))
#if QT_CONFIG(tooltip)
        self.minimize_window_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_window_button.setText(QCoreApplication.translate("MainWindow", u"\ue024", None))
#if QT_CONFIG(tooltip)
        self.close_window_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.close_window_button.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(tooltip)
        self.timeEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0440\u0435\u043c\u044f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0430\u043f\u0443\u0441\u043a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"by Khemraev Yusup", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u0434\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u043e\u0439 \u043f\u0443\u0442\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u043e\u0439 \u043f\u0443\u0442\u044c", None))
        self.checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0443\u0442\u044c \u0434\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0434\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
    # retranslateUi


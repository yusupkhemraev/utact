import sys
import os
import schedule
import time
from ui_des import *
from threading import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.ui.pushButton.clicked.connect(self.add_path)
        self.ui.pushButton_3.clicked.connect(self.run_app)
        self.ui.pushButton_2.clicked.connect(self.other_path)


        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        
        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.main_header.mouseMoveEvent = moveWindow


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
 

    def add_path(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Выберите программу', 'C:\\Program Files', ' *.exe')
        self.ui.lineEdit.setText(self.file_path[0])

    def run_app(self):
        self.get_time = str(self.ui.timeEdit.time().toString())
        self.app_path = self.ui.lineEdit.text()

        if self.app_path == '':
            self.msg('Ошибка! ❌', 'А путь кто укажет? 🤨')

        else:
            schedule.every().day.at(self.get_time).do(lambda: os.system('"' + self.app_path + '"'))
            self.msg('Успех 😁', 'Программа запустится в указанное времья! 😉')

            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.timeEdit.setEnabled(False)
            self.ui.lineEdit.setEnabled(False)

        if str(self.ui.checkBox.checkState()) == '2':
            schedule.every().day.at('07:00:00').do(lambda: os.system('netsh wlan disconnect'))

    def msg(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon(u':/icons/icons/icon.png'))
        msg.setText(message)
        msg.exec()

    def other_path(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.timeEdit.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)

    def sched(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


class SystemTrayIcon(QtWidgets.QSystemTrayIcon, MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, QtGui.QIcon(u':/icons/icons/icon.png'), parent)
        menu = QtWidgets.QMenu(parent)

        view_action = menu.addAction('Открыть')
        view_action.triggered.connect(window.show)

        exit_action = menu.addAction('Выход')
        exit_action.triggered.connect(app.quit)

        self.setContextMenu(menu)



if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        window = MainWindow()
        window.show()
        trayIcon = SystemTrayIcon(window)
        trayIcon.show()
        thr = Thread(target=window.sched, daemon=True)
        thr.start()
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)

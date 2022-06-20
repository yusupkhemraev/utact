import sys
import os
import schedule
import time
from ui_des import *
from threading import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # loadJsonStyle(self, self.ui)

        self.ui.pushButton.clicked.connect(self.add_path)
        self.ui.pushButton_3.clicked.connect(self.run_app)
        self.ui.pushButton_2.clicked.connect(self.other_path)


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
        msg.setWindowIcon(QtGui.QIcon('icons/icon.png'))
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
        QtWidgets.QSystemTrayIcon.__init__(self, QtGui.QIcon('icons/icon.png'), parent)
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

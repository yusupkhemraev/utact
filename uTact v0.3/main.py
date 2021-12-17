import sys
from win10toast import ToastNotifier
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
import icon_rc
from des import *
from threading import *
import schedule
import os
import time


app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/MainIcon/icon_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
MainWindow.setWindowIcon(icon)

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()

viewApp = QAction("Открыть")
viewApp.triggered.connect(MainWindow.show)
QtCore.QMetaObject.connectSlotsByName(MainWindow)
menu.addAction(viewApp)

quit = QAction("Выход")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)
tray.show()

try:
	def addPath():
		file_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Выберите программу', 'C:\Program Files', ' *.exe')
		ui.lineEdit.setText(file_path[0])

	ui.pushButton.clicked.connect(addPath)

	def runApp():
		getTime = str(ui.timeEdit.time().toString())
		appPath = ui.lineEdit.text()

		if appPath == '':
			msg = QtWidgets.QMessageBox()
			msg.setWindowTitle('uTact')
			msg.setWindowIcon(icon)
			msg.setText('А путь кто укажет ?')
			msg.setIcon(msg.Warning)
			msg.exec()
		else:
			schedule.every().day.at(getTime).do(lambda: os.system('"' + appPath + '"'))
			msg = QtWidgets.QMessageBox()
			msg.setWindowTitle('uTact')
			msg.setWindowIcon(icon)
			msg.setText('Программа запустится в указанное времья !')
			msg.setIcon(msg.Information)
			msg.exec()

			ui.pushButton.setEnabled(False)
			ui.pushButton_3.setEnabled(False)
			ui.timeEdit.setEnabled(False)
			ui.lineEdit.setEnabled(False)

		if str(ui.checkBox.checkState()) == '2':
			schedule.every().day.at('07:00:00').do(lambda: os.system('netsh wlan disconnect'))
		else:
			pass
			
	ui.pushButton_3.clicked.connect(runApp)

	def otherPath():
		ui.pushButton.setEnabled(True)
		ui.pushButton_3.setEnabled(True)
		ui.timeEdit.setEnabled(True)
		ui.lineEdit.setEnabled(True)

	ui.pushButton_2.clicked.connect(otherPath)

	

	def sched(num):
		while True:
		    schedule.run_pending()
		    time.sleep(num)

	thr = Thread(target = sched, daemon=True, args = (1,))
	thr.start()
except:
	msg = QtWidgets.QMessageBox()
	msg.setWindowTitle('Какая-то ошибка )')
	msg.setWindowIcon(icon)
	msg.setText('Найдены ошибки. Исправьте их.')
	msg.setIcon(msg.Warning)
	msg.exec()

sys.exit(app.exec())
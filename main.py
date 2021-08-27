#!/usr/bin/python3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from sys import argv
from time import sleep
from threadTest import Threadd
ui, _ = loadUiType('index.ui')


class Mainwindow(QMainWindow, ui, QThread):
    def __init__(self,  parent=None):
        super(Mainwindow, self).__init__(parent=None)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Scrap Pro ==FARES-EMAD==")
        self.setWindowIcon(QIcon("python.ico"))
        self.move(600, 200)
        self.setStyleSheet(open('style/datk.css').read())
        self.handel()

    def handel(self):
        self.pushButton_start.clicked.connect(lambda: self.startFunc())
        self.pushButton_clear.clicked.connect(lambda: self.clearFunc())
        self.pushButton_close.clicked.connect(lambda: self.closeFunc())

    def startFunc(self):
        self.get = Threadd()
        self.get.salary.connect(self.salary)
        self.get.name.connect(self.name)
        self.get.start()

    def salary(self, txt_salary):
        self.textEdit_salary.append(f'{txt_salary}')

    def name(self, txt_name):
        self.textEdit_name.append(f'{txt_name}')

    def clearFunc(self):
        self.textEdit_salary.clear()
        self.textEdit_name.clear()

    def closeFunc(self):
        self.destroy()


def main():
    app = QApplication(argv)
    window = Mainwindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

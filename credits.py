import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel)
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLabel, QPixmap, QGridLayout
from PyQt5.QtCore import Qt


class Credwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QWidget{background-color: rgb(64, 64, 64)}")

        layout = QGridLayout()

        myFont = QtGui.QFont("Comic Sans MS", 40)
        myFont.setBold(True)

        myFont2 = QtGui.QFont("Comic Sans MS", 28)

        myFont3 = QtGui.QFont("Comic Sans MS", 14)

        myFont4 = QtGui.QFont("Comic Sans MS", 14)

        lablist = []

        lab1 = QLabel("Poisson 1.0", self)
        lab1.setFont(myFont)
        lab1.move(240, 90)
        lablist.append(lab1)

        lab2 = QLabel("Wisa Förbom", self)
        lab2.setFont(myFont2)
        lab2.move(210, 150)
        lablist.append(lab2)

        lab3 = QLabel("© 2019", self)
        lab3.setFont(myFont3)
        lab3.move(280, 200)
        lablist.append(lab3)

        lab4 = QLabel("Aalto-university\nSchool Of Electrical\nEngineering (ELEC).", self)
        lab4.setFont(myFont4)
        lablist.append(lab4)

        lab4.move(180, 232)

        pic = QLabel()
        ink = QLabel()
        inkubio = QPixmap("images/inkubio-logo.png")
        pixmap = QPixmap("images/aalto.png").scaled(60, 35, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pic.setPixmap(pixmap)
        ink.setPixmap(inkubio)
        ink.move(400, 200)
        pic.move(250, 200)
        lablist.append(pic)
        lablist.append(ink)

        constn = 1
        for i in lablist:
            i.setStyleSheet("QLabel{color: rgb(255, 255, 255)}")
            layout.addWidget(i, constn, 1)
            constn += 1

        self.setLayout(layout)

        self.setGeometry(580, 270, 200, 200)
        self.setFixedSize(300, 390)
        self.setWindowTitle('About')
        self.setWindowIcon(QIcon("images/info.png"))
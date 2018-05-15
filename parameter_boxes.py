from PyQt5 import QtCore, QtGui, QtWidgets
from graph_window import *
import sys



class NormalSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.labelFont = QtGui.QFont(None, 14)
        self.initSettings()


    def initSettings(self):

        vbox = QVBoxLayout()

        hbox1 = QtWidgets.QHBoxLayout()
        EX = QtWidgets.QLabel("Expected value:")
        EX.setFont(self.labelFont)
        EX.setStyleSheet("color: rgb(255, 255, 255)")
        EXBox = QtWidgets.QLineEdit()
        hbox1.addWidget(EX)
        hbox1.addWidget(EXBox)
        vbox.addLayout(hbox1)

        hbox2 = QtWidgets.QHBoxLayout()
        SD = QtWidgets.QLabel("Standard deviation:")
        SD.setFont(self.labelFont)
        SD.setStyleSheet("color: rgb(255, 255, 255)")
        SDBox = QtWidgets.QLineEdit()
        hbox2.addWidget(SD)
        hbox2.addWidget(SDBox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)



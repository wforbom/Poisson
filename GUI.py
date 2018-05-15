from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from option_window import *
from graph_window import *
from credits import *
import sys



class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):

        hbox = QHBoxLayout()


        menuBar = self.menuBar()



        self.toolBar = self.addToolBar("Exit")
        distAct = QAction(QIcon("images/DIST.png"), "Probability distribution mode", self)
        settAct = QAction(QIcon("images/VENN.png"), "Set theory mode", self)
        pascalAct = QAction(QIcon("images/PASCAL.png"), "Pascal's triangle", self)
        combAct = QAction(QIcon("images/COMB.png"), "Combinatorics mode", self)
        infoAct = QAction(QIcon("images/info.png"), "Info and credits", self)
        self.toolBar.addAction(distAct)
        self.toolBar.addAction(settAct)
        self.toolBar.addAction(pascalAct)
        self.toolBar.addAction(combAct)
        self.toolBar.addAction(infoAct)
        infoAct.triggered.connect(self.infoButtPush)
        self.credits = Credwindow()



        HSplit = QSplitter(Qt.Horizontal)

        optionWindow = OptionWindow()
        graphWindow = GraphWindow()
        self.setCentralWidget(QWidget())

        HSplit.addWidget(optionWindow)
        HSplit.addWidget(graphWindow)
        HSplit.setSizes([1, 1000])


        hbox.addWidget(HSplit)
        self.centralWidget().setLayout(hbox)

        self.setGeometry(80, 45, 1280, 720)
        self.setWindowTitle("POISSON alpha 1.0")
        self.show()


    def infoButtPush(self):
        self.credits.show()
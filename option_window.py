from PyQt5 import QtCore, QtGui, QtWidgets
from graph_window import *
from parameter_boxes import *
import sys


class OptionWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.labelFont = QtGui.QFont(None, 14)
        self.dist = None
        self.Ddists = {"Binomial":1, "Geometric":2, "Hypergeometric":3, "Poisson":4, "Zipf":5}
        self.Cdists = ["Normal", "Cauchy", "Exponential", "Χ²", "Laplace", "Student t", "Weibull", "Linear"]

        self.parameterBox = None

        self.initWidget()


    def initWidget(self):
        self.setStyleSheet("QGraphicsView {color: rgb(64, 64, 64)}")

        vbox = QtWidgets.QVBoxLayout()

        ##0 TITLE##
        titlefont = QtGui.QFont(None, 20, QtGui.QFont.Bold)
        title = QtWidgets.QLabel("PROBABILITY DISTRIBUTIONS")
        title.setStyleSheet("color: rgb(255, 255, 255);")
        title.setFont(titlefont)
        title
        vbox.addWidget(title)
        ###   ###

        ##1 DISTRIBUTION OPTIONS##
        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addStretch(1)
        distList = self.addOptions()
        hbox1.addWidget(distList[0])
        hbox1.addWidget(distList[1])
        vbox.addLayout(hbox1)
        ###         ###

        ##2 PDF/CDF##
        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addStretch(1)
        self.addModes()
        vbox.addLayout(hbox2)
        vbox.addWidget(self.checkBox)

        vbox.addStretch(1)


        self.setLayout(vbox)


    def addOptions(self):

        self.optionBoxD = QtWidgets.QComboBox(self)
        self.optionBoxD.addItem("DISCRETE:")
        self.optionBoxD.addItem("Binomial")
        self.optionBoxD.addItem("Geometric")
        self.optionBoxD.addItem("Hypergeometric")
        self.optionBoxD.addItem("Poisson")
        self.optionBoxD.addItem("Zipf")
        self.optionBoxD.setFixedWidth(150)

        self.optionBoxC = QtWidgets.QComboBox(self)
        self.optionBoxC.addItem("CONTINUOUS:")
        self.optionBoxC.addItem("Normal")
        self.optionBoxC.addItem("Exponential")
        self.optionBoxC.addItem("Linear")
        self.optionBoxC.addItem("Χ²")
        self.optionBoxC.addItem("Student t")
        self.optionBoxC.addItem("Weibull")
        self.optionBoxC.addItem("Cauchy")
        self.optionBoxC.addItem("Laplace")
        self.optionBoxC.setFixedWidth(150)

        self.optionBoxD.currentIndexChanged.connect(self.setDistribution)
        self.optionBoxC.currentIndexChanged.connect(self.setDistribution)


        distList = [self.optionBoxC, self.optionBoxD]
        return distList


    def addModes(self):

        self.checkBox = QtWidgets.QCheckBox("CDF", self)
        self.checkBox.setStyleSheet("QCheckBox { color: white }")



    #def addBounders(self):



    def setDistribution(self):
        Ctext = self.optionBoxC.currentText()
        Dtext = self.optionBoxD.currentText()

        #if Dtext in self.Ddists:
        #    print(self.optionBoxD.currentText())
        #else:
        #    print("Mode reset")
        #    self.clearParameters()

        if Ctext in self.Cdists:
            print(self.optionBoxC.currentText())
            GraphWindow().plotDistribution(Ctext)
            self.setParameters(Ctext)
        else:
            print("Mode reset")
            self.clearParameters()



    def setParameters(self, type):

        if type == "Normal":
            self.parameterBox = self.layout().addWidget(NormalSettings())


    def clearParameters(self):
        print(self.layout().itemAt(0))
        print(self.layout().itemAt(1))
        print(self.layout().itemAt(2))
        print(self.layout().itemAt(3))
        print(self.layout().itemAt(4))
        print(self.layout().itemAt(5))

       # dw = self.layout().takeAt(1)
        #self.layout().removeItem(dw)


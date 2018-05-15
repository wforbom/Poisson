from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import matplotlib.mlab as mlab
import numpy as np
import math

import matplotlib.pyplot as plt
import sys



class GraphWindow(QWidget):
    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.nav = NavigationToolbar(self.canvas, self)
        self.initView()


    def initView(self):
        layout = QVBoxLayout()
        self.figure.set_facecolor("gray")
        layout.addWidget(self.nav)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


    def plotDistribution(self, type):

        if type == "Normal":
            mu = 0
            var = 1
            sd = math.sqrt(var)
            X = np.linspace(mu - 4, mu + 4)
            Y = mlab.normpdf(X, mu, sd)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.grid(color="gray", linestyle="-", linewidth=3)
        ax.plot(X, Y, "*-")
        self.canvas.draw()


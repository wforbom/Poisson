from GUI import GUI
from PyQt5.QtWidgets import QApplication
import sys


def main():

    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow{background-color: rgb(64, 64, 64)}")

    mainWindow = GUI()
    mainWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

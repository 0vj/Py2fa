import sys # needed for `argv` tranfer to `QApplication`
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from py2fa import Ui_MainWindow

class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # This is needed here for variable and method access
        super().__init__()
        self.setupUi(self)  # Initialize a design
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

def main():
    app = QtWidgets.QApplication(sys.argv)  # New instance of `QApplication`
    window = ExampleApp()  # Create an object of class ExampleApp
    window.show()  # Show a window
    app.exec_()  # Run the app

if __name__ == '__main__':
    main()

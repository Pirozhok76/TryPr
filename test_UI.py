from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class myWidget(QMainWindow):

    def __init__(self):
        super(myWidget, self).__init__()
        uic.loadUi('test.ui', self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWidget()
    sys.exit(app.exec_())

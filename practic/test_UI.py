from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
import practic


class myWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        appearance = self.palette()
        appearance.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor("light blue"))
        self.setPalette(appearance)
        self.setAutoFillBackground(True)

        uic.loadUi('test.ui', self)
        self.show()

    #def calc_delta(self):
     #   practic.de

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWidget()
    sys.exit(app.exec_())

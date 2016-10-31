import sys


from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)

from PyQt5.QtGui import QIcon

from PyQt5.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('Calibri', 10)) #установка шрифта

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton ('Вычиислить', self)
        btn.setToolTip('Выполнить вычисление')
        btn.resize(btn.sizeHint())
        btn.move(120, 150)

        self.setGeometry(300, 300, 300, 220) # x-y-w-h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icon.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    #создание объекта приложения

    mw = MainWindow()


    sys.exit(app.exec_())

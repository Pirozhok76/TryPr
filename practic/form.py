import sys

from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)
    #создание объекта приложения

    mw = QWidget()
    # mw = main window

    mw.resize(800, 600)
    mw.move(550, 300)

    mw.setWindowTitle('main')
    mw.show()

    sys.exit(app.exec_())

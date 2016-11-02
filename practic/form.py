import sys


from PyQt5.QtWidgets import (QMessageBox, QToolTip, QPushButton, QApplication,
                             QDesktopWidget, QMainWindow, qApp, QAction)

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('Calibri', 10)) #установка шрифта

        btn = QPushButton('Вычислить', self)
        btn.setStatusTip('Вычислить')
        btn.resize(btn.sizeHint())
        btn.move(120, 150)

        exitAction = QAction(QIcon('exit.png'), '&Выход', self) #добавление пункта меню- Выход
        exitAction.setShortcut('Ctrl+Q') #горячие клавиши
        exitAction.setStatusTip('Выход из приложения') #подсказка на статус-баре
        exitAction.triggered.connect(qApp.quit) #сигнал на закрытие


        '''quit_btn = QPushButton( 'Выход', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit) #вызов сигнала "нажатие"
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(50, 150)
        #кнопка выход'''

        self.statusBar() #статусбар

        menubar = self.menuBar() #создание меню
        filemenu = menubar.addMenu('&Файл') #создание пункта меню "ФАйл"
        filemenu.addAction(exitAction) #добавление пункта "выход"

        self.setGeometry(300, 300, 300, 220) # x-y-w-h
        self.setWindowTitle('MainWindow')
        self.setWindowIcon(QIcon('icon.png'))

        self.show()

    def closeEvent(self, event): # генерация события при закрытии
        reply = QMessageBox.question(self, 'Внимание!',
                                     'Вы уверены что хотите закрыть программу?', QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No) #показ окна с сообщением
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self): #центрирование окна
        qr = self.frameGeometry() #получ-е прямоугольника,опред-го геометрию гл. окна(включает любые рамки)
        cp = QDesktopWidget().availableGeometry().center() #получ-е разрешения экрана монитора.получ-е центр.точки
        qr.moveCenter(cp) #центр прямоуг-ка в центр экрана
        self.move(qr.topLeft()) #гл.окно в верхний левый угол прямоуг-ка



if __name__ == '__main__':

    app = QApplication(sys.argv)
    #создание объекта приложения

    mw = MainWindow()


    sys.exit(app.exec_())

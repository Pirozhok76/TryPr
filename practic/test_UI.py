from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QAction, qApp
from PyQt5.QtGui import QIcon
import sys
from practice import *


class myWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        appearance = self.palette()
        appearance.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor("white"))
        self.setPalette(appearance)
        self.setAutoFillBackground(True)



        self.wnd = uic.loadUi('test2.ui', self)

        exitAction = QAction(QIcon('exit.png'), '&Выход', self)  # добавление пункта меню- Выход
        exitAction.setShortcut('Ctrl+Q')  # горячие клавиши
        exitAction.setStatusTip('Выход из приложения')  # подсказка на статус-баре
        exitAction.triggered.connect(qApp.quit)  # сигнал на закрытие

        self.saveAction = QAction('Сохранить результат в файл')

        menubar = self.menuBar()  # создание меню
        filemenu = menubar.addMenu('&Файл')  # создание пункта меню "ФАйл"
        filemenu.addAction(self.saveAction)
        filemenu.addAction(exitAction)  # добавление пункта "выход"

        # self.wnd.lbl_1.setText(u"\u03C0" + 'kc')
        self.wnd.btn1.clicked.connect(self.run)
        self.wnd.dblSpinBox_13.valueChanged.connect(self._onSpinBox_13ValueChanged)  # для r_vnutr and r_vnesh

        def center(self):  # центрирование окна
            qr = self.frameGeometry()  # получ-е прямоугольника,опред-го геометрию гл. окна(включает любые рамки)
            cp = QDesktopWidget().availableGeometry().center()  # получ-е разрешения экрана монитора.получ-е центр.точки
            qr.moveCenter(cp)  # центр прямоуг-ка в центр экрана
            self.move(qr.topLeft())  # гл.окно в верхний левый угол прямоуг-ка

        self.show()

    def _onSpinBox_13ValueChanged(self):
        self.wnd.dblSpinBox_9.setValue(self.wnd.dblSpinBox_13.value())
        self.wnd.dblSpinBox_16.setValue(self.wnd.dblSpinBox_13.value())

    def run(self):

        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        # https: // pythonworld.ru / gui / pyqt5 - dialogs.html

        piks_d = self.wnd.dblSpinBox.value()
        pi0_d = self.wnd.dblSpinBox_2.value()
        theta2_d = self.wnd.dblSpinBox_7.value()
        # rm_d = self.wnd.dblSpinBox_14.value()
        r_vnutr_d = self.wnd.dblSpinBox_17.value()
        r_vnesh_d = self.wnd.dblSpinBox_11.value()
        r2_d = self.wnd.dblSpinBox_19.value()

        if self.wnd.radioButton.isChecked():
            eps = Eps[0]
        elif self.wnd.radioButton_2.isChecked():
            eps = Eps[1]
        elif self.wnd.radioButton_3.isChecked():
            eps = Eps[2]
        elif self.wnd.radioButton_4.isChecked():
            eps = Eps[3]
        elif self.wnd.radioButton_5.isChecked():
            eps = Eps[4]

        pi0_min = self.wnd.dblSpinBox_5.value()
        pi0_max = self.wnd.dblSpinBox_6.value()

        piks_min = self.wnd.dblSpinBox_3.value()
        piks_max = self.wnd.dblSpinBox_4.value()

        theta2_min = self.wnd.spinBox.value()
        theta2_max = self.wnd.spinBox_2.value()

        # rm_min = self.wnd.dblSpinBox_12.value()
        # rm_max = self.wnd.dblSpinBox_18.value()
        # print('piks_d: ' + str(piks_d))

        r_vnesh_min = self.wnd.dblSpinBox_9.value()
        r_vnesh_max = self.wnd.dblSpinBox_10.value()

        r_vnutr_min = self.wnd.dblSpinBox_15.value()
        r_vnutr_max = self.wnd.dblSpinBox_16.value()

        r2_min = self.wnd.dblSpinBox_13.value()
        r2_max = self.wnd.dblSpinBox_20.value()

        # self.wnd.dblSpinBox_16.value() = self.wnd.dblSpinBox_13.value() для r_vnutr

        # self.wnd.dblSpinBox_9.value() = self.wnd.dblSpinBox_13.value() для r_vnesh

        theta2 = theta2_min
        pi0 = pi0_min
        piks = piks_min
        # rm = rm_min
        r_vnesh = r_vnesh_min
        r_vnutr = r_vnutr_min
        r2 = r2_min

        while piks <= piks_max:
            self.res_1 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
            piks += piks_d
            print('результат:')
            print(self.res_1)

        while pi0 <= pi0_max:
            self.res_2 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
            pi0 += pi0_d
        # print('res_2 = ', res_2)

        while theta2 <= theta2_max:
            self.res_3 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
            theta2 += theta2_d

        # while rm <= rm_max:
        #     res_4 = main_calc(piks, pi0, theta2, rm, r_vnesh,r_vnutr,r2)
        #     rm += rm_d

        while r_vnesh <= r_vnesh_max:
            self.res_5 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
            r_vnesh += r_vnesh_d

        while r_vnutr <= r_vnutr_max:
            self.res_6 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
            r_vnutr += r_vnutr_d

        while r2 <= r2_max:
            self.res_7 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
            r2 += r2_d

            #self.wnd.textEdit.setText(str(self.res_7[0] ) + ('  ') + str(self.res_7[1]))
            #self.wnd.listWidget.text(str(self.res_7[0]))
        #self.wnd.textEdit_2.setValue(self.res_7[1])

    # def calc_delta(self):
    # practic.de


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWidget()
    sys.exit(app.exec_())

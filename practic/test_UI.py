from PyQt5 import QtCore, QtGui, uic

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, \
    QDesktopWidget, QAction, qApp, QFileDialog

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

        self.saveAction = self.wnd.action

        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Сохранить результаты в файл')
        self.saveAction.triggered.connect(self.showDialog)


        self.exitAction = self.wnd.action_2
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Выход из приложения')  # подсказка на статус-баре

        self.exitAction.triggered.connect(qApp.quit)


        self.wnd.btn1.clicked.connect(self.run)
        # self.wnd.btn1.clicked.connect(self.chEnAction())
        self.wnd.dblSpinBox_13.valueChanged.connect(self._onSpinBox_13ValueChanged)  # для r_vnutr and r_vnesh


        qr = self.frameGeometry()  # получ-е прямоугольника,опред-го геометрию гл. окна(включает любые рамки)
        cp = QDesktopWidget().availableGeometry().center()  # получ-е разрешения экрана монитора.получ-е центр.точки
        qr.moveCenter(cp)  # центр прямоуг-ка в центр экрана
        self.move(qr.topLeft())  # гл.окно в верхний левый угол прямоуг-ка

        self.show()

    def _onSpinBox_13ValueChanged(self):
        self.wnd.dblSpinBox_9.setValue(self.wnd.dblSpinBox_13.value())
        self.wnd.dblSpinBox_16.setValue(self.wnd.dblSpinBox_13.value())

    def showDialog(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранить файл', '/results.txt')[0]
        f = open(fname, 'w')
        f.write(self.wnd.textEdit.toPlainText() + self.wnd.textEdit_2.toPlainText())
        f.close()


    #
    # with f:
    #     data = f.save()
    #     self.res_1()


    def run(self):

        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        # https: // pythonworld.ru / gui / pyqt5 - dialogs.html

        # self.wnd.dblSpinBox_16.value() = self.wnd.dblSpinBox_13.value() для r_vnutr

        # self.wnd.dblSpinBox_9.value() = self.wnd.dblSpinBox_13.value() для r_vnesh

        r_vnesh_min = self.wnd.dblSpinBox_9.value()
        r_vnesh_max = self.wnd.dblSpinBox_10.value()
        r_vnutr_min = self.wnd.dblSpinBox_15.value()
        r_vnutr_max = self.wnd.dblSpinBox_16.value()

        r_vnutr_d = self.wnd.dblSpinBox_17.value()
        r_vnesh_d = self.wnd.dblSpinBox_11.value()

        # дисэйблить контролы

        r_vnesh = r_vnesh_min
        while r_vnesh <= r_vnesh_max:
            self.calc_part(self.wnd.textEdit, None, r_vnesh)
            r_vnesh += r_vnesh_d

        r_vnutr = r_vnutr_min
        while r_vnutr <= r_vnutr_max:
            self.calc_part(self.wnd.textEdit_2, r_vnutr, None)
            r_vnutr += r_vnutr_d

            # self.wnd.textEdit.setText(str(self.res_7[0] ) + ('  ') + str(self.res_7[1]))
            # self.wnd.listWidget.text(str(self.res_7[0]))
            # self.wnd.textEdit_2.setValue(self.res_7[1])


            # энэйблить контролы

    # def calc_delta(self):
    # practic.de

    def calc_part(self, textEdit, r_vnutr, r_vnesh):
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



        r2_min = self.wnd.dblSpinBox_13.value()
        r2_max = self.wnd.dblSpinBox_20.value()

        piks_d = self.wnd.dblSpinBox.value()
        pi0_d = self.wnd.dblSpinBox_2.value()
        theta2_d = self.wnd.dblSpinBox_7.value()
        # rm_d = self.wnd.dblSpinBox_14.value()
        r2_d = self.wnd.dblSpinBox_19.value()

        r2 = r2_min
        while r2 <= r2_max:
            # self.res_7 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)

            piks = piks_min
            while piks <= piks_max:
                # self.res_1 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
                # print('результат при piks = :' + str(piks))
                # print(self.res_1)

                # self.wnd.textEdit.append()

                # print('res_2 = ', res_2)

                theta2 = theta2_min
                while theta2 <= theta2_max:
                    # self.res_3 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)

                    # while rm <= rm_max:
                    #     res_4 = main_calc(piks, pi0, theta2, rm, r_vnesh,r_vnutr,r2)
                    #     rm += rm_d

                    pi0 = pi0_min
                    while pi0 <= pi0_max:
                        res = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps)
                        r2_str = round(r2, 1)
                        piks_str = round(piks, 4)
                        theta2_str = round(theta2, 2)
                        pi0_str = round(pi0, 2)
                        if r_vnesh:
                            r_vnesh_str = round(r_vnesh, 3)
                            s = 'результат при: r2 = {}; piks = {}; theta2 = {}; pi0 = {}; r_vnesh = {}'.format(r2_str,
                                                                                                                piks_str,
                                                                                                                theta2_str,
                                                                                                                pi0_str,
                                                                                                                r_vnesh_str)
                        else:
                            r_vnutr_str = round(r_vnutr, 3)
                            s = 'результат при: r2 = {}; piks = {}; theta2 = {}; pi0 = {}; r_vnutr = {}'.format(r2_str,
                                                                                                                piks_str,
                                                                                                                theta2_str,
                                                                                                                pi0_str,
                                                                                                                r_vnutr_str)
                        textEdit.append(s)
                        textEdit.append(str(res))
                        pi0 += pi0_d

                    theta2 += theta2_d

                piks += piks_d

            r2 += r2_d


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWidget()
    sys.exit(app.exec_())

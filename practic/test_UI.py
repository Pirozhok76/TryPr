from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
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



        self.wnd = uic.loadUi('test1.ui', self)
        # self.wnd.lbl_1.setText(u"\u03C0" + 'kc')
        self.wnd.btn1.clicked.connect(self.run)
        self.show()

    def run(self):

        piks_d = self.wnd.dblSpinBox.value()
        pi0_d = self.wnd.dblSpinBox_2.value()
        theta2_d = self.wnd.dblSpinBox_7.value()
        # rm_d = self.wnd.dblSpinBox_14.value()
        r_vnutr_d = self.wnd.dblSpinBox_17.value()
        r_vnesh_d = self.wnd.dblSpinBox_11.value()
        r2_d = self.wnd.dblSpinBox_19.value()


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

        theta2 = theta2_min
        pi0 = pi0_min
        piks = piks_min
        # rm = rm_min
        r_vnesh = r_vnesh_min
        r_vnutr = r_vnutr_min
        r2 = r2_min

        while piks <= piks_max:
            res_1 = main_calc(piks, pi0, theta2, r_vnesh,r_vnutr,r2)
            piks += piks_d
            # print('результат:')
            # print(res)

        while pi0 <= pi0_max:
            res_2 = main_calc(piks, pi0, theta2,r_vnesh,r_vnutr,r2)
            pi0 += pi0_d
            # print('res_2 = ', res_2)

        while theta2 <= theta2_max:
            res_3 = main_calc(piks, pi0, theta2, r_vnesh,r_vnutr,r2)
            theta2 += theta2_d

        # while rm <= rm_max:
        #     res_4 = main_calc(piks, pi0, theta2, rm, r_vnesh,r_vnutr,r2)
        #     rm += rm_d

        while r_vnesh <= r_vnesh_max:
            res_5 = main_calc(piks, pi0, theta2, r_vnesh,r_vnutr,r2)
            r_vnesh += r_vnesh_d

        while r_vnutr <= r_vnutr_max:
            res_6 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2)
            r_vnutr += r_vnutr_d

        while r2 <= r2_max:
            res_7 = main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2)
            r2 += r2_d


                #def calc_delta(self):
     #   practic.de

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWidget()
    sys.exit(app.exec_())

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from game_menu import Ui_MainWindow

from nim import Ui_nim
from manual.settings_image_manual import Ui_Form


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def open():
    global nim
    nim = QtWidgets.QWidget()
    ui = Ui_nim()
    ui.setupUi(nim)
    nim.show()
    # MainWindow.close()
    MainWindow.hide()

    def instr():
        global st_im_mn
        st_im_mn = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(st_im_mn)
        st_im_mn.show()
        nim.hide()


    ui.bt_instruction.clicked.connect(instr)


ui.pushButton.clicked.connect(open)

sys.exit(app.exec_())

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from game_menu_1 import Ui_Game_Menu

from nim import Ui_nim
from manual.settings_image_manual import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Game_Menu = QtWidgets.QMainWindow()
ui = Ui_Game_Menu()
ui.setupUi(Game_Menu)
Game_Menu.show()


def game():
    global nim
    nim = QtWidgets.QWidget()
    ui = Ui_nim()
    ui.setupUi(nim)
    nim.show()
    # MainWindow.close()
    Game_Menu.hide()

    def instruction():
        global st_im_mn
        st_im_mn = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(st_im_mn)
        st_im_mn.show()
        nim.hide()

        def return_game():
            global nim
            nim.show()
            st_im_mn.hide()

        ui.bt_exit.clicked.connect(lambda: return_game())

    def return_menu():
        nim.hide()
        Game_Menu.show()

    ui.bt_instruction.clicked.connect(lambda: instruction())
    ui.bt_exit.clicked.connect(lambda: return_menu())


ui.pushButton.clicked.connect(lambda: game())
# ui.pushButton

sys.exit(app.exec_())

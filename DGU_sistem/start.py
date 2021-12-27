import sys
from PyQt5 import QtWidgets
from document_generation import Ui_Form
from DGU_sistems import Ui_DGU_sistem

app = QtWidgets.QApplication(sys.argv)
DGU_sistem = QtWidgets.QWidget()
ui = Ui_DGU_sistem()
ui.setupUi(DGU_sistem)
DGU_sistem.show()
def perform_bt_creat():
    global Form
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    DGU_sistem.hide()
    Form.show()

    def return_table():
        global DGU_sistem
        DGU_sistem.show()
        Form.hide()


    ui.exit.clicked.connect(lambda: return_table())



ui.bt_creat.clicked.connect(lambda: perform_bt_creat())
sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'course.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(70, 90)
        self.one = QtWidgets.QRadioButton(Form)
        self.one.setGeometry(QtCore.QRect(5, 5, 97, 21))
        self.one.setObjectName("one")
        self.two = QtWidgets.QRadioButton(Form)
        self.two.setGeometry(QtCore.QRect(5, 25, 97, 21))
        self.two.setObjectName("two")
        self.three = QtWidgets.QRadioButton(Form)
        self.three.setGeometry(QtCore.QRect(5, 45, 97, 21))
        self.three.setObjectName("three")
        self.four = QtWidgets.QRadioButton(Form)
        self.four.setGeometry(QtCore.QRect(5, 65, 97, 21))
        self.four.setObjectName("four")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.one.setText(_translate("Form", "4 курс"))
        self.two.setText(_translate("Form", "3 курс"))
        self.three.setText(_translate("Form", "2 курс"))
        self.four.setText(_translate("Form", "1 курс"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
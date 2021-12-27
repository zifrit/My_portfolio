# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DGU_sistems.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_DGU_sistem(object):
    def setupUi(self, DGU_sistem):
        DGU_sistem.setObjectName("DGU_sistem")
        DGU_sistem.resize(600, 480)
        self.kurs = QtWidgets.QLabel(DGU_sistem)
        self.kurs.setGeometry(QtCore.QRect(50, 100, 60, 16))
        self.kurs.setObjectName("kurs")
        self.profil = QtWidgets.QLabel(DGU_sistem)
        self.profil.setGeometry(QtCore.QRect(50, 170, 71, 16))
        self.profil.setObjectName("profil")
        self.dd_orders = QtWidgets.QLabel(DGU_sistem)
        self.dd_orders.setGeometry(QtCore.QRect(50, 310, 181, 16))
        self.dd_orders.setObjectName("dd_orders")
        self.name = QtWidgets.QLabel(DGU_sistem)
        self.name.setGeometry(QtCore.QRect(50, 30, 60, 16))
        self.name.setObjectName("name")
        self.type_social = QtWidgets.QLabel(DGU_sistem)
        self.type_social.setGeometry(QtCore.QRect(50, 240, 201, 16))
        self.type_social.setObjectName("type_social")
        self.input_kurs = QtWidgets.QLineEdit(DGU_sistem)
        self.input_kurs.setGeometry(QtCore.QRect(50, 120, 500, 22))
        self.input_kurs.setObjectName("input_kurs")
        self.input_profil = QtWidgets.QLineEdit(DGU_sistem)
        self.input_profil.setGeometry(QtCore.QRect(50, 190, 500, 22))
        self.input_profil.setText("")
        self.input_profil.setObjectName("input_profil")
        self.input_type_social = QtWidgets.QLineEdit(DGU_sistem)
        self.input_type_social.setGeometry(QtCore.QRect(50, 260, 500, 22))
        self.input_type_social.setObjectName("input_type_social")
        self.input_dd_orders = QtWidgets.QLineEdit(DGU_sistem)
        self.input_dd_orders.setGeometry(QtCore.QRect(50, 330, 500, 22))
        self.input_dd_orders.setObjectName("input_dd_orders")
        self.input_name = QtWidgets.QLineEdit(DGU_sistem)
        self.input_name.setGeometry(QtCore.QRect(50, 50, 500, 22))
        self.input_name.setObjectName("input_name")
        self.bt_search = QtWidgets.QPushButton(DGU_sistem)
        self.bt_search.setGeometry(QtCore.QRect(50, 400, 80, 26))
        self.bt_search.setObjectName("bt_serch")
        self.bt_add = QtWidgets.QPushButton(DGU_sistem)
        self.bt_add.setGeometry(QtCore.QRect(180, 400, 90, 26))
        self.bt_add.setObjectName("bt_add")
        self.bt_clear = QtWidgets.QPushButton(DGU_sistem)
        self.bt_clear.setGeometry(QtCore.QRect(300, 400, 90, 26))
        self.bt_clear.setObjectName("bt_clear")
        self.bt_creat = QtWidgets.QPushButton(DGU_sistem)
        self.bt_creat.setGeometry(QtCore.QRect(408, 400, 150, 26))
        self.bt_creat.setObjectName("bt_creat")

        self.retranslateUi(DGU_sistem)
        QtCore.QMetaObject.connectSlotsByName(DGU_sistem)

        #     команды
        self.add_to_base()
        self.search_in_base()
        self.clear_menu()
        # self.creat_table()

    def retranslateUi(self, DGU_sistem):
        _translate = QtCore.QCoreApplication.translate
        DGU_sistem.setWindowTitle(_translate("DGU_sistem", "Form"))
        self.kurs.setText(_translate("DGU_sistem", "Курс"))
        self.profil.setText(_translate("DGU_sistem", "Профиль"))
        self.dd_orders.setText(_translate("DGU_sistem", "Дата назначанеия и срок"))
        self.name.setText(_translate("DGU_sistem", "ФИО"))
        self.type_social.setText(_translate("DGU_sistem", "Вид социальной стипендии"))
        self.bt_search.setText(_translate("DGU_sistem", "Поиск"))
        self.bt_add.setText(_translate("DGU_sistem", "Добавить"))
        self.bt_clear.setText(_translate("DGU_sistem", "Очистить"))
        self.bt_creat.setText(_translate("DGU_sistem", "Создать таблицу"))

    def add_to_base(self):
        self.bt_add.clicked.connect(lambda: self.perform_add_to_base())

    def search_in_base(self):
        self.bt_search.clicked.connect(lambda: self.perform_bt_search())

    def clear_menu(self):
        self.bt_clear.clicked.connect(lambda: self.perform_bt_clear())

    # def creat_table(self):
    #     self.bt_creat.clicked.connect(lambda: self.perform_bt_creat())

    # def perform_bt_creat(self):
    #     pass
        # код по генирации данных в блокноте
        # with sqlite3.connect('db/database.db') as db:
        #     cursor = db.cursor()
        #     cursor.execute((" Select * from DGU_sistem "))
        #     with open('Таблица со степендиантыми.txt', 'w', encoding='utf-8') as file:
        #         file.write(
        #             '|ФИО' + ' ' * 37 + '|Курс ' + '|Профиль   ' + '|Вид стипендии' + ' ' * 17 + '|Дата стипендии\n')
        #     for i in cursor:
        #         len_nema = i[0] + (' ' * (40 - len(i[0])))
        #         len_kurs = str(i[1]) + ('    ')
        #         len_profil = i[2] + (' ' * (10 - len(i[2])))
        #         len_type_social = i[3] + (' ' * (30 - len(i[3])))
        #         with open('Таблица со степендиантыми.txt', 'a', encoding='utf-8') as file:
        #             file.write('+' + '-' * 128 + '+\n')
        #             file.write(f'|{len_nema}|{len_kurs}|{len_profil}|{len_type_social}|{i[4]}\n')
        #             file.write('+' + '-' * 128 + '+\n')
        #     db.commit()

    def perform_bt_search(self):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            cursor.execute((" Select * from DGU_sistem "))
            FIO = self.input_name.text()
            for i in cursor:
                if FIO == i[0]:
                    self.input_kurs.setText(str(i[1]))
                    self.input_profil.setText(i[2])
                    self.input_type_social.setText(i[3])
                    self.input_dd_orders.setText(i[4])
                    break
            db.commit()

    def perform_bt_clear(self):
        self.input_name.setText('')
        self.input_kurs.setText('')
        self.input_profil.setText('')
        self.input_type_social.setText('')
        self.input_dd_orders.setText('')

    def perform_add_to_base(self):
        FIO = self.input_name.text()
        Kurs = int(self.input_kurs.text())
        Profil_student = self.input_profil.text()
        Type_social = self.input_type_social.text()
        DD_MM_YY_order = self.input_dd_orders.text()
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            insert = [(FIO, Kurs, Profil_student, Type_social, DD_MM_YY_order)]
            # query = """ CREATE TABLE if not exists expenses (FIO text, kurs integer, profil text, type_social text, dd_orders text ) """
            query = """ insert into DGU_sistem (FIO, kurs, profil, type_social, dd_orders) values (?, ?, ?, ?, ?);"""
            cursor.executemany(query, insert)
            db.commit()
        self.input_name.setText('')
        self.input_kurs.setText('')
        self.input_profil.setText('')
        self.input_type_social.setText('')
        self.input_dd_orders.setText('')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DGU_sistem = QtWidgets.QWidget()
    ui = Ui_DGU_sistem()
    ui.setupUi(DGU_sistem)
    DGU_sistem.show()
    sys.exit(app.exec_())

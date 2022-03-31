# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tesT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        self.check_what_in_table = {
            'FIO': False,
            'Course': False,
            'Profile': False,
            'Type_social': False,
            'Data_start_end': False,
        }
        self.way_Date_base = 'db/database.db'
        # self.pull_down_menu_formats = QtWidgets.QComboBox(Form)
        # self.pull_down_menu_formats.setGeometry(QtCore.QRect(110, 60, 291, 22))
        # self.pull_down_menu_formats.setObjectName("pull_down_menu_formats")
        # self.pull_down_menu_formats.addItem("")
        # self.pull_down_menu_formats.addItem("")
        # self.pull_down_menu_formats.addItem("")
        self.creat_tables_from_excel = QtWidgets.QPushButton(Form)
        self.creat_tables_from_excel.setGeometry(QtCore.QRect(190, 30, 81, 26))
        self.creat_tables_from_excel.setObjectName("creat_tables_from_excel")
        self.creat_tables_from_notepad = QtWidgets.QPushButton(Form)
        self.creat_tables_from_notepad.setGeometry(QtCore.QRect(190, 80, 81, 26))
        self.creat_tables_from_notepad.setObjectName("creat_tables_from_notepad")
        # self.lb_info_about_format = QtWidgets.QLabel(Form)
        # self.lb_info_about_format.setGeometry(QtCore.QRect(110, 30, 281, 16))
        # self.lb_info_about_format.setObjectName("lb_info_about_format")
        self.checkBox_fio = QtWidgets.QCheckBox(Form)
        self.checkBox_fio.setGeometry(QtCore.QRect(15, 20, 85, 21))
        self.checkBox_fio.setObjectName("checkBox_fio")
        self.checkBox_kurss = QtWidgets.QCheckBox(Form)
        self.checkBox_kurss.setGeometry(QtCore.QRect(15, 50, 85, 21))
        self.checkBox_kurss.setObjectName("checkBox_kurss")
        self.checkBox_type_of_scholarship = QtWidgets.QCheckBox(Form)
        self.checkBox_type_of_scholarship.setGeometry(QtCore.QRect(15, 80, 121, 21))
        self.checkBox_type_of_scholarship.setObjectName("checkBox_type_of_scholarship")
        self.checkBox_profil = QtWidgets.QCheckBox(Form)
        self.checkBox_profil.setGeometry(QtCore.QRect(15, 110, 85, 21))
        self.checkBox_profil.setObjectName("checkBox_profil")
        self.checkBox_date_start_end = QtWidgets.QCheckBox(Form)
        self.checkBox_date_start_end.setGeometry(QtCore.QRect(15, 140, 151, 21))
        self.checkBox_date_start_end.setObjectName("checkBox_5")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(190, 130, 81, 26))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # self.click()
        self.creat_table_from()
        self.checkbox_1()
        self.checkbox_2()
        self.checkbox_3()
        self.checkbox_4()
        self.checkbox_5()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.pull_down_menu_formats.setItemText(0, _translate("Form", "none"))
        # self.pull_down_menu_formats.setItemText(1, _translate("Form", "блокнот"))
        # self.pull_down_menu_formats.setItemText(2, _translate("Form", "excel"))
        self.creat_tables_from_excel.setText(_translate("Form", "excel"))
        self.creat_tables_from_notepad.setText(_translate("Form", "notepad"))
        # self.lb_info_about_format.setText(_translate("Form", "формат получения данных"))
        self.checkBox_fio.setText(_translate("Form", "ФИО"))
        self.checkBox_kurss.setText(_translate("Form", "Курсс"))
        self.checkBox_type_of_scholarship.setText(_translate("Form", "Вид стипендии"))
        self.checkBox_profil.setText(_translate("Form", "Профиль"))
        self.checkBox_date_start_end.setText(_translate("Form", "Дата начала и конца"))
        self.exit.setText(_translate("Form", "exit"))

    # def click(self):
    #     self.pull_down_menu_formats.activated[str].connect(self.onActivated)

    # def onActivated(self, text):
    #     self.initializing_tables_bt.setText(text)

    def creat_table_from(self):
        self.creat_tables_from_excel.clicked.connect(lambda: self.perform_creat_table_from())

    def perform_creat_table_from(self):
        FIO = []
        Course = []
        Profile = []
        Type_social = []
        Data_start_end = []
        for x, y in self.check_what_in_table.items():

            if x == 'FIO' and y == True:
                # print('yes1')
                with sqlite3.connect(self.way_Date_base) as db:
                    cursor = db.cursor()
                    cursor.execute((" Select * from expenses "))
                    for i in cursor:
                        FIO.append(i[0])

            if x == 'Course' and y == True:
                # print('yes2')
                with sqlite3.connect(self.way_Date_base) as db:
                    cursor = db.cursor()
                    cursor.execute((" Select * from expenses "))
                    for i in cursor:
                        Course.append(str(i[1]))

            if x == 'Profile' and y == True:
                # print('yes3')
                with sqlite3.connect(self.way_Date_base) as db:
                    cursor = db.cursor()
                    cursor.execute((" Select * from expenses "))
                    for i in cursor:
                        Profile.append(i[2])

            if x == 'Type_social' and y == True:
                # print('yes4')
                with sqlite3.connect(self.way_Date_base) as db:
                    cursor = db.cursor()
                    cursor.execute((" Select * from expenses "))
                    for i in cursor:
                        Type_social.append(i[3])

            if x == 'Data_start_end' and y == True:
                # print('yes5')
                with sqlite3.connect(self.way_Date_base) as db:
                    cursor = db.cursor()
                    cursor.execute((" Select * from expenses "))
                    for i in cursor:
                        # self.check_end(i[4])
                        Data_start_end.append(self.check_end(i[4]))
            else:
                # print('yes6')
                pass

        base = {
            'ФИО': FIO,
            'Курс': Course,
            'Профиль': Profile,
            'Вид стипендии': Type_social,
            'Сроки назначения': Data_start_end,
        }
        if self.initializing_tables_bt.text() == 'excel':
            new_base = {}
            for i, j in base.items():
                if j != []:
                    new_base[i] = j
            base = pd.DataFrame(new_base)
            # print(base)
            base.to_excel('../вывод/teams.xlsx', sheet_name='report')


        elif self.initializing_tables_bt.text() == 'блокнот':
            with sqlite3.connect(self.way_Date_base) as db:
                cursor = db.cursor()
                cursor.execute((" Select * from expenses "))
                with open('../вывод/Таблица со степендиантыми.txt', 'w', encoding='utf-8') as file:
                    file.write(
                        '|ФИО' + ' ' * 37 + '|Курс ' + '|Профиль   ' + '|Вид стипендии' + ' ' * 17 + '|Дата стипендии\n')
                for i in cursor:
                    if self.check_what_in_table['FIO'] == True:
                        len_nema = i[0] + (' ' * (40 - len(i[0])))
                    else:
                        len_nema = (' ' * 40)

                    if self.check_what_in_table['Course'] == True:
                        len_kurs = str(i[1]) + ('    ')
                    else:
                        len_kurs = ('     ')

                    if self.check_what_in_table['Profile'] == True:
                        len_profil = i[2] + (' ' * (10 - len(i[2])))
                    else:
                        len_profil = ' ' * 10

                    if self.check_what_in_table['Type_social'] == True:
                        len_type_social = i[3] + (' ' * (30 - len(i[3])))
                    else:
                        len_type_social = ' ' * 30

                    if self.check_what_in_table['Data_start_end'] == True:
                        # i[4] = self.check_end(str(i[4]))
                        # print(i[4])
                        len_date_start_end = self.check_end(i[4]) + (' ' * (60 - len(self.check_end(i[4]))))
                    else:
                        len_date_start_end = ' ' * 60

                    with open('../вывод/Таблица со степендиантыми.txt', 'a', encoding='utf-8') as file:
                        file.write('+' + '-' * 128 + '+\n')
                        file.write(f'|{len_nema}|{len_kurs}|{len_profil}|{len_type_social}|{len_date_start_end}\n')
                        file.write('+' + '-' * 128 + '+\n')
                db.commit()
        elif self.initializing_tables_bt.text() == 'none' or self.initializing_tables_bt.text() == 'click':
            print('3')

    def check_end(self, date):
        import datetime
        if date in ['сирота', 'бессрочно', 'инвалид', 'Инвалид', 'ИНВАЛИД', 'Бессрочно', 'БЕССРОЧНО', 'Сирота',
                    'СИРОТА']:
            return date
        date_bd = date.split('-')[1].split('.')
        # print(date_bd)
        before = datetime.datetime.today()
        often = datetime.datetime(int(date_bd[2]), int(date_bd[1]), int(date_bd[0]))
        time = str(often - before).split(',')[0].split(' ')[0]
        # time = str(time).split(',')[0].split(' ')[0]
        try:
            if int(time) < 0:
                return f'{date} "истек"   {str(time)} дней прошло'
            else:
                return f'{date} "не истек"   {str(time)} дней осталось'
        except:
            return f'{date} "сегодня"'

    def checkbox_1(self):
        self.checkBox_fio.stateChanged.connect(self.perform_checkBox_1)

    def perform_checkBox_1(self, state):
        if state == Qt.Checked:
            self.check_what_in_table['FIO'] = True
        else:
            self.check_what_in_table['FIO'] = False

    def checkbox_2(self):
        self.checkBox_kurss.stateChanged.connect(self.perform_checkBox_2)

    def perform_checkBox_2(self, state):
        if state == Qt.Checked:
            self.check_what_in_table['Course'] = True
        else:
            self.check_what_in_table['Course'] = False

    def checkbox_3(self):
        self.checkBox_profil.stateChanged.connect(self.perform_checkBox_3)

    def perform_checkBox_3(self, state):
        if state == Qt.Checked:
            self.check_what_in_table['Profile'] = True
        else:
            self.check_what_in_table['Profile'] = False

    def checkbox_4(self):
        self.checkBox_type_of_scholarship.stateChanged.connect(self.perform_checkBox_4)

    def perform_checkBox_4(self, state):
        if state == Qt.Checked:
            self.check_what_in_table['Type_social'] = True
        else:
            self.check_what_in_table['Type_social'] = False

    def checkbox_5(self):
        self.checkBox_date_start_end.stateChanged.connect(self.perform_checkBox_5)

    def perform_checkBox_5(self, state):
        if state == Qt.Checked:
            self.check_what_in_table['Data_start_end'] = True
        else:
            self.check_what_in_table['Data_start_end'] = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

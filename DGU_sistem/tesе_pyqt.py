import openpyxl
import sqlite3


def deleted(name_delete):
    pass


def pps(import_file, action=0):
    if action == 1:
        for name in ['ИБ', 'ИСИТ', 'ИСИП', 'ПИЭ', 'ПИМ', 'ПИ', 'ПИЭУ']:
            print(name)
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = (''' DELETE from expenses WHERE profil = ?''')
                cursor.execute(query, (name,))
    elif action == 0:
        try:
            book = openpyxl.open(import_file, read_only=True)
            sheet = book.active
            for i in range(2, 300):
                FIO = sheet[i][1].value
                Kurs = sheet[i][2].value
                Profil_student = sheet[i][3].value.upper()
                Type_social = sheet[i][4].value
                DD_MM_YY_order = sheet[i][5].value
                with sqlite3.connect('db/database.db') as db:
                    cursor = db.cursor()
                    insert = [(FIO, Kurs, Profil_student, Type_social, DD_MM_YY_order)]
                    # query = """ CREATE TABLE if not exists expenses (FIO text, kurs integer, profil text, type_social text, dd_orders text ) """
                    query = """ insert into expenses (FIO, kurs, profil, type_social, dd_orders) values (?, ?, ?, ?, ?);"""
                    cursor.executemany(query, insert)
                    db.commit()
        except:
            print('error')


a = 'иб.xlsx'
# a.upper()
pps(a, int(input()))

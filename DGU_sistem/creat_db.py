import sqlite3

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    # query = """ CREATE TABLE if not exists expenses (FIO text, kurs integer, profil text, type_social text, dd_orders text ) """
    query = """ insert into expenses """
    cursor.execute(query)
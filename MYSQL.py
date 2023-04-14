import mysql.connector

def DBConnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gsb_rv"
        )
    return mydb

def DBSelect(MyDB, Query):
    mycursor = MyDB.cursor()
    mycursor.execute(f"{Query}")
    myresult = mycursor.fetchall()
    return myresult

def DBInsert(MyDB, Query):
    mycursor = MyDB.cursor()
    mycursor.execute(f"{Query}")
    MyDB.commt()
    MyDB.close()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="applivisiteur"
)

mycursor = mydb.cursor()
query=('SELECT * FROM test')
mycursor.execute(query)
for x in mycursor:
  print(x)


# TODO 
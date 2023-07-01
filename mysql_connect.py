import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="chutometro"
)

Connection = mydb.cursor()
#print(Connection)
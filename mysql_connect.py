import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="chutometro"
)

Connection = db.cursor()

def executeDatabaseCommand():
  db.commit()

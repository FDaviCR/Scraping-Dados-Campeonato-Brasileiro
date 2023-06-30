import mysql.connector

Connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="chutometro"
)

print(Connection)
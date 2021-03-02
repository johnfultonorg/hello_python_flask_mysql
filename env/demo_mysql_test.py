import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="314159265Password!",
  database="pet_info"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pets")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
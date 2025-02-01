from decouple import config
import mysql.connector


mydb = mysql.connector.connect(
    host=config("host"),
    user=config("user"),
    password=config("password"),
    database=config("database"),
)


mycursor = mydb.cursor()
mycursor.execute("select * from Students")
results = mycursor.fetchall()

for row in results:
    print(row)

mycursor.close()
mydb.close()

from decouple import config
import mysql.connector


mydb = mysql.connector.connect(
    host=config("host"),
    user=config("user"),
    password=config("password"),
    database=config("database"),
)
mycursor = mydb.cursor()
sql = "update Students set email = %s where StudentID = %s"
val = ("mujuniurbans@email.com", 4)
mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()

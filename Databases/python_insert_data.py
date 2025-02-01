from decouple import config
import mysql.connector


mydb = mysql.connector.connect(
    host=config("host"),
    user=config("user"),
    password=config("password"),
    database=config("database"),
)
mycursor = mydb.cursor()
sql = "INSERT INTO Students(StudentID,FirstName,LastName,Email,EnrollmentDate) Values(%s,%s,%s,%s,%s)"
val = (4, "Mujuni", "Urbans", "mujuni@email.com", "2022-01-09")
mycursor.execute(sql, val)
mydb.commit()

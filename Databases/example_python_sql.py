from decouple import config
import mysql.connector


mydb = mysql.connector.connect(
    host=config("host"),
    user=config("user"),
    password=config("password"),
    database=config("database"),
)
# Create a database table.
mycursor = mydb.cursor()
mycursor.execute(
    """
create table if not exists Customers(id int auto_increment primary key,
name varchar(100) not null,
email varchar(100) not null unique)
"""
)
print("Table created successfully.")


# Insert some data.
sql = """
# insert into Customers (name,email)
#     values(%s,%s)
# """
val = ("Mukulu John", "johnmukulu@email.com")
mycursor.execute(sql, val)
mydb.commit()  # Save changes to the database.
print(f"{mycursor.rowcount}, record(s) inserted.")

val = ("Jane Smith", "janesmith@email.com")
mycursor.execute(sql, val)
mydb.commit()  # Save changes to the database.
print(f"{mycursor.rowcount}, record(s) inserted.")

# Update data.
sql = """
    update Customers set id = %s where name = %s 
    
    """
val = (2, "Jane Smith")
mycursor.execute(sql, val)
mydb.commit()
mycursor.execute("SELECT * FROM Customers")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

mycursor.close()
mydb.close()
print("Database connection closed.")

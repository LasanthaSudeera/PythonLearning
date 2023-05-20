import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="python_learning", user="root", password="password")
if conn.is_connected:
    print("Connected to Mysql")

# Read operation (Get the first raw)
cursor = conn.cursor()
cursor.execute("SELECT * from emp")
# row = cursor.fetchone()
# print(row)

# Get all the records
all = cursor.fetchall()
print(all)


# Insert record
try:
    cursor.execute("insert into emp values(3,'Python User', 3000)")
    conn.commit()
except:
    conn.rollback()
    print("Error occured")


# Delete
try:
    cursor.execute("delete from emp where id = 2")
    conn.commit()
except:
    conn.rollback()
    print("Error occured")




# Close the connection
conn.close()

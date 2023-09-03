import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123")

cursor=con.cursor()
#cursor.execute("CREATE DATABASE customer")
#print("successfully created")
cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
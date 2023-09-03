import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="employee")
cursor=con.cursor()
cursor.execute("select* from emp")
data=cursor.fetchone()
print(data)
data=cursor.fetchone()
print(data)
print("Total Number of Row=", cursor.rowcount)
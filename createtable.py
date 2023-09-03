import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="customer")
cursor=con.cursor()
#cursor.execute("create table cust (id integer primary key, name varchar(50), age integer, gender varchar(2))")
cursor.execute("show tables")
for i in cursor:
    print(i)
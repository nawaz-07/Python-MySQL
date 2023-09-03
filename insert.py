import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="customer")

cursor=con.cursor()

# id=int(input("Enter Number:"))
# name=input("Enter Name:")
# age=int(input("Enter Age:"))
# gender=input("Enter Gender:")

# query= "INSERT INTO cust VALUES({},'{}',{},'{}')".format(id,name,age,gender)
# cursor.execute(query)
cursor.execute("select * from cust")
result=cursor.fetchall()
for i in result:
    print(i)


# cursor.commit()
# print(cursor.rowcount,"Record Inserted")
import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="employee")
cursor=con.cursor()
# query="update emp set salary=31000 where id=102"
# cursor.execute(query)
# con.commit()
# print("Data Updated Successfully")

id=int(input("Enter id:"))
Salary=int(input("Enter the salary:"))
query="update emp set Salary={} where id={}".format(Salary,id)
cursor.execute(query)
con.commit()
import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="employee")
cursor=con.cursor()
while True:
  id = int(input("Enter id:"))
  Name= input("Enter Name:")
  Salary=int(input("Enter Salary:"))
  query="Insert into emp values({},'{}',{})".format(id,Name,Salary)
  cursor.execute(query)
  con.commit()
  print("Inserted Successfully")
  x=int(input("1->Enter More\n 2->Exit\n Enter Choice:"))
  if x==2:
    break
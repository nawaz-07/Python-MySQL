import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="employee")
cursor=con.cursor()
#sql="Create table emp2( Id integer PRIMARY KEY, Name varchar(50),Age integer,Email varchar(30)) "
#cursor.execute(sql)
while True:  
    x=int(input("1->Insert Data\n2->Update Data\n3->Delete Data\n4->Show Table\n5->Exit\nEnter Choice:"))
    if x==1:
        try:
            id=int(input("Enter Emplyee Id:"))
            name=input("Enter Employee Name:")
            age=int(input("Enter Employee Age:"))
            email=input("Enter Employee Email Id:")
            sql = "INSERT INTO emp2 VALUES({},'{}',{},'{}')".format(id,name,age,email)
            cursor.execute(sql)
            con.commit()
            print("Data Inserted Secessfully")
        except:
            print("Please Input Correct Value")

    elif x==2:
        z=int(input("1->To ChangeName\n2->To ChangeAge\n3->To Change Email\n4->Update All\n5->Exit\nEnter Choice:"))
        if z==1:
            try:
                id=int(input("Enter Emplyee Id:"))
                name=input("Enter Employee Name:")
                sql="UPDATE emp2 set name='{}' where id={}".format(name,id)
                cursor.execute(sql)
                con.commit()
                print("Name is Updated")
            except:
                print("Enter Correct Value")    
        elif z==2:
            try:
                id=int(input("Enter Emplyee Id:"))
                age=int(input("Enter Employee Age:"))
                sql="UPDATE emp2 set age={} where id={}".format(age,id)
                cursor.execute(sql)
                con.commit()
                print("Age is Updated")
            except:
                print("Enter Correct Value")
        elif z==3:
            try:
                id=int(input("Enter Emplyee Id:"))
                email=input("Enter Employee Email Id:")
                sql="UPDATE emp2 set email='{}' where id={}".format(email,id)
                cursor.execute(sql)
                con.commit()
                print("Email is Updated")
            except:
                print("Enter Correct Value")    
        elif z==4:
            try:
                id=int(input("Enter Emplyee Id:"))
                name=input("Enter Employee Name:")
                age=int(input("Enter Employee Age:"))
                email=input("Enter Employee Email Id:")
                sql="UPDATE emp2 set name='{}',age={},email='{}' where id={}".format(name,age,email,id)
                cursor.execute(sql)
                con.commit()        
                print("All Data Updated Seccessfully") 
            except:
                print("Enter Correct Value")    
        elif z==5:
            break 
    elif x==3:
        id=int(input("Enter Id:"))
        sql="delete from emp2 where id={}".format(id)
        cursor.execute(sql)
        con.commit()
        print("Row Deleted Successfully")       
    elif x==4:   
        sql="select * from emp2"
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data) 
        print("Total Number of Row=", cursor.rowcount)
    elif x==5:
        break

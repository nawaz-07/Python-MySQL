import csv
import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="Nawaz@123",
              database="student")
cursor=con.cursor()

# sql="Create table champs (Id INTEGER PRIMARY KEY,First_Name VARCHAR(20),Last_Name VARCHAR(20),Age INTEGER,College_Name VARCHAR(15))"
# cursor.execute(sql)
with open("ITQuizWinner.csv",'r') as file:
    csv_data=csv.reader(file)
    next(csv_data)

    for i in csv_data:
        id=i[0]
        fname=i[1]
        lname=i[2]
        age=i[3]
        college=i[4]

        sql="INSERT INTO champs(Id,First_Name,Last_Name,Age,College_name) VALUES (%s,%s,%s,%s,%s)"
        data=(id,fname,lname,age,college)
        cursor.execute(sql,data)
con.commit()
con.close()
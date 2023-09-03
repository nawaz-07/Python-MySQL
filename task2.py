import csv
import mysql.connector as c
# Replace the placeholders with your actual MySQL database details
con = c.connector.connect(
    host="localhost",
    user="root",
    password="Nawaz@123",
    database="employee"
)
cursor = con.cursor()
with open('student.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip header row if necessary

    for row in csv_data:
        # Assuming your CSV columns are in the order: name, age, email
        Id=row[0]
        Name = row[1]
        Age = row[2]
        Email = row[3]

        # Prepare and execute the SQL query
        sql = "INSERT INTO emp3 (id,name, age, email) VALUES (%s,%s, %s, %s)"
        data = (Id,Name, Age, Email)
        cursor.execute(sql, data)
con.commit()
cursor.close()
con.close()
#Day 20 - SQL joins
# Gokul Dhakshana Murthy

import mysql.connector

try:
    database = mysql.connector.connect(host="localhost", user="root", password="*****", database="free", buffered = True,)

    dbcur = database.cursor()

    dbcur.execute('drop table Employee')
    dbcur.execute("create table Employee(EmpName varchar(20), EmpID int, EmpSalary float)")

    dbcur.execute("insert into Employee values ('Lisa',10,79500.24)")
    dbcur.execute("insert into Employee values ('Courtney',20,73450.14)")
    dbcur.execute("insert into Employee values ('Aniston',30,84100.22)")
    dbcur.execute("insert into Employee values ('David',40,45230.11)")
    dbcur.execute("insert into Employee values ('Le blanc',50,88795.23)")
    dbcur.execute("insert into Employee values ('Mathhew',60,125463.55)")

    print('Employee Table ')
    dbcur.execute("Select * from Employee")

    rows = dbcur.fetchall()
    print(rows)
    print()

    print('Ouery 1 - To get Max and Min Salary from Employee Table  :  ')
    dbcur.execute('select max(EmpSalary), min(EmpSalary) from Employee')
    print(dbcur.fetchall())
    print()

    print('Query 2 - To get No. of Employees working with the company :  ')
    dbcur.execute('select count(EmpName) from Employee')
    print(dbcur.fetchall())
    print()

    print('Query 3 - To get the first three characters of Employee Name : ')
    dbcur.execute('select substring(EmpName,1,3) from Employee')
    print(dbcur.fetchall())
     
except mysql.connector.Error as e :
     print("There is a problem ", e)
     


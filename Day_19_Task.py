import mysql.connector
import xlrd
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="********",
      database="free",
      buffered = True,
    )

    book = xlrd.open_workbook("Day_19_Excel_task.xlsx")
    sheet = book.sheet_by_name("Sheet1")

    cur = mydb.cursor()

    cur.execute('drop table Student_Database')
    cur.execute("create table Student_Database(ID int,RegisterNumber int,Name varchar(20),Marks int,Address varchar(20),Elective varchar(20))")
    query = "INSERT INTO Student_Database (ID ,RegisterNumber ,Name , Marks, Address , Elective) VALUES (%s, %s , %s , %s ,%s ,%s)"

    for r in range(0, sheet.nrows):
        ID = str(sheet.cell(r, 0).value)
        RegisterNumber = str(sheet.cell(r, 1).value)
        Name = str(sheet.cell(r, 2).value)
        Marks = str(sheet.cell(r, 4).value)
        Address = str(sheet.cell(r, 5).value)
        Elective = str(sheet.cell(r, 6).value)

        cur.execute(query, (ID,RegisterNumber,Name, Marks, Address, Elective))

    cur.execute("Select * from Student_Database")

    rows = cur.fetchall()

    for row in rows:
        print()
        print('ID:', row[0])
        print('RegisterNumber:', row[1])
        print('Name:', row[2])
        print('Marks:', row[3])
        print('Address:', row[4])
        print('Elective:', row[5])
     
except mysql.connector.Error as e :
     print("There is a problem ", e)
     


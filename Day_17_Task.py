#day 17 Task
# Gokul Dhakshana Murthy

#Imporying MySQL Connector
import mysql.connector
try:
    # connecting database with python
    con = mysql.connector.connect(host = 'localhost', user = 'root', password = 'createpas')
      
    cursor=con.cursor()
    #to get the version
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version : ', data)
    
    # manager table creation in 'free' database
    cursor.execute('use free')
    cursor.execute("create table manager(id int,name varchar(20))")    
    # inserting values in manager table
    cursor.execute("insert into manager values(10,'Phoebe Buffay')")
    cursor.execute("insert into manager values(20,'Joey Tribbiani')")
    cursor.execute("insert into manager values(30,'Monica Geller')")

    print("Manager Table created successfully and values inserted")
   
    # student table creation in 'free' database
    cursor.execute("create table student(id int,name varchar(15))")
    # inserting values into student table
    cursor.execute("insert into student values(40,'Ross Geller')")
    cursor.execute("insert into student values(50,'Chandler Bing')")
    cursor.execute("insert into student values(60,'Rachel Green')")
    print("Student Table created successfully and values inserted")
    

    #creating employee table
    cursor.execute("create table employee(id int,name varchar(15))")
    print("Employee Table created successfully")
    # inserting values into employee table
    cursor.execute("insert into employee values(11,'Janice')")
    cursor.execute("insert into employee values(12,'Mike Hannigan')")
    cursor.execute("insert into employee values(13,'Judy Geller')")
    cursor.execute("insert into employee values(14,'David Schwimmer')")
    print("Values inserted into employee table successfully")

    #printing employee table using for loop
    print("Printing employee table using for loop.....")
    cursor.execute("select * from employee")
    rows=cursor.fetchall()
    j=0
    for i in rows:
        print("Row ",(j+1),": ",i)
        j+=1
    con.commit()
except mysql.connector.Error as e:
    print("There is a problem ", e)
con.close()

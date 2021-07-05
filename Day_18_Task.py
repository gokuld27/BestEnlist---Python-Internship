#day 18 Task
# Gokul Dhakshana Murthy

#Imporying MySQL Connector
import mysql.connector
try:
    # connecting database with python
    con = mysql.connector.connect(host = 'localhost', user = 'root', password = '*******')
      
    cursor = con.cursor()
    #Creating Table
    cursor.execute('use free')
    '''cursor.execute("create table clinic(Doctor_id int,Doctor_name varchar(20),No_patients int)")
    cursor.execute("insert into clinic values(1,'Phoebe Buffay',7)")
    cursor.execute("insert into clinic values(2,'Joseph Tribbiani',1)")
    cursor.execute("insert into clinic values(3,'Monica Geller',20)")
    cursor.execute("insert into clinic values(4,'Chandler Bing',0)")
    cursor.execute("insert into clinic values(5,'Rachel Green',3)")
    cursor.execute("insert into clinic values(6,'Ross Geller',0)")'''
    print('Doctor(s) database created successfully with values inserted')
    print('~'*75)
    
    cursor.execute("SELECT Doctor_name FROM clinic WHERE No_patients > 5")
    print('Get the doctor(s) who have more than 5 patients visited : ')
    query1 = cursor.fetchall()
    for i in query1:
        print(i)
    cursor.execute("SELECT Doctor_name FROM clinic WHERE No_patients = 0")
    print('~'*75)
    print('Get the doctor(s) who have no patients visited : ')
    query2 = cursor.fetchall()
    for i in query2:
        print(i)

except mysql.connector.Error as e :
     print("There is a problem ", e)
     
con.close()

#Day 12 - File Operations
#Gokul Dhakshana Murthy
#Append the data your name in to it.


#Opening a file in append and read mode
aFile = open('30 days 30 hour operations.txt','a+')

#getting name from the user 
name = input('Enter name : ')

#appending name into the file
aFile.write(name)

print('Name has been appended successfully ! \n')

#closing file
aFile.close()

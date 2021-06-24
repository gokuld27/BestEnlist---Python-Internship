#Day 12 - File Operations
#Gokul Dhakshana Murthy
#1. Create a file named 30 days 30 hour operations adn write data in it - I have completed 10 days successfully


#Opening a file in write mode
File = open("30 days 30 hour operations.txt","w+")

#opertion to write the content
File.write('I have completed 10 days successfully\n')

#Printing the content of the file
print(File.read())

#Closing the file
File.close()

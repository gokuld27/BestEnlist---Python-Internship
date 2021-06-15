#Day 4 - Task 3 - Python variables & Data types
#Gokul Dhakdhana Murthy

#Ex 1
print( '1. Create three variables (a,b,c) to same value of any integer & do the following'
             '\n\ta) Divide a by 10'
              '\n\tb) Multiply b by 50'
              ' \n\tc) Add c value by 60\n')

a = b = c = 500#assignimg same value to three variables

print("Divide a by 10 = ", a/10)
print("Multiply b by 50 =  ", b*50)
print("Add c value by 60 = ",c+60 )
print()

#Ex 2
print('2. Create a String variable of 5 characters and replace the 3rd character with G\n ')
# using replace() function
string = 'Gokul'
print ('Using Buit-in function = ', string.replace(string[2],'G'))


#without using any built-in function

def split(string):
    return [char for char in string]

q = split(string)
q[2] = 'G'

def charToString(q):
    replacedString = ''
    for i in q:
        replacedString += i
    return replacedString

print("Without using Buit-in function = ", charToString(q))
print()

#Ex 3
print('3. Create two values (a,b) of int, float data type and convert the vice versa\n')
a = 50
b = 23.55
print('Converting integer a to floating datatype = ',float(a))
print('Converting floating b to integer datatype = ',int(b))

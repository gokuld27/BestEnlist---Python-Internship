# Day 9 Exercises
# Gokul Dhakshana Murthy
import math
# 1. Write a program to loop through a list of numbers and add +2 to every value to the elements of the list
List = []
p = int(input("Enter no of elements in a list : "))
print("Enter list elements")
for i in range(0,p):
    n = int(input())
    List.append(n)
print(List)

for i in range(0,p): # Loop to add 2 to each elmt
    List[i] = List[i] + 2
print('Resultant List = ',List)

print("________________________________________________________")


'''2. Write the python program to get below pattern
54321
4321
321
21
1'''

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end = '')
    print()

print("________________________________________________________")


# 3. Python program to print fibonacci series
n = int(input("Enter the limit for the Series : "))
fibo, a, b = 0, 0, 1

if n == 0:
    print("Fibonacci Series : 0")
else:
    print("Fibonacci Series :  ")
    for i in range(0,n):
        fibo = fibo + a
        a = b
        b = fibo
        print(fibo, end = '   ')
    
print("\n________________________________________________________")


'''4. Explain Armstrong Number and write a codewith function
Armstrong Number is nothing but the sum of its own digits each raised to the power of digits is equal to the number itself '''
def armstrong(n,_sum):
    temp  = n
    while temp >0 :
        a = temp % 10
        _sum += a**q
        temp = temp//10
    return _sum

n = int(input("Enter the number to check Armstrong or not : "))
q = len(str(n))
_sum = 0
call = armstrong(n,_sum)

if n == call:
    print(n," is an Armstrong Number")
else:
     print(n," is NOT an Armstrong Number")
print("________________________________________________________")


# 5. program to print the multiplication table of 9
n = int(input("Enter the Multiplication Table Limit : "))
print()
print('\t\tMultiplication Table of 9\n')
for i in range(0,n):
    print('9 x ',i,' = ',9*i)
print("________________________________________________________")


# 6. Check if a number is positive or negative
n = int(input("Enter a Integer number : "))
if n >= 0:
    print(n," is POSITIVE in nature")
else:
    print(n," is NEGATIVE in nature")
	
	
print("________________________________________________________")


# 7. write a program to convert number of days to ages
DAYS = int(input("Enter a Number of Days : "))
_days = DAYS // 365
print("Age is ", _days)
print("\n________________________________________________________")


# 8. Solve Trigonometric problem using math func write a program to solve using math function
Ang = math.pi/6
print(math.degrees(Ang))
print(math.radians(60))
print("Functions: \n\t Sine :",math.sin(Ang),"\n\tCosine :",math.cos(Ang), "\n\tTangent :",math.tan(Ang) ,"\n\tSine Inverse:",math.asin(Ang), "\n\tCosine Inverse:",math.acos(Ang), "\n\tTangent Inverse:",math.atan(Ang))

print("________________________________________________________")


# 9. Create a basic arithmetic calculator:
print("Enter your choice : \n\t1.Addition \n\t2. Subtraction \n\t3. Multiplication \n\t4. Division\n\t5. Exit at any time")
choice = input()
while True:
    print('Enter two operands to perform Arithmetic Operation :')
    n = int(input())
    m = int(input())
    if choice == '1':
        print(n," + ",m,' = ', n+m)
        
    elif choice == '2':
        print(n," - ",m,' = ', n-m)
        
    elif choice == '3':
        print(n," x ",m,' = ', n*m)
        
    elif choice == '4':
        print(n," / ",m,' = ', n/m)
        
    else:
        print("Invalid Input")
        exit()
		
print("________________________________________________________")

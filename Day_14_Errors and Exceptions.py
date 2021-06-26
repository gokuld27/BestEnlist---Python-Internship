#Day 14 - Errors and Exceptions
#Gokul Dhakshana Murthy


# 1. List down all the error types and check all the errors using a python program for all errors
print('Ex : 1')
''' ERRORS :
        An unsexpected or abnormal behaviour of the program
         Major Types:
                1. Logical Errors
                            - Specifies all those type of errors in which the program exceutes but gives incorrect results.
                2. Syntactical Errors
                            - When we violate the rules of python prgramming language.
                            - It is common when we learn a new programming language. '''

# Example for Logical Errors:

# Divide by Zero division Error

numerator = int(input('Enter a numerator : '))
denominator = int(input('Enter a denominator : '))

try:
    quotient = numerator/denominator
    print('The quotient is : ',quotient)
except ZeroDivisionError:
    print('Division by zero is not possible ! ')
    
# Example for syntactical Errors:
i = 0
try:
   # if i == 0 print(i)  - Invalid Syntax 
   if i == 0:
       print(i)
except SyntaxError:
    print('Syntax Error found ! Check once and try again ')

# Example for Value Error
try:
    float('qqq')
except ValueError as msg: 
    print(msg)

# Example for Name Error
try: 
    tuple1 = (1,2,3)
    print(tupl)
except NameError as msg: 
    print(msg)

    
# Example for Assertion Error
try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)
except AssertionError as msg: 
    print(msg)
    
# Example for Overflow Error
i=1
try:
    f = 3.0**i
    for i in range(100):
        print (i, f)
        f = f ** 2
except OverflowError as err:
    print ('Overflowed after ', f, err)
# Example for Import Error
import sys
try:
    from time import datetime
except Exception as msg:
    print (msg)
    
# Example for Key Error
import sys
try:
    s = {'a':5, 'b':7}['c']

except KeyError as msg:
    print (msg)
# Example for Value Error
try:
    def f():
        z=['foo','bar']
        for i in z:
            if i == 'foo':
                print(i)
except IndentationError as msg:
    print (msg)

# 2. Design a simple calculator app with try and except for all use cases

# This function adds two numbers
def add(x, y):
    try : 
        return x + y
    except (KeyboardInterrupt, ValueError, TypeError):
        print('Error Occured ! Try again')
        

# This function subtracts two numbers
def subtract(x, y):
    try : 
        return x - y
    except (KeyboardInterrupt, ValueError, TypeError):
        print('Error Occured ! Try again')
    

# This function multiplies two numbers
def multiply(x, y):
    try : 
        return x * y
    except (KeyboardInterrupt, ValueError, TypeError):
        print('Error Occured ! Try again')

# This function divides two numbers
def divide(x, y):
    try:
         return x / y
    except ZeroDivisionError:
        print('Division by zero is not possible ! Try again')

print('Ex : 2')
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Calculator failed ")

# 3. Print one message if the try block raises a NameError and another for other errors
print('Ex : 3')
try:
    n = int(input('Enter name : '))
    if n == 111:
        print(i)
        raise NameError
    elif n < 0:
        raise ValueError
except NameError as q:
    print(q)
except ValueError as w:
    print(w)


# 4. When try-except scenario is not required?
print('Ex : 4')
print(''' Python Errors and exceptions are error cases that alter the normal flow of a program
    When you feel like your program has some execeptions and errors by yourself you can
    make use of try_except scenarios. If it is not necessary then don't make use of it ''')

# 5. Try getting an input inside the try catch block
print('Ex : 5')
try :
    number = int(input('Enter some value : '))
except :
    print('Inavlid Value !')

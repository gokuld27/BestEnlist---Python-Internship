# Day 7 _ Task 6
# Gokul Dhakshana Murthy

#1.	Create a function getting two integer inputs from user. & print the following:

#Addition of two numbers is +value

#Subtraction of two numbers is +value

#Division of two numbers is +value

#Multiplication of two numbers is +value
#Here the value represents math function associated

def getvalue():
    a=int(input("Enter first number:"))
    b=int(input("Enter Second number:"))
    print("Addition of two numbers is:",addition(a,b))
    print("Subtraction of two numbers is:",subtraction(a,b))
    print("Multiplication of two numbers is:",multiplication(a,b))
    print("Division of two numbers is:",division(a,b))
    
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

getvalue()

#2. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree


def printdetails(pat,temp):
    print("Patient Name:",pat)
    print("Patient current temperature:",temp)
    
    
def covid(name,temperature=98):
    patientname=name
    finaltemp=temperature
    printdetails(patientname,finaltemp)

covid("patient1",98.6)
covid("patient2",98)
covid("patient3",100)

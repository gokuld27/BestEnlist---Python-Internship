# Day 5 - Task 4
#Gokul Dhakshana Murthy

#1) Write a program to create a list of n integer values and do the following

#Add an item in to the list (using function)
def addItem(num,b):
    pos=int(input('Enter the position for the number to be inserted : '))
    num.insert(pos,b)
    return num
#Delete (using function)
def deleteItem(b):
    num.remove(b)
    return num

num=list()
n=int(input('Enter the No. of value : '))
print('Enter the values : ')
for i in range(n):
    a=int(input())
    num.append(a)
print('List is : ',num)
b=int(input('Enter the element to be inserted : '))
num=addItem(num,b)
print('List after insertion : ',num)
b=int(input('Enter the element to be deleted : '))
num=deleteItem(b)
print('List after deletion : ',num)

#Store the largest number from the list to a variable
#Store the Smallest number from the list to a variable
minimum=min(num)
maximum=max(num)
print('Minimum element is : ',minimum)
print('Maximum element is : ',maximum)

#2) Create a tuple and print the reverse of the created tuple
tuple1=(4,5,6,7,3)
print('The created Tuple is : ',tuple1)
print('The reversed Tuple is : ',tuple1[::-1])

#     3) Create a tuple and convert tuple into list
tuple2=list(tuple1)
print('Converting tuple to list : ',tuple2)

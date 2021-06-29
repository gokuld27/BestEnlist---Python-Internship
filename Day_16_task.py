#day 16 Task
#Gokul Dhakshana Murthy

x=int(input("Enter value for x : "))
y=int(input("Enter Value for y : "))
aj=lambda x,y  : x*y
print(aj(x,y))
print("."*100)


def fibonacci(count):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count)))
    return fib_list[:count]
n=int(input("Enter Number of terms : "))
print(fibonacci(n))
print("."*100)


list1=[]
n=int(input("Enter Number of elements in a list : "))
for i in range(0,n):
    ele=int(input("Enter element :  "))
    list1.insert(i,ele)


a=int(input("Enter Number which is to be added to the list : "))
numbers=list(map(lambda number:number*a,list1))
print(numbers)
print("."*100)


my_list=[]
n1=int(input("Enter Number of Elements in a list : "))
for i in range(0,n1):
    ele1=int(input("Enter Element : "))
    my_list.append(ele1)
result=list(filter(lambda x: (x % 9 == 0), my_list))
print("Numbers divisible by 9 are ",result)
print("."*100)


list2=[]
n3=int(input("Enter Number of elements in a list : "))
for i in range(0,n3):
    ele3=int(input("Enter Element : "))
    list2.append(ele3)
even_ele=len(list(filter(lambda x: (x%2 == 0),list2)))
print("Number of even numbers in the list is : ")
print(even_ele)
print("."*25)

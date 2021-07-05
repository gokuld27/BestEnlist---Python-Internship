# Day 8 _ Task 7
#Gokul Dhakshana Murthy

print('Ex 1')
#1.Python script to merge two Python dictionaries
Dictionary1={'rollno':'1','name':'Queena','age':'18','sex':'Female'}
Dictionary2={'rollno1':'2','dept':'CSE'}
print('Dict1 : ',Dictionary1)
print('Dict2 : ',Dictionary2)
Dictionary1.update(Dictionary2)
print('Merged Dictonary : ',Dictionary1)

print('Ex 2')

#2.program to sort the value from descending to ascending in list and convert it in to a set
list1=[50,40,30,20,10]
print('list1 : ',list1)
list1.sort()
print('sorted list1 : ',list1)
set1=set(list1)
print('list1 after converting to set : ',set1)

print('Ex 3')

#3.Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function
dict3={'key':[5,4,3,2,1]}
print('dict3 : ',dict3)
dict3['key'].sort()
print('dict3 after sorting its items with INBUILT  function : ',dict3)
dict4={'key':[5,4,3,2,1]}
print('Sorting the items without using INBUILT function')
for i in range(len(dict4['key'])):
    for j in range(i + 1, len(dict4['key'])):
        if dict4['key'][i] > dict4['key'][j]:
           dict4['key'][i], dict4['key'][j] = dict4['key'][j], dict4['key'][i]
print('Dict4 after sorting its items without function : ',dict4)

print('Ex 4')

#4.Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
str1='name is a good person and his/her name has a meaning called love'
print('str1 : ',str1)
str2=input('Enter your  name :')
str3=str1.replace('name', str2)
print('After changing the first occurance of the string with user specified input : ',str3)

print('Ex 5')


#5.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter
str4='all occurrences of its first char have been changed to capital letter'
print('str4 : ',str4)
list2=str4.split()
str5=input('Enter the word that you want to capitalize : ')
str6=''
for i in list2:
    if i==str5:
        str6+=(i.capitalize()+' ')
        continue
    str6+=(i+' ')
print('After changing all the occurances of the word in str4 :',str6)

print('Ex 6')


#6.Python program to find the repeated items of a list
list3=[11,21,3,2,21,9,0,3,21,21,21,6]
print('list3 : ',list3)
print('The repeated items are : ',end='')
list4=[]
for i in range(len(list3)):
    if list3.count(list3[i])>1 and list3[i] not in list4:
        list4.append(list3[i])
        print(list3[i],end=' ')
print()

print('Ex 7')

#7.Python program to check the sum of three elements and divided by a value which is given as an input by the user
num1=int(input('Enter the number 1 : '))
num2=int(input('Enter the number 2 : '))
num3=int(input('Enter the number 3 : '))
val=int(input('Enter the divisor value : '))
print('After performning the operation : ',(num1+num2+num3)/val)

print('Ex 8')

#8.Python program to find the Mean,median,mode among three given numbers
print('The three numbers ',num1,num2,num3)
print('Mean : ',(num1+num2+num3)/3)
list5=[num1,num2,num3]
list5.sort()
print('Median : ',list5[1])
for i in range(len(list5)):
    if list5.count(list5[i])>1:
        print('Mode : ',list5[i])
        break


print('Ex 9')
#9.Python program to swap cases of a given string
str7='Python Program to Swap Cases of a given String'
print('str7 : ',str7)
print('After swapping the cases : ',str7.swapcase())

print('Ex 10')

#10.program to convert an integer to binary & octa decimal
num4=16
print('num6 : ',num4)
print('num6 in binary : ',bin(num4))
print('num6 in octa decimal : ',oct(num4))



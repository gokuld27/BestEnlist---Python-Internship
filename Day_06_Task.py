# Day 5 - Dictionary, Sets
# Gokul Dhakshana Murthy

# Creating and displaying Dictionaries
Dictionary1={'rollno':'1','name':'Queena','age':'18','sex':'Female'}
Dictionary2={'rollno1':'2','dept':'CSE'}
print('Dictionary - 1 = ',Dictionary1)
print('Dictionary - 2 = ',Dictionary2)

# 1. Python Script to merge two dictionaries
Dictionary1.update(Dictionary2)
print('Resultant Dictionary = ',Dictionary1)

# 2. Python program to remove a key from a dictionary
Dictionary1.pop("age")
print('Dictionary1 after removing key "age" = ',Dictionary1)

#3. Python program to map two lists into a dictionary
list1=[2,4,8,16,32]
list2=['OS','DBMS','QABS','IICT','DS']
Dictionary3=dict()
print('List - 1 : ',list1)
print('List - 2 : ',list2)
for i in range(len(list1)):
    Dictionary3[list1[i]]=list2[i]
print('After converting two list to dictionary : ',Dictionary3)

#Creating set
Set1={2,4,8,16,32}
Set2={32,8}
print('Set - 1 : ',Set1)
print('Set - 2 : ',Set2)
#4. Python program to find the length of a set
print('Length of Set - 1 : ',len(Set1))


# 5. Python program to remove the intersection of a 2nd set from the 1st set
Set3=Set1.difference(Set2)
print('After removing the intersection of a 2nd set from the 1st set ',Set3)

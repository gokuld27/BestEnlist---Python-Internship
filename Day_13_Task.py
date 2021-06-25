#Day 13 Task
# Gokul Dhakshana Murthy

import re

#1.Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
print('1.Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)')
txt = input('Enter the string : ')
if(re.search('[a-z]', txt) or re.search('[A-Z]', txt) or re.search('[0-1]', txt)):
    print('The string contains the character set [a-z],[A-Z],[0-9]')
else:
     print('The string does not contain the character set [a-z],[A-Z],[0-9]')

# 2.Write a Python program that matches a word containing ab
print('2.Write a Python program that matches a word containing ab')
txt = input('Enter the string : ')
if(re.findall('ab', txt)):
    print('Match found with ab',re.findall('ab', txt))
else:
    print('Match not found')

# 3.Write a Python program to check for a number at the end of a word/sentence
print('3.Write a Python program to check for a number at the end of a word/sentence')

txt=input('Enter the string : ')

if(re.findall('[0-9]$', txt)):
    print('The string ends with a number')
else:
    print('The string does not ends with a number')

#4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
print('4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string')
txt=input('Enter the string : ')
x=[]
if(re.findall('[0-9][0-9][0-9]', txt) or re.findall('[0-9][0-9]',txt) or re.findall('[0-9]', txt)):
    x+=([re.findall('[0-9][0-9][0-9]', txt)] + [re.findall('[0-9][0-9]',txt)] + [re.findall('[0-9]', txt)])
    print('Contains digits of 1-3 length : ',x)
else:
    print('No 1-3 length numbers found numbers found')

#5.Write a Python program to match a string that contains only uppercase letters
print('5.Write a Python program to match a string that contains only uppercase letters')

txt=input('Enter the string : ')

if(re.findall('[A-Z]', txt)):
    print('The string contains uppercase letters : ',re.findall('[A-Z]', txt))
else:
    print('The string contains no upper case letters')

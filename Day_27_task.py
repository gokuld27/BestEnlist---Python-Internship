# Day 27
# Gokul Dhakshana Murthy

import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
  

res = requests.get('https://news.ycombinator.com/news?p=2')

soup =  BeautifulSoup(res.text, 'lxml')

tags = {tag.name for tag in soup.find_all()}

class_list = set()

wb = Workbook()


sheet = wb.add_sheet('Sheet')



for tag in tags:
  
    
    for i in soup.find_all( tag ):
  
        
        if i.has_attr( "class" ):
  
            if len( i['class'] ) != 0:
                class_list.add(" ".join( i['class']))

class_list=list(class_list)
for i in range(len(class_list)):
    sheet.write(i,0,class_list[i])

wb.save('Day_27_TaskExcel.xls')

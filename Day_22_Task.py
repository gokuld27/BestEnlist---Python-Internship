# Day 22
# Gokul Dhakshana Murthy

from PIL import Image
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader
import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
  database="free",
  buffered = True,
)

dbse = mydb.cursor()

img1 = Image.open('Doggy.jpg')
img1.show()
print(img1.format)
print(img1.mode)

def merging_PDF():
    merge = PdfFileMerger()
    merge.append(PdfFileReader('PDF.pdf', 'rb'))
    merge.append(PdfFileReader('PDF2.pdf', 'rb'))
    merge.write("MergedPDF.pdf")

def webscraping():
    URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL)    
    soup = BeautifulSoup(r.content, 'html.parser')    
    quotes=[]      
    table = soup.find('div', attrs = {'id':'all_quotes'}) 

    dbse.execute('Drop table web_data')
    dbse.execute('Create table web_data(theme text, quote text, url text)')

    query = """Insert into web_data (theme, quote, url) values (%s, %s, %s)"""
    
    for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        quote = {}
        quote['theme'] = row.h5.text
        quote['url'] = row.a['href']
        quote['lines'] = row.img['alt'].split(" #")[0]
        quotes.append(quote)

        dbse.execute(query, (quote['theme'], quote['lines'], quote['url']))

def filterdata():
    dbse.execute('Select quote from web_data where theme = \'hard work\'')
    data = list(dbse.fetchall())
    for d in data:
        print(d[0])
        
merging_PDF()
webscraping()
filterdata()

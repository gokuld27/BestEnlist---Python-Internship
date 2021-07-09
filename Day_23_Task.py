#Day 23 Task
# Gokul Dhakshana Murthy

from tkinter import *
from tkinter import filedialog
from PIL import Image
import requests
from bs4 import BeautifulSoup
import PyPDF2
import warnings
from PyPDF4 import PdfFileWriter, PdfFileReader
import PyPDF4

warnings.filterwarnings("ignore")

output = 'combined_pdf.pdf'

def browseFiles():
    
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("jpeg files",
                                                        "*.jpeg*"),
                                                       ("all files",
                                                        "*.*")))
    
    label_file_explorer.configure(text="File Opened: "+filename)

    im = Image.open(filename)
    
    im.save("converted.png", "PNG")

def getWeather():
    res = requests.get('https://www.weather-forecast.com/locations/'+weather_entry.get()+'/forecasts/latest')

    soup =  BeautifulSoup(res.text, 'lxml')

    cont=soup.find('span','phrase')
    
    weather_details.configure(text=cont.text,wraplength=200,justify=CENTER,width=50,height=10,anchor=CENTER)

def getpdf1():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("pdf files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
    
    
    pdfmerger_display_file1.configure(text=filename)

def getpdf2():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("pdf files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
    
    pdfmerger_display_file2.configure(text=filename)

     
def PDFmerge():
    pdfs = [pdfmerger_display_file1.cget("text"),pdfmerger_display_file2.cget("text")]
    pdfMerger = PyPDF2.PdfFileMerger(strict=False)
    for pdf in pdfs:
        pdfMerger.append(pdf)
    with open(output, 'wb') as f:
        pdfMerger.write(f)
    input_pdf='combined_pdf.pdf'
    watermark='watermark.pdf'
    output_pdf='merge.pdf'
    watermark_instance = PdfFileReader(watermark)
    watermark_page = watermark_instance.getPage(0)
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)
        
window = Tk()

window.title("Tkinter mini project")

window.geometry('700x500')

window.configure(background = "snow2")



label_file_explorer=Label(window,text="Your Selected File Will appear here.....")

lableBrowseFiles=Label(window,text="Browse JPEG files").grid(row=1,column=1)

buttonBrowseFiles=Button(window,text="Browse",command=browseFiles).grid(row=1,column=2)

label_file_explorer.grid(row=2,column=1)

weather_label=Label(window,text="Enter the location : ").grid(row=3,column=1)

weather_entry=Entry(window)

weather_details=Label(window)

weather_fetch=Button(window,text="Fetch weather",command=getWeather).grid(row=3,column=3)

weather_entry.grid(row=3,column=2)

weather_details.grid(row=4,column=2)

pdfmerger_display_file1=Label(window)

pdfmerger_display_file2=Label(window)


pdfmerger_file1_label=Label(window,text="select pdf file 1 : ").grid(row=5,column=1)

pdfmerger_file1_browseButton=Button(window,text="Browse",command=getpdf1).grid(row=5,column=2)

pdfmerger_file2_label=Label(window,text="select pdf file 1 : ").grid(row=6,column=1)

pdfmerger_file2_browseButton=Button(window,text="Browse",command=getpdf2).grid(row=6,column=2)

pdf_merge_button=Button(window,text="Merge with water mark",command=PDFmerge).grid(row=7,column=2)

pdfmerger_display_file1.grid(row=5,column=3)

pdfmerger_display_file2.grid(row=6,column=3)



window.mainloop()

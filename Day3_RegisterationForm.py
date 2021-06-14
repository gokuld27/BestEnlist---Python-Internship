#Day 3 - Task 2 - Simple Registeration Form
#Gokul Dhakshana Murthy

#IMPORTING NECESSARY MODELUS
from tkinter import *
from tkinter import ttk
wd = Tk()

#DECLARING WINDOW TITLE
wd.title("Employees.com")

#DECLARING WINDOW SIZE
wd.geometry('900x600')

#DECLARING WINDOW COLOUR
wd.configure(background = "Wheat");

#FIELD DECLARATION
title = Label(wd, text = 'Employee Registeration Form', background = 'Silver',foreground= 'Navy Blue', font = ('Segoe Print' , 15)).grid(row = 0, column = 4)
a = Label(wd ,text = "First Name").grid(row = 2,column = 2)
b = Label(wd ,text = "Last Name").grid(row = 3,column = 2)
c = Label(wd ,text = "Email Id").grid(row = 4,column = 2)
d = Label(wd ,text = "Contact Number").grid(row = 5,column = 2)

a1 = Entry(wd).grid(row = 2,column = 3)
b1 = Entry(wd).grid(row = 3,column = 3)
c1 = Entry(wd).grid(row = 4,column = 3)
d1 = Entry(wd).grid(row = 5,column = 3)

#using Radio Buttons
e = Label(wd ,text = "Gender ").grid(row = 6,column = 2)
rug =  IntVar()
R1 = Radiobutton(wd, text="Male", variable=rug, value=1,).grid(row=6,column=4)
R2 = Radiobutton(wd, text="Female", variable=rug, value=2,).grid(row=6,column=6)
R3 = Radiobutton(wd, text="Others", variable=rug, value=3,).grid(row=6,column=8)

#using drop down feature
SelectAge = Label(wd ,text = "Country  ").grid(row = 7,column = 2)
variable = StringVar(wd)
variable.set('Japan')
country = OptionMenu(wd, variable,'India','US','SouthAfrica','China','Australia','Japan','Europe','Greece').grid(row=7,column=3)


LangKnown = Label(wd ,text = "Programming Languages known ").grid(row = 8,column = 2)
qq = Checkbutton(wd,text='C').grid(row=8,column=3)
ww = Checkbutton(wd,text='C#').grid(row=8,column=4)
ee = Checkbutton(wd,text='C++').grid(row=8,column=5)
tt = Checkbutton(wd,text='Java').grid(row=8,column=6)
rr = Checkbutton(wd,text='Python').grid(row=8,column=7)
rr = Checkbutton(wd,text='Dart').grid(row=8,column=8)

#using checkbox
sk = Label(wd ,text = "Interpersonal Skills  ").grid(row = 9,column = 2)
sk1 = Text(wd,width=20, height=3).grid(row=9,column=3)


ye=Label(wd ,text = "Years of Experience ").grid(row=10,column = 2)
ye1 = Spinbox(wd, from_=0, to=50).grid(row=10,column=3)


aoi = Label(wd ,text = "Areas of Interest ").grid(row = 11,column = 2)
aoi1 = Entry(wd).grid(row = 11,column = 3)

#function declaration
def clicked():
   result = "Welcome to " + txt.get()
   lbl.configure(text = result)
ovr = Button(wd ,text="Submit",bg = 'Teal', font = ('Corbel', 15)).grid(row=13,column=3)
wd.mainloop()

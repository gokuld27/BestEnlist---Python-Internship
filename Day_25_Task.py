# Day 25 - DATE & TIME
# Gokul Dhakshana Murthy

from datetime import datetime, timedelta, date

def convertTime():    
    string_date = '27-10-01 09:35:35'
    date_time_conversion = datetime.strptime(string_date,'%d-%m-%y %H:%M:%S')
    print('After conversion the type of DATE is : ',type(date_time_conversion))

def subract5Days():
    DaTe = date.today() - timedelta(days=5)
    print('Current System Date : ',date.today())
    print('FIVE days before current date : ',DaTe)

def convertTimeUsingFunction():
    DaTe_TiMe = datetime.combine(date.today(), datetime.min.time())
    print('Date after converting using function ',DaTe_TiMe)
    print('The type of Date after conversion : ',type(DaTe_TiMe))

def next7Days():
    print('Printing next 7 days from ',datetime.today(),' (today)')
    presentDay = datetime.today()
    for i in range(1,8):
        data = presentDay + timedelta(days = i)
        print(data.strftime('%A'))


# FUNCTION CALL 
convertTime()
subract5Days()
convertTimeUsingFunction()
next7Days()

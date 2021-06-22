'''Day 10 - Inheritance for Banking purpose
- Gokul Dhakshana Murthy'''

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Banking:
    balance = 0
    def _init_(self):
        self.balance=0
                
    def deposit(self):
        amount = float(input("Enter the amount to be Deposited : "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
        print('\nDo you need a printed Reciept ?')
        ch = input()
        if (ch == 'yes') or (ch == 'Yes') or (ch == 'YES') or (ch == 'y') or (ch == 'Y') :            
            print('\t\t\t\t\tRECIEPT\n')
            print('\t\t\t\tAGC Bank Service')
            print('\nAmount Deposited: ',amount)
            print('\n \t Thank You for using AGC Bank service !!! Visit Again !!!\n')
        else:
            print('\nTransaction Successfull\n')
        print("*"*100)
  
    def withdraw(self):
        amount = float(input("Enter the amount to be Withdrawn : "))
        if self.balance >= amount:
            self.balance-=amount
            print("\n You Withdrew : ", amount)
        else:
            print("\n Insufficient balance !!\nCheck your Balance ")
            print('To check balance press 2 ')
            print('\n \t Thank You for using AGC Bank service !!! Visit Again !!!\n')
        print("*"*100)
  
    def display_balance(self):
        print("\n Net Available Balance = ",self.balance)
        print('\n \t Thank You for using AGC Bank service !!! Visit Again !!!\n')
        print("*"*100)

class Ecommerce(Banking):
    cart = []
    def _init_(self):
        self.cart=[]
    def product_category_selection(self):
        while True:
            category = input("Categories \n 1.Men \n 2.Women \n 3.Electronics \n 4. Grocery\n 5. Proceed with bill payment \nEnter a Category : ")
            if category =='1':
                choose = input('Select Product \n1. Shirt 2. T-Shirt 3. Trousers \n')
                if choose =='1':
                    print('Shirt added to cart \n')
                    self.cart.append('Shirt')
                elif choose == '2':
                    print('T-Shirt added to cart \n')
                    self.cart.append('T-Shirt')
                elif choose == '3':
                    print('Trouser added to cart \n')
                    self.cart.append('Trouser')
                else:
                    print('No product selected from Men Category\n')

            elif category == '2':
                choose = input('Select Product \n1. Kurta 2. Frocks 3. Saree \n')
                if choose =='1':
                    print('Kurta added to cart \n')
                    self.cart.append('Kurta')
                elif choose == '2':
                    print('Frocks added to cart \n')
                    self.cart.append('Frock')
                elif choose == '3':
                    print('Saree added to cart \n')
                    self.cart.append('Saree')
                else:
                    print('No product selected from Women Category\n')
            elif category =='3':
                choose = input('Select Product \n1. Computer 2. TV 3. AirConditioner \n')
                if choose =='1':
                    print('Computer added to cart \n')
                    self.cart.append('Computer')
                elif choose == '2':
                    print('TV added to cart \n')
                    self.cart.append('TV')
                elif choose == '3':
                    print(' AirConditioner added to cart \n')
                    self.cart.append(' AirConditioner')
                else:
                    print('No product selected from Electronics Category\n')
            elif category == '4':
                choose = input('Select Product \n1. Rice 2. Vegetables 3. Dals/pulses  \n')
                if choose =='1':
                    print('Rice added to cart \n')
                    self.cart.append('Rice')
                elif choose == '2':
                    print('Vegetables added to cart \n')
                    self.cart.append('Vegetables')
                elif choose == '3':
                    print('Dals/pulses added to cart \n')
                    self.cart.append('Dals/pulses')
                else:
                    print('No product selected from Grocery Category\n')
            elif category == '5':
                print('Billing Process')
                break
            

    def bill_payment(self,s):
        _amount = 0
        for i in range(len(self.cart)):
            if self.cart[i] == 'Shirt' :
                _amount += 500
            elif self.cart[i] == 'T-Shirt' :
                _amount += 345.56
            elif self.cart[i] == 'Trouser' :
                _amount += 800
            elif self.cart[i] == 'Kurta' :
                _amount += 463.00
            elif self.cart[i] == 'Frock' :
                _amount += 1250.98
            elif self.cart[i] == 'Saree' :
                _amount += 765.9
            elif self.cart[i] == 'Computer' :
                _amount += 50500
            elif self.cart[i] == 'TV' :
                _amount += 35500
            elif self.cart[i] == 'AirConditioner' :
                _amount += 50000
            elif self.cart[i] == 'Rice' :
                _amount += 1150.50
            elif self.cart[i] == 'Vegetables' :
                _amount += 345.92
            elif self.cart[i] == 'Dal/pulses' :
                _amount += 1111.1
            else :
                print('Unknown Product\n')
        print('Your Bill Amount : ',_amount)
        print("Cash or NetBanking")
        via = input()
        if via == 'Cash':
            print('Pay Rs. ',_amount,' to the delivery person')
        else:
            s.balance-=_amount
    

# creating an object of class
s = Banking()
e = Ecommerce()  
# Calling functions with that class object
print("\t\t\tAGC Banking and E - Commerce\n\tHello!!! Welcome to the Deposit  &  Withdrawal Machine ")
while True:
    print("Enter your choice : \n\t1.Deposit \n\t2. Withdrawal \n\t3. Balance Enquiry \n\t4. E - Commerce\n\t5. Exit\n")
    choice = input()
    if choice == '1':
        s.deposit()
    elif choice == '2':
       s.withdraw()
    elif choice == '3':
        s.display_balance()
    elif choice == '4':
        print('\t\t\tWelcome to AGC E - Commerce ')
       
        e.product_category_selection()
        
        e.bill_payment(s)
    elif choice == '5' :
        exit('Thank you ')

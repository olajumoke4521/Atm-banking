import csv
import datetime

class Bank:
    def __init__(self,name):
        self.name = name

class New_user():
    def __init__(self, name, account_no, sex, address, pin, balance, bank):
        self.name = name 
        self.sex = sex 
        self.account_no = account_no
        self.adresss = address
        self.pin = pin
        self.balance = 0
        self.bank = bank

    def login(self, pin):
        if pin == self.pin:
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        if self.login(old_pin) == True:
            self.pin = new_pin
            print("Pin has been changed successful.")
        else:
            print("Enter the correct old pin.")
    


class Transaction(New_user):
    def __init__(self, date, transaction_type, balance_before, balance_after, amount):
        self.date = date
        self.transaction_type = transaction_type
        self.balance_before = balance_before
        self.balance_after = balance_after
        self.amount = amount

    def withdrawalcash(self, amount):
        if self.New_user.balance > amount:
            self.balance_before = self.New_user.balance
            self.New_user.balance = self.New_user.balance - amount
            self.balance_after = self.New_user.balance
            self.amount = amount
            print("Transaction successful.")
        else:
            print("Insufficient Balance")

    def depositcash(self, amount):
        self.amount = amount
        self.balance_before = self.New_user.balance
        self.New_user.balance = self.New_user.balance + amount
        self.balance_after = self.New_user.balance
        print("The deposit is successful.")

    def acc_balance(self):
        return self.balance_after

print('Hello ! Welcome to APU bank !')
print('Please login to proceed.')
username = input('Please enter your username:')
password = input('Please enter your password:')
with open('customer_details.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_reader:
        data = row
        if username in data and password in data:
            print('Login Successful')
    opt = int(input('Do you want to continue? Enter 0 to continue, 1 to Terminate:'))
    while True:
        if (opt == 0):
            print('What would you like to do? \n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Change password')
            opt = int(input('Enter your choice:'))
            if(opt == 1):
                depositcash()
                break
            elif(opt == 2):
                 withdrawalcash()
                 break
            elif(opt == 3):
                 balance()
                 break
            elif(opt == 4):
                change_pin()
            else:
                print('Wrong Option')
                opt= int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate:'))
        elif (opt == 1):
            print('Goodbye')
            break
        else:
            print('Wrong option')
            opt= int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate.'))
    else:
        print('Incorrect Username or Password. Please try again.')
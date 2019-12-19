'''
Released under BSD.
Source code available at https://github.com/gaganmalvi/DecixBMS
(C) Gagan Malvi 2019
'''
import pymysql as p
import os

def intro():
    clrscr()
    print("\t\t+------------------------------+")
    print("\t\t|    Bank Management System    |")
    print("\t\t+------------------------------+")
    print("\t\t|  The tool you can bank upon! |")
    print("\t\t+------------------------------+")
    input()

def NewAccount():
    sno = input('Enter the new account number :')
    name= input('Enter the new account name   :')
    Type= input('Enter account type [C/S]     :')
    amt = input('Enter initial amount         :')
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    q1 = 'insert into accounts values('+str(sno)+','+str(name)+','+str(Type)+','+str(amt)+');'
    a.execute(q1)
    c.commit()
    print('New account created successfully, press any key to continue...')

def clrscr():
	if os.name=="nt":
		u = os.system("cls")
	else:
		u = os.system("clear")

def modifyAccount(num):
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    sno = input('Enter the account number            : ')
    name = input('Enter the name of the account holder: ')
    acctype = input('Enter type of account (C/S)         : ')
    q1 = 'update accounts set AccName = '+str(name)+' where sno = '+str(sno)
    q2 = 'update accounts set AccType = '+str(acctype)+' where sno = '+str(sno)
    a.execute(q1)
    a.execute(q2)
    c.commit()
    print('Account updated successfully. Press any key to continue.')

def deposit(num):
    print('Deposit to Account Number: ',num)
    amount = input ('Enter the amount to deposit:')
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    q1 = 'update accounts set amount=amount+'+str(amount)+' where sno='+str(num)+';'
    a.execute(q1)
    c.commit()
    print('Deposited the required amount successfully. Press any key to continue.')

def withdraw(num):
    print('Withdraw to Account Number: ',str(num))
    amount = input ('Enter amount to withdraw: ')
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    q1 = 'update accounts set amount=amount-'+str(amount)+' where sno='+str(num)+';'
    a.execute(q1)
    c.commit()
    print('Withdrew the required amount successfully, press any key to continue.')

def balanceEnquiry(num):
    print('Balance (Account Number: '+str(num)+')')
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    q = 'select amount from accounts where sno='+str(num)+';'
    a.execute(q)
    d = a.fetchall()
    print('==========================') 
    for i in d:
        for j in i:
            print ('Balance in INR:',j,end='\t')
        print()

def deleteAccount(num):
    x = input('DELETING ACCOUNT FOR S/N '+str(num)+'DO YOU WANT TO CONTINUE? CHANGES ARE IRREVERSIBLE! (Y/N):')
    if x == 'Y':
        c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
        a = c.cursor()
        a.execute('delete from accounts where sno='+str(num)+';')
        c.commit()
        print('Deleted account successfully, press any key to continue')
    else:
        print('Wrong option, try again!')

def displayAll():
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    a.execute('select * from accounts;')
    d = a.fetchall()
    print ('List of All Account Holders')
    print ('===========================')
    print ('AccountNo\tAccountHolder\t\tType\t\tAmount')
    print ('=========\t=============\t\t====\t\t======')
    for i in d:
        for j in i:
            print (j,end='\t\t')
        print()

ch=''
num=0
intro()

while ch != 8:
    clrscr()
    print('=====================')
    print('Decix Bank Management')
    print('=====================')
    c = p.connect (host='localhost',user='root',password='Gaganmalvi@123',database='bms')
    a = c.cursor()
    q = 'select * from menu'
    a.execute(q)
    d = a.fetchall()
    print ('Option\tAction')
    for i in d:
        for j in i:
            print (j,end='\t')
        print()

    print("Select Your Option (1-8) ")
    ch = input()

    if ch == '1':
         clrscr()
         NewAccount()
    elif ch =='2':
         clrscr()
         num = int(input("Enter The account No. : "))
         deposit(num)
    elif ch == '3':
         clrscr()
         num = int(input("Enter The account No. : "))
         withdraw(num)
    elif ch == '4':
         clrscr()
         num = int(input("Enter The account No. : "))
         balanceEnquiry(num)
    elif ch == '5':
         clrscr()
         displayAll()
    elif ch == '6':
         clrscr()
         num =int(input("Enter The account No. : "))
         deleteAccount(num)
    elif ch == '7':
         clrscr()
         modifyAccount(num)
    elif ch == '8':
         clrscr()
         print("\t+-----------------------------+")
         print("\t|Thank you for using DecixBMS!|")
         print("\t+-----------------------------+")
         break
    else :
         print("Invalid choice")
    ch = input()

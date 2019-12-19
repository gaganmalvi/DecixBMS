import os
import pymysql as p
'''
DecixBMS Installer
Change the password to your MySQL passwd
'''
c = p.connect(host = 'localhost', user = 'root', password = 'Gaganmalvi@123')
a = c.cursor()
def clrscr():
	if os.name=="nt":
		u = os.system("cls")
	else:
		u = os.system("clear")
def installDecix():
	a.execute('create database bms;')
	a.execute('use bms;')
	a.execute('create table menu (sno integer,actions varchar(40));')
	a.execute('create table accounts(sno integer, AccName varchar(20), AccType char(1), amount integer);')
	a.execute('insert into menu values(1,"New Account");')
	a.execute('insert into menu values(2,"Deposit Money");')
	a.execute('insert into menu values(3,"Withdrawal of Money");')
	a.execute('insert into menu values(4,"Balance Enquiry");')
	a.execute('insert into menu values(5,"Account Holders List");')
	a.execute('insert into menu values(6,"Closure of Account");')
	a.execute('insert into menu values(7,"Modify Account");')
	a.execute('insert into menu values(8,"Exit BMS");')
	c.commit()
	print('Installed successfully!')

def uninstDecix():
        a.execute('drop database bms;')
        c.commit()
        print('Uninstalled!')
def mainRun():
        print('==================')
        print('DecixBMS Installer')
        print('==================')
        print('1. Install DecixBMS')
        print('2. Uninstall DecixBMS')
        z = input('Choice:')
        if z == '1':
                installDecix()
        elif z == '2':
                uninstDecix()
        else:
                print('Wrong choice!')

mainRun()

	

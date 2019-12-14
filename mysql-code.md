//* 
PREREQUISITES - 
1. pymysql library - pip3 install pymysql
2. mysql-server - available in ubuntu repos
3. mysql-client - available in ubuntu repos
*//

//* 
The piece of code required to create a MySQLdb for the Python program to just work.
Set your MySQL root config password to Gaganmalvi@123 or change the script according to your own password and username
and execute these lines in the MySQL shell. 
*//

create database bms;
use bms;
create table menu (sno integer,actions varchar(40));
create table accounts(sno integer, AccName varchar(20), AccType char(1), amount integer);
insert into menu values(1,'New Account');
insert into menu values(2,'Deposit Money');
insert into menu values(3,'Withdrawal of Money');
insert into menu values(4,'Balance Enquiry');
insert into menu values(5,'Account Holders List');
insert into menu values(6,'Closure of Account');
insert into menu values(7,'Modify Account');
insert into menu values(8,'Exit BMS');
commit;


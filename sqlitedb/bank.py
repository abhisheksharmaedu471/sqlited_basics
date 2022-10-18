


import sqlite3
import sys
import os

class Bank:
    
    
    def __init(self):
        if not os.path.exists('bank.db'):
            self.conn=sqlite3.connect('bank.db')
            self.c=self.conn.cursor()
            self.b=0
            self.c.execute("CREATE TABLE if not exists record(amount int)")
        else:
            self.conn=sqlite3.connect('bank.db')
            self.c=self.conn.cursor()
            
            self.c.execute('SELECT * FROM record')
            emp2=[i for i in self.c.fetchall()]
            self.b=emp2[-1][0]

    def screen_options(self):
        print("1-Deposit")
        print("2-Withdraw")
        print("3-Check Balance")
        print("4-Exit")
        m=int(input("enter choice"))
        return m
    def deposit(self):
       
        a=int(input("enter amount to deposit:"))
        self.b +=a
       
        
    def withdraw(self):
        a=int(input("enter amount to deposit:"))
        self.b -=a
    def check_balance(self):
        print('balance is{}'.format(self.b))
        
       

    

b1=Bank()
while True:
    k=b1.screen_options()
    if k==1:
        b1.deposit()
    elif k==2:
        b1.withdraw()
    elif k==3:
        b1.check_balance()
    elif k==4:
        b1.c.execute("INSERT INTO bank VALUES(?)",(b1.b))
        b1.con.commit()
        b1.con.close()
        
        sys.exit()
    else:
        print("invalid")
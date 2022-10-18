import sqlite3
conn=sqlite3.connect('newdb')
c=conn.cursor()
#c.execute("CREATE TABLE if not exists record(name text,age int)")

for i in range(1):
    a=input('enter_name:')
    b=input('enter_age:')
c.execute("insert into record values(?,?)",(a,b))
conn.commit()
conn.close()
import sqlite3
conn=sqlite3.connect('newdb')
c=conn.cursor()
c.execute("DELETE from record  where age<21")
conn.commit()
c.execute('SELECT * FROM record')
emp2=c.fetchall()
for i in emp2:
    print(i)
conn.close()
# -*- coding:utf-8 -*-
#!/usr/bin/python
import sqlite3
import os

cwd = os.getcwd()
print cwd

db=sqlite3.connect(cwd+'/db/example.db')

cur = db.cursor()

for t in [('2015-03-28', 'BUY', 'IBM', 1000, 45.00), 
          ('2015-04-05', 'BUY', 'MSOFT', 1000, 72.00), 
          ('2014-04-06', 'SELL', 'IBM', 500, 53.00)]: 
    cur.execute('insert into stocks values (?,?,?,?,?)', t)

db.commit()

cur.execute('select * from stocks order by price') 
while True: 
    tmp=cur.fetchone() 
    if tmp: 
        print tmp 
    else: 
        break 

# -*- coding:utf-8 -*-
#!/usr/bin/python
import sqlite3
import os

cwd = os.getcwd()
print cwd

db=sqlite3.connect(cwd+'/db/example.db')

cur = db.cursor()

cur.execute("""insert into stocks values ('2015-06-05','CUT','CAT',111,135.14)""") 

db.commit()
cur.execute('SELECT * FROM stocks')
print cur.fetchall()

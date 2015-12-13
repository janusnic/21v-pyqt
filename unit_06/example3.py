# -*- coding:utf-8 -*-
#!/usr/bin/python
import sqlite3
import os

cwd = os.getcwd()
print cwd

db=sqlite3.connect(cwd+'/db/example.db')

cur = db.cursor()

cur.execute('select * from stocks order by price') 
print cur.fetchall()

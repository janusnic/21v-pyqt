# -*- coding: utf-8 -*- 
import sqlite3 

workers=(('John',3,10000),('Nik',5,15000)) 

def dict_factory(cursor, row): 
    d = {} 
    for idx, col in enumerate(cursor.description): 
        d[col[0]] = row[idx] 
    return d 

con = sqlite3.connect(":memory:") 
con.row_factory = dict_factory 
cur = con.cursor() 
cur.execute("create table test(name text, experience integer, screw integer)") 
cur.executemany('insert into test(name,experience,screw) values (?,?,?)',workers)
cur.execute('select * from test') 

for item in cur.fetchall(): 
    print 'worker %s have %i years of experience and %i $ of screw'%(item['name'],item['experience'],item['screw'])
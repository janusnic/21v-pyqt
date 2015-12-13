# -*- encoding: utf-8 -*- 
import sqlite3, sys 
# Подготавливаем данные БД 
alphabet=[chr(i) for i in xrange(97,123)] 
# Создаем первую БД и заполняем ее данными 
con=sqlite3.connect(':memory:') 
cur=con.cursor() 
cur.execute('create table test(s)') 
cur.executemany('insert into test values (?)',alphabet) 
con.commit() 
# делаем файл дамп данных первой базы 
with open('/tmp/dump.sql', 'w') as f: 
    for line in con.iterdump(): 
        f.write('%s\n' % line) 
con.close() 

# создаем вторую БД 
con=sqlite3.connect(':memory:') 

cur=con.cursor() 
# восстанавливаем дамп первой базы во второй 
dump=open('/tmp/dump.sql') 
for i in dump: 
    try: 
        cur.execute(i) 
    except: 
        print sys.exc_info() 
dump.close() 
# проверяем наличия данных 
cur.execute('select * from test') 
print cur.fetchall()
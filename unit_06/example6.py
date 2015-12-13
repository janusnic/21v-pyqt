# -*- coding: utf-8 -*- 
import sqlite3 

con = sqlite3.connect(":memory:") 
con.execute("create table person (id integer primary key, firstname varchar unique)") 

# Будет выполненно успешно, con.commit() будет вызван автоматически 
with con: 
    con.execute("insert into person(firstname) values (?)", ("Joe",)) 

# con.rollback() будет вызван после блока with окончившегося исключением 
# которое должно быть перехвачено и корректно обработано 
try: 
    with con: 
        con.execute("insert into person(firstname) values (?)", ("Joe",)) 
except sqlite3.IntegrityError: 
    print "couldn't add Joe twice"
# -*- encoding: utf-8 -*- 
import sqlite3 
con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.execute("CREATE TABLE people(name_last TEXT, age INTEGER)") 
cur.executemany("INSERT INTO people VALUES(?,?)",[('Smart',32),('Tesla',87),('Yeltsin',72)]) 

who = "Yeltsin" 
age = 72 
cur.execute("select name_last, age from people where name_last=? and age=?", (who, age)) 
print cur.fetchone() 

cur.execute("select name_last, age from people where name_last=:who and age=:age",{"who": who, "age": age}) 
print cur.fetchone()
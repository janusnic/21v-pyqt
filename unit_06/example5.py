# -*- coding: utf-8 -*- 
import sqlite3 

con = sqlite3.connect(":memory:") 
con.row_factory = sqlite3.Row 

cur = con.cursor() 
cur.execute("CREATE TABLE people(name_last,age)") 
cur.execute("INSERT INTO people values (?,?)",[(u'Порощенко'),25]) 
cur.execute("select name_last, age from people") 
for row in cur: 
    assert row[0] == row["name_last"] 
    assert row["name_last"] == row["nAmE_lAsT"] 
    assert row[1] == row["age"] 
    assert row[1] == row["AgE"] 
print row[0],row[1]
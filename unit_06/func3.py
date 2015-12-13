import sqlite3 

alphabet=[chr(i) for i in xrange(97,123)] 

def collate_reverse(string1, string2): 
    return -cmp(string1, string2) 

con = sqlite3.connect(":memory:") 
con.create_collation("reverse", collate_reverse) 
cur = con.cursor() 
cur.execute("create table test(x)") 
cur.executemany("insert into test(x) values (?)", alphabet) 

cur.execute("select x from test order by x") 
print 'print alphabet' 
print cur.fetchall() 

cur.execute("select x from test order by x collate reverse") 
print 'print reverse alphabet' 
print cur.fetchall() 

con.close()
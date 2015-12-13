import sqlite3 as sqlite

def select_authorizer(*args):  
    print(args)  
    return sqlite.SQLITE_OK  #should allow all operations           

conn = sqlite.connect(":memory:")
conn.execute("CREATE TABLE A (name integer PRIMARY KEY AUTOINCREMENT)")
conn.set_authorizer(select_authorizer)
conn.execute("SELECT * FROM A").fetchall() #should still work